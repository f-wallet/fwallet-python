# TransfersPostTransfersSimulateFeeRequest

Preview the fee for a hypothetical transaction without executing it. Useful for showing users the fee before they confirm a transfer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_type** | **str** | Transaction type to simulate (e.g. &#39;transfer&#39;, &#39;deposit&#39;, &#39;payout&#39;) | 
**amount** | **float** | Amount in human-readable units | 
**currency_code** | **str** | ISO 4217 currency code. UGX and TSH have no decimal subdivisions; KES, USD, CNY, GBP use cents (1/100). | 

## Example

```python
from fwallet.models.transfers_post_transfers_simulate_fee_request import TransfersPostTransfersSimulateFeeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransfersPostTransfersSimulateFeeRequest from a JSON string
transfers_post_transfers_simulate_fee_request_instance = TransfersPostTransfersSimulateFeeRequest.from_json(json)
# print the JSON string representation of the object
print(TransfersPostTransfersSimulateFeeRequest.to_json())

# convert the object into a dict
transfers_post_transfers_simulate_fee_request_dict = transfers_post_transfers_simulate_fee_request_instance.to_dict()
# create an instance of TransfersPostTransfersSimulateFeeRequest from a dict
transfers_post_transfers_simulate_fee_request_from_dict = TransfersPostTransfersSimulateFeeRequest.from_dict(transfers_post_transfers_simulate_fee_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


