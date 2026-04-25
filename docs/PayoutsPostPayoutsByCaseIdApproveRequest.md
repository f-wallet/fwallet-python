# PayoutsPostPayoutsByCaseIdApproveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_id** | **str** | ID of the approver (must be different from requestedBy) | 

## Example

```python
from fwallet.models.payouts_post_payouts_by_case_id_approve_request import PayoutsPostPayoutsByCaseIdApproveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutsPostPayoutsByCaseIdApproveRequest from a JSON string
payouts_post_payouts_by_case_id_approve_request_instance = PayoutsPostPayoutsByCaseIdApproveRequest.from_json(json)
# print the JSON string representation of the object
print(PayoutsPostPayoutsByCaseIdApproveRequest.to_json())

# convert the object into a dict
payouts_post_payouts_by_case_id_approve_request_dict = payouts_post_payouts_by_case_id_approve_request_instance.to_dict()
# create an instance of PayoutsPostPayoutsByCaseIdApproveRequest from a dict
payouts_post_payouts_by_case_id_approve_request_from_dict = PayoutsPostPayoutsByCaseIdApproveRequest.from_dict(payouts_post_payouts_by_case_id_approve_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


