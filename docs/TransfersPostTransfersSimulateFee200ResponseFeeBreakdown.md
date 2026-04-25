# TransfersPostTransfersSimulateFee200ResponseFeeBreakdown


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flat** | **str** | Flat fee component | 
**percentage** | **str** | Percentage fee component (computed from basis points) | 

## Example

```python
from fwallet.models.transfers_post_transfers_simulate_fee200_response_fee_breakdown import TransfersPostTransfersSimulateFee200ResponseFeeBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of TransfersPostTransfersSimulateFee200ResponseFeeBreakdown from a JSON string
transfers_post_transfers_simulate_fee200_response_fee_breakdown_instance = TransfersPostTransfersSimulateFee200ResponseFeeBreakdown.from_json(json)
# print the JSON string representation of the object
print(TransfersPostTransfersSimulateFee200ResponseFeeBreakdown.to_json())

# convert the object into a dict
transfers_post_transfers_simulate_fee200_response_fee_breakdown_dict = transfers_post_transfers_simulate_fee200_response_fee_breakdown_instance.to_dict()
# create an instance of TransfersPostTransfersSimulateFee200ResponseFeeBreakdown from a dict
transfers_post_transfers_simulate_fee200_response_fee_breakdown_from_dict = TransfersPostTransfersSimulateFee200ResponseFeeBreakdown.from_dict(transfers_post_transfers_simulate_fee200_response_fee_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


