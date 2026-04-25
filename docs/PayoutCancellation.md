# PayoutCancellation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**journal_entry_id** | **UUID** | Journal entry reversing the hold (suspense back to wallet) | 
**case_id** | **UUID** | The rejected case ID | 
**amount** | **str** | Released amount in smallest currency unit | 
**currency_code** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from fwallet.models.payout_cancellation import PayoutCancellation

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutCancellation from a JSON string
payout_cancellation_instance = PayoutCancellation.from_json(json)
# print the JSON string representation of the object
print(PayoutCancellation.to_json())

# convert the object into a dict
payout_cancellation_dict = payout_cancellation_instance.to_dict()
# create an instance of PayoutCancellation from a dict
payout_cancellation_from_dict = PayoutCancellation.from_dict(payout_cancellation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


