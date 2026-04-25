# ApprovalCase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Case ID | 
**case_type** | **str** | Type of approval case | 
**status** | **str** | pending: awaiting approval. approved: settled. rejected: hold reversed. expired: auto-expired after 24h. | 
**payload** | **Dict[str, Optional[object]]** | Case payload (amount, walletId, payoutMethod, etc.) | 
**requested_by** | **str** | Who requested this payout | 
**decided_by** | **str** | Who approved/rejected (null if still pending) | 
**created_at** | **str** | ISO 8601 timestamp | 

## Example

```python
from fwallet.models.approval_case import ApprovalCase

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalCase from a JSON string
approval_case_instance = ApprovalCase.from_json(json)
# print the JSON string representation of the object
print(ApprovalCase.to_json())

# convert the object into a dict
approval_case_dict = approval_case_instance.to_dict()
# create an instance of ApprovalCase from a dict
approval_case_from_dict = ApprovalCase.from_dict(approval_case_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


