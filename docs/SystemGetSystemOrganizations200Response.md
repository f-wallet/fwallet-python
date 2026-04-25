# SystemGetSystemOrganizations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SystemGetSystemOrganizations200ResponseDataInner]**](SystemGetSystemOrganizations200ResponseDataInner.md) |  | 

## Example

```python
from fwallet.models.system_get_system_organizations200_response import SystemGetSystemOrganizations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SystemGetSystemOrganizations200Response from a JSON string
system_get_system_organizations200_response_instance = SystemGetSystemOrganizations200Response.from_json(json)
# print the JSON string representation of the object
print(SystemGetSystemOrganizations200Response.to_json())

# convert the object into a dict
system_get_system_organizations200_response_dict = system_get_system_organizations200_response_instance.to_dict()
# create an instance of SystemGetSystemOrganizations200Response from a dict
system_get_system_organizations200_response_from_dict = SystemGetSystemOrganizations200Response.from_dict(system_get_system_organizations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


