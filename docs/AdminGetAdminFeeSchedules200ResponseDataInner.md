# AdminGetAdminFeeSchedules200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**is_default** | **bool** |  | 
**rules** | [**List[AdminGetAdminFeeSchedules200ResponseDataInnerRulesInner]**](AdminGetAdminFeeSchedules200ResponseDataInnerRulesInner.md) |  | 

## Example

```python
from fwallet.models.admin_get_admin_fee_schedules200_response_data_inner import AdminGetAdminFeeSchedules200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGetAdminFeeSchedules200ResponseDataInner from a JSON string
admin_get_admin_fee_schedules200_response_data_inner_instance = AdminGetAdminFeeSchedules200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(AdminGetAdminFeeSchedules200ResponseDataInner.to_json())

# convert the object into a dict
admin_get_admin_fee_schedules200_response_data_inner_dict = admin_get_admin_fee_schedules200_response_data_inner_instance.to_dict()
# create an instance of AdminGetAdminFeeSchedules200ResponseDataInner from a dict
admin_get_admin_fee_schedules200_response_data_inner_from_dict = AdminGetAdminFeeSchedules200ResponseDataInner.from_dict(admin_get_admin_fee_schedules200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


