# AdminGetAdminFeeSchedules200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AdminGetAdminFeeSchedules200ResponseDataInner]**](AdminGetAdminFeeSchedules200ResponseDataInner.md) |  | 

## Example

```python
from fwallet.models.admin_get_admin_fee_schedules200_response import AdminGetAdminFeeSchedules200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGetAdminFeeSchedules200Response from a JSON string
admin_get_admin_fee_schedules200_response_instance = AdminGetAdminFeeSchedules200Response.from_json(json)
# print the JSON string representation of the object
print(AdminGetAdminFeeSchedules200Response.to_json())

# convert the object into a dict
admin_get_admin_fee_schedules200_response_dict = admin_get_admin_fee_schedules200_response_instance.to_dict()
# create an instance of AdminGetAdminFeeSchedules200Response from a dict
admin_get_admin_fee_schedules200_response_from_dict = AdminGetAdminFeeSchedules200Response.from_dict(admin_get_admin_fee_schedules200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


