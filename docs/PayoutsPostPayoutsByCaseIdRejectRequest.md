# PayoutsPostPayoutsByCaseIdRejectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_id** | **str** | ID of the person rejecting | 
**reason** | **str** | Reason for rejection (recorded in audit trail) | [optional] 

## Example

```python
from fwallet.models.payouts_post_payouts_by_case_id_reject_request import PayoutsPostPayoutsByCaseIdRejectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutsPostPayoutsByCaseIdRejectRequest from a JSON string
payouts_post_payouts_by_case_id_reject_request_instance = PayoutsPostPayoutsByCaseIdRejectRequest.from_json(json)
# print the JSON string representation of the object
print(PayoutsPostPayoutsByCaseIdRejectRequest.to_json())

# convert the object into a dict
payouts_post_payouts_by_case_id_reject_request_dict = payouts_post_payouts_by_case_id_reject_request_instance.to_dict()
# create an instance of PayoutsPostPayoutsByCaseIdRejectRequest from a dict
payouts_post_payouts_by_case_id_reject_request_from_dict = PayoutsPostPayoutsByCaseIdRejectRequest.from_dict(payouts_post_payouts_by_case_id_reject_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


