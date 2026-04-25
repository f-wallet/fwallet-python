# MoMoWebhookPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The MoMo provider&#39;s unique transaction ID. Used as the idempotency key to prevent double-crediting. | 
**phone_number** | **str** | Depositor&#39;s phone number | 
**amount** | **float** | Deposit amount in human-readable units (e.g. 500000 for 500,000 UGX) | 
**currency_code** | **str** | Currency of the deposit (must match the wallet&#39;s currency) | 
**wallet_id** | **UUID** | Target wallet to credit | 
**signature** | **str** | HMAC-SHA256 signature from the MoMo provider for verification | 
**timestamp** | **str** | ISO 8601 timestamp from the provider | 

## Example

```python
from fwallet.models.mo_mo_webhook_payload import MoMoWebhookPayload

# TODO update the JSON string below
json = "{}"
# create an instance of MoMoWebhookPayload from a JSON string
mo_mo_webhook_payload_instance = MoMoWebhookPayload.from_json(json)
# print the JSON string representation of the object
print(MoMoWebhookPayload.to_json())

# convert the object into a dict
mo_mo_webhook_payload_dict = mo_mo_webhook_payload_instance.to_dict()
# create an instance of MoMoWebhookPayload from a dict
mo_mo_webhook_payload_from_dict = MoMoWebhookPayload.from_dict(mo_mo_webhook_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


