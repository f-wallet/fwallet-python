# PayoutSettlement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**journal_entry_id** | **UUID** | Journal entry recording the settlement (suspense to payout-clearing) | 
**case_id** | **UUID** | The approved case ID | 
**amount** | **str** | Settled amount in smallest currency unit | 
**currency_code** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from fwallet.models.payout_settlement import PayoutSettlement

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutSettlement from a JSON string
payout_settlement_instance = PayoutSettlement.from_json(json)
# print the JSON string representation of the object
print(PayoutSettlement.to_json())

# convert the object into a dict
payout_settlement_dict = payout_settlement_instance.to_dict()
# create an instance of PayoutSettlement from a dict
payout_settlement_from_dict = PayoutSettlement.from_dict(payout_settlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


