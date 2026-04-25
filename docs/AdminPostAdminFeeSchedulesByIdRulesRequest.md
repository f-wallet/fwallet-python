# AdminPostAdminFeeSchedulesByIdRulesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_type** | **str** |  | 
**currency_code** | **str** |  | [optional] 
**min_amount** | **float** |  | [optional] 
**max_amount** | **float** |  | [optional] 
**flat_fee** | **float** |  | [optional] [default to 0]
**percentage_fee** | **float** |  | [optional] [default to 0]
**min_fee** | **float** |  | [optional] 
**max_fee** | **float** |  | [optional] 

## Example

```python
from fwallet.models.admin_post_admin_fee_schedules_by_id_rules_request import AdminPostAdminFeeSchedulesByIdRulesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPostAdminFeeSchedulesByIdRulesRequest from a JSON string
admin_post_admin_fee_schedules_by_id_rules_request_instance = AdminPostAdminFeeSchedulesByIdRulesRequest.from_json(json)
# print the JSON string representation of the object
print(AdminPostAdminFeeSchedulesByIdRulesRequest.to_json())

# convert the object into a dict
admin_post_admin_fee_schedules_by_id_rules_request_dict = admin_post_admin_fee_schedules_by_id_rules_request_instance.to_dict()
# create an instance of AdminPostAdminFeeSchedulesByIdRulesRequest from a dict
admin_post_admin_fee_schedules_by_id_rules_request_from_dict = AdminPostAdminFeeSchedulesByIdRulesRequest.from_dict(admin_post_admin_fee_schedules_by_id_rules_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


