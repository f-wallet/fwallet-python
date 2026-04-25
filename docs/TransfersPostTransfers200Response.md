# TransfersPostTransfers200Response

Result of a completed transfer, including the fee breakdown. If the same Idempotency-Key is replayed, the original result is returned with an Idempotent-Replayed: true header.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Transfer ID (same as journal entry ID) | 
**journal_entry_id** | **UUID** | The underlying ledger journal entry recording this transfer | 
**from_wallet_id** | **UUID** | Source wallet | 
**to_wallet_id** | **UUID** | Destination wallet | 
**amount** | **str** | Transfer amount in smallest currency unit | 
**fee** | **str** | Fee charged in smallest currency unit | 
**currency_code** | **str** | Transfer currency | 
**status** | **str** | Transfer status | 
**created_at** | **str** | ISO 8601 timestamp | 

## Example

```python
from fwallet.models.transfers_post_transfers200_response import TransfersPostTransfers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TransfersPostTransfers200Response from a JSON string
transfers_post_transfers200_response_instance = TransfersPostTransfers200Response.from_json(json)
# print the JSON string representation of the object
print(TransfersPostTransfers200Response.to_json())

# convert the object into a dict
transfers_post_transfers200_response_dict = transfers_post_transfers200_response_instance.to_dict()
# create an instance of TransfersPostTransfers200Response from a dict
transfers_post_transfers200_response_from_dict = TransfersPostTransfers200Response.from_dict(transfers_post_transfers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


