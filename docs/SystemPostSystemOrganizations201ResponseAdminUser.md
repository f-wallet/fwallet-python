# SystemPostSystemOrganizations201ResponseAdminUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**org_role** | **str** |  | 
**tenant_id** | **UUID** |  | 

## Example

```python
from fwallet.models.system_post_system_organizations201_response_admin_user import SystemPostSystemOrganizations201ResponseAdminUser

# TODO update the JSON string below
json = "{}"
# create an instance of SystemPostSystemOrganizations201ResponseAdminUser from a JSON string
system_post_system_organizations201_response_admin_user_instance = SystemPostSystemOrganizations201ResponseAdminUser.from_json(json)
# print the JSON string representation of the object
print(SystemPostSystemOrganizations201ResponseAdminUser.to_json())

# convert the object into a dict
system_post_system_organizations201_response_admin_user_dict = system_post_system_organizations201_response_admin_user_instance.to_dict()
# create an instance of SystemPostSystemOrganizations201ResponseAdminUser from a dict
system_post_system_organizations201_response_admin_user_from_dict = SystemPostSystemOrganizations201ResponseAdminUser.from_dict(system_post_system_organizations201_response_admin_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


