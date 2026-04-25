# TransfersPostTransfersRequest

Execute a wallet-to-wallet transfer. The fee engine computes the commission from the tenant's fee schedule based on the transactionType. Requires an Idempotency-Key header.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_wallet_id** | **UUID** | Source wallet ID. Must be active and have sufficient balance (amount + fee). | 
**to_wallet_id** | **UUID** | Destination wallet ID. Must be active and in the same currency as the source. | 
**amount** | **float** | Transfer amount in human-readable units (e.g. 10000 for 10,000 UGX, or 10.50 for $10.50 USD). Converted to smallest currency unit internally. | 
**currency_code** | **str** | ISO 4217 currency code. UGX and TSH have no decimal subdivisions; KES, USD, CNY, GBP use cents (1/100). | 
**transaction_type** | **str** | Transaction type for fee routing. Defaults to &#39;transfer&#39;. B2B platforms can pass custom types to match different fee schedule rules (e.g., a type with 0% fee for specific operations). | [optional] 

## Example

```python
from fwallet.models.transfers_post_transfers_request import TransfersPostTransfersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransfersPostTransfersRequest from a JSON string
transfers_post_transfers_request_instance = TransfersPostTransfersRequest.from_json(json)
# print the JSON string representation of the object
print(TransfersPostTransfersRequest.to_json())

# convert the object into a dict
transfers_post_transfers_request_dict = transfers_post_transfers_request_instance.to_dict()
# create an instance of TransfersPostTransfersRequest from a dict
transfers_post_transfers_request_from_dict = TransfersPostTransfersRequest.from_dict(transfers_post_transfers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


