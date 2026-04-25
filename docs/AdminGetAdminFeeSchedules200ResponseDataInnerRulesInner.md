# AdminGetAdminFeeSchedules200ResponseDataInnerRulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**transaction_type** | **str** |  | 
**currency_code** | **str** |  | 
**flat_fee** | **str** |  | 
**percentage_fee** | **float** |  | 

## Example

```python
from fwallet.models.admin_get_admin_fee_schedules200_response_data_inner_rules_inner import AdminGetAdminFeeSchedules200ResponseDataInnerRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGetAdminFeeSchedules200ResponseDataInnerRulesInner from a JSON string
admin_get_admin_fee_schedules200_response_data_inner_rules_inner_instance = AdminGetAdminFeeSchedules200ResponseDataInnerRulesInner.from_json(json)
# print the JSON string representation of the object
print(AdminGetAdminFeeSchedules200ResponseDataInnerRulesInner.to_json())

# convert the object into a dict
admin_get_admin_fee_schedules200_response_data_inner_rules_inner_dict = admin_get_admin_fee_schedules200_response_data_inner_rules_inner_instance.to_dict()
# create an instance of AdminGetAdminFeeSchedules200ResponseDataInnerRulesInner from a dict
admin_get_admin_fee_schedules200_response_data_inner_rules_inner_from_dict = AdminGetAdminFeeSchedules200ResponseDataInnerRulesInner.from_dict(admin_get_admin_fee_schedules200_response_data_inner_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


