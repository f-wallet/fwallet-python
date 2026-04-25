# AdminPostAdminFeeSchedulesByIdRules201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**transaction_type** | **str** |  | 
**flat_fee** | **str** |  | 
**percentage_fee** | **float** |  | 

## Example

```python
from fwallet.models.admin_post_admin_fee_schedules_by_id_rules201_response import AdminPostAdminFeeSchedulesByIdRules201Response

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPostAdminFeeSchedulesByIdRules201Response from a JSON string
admin_post_admin_fee_schedules_by_id_rules201_response_instance = AdminPostAdminFeeSchedulesByIdRules201Response.from_json(json)
# print the JSON string representation of the object
print(AdminPostAdminFeeSchedulesByIdRules201Response.to_json())

# convert the object into a dict
admin_post_admin_fee_schedules_by_id_rules201_response_dict = admin_post_admin_fee_schedules_by_id_rules201_response_instance.to_dict()
# create an instance of AdminPostAdminFeeSchedulesByIdRules201Response from a dict
admin_post_admin_fee_schedules_by_id_rules201_response_from_dict = AdminPostAdminFeeSchedulesByIdRules201Response.from_dict(admin_post_admin_fee_schedules_by_id_rules201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


