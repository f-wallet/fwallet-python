# TransfersPostTransfersSimulateFee200Response

Fee simulation result. Shows the breakdown between flat and percentage components, and the total amount that would be debited from the sender's wallet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | **str** | Total fee in smallest currency unit | 
**fee_breakdown** | [**TransfersPostTransfersSimulateFee200ResponseFeeBreakdown**](TransfersPostTransfersSimulateFee200ResponseFeeBreakdown.md) |  | 
**total_debit** | **str** | Total amount that would be debited from the sender (amount + fee) | 

## Example

```python
from fwallet.models.transfers_post_transfers_simulate_fee200_response import TransfersPostTransfersSimulateFee200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TransfersPostTransfersSimulateFee200Response from a JSON string
transfers_post_transfers_simulate_fee200_response_instance = TransfersPostTransfersSimulateFee200Response.from_json(json)
# print the JSON string representation of the object
print(TransfersPostTransfersSimulateFee200Response.to_json())

# convert the object into a dict
transfers_post_transfers_simulate_fee200_response_dict = transfers_post_transfers_simulate_fee200_response_instance.to_dict()
# create an instance of TransfersPostTransfersSimulateFee200Response from a dict
transfers_post_transfers_simulate_fee200_response_from_dict = TransfersPostTransfersSimulateFee200Response.from_dict(transfers_post_transfers_simulate_fee200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


