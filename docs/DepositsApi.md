# fwallet.DepositsApi

All URIs are relative to *https://api.fwallet.co.ug*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deposits_post_deposits_bank_slip_verify**](DepositsApi.md#deposits_post_deposits_bank_slip_verify) | **POST** /v1/deposits/bank-slip/verify | Create Deposits
[**deposits_post_deposits_bank_statements**](DepositsApi.md#deposits_post_deposits_bank_statements) | **POST** /v1/deposits/bank-statements | Create Deposits
[**deposits_post_deposits_momo_webhook**](DepositsApi.md#deposits_post_deposits_momo_webhook) | **POST** /v1/deposits/momo-webhook | Create Deposits


# **deposits_post_deposits_bank_slip_verify**
> BankSlipResult deposits_post_deposits_bank_slip_verify(bank_slip_verify_request=bank_slip_verify_request)

Create Deposits

Verify a bank deposit slip against imported bank statement data. A branch manager enters the slip's reference number and amount. The system checks if a matching bank statement line exists: if found with matching amount, the user is credited immediately (verified). If the bank feed hasn't arrived yet, returns pending. If the reference exists but the amount differs, returns mismatch for manual investigation.

### Example

* Api Key Authentication (hmacNonce):
* Api Key Authentication (apiKey):
* Api Key Authentication (hmacContentSha256):
* Api Key Authentication (hmacTimestamp):
* Api Key Authentication (hmacKeyId):
* Api Key Authentication (hmacSignature):

```python
import fwallet
from fwallet.models.bank_slip_result import BankSlipResult
from fwallet.models.bank_slip_verify_request import BankSlipVerifyRequest
from fwallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fwallet.co.ug
# See configuration.py for a list of all supported configuration parameters.
configuration = fwallet.Configuration(
    host = "https://api.fwallet.co.ug"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: hmacNonce
configuration.api_key['hmacNonce'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacNonce'] = 'Bearer'

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: hmacContentSha256
configuration.api_key['hmacContentSha256'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacContentSha256'] = 'Bearer'

# Configure API key authorization: hmacTimestamp
configuration.api_key['hmacTimestamp'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacTimestamp'] = 'Bearer'

# Configure API key authorization: hmacKeyId
configuration.api_key['hmacKeyId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacKeyId'] = 'Bearer'

# Configure API key authorization: hmacSignature
configuration.api_key['hmacSignature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacSignature'] = 'Bearer'

# Enter a context with an instance of the API client
with fwallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fwallet.DepositsApi(api_client)
    bank_slip_verify_request = fwallet.BankSlipVerifyRequest() # BankSlipVerifyRequest |  (optional)

    try:
        # Create Deposits
        api_response = api_instance.deposits_post_deposits_bank_slip_verify(bank_slip_verify_request=bank_slip_verify_request)
        print("The response of DepositsApi->deposits_post_deposits_bank_slip_verify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepositsApi->deposits_post_deposits_bank_slip_verify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_slip_verify_request** | [**BankSlipVerifyRequest**](BankSlipVerifyRequest.md)|  | [optional] 

### Return type

[**BankSlipResult**](BankSlipResult.md)

### Authorization

[hmacNonce](../README.md#hmacNonce), [apiKey](../README.md#apiKey), [hmacContentSha256](../README.md#hmacContentSha256), [hmacTimestamp](../README.md#hmacTimestamp), [hmacKeyId](../README.md#hmacKeyId), [hmacSignature](../README.md#hmacSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Verification result: verified (user credited), pending (awaiting bank data), or mismatch (amount discrepancy) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deposits_post_deposits_bank_statements**
> DepositsPostDepositsBankStatements200Response deposits_post_deposits_bank_statements(deposits_post_deposits_bank_statements_request=deposits_post_deposits_bank_statements_request)

Create Deposits

Import bank statement lines for reconciliation. These lines are used to verify bank slip deposits — when a user presents a slip, the system checks these records for a matching reference and amount. In production, this would connect to a bank feed API; for Phase 1 it accepts manual/CSV-imported data.

### Example

* Api Key Authentication (hmacNonce):
* Api Key Authentication (apiKey):
* Api Key Authentication (hmacContentSha256):
* Api Key Authentication (hmacTimestamp):
* Api Key Authentication (hmacKeyId):
* Api Key Authentication (hmacSignature):

```python
import fwallet
from fwallet.models.deposits_post_deposits_bank_statements200_response import DepositsPostDepositsBankStatements200Response
from fwallet.models.deposits_post_deposits_bank_statements_request import DepositsPostDepositsBankStatementsRequest
from fwallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fwallet.co.ug
# See configuration.py for a list of all supported configuration parameters.
configuration = fwallet.Configuration(
    host = "https://api.fwallet.co.ug"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: hmacNonce
configuration.api_key['hmacNonce'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacNonce'] = 'Bearer'

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: hmacContentSha256
configuration.api_key['hmacContentSha256'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacContentSha256'] = 'Bearer'

# Configure API key authorization: hmacTimestamp
configuration.api_key['hmacTimestamp'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacTimestamp'] = 'Bearer'

# Configure API key authorization: hmacKeyId
configuration.api_key['hmacKeyId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacKeyId'] = 'Bearer'

# Configure API key authorization: hmacSignature
configuration.api_key['hmacSignature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacSignature'] = 'Bearer'

# Enter a context with an instance of the API client
with fwallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fwallet.DepositsApi(api_client)
    deposits_post_deposits_bank_statements_request = fwallet.DepositsPostDepositsBankStatementsRequest() # DepositsPostDepositsBankStatementsRequest |  (optional)

    try:
        # Create Deposits
        api_response = api_instance.deposits_post_deposits_bank_statements(deposits_post_deposits_bank_statements_request=deposits_post_deposits_bank_statements_request)
        print("The response of DepositsApi->deposits_post_deposits_bank_statements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepositsApi->deposits_post_deposits_bank_statements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deposits_post_deposits_bank_statements_request** | [**DepositsPostDepositsBankStatementsRequest**](DepositsPostDepositsBankStatementsRequest.md)|  | [optional] 

### Return type

[**DepositsPostDepositsBankStatements200Response**](DepositsPostDepositsBankStatements200Response.md)

### Authorization

[hmacNonce](../README.md#hmacNonce), [apiKey](../README.md#apiKey), [hmacContentSha256](../README.md#hmacContentSha256), [hmacTimestamp](../README.md#hmacTimestamp), [hmacKeyId](../README.md#hmacKeyId), [hmacSignature](../README.md#hmacSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statement lines imported successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deposits_post_deposits_momo_webhook**
> MoMoDepositResult deposits_post_deposits_momo_webhook(mo_mo_webhook_payload=mo_mo_webhook_payload)

Create Deposits

Process a MoMo deposit webhook. When a user deposits via Mobile Money, the MoMo provider sends a webhook notification. FWallet verifies the signature, checks idempotency (by transactionId), and credits the user's wallet immediately. The deposit is recorded for later settlement reconciliation. Accounting: DR user wallet (balance increases), CR momo-clearing (settlement pending).

### Example

* Api Key Authentication (hmacNonce):
* Api Key Authentication (apiKey):
* Api Key Authentication (hmacContentSha256):
* Api Key Authentication (hmacTimestamp):
* Api Key Authentication (hmacKeyId):
* Api Key Authentication (hmacSignature):

```python
import fwallet
from fwallet.models.mo_mo_deposit_result import MoMoDepositResult
from fwallet.models.mo_mo_webhook_payload import MoMoWebhookPayload
from fwallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fwallet.co.ug
# See configuration.py for a list of all supported configuration parameters.
configuration = fwallet.Configuration(
    host = "https://api.fwallet.co.ug"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: hmacNonce
configuration.api_key['hmacNonce'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacNonce'] = 'Bearer'

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: hmacContentSha256
configuration.api_key['hmacContentSha256'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacContentSha256'] = 'Bearer'

# Configure API key authorization: hmacTimestamp
configuration.api_key['hmacTimestamp'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacTimestamp'] = 'Bearer'

# Configure API key authorization: hmacKeyId
configuration.api_key['hmacKeyId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacKeyId'] = 'Bearer'

# Configure API key authorization: hmacSignature
configuration.api_key['hmacSignature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacSignature'] = 'Bearer'

# Enter a context with an instance of the API client
with fwallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fwallet.DepositsApi(api_client)
    mo_mo_webhook_payload = fwallet.MoMoWebhookPayload() # MoMoWebhookPayload |  (optional)

    try:
        # Create Deposits
        api_response = api_instance.deposits_post_deposits_momo_webhook(mo_mo_webhook_payload=mo_mo_webhook_payload)
        print("The response of DepositsApi->deposits_post_deposits_momo_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepositsApi->deposits_post_deposits_momo_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_mo_webhook_payload** | [**MoMoWebhookPayload**](MoMoWebhookPayload.md)|  | [optional] 

### Return type

[**MoMoDepositResult**](MoMoDepositResult.md)

### Authorization

[hmacNonce](../README.md#hmacNonce), [apiKey](../README.md#apiKey), [hmacContentSha256](../README.md#hmacContentSha256), [hmacTimestamp](../README.md#hmacTimestamp), [hmacKeyId](../README.md#hmacKeyId), [hmacSignature](../README.md#hmacSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deposit processed successfully (or replayed if the transactionId was already seen) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

