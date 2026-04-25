# SystemPostSystemOrganizationsRequestAdmin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 
**password** | **str** |  | [optional] 

## Example

```python
from fwallet.models.system_post_system_organizations_request_admin import SystemPostSystemOrganizationsRequestAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of SystemPostSystemOrganizationsRequestAdmin from a JSON string
system_post_system_organizations_request_admin_instance = SystemPostSystemOrganizationsRequestAdmin.from_json(json)
# print the JSON string representation of the object
print(SystemPostSystemOrganizationsRequestAdmin.to_json())

# convert the object into a dict
system_post_system_organizations_request_admin_dict = system_post_system_organizations_request_admin_instance.to_dict()
# create an instance of SystemPostSystemOrganizationsRequestAdmin from a dict
system_post_system_organizations_request_admin_from_dict = SystemPostSystemOrganizationsRequestAdmin.from_dict(system_post_system_organizations_request_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


