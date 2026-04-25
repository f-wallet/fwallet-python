import base64
import hashlib
import hmac
import uuid
from datetime import datetime, timezone
from urllib.parse import parse_qsl, urlencode, urlparse


def sign_fwallet_request(
    *,
    url: str,
    method: str,
    key_id: str,
    signing_secret: str,
    body: str = "",
    idempotency_key: str | None = None,
    actor_type: str | None = None,
    actor_id: str | None = None,
    nonce: str | None = None,
    timestamp: str | None = None,
) -> dict[str, str]:
    timestamp = timestamp or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    nonce = nonce or str(uuid.uuid4())
    content_sha256 = sha256_base64url(body.encode("utf-8"))
    canonical = build_canonical_request(
        timestamp=timestamp,
        nonce=nonce,
        method=method,
        path_with_query=canonical_path_with_sorted_query(url),
        content_sha256=content_sha256,
        idempotency_key=idempotency_key,
        actor_type=actor_type,
        actor_id=actor_id,
    )
    signature = format_signature(hmac_sha256_base64url(signing_secret, canonical))
    headers = {
        "X-FWallet-Key-Id": key_id,
        "X-FWallet-Timestamp": timestamp,
        "X-FWallet-Nonce": nonce,
        "X-FWallet-Content-SHA256": content_sha256,
        "X-FWallet-Signature": signature,
    }
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key
    if actor_type:
        headers["X-FWallet-Actor-Type"] = actor_type
    if actor_id:
        headers["X-FWallet-Actor-Id"] = actor_id
    return headers


def build_canonical_request(
    *,
    timestamp: str,
    nonce: str,
    method: str,
    path_with_query: str,
    content_sha256: str,
    idempotency_key: str | None = None,
    actor_type: str | None = None,
    actor_id: str | None = None,
) -> str:
    return "\n".join(
        [
            "v1",
            timestamp,
            nonce,
            method.upper(),
            path_with_query,
            content_sha256,
            idempotency_key or "",
            actor_type or "",
            actor_id or "",
        ]
    )


def canonical_path_with_sorted_query(url: str) -> str:
    parsed = urlparse(url)
    params = sorted(parse_qsl(parsed.query, keep_blank_values=True))
    query = urlencode(params)
    return f"{parsed.path}?{query}" if query else parsed.path


def sha256_base64url(value: bytes) -> str:
    return base64url(hashlib.sha256(value).digest())


def hmac_sha256_base64url(secret: str, payload: str) -> str:
    return base64url(hmac.new(secret.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256).digest())


def format_signature(signature: str) -> str:
    return f"v1=:{signature}:"


def create_idempotency_key(prefix: str = "fwallet") -> str:
    return f"{prefix}_{uuid.uuid4()}"


def base64url(value: bytes) -> str:
    return base64.urlsafe_b64encode(value).decode("ascii").rstrip("=")
