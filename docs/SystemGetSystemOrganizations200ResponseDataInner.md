# SystemGetSystemOrganizations200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**status** | **str** |  | 
**created_at** | **str** |  | 

## Example

```python
from fwallet.models.system_get_system_organizations200_response_data_inner import SystemGetSystemOrganizations200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of SystemGetSystemOrganizations200ResponseDataInner from a JSON string
system_get_system_organizations200_response_data_inner_instance = SystemGetSystemOrganizations200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(SystemGetSystemOrganizations200ResponseDataInner.to_json())

# convert the object into a dict
system_get_system_organizations200_response_data_inner_dict = system_get_system_organizations200_response_data_inner_instance.to_dict()
# create an instance of SystemGetSystemOrganizations200ResponseDataInner from a dict
system_get_system_organizations200_response_data_inner_from_dict = SystemGetSystemOrganizations200ResponseDataInner.from_dict(system_get_system_organizations200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


