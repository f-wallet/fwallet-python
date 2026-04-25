# SystemPostSystemOrganizations201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | [**SystemGetSystemOrganizations200ResponseDataInner**](SystemGetSystemOrganizations200ResponseDataInner.md) |  | 
**admin_user** | [**SystemPostSystemOrganizations201ResponseAdminUser**](SystemPostSystemOrganizations201ResponseAdminUser.md) |  | 
**temporary_password** | **str** |  | 
**invite_status** | **str** |  | 
**invite_email** | [**SystemPostSystemOrganizations201ResponseInviteEmail**](SystemPostSystemOrganizations201ResponseInviteEmail.md) |  | 

## Example

```python
from fwallet.models.system_post_system_organizations201_response import SystemPostSystemOrganizations201Response

# TODO update the JSON string below
json = "{}"
# create an instance of SystemPostSystemOrganizations201Response from a JSON string
system_post_system_organizations201_response_instance = SystemPostSystemOrganizations201Response.from_json(json)
# print the JSON string representation of the object
print(SystemPostSystemOrganizations201Response.to_json())

# convert the object into a dict
system_post_system_organizations201_response_dict = system_post_system_organizations201_response_instance.to_dict()
# create an instance of SystemPostSystemOrganizations201Response from a dict
system_post_system_organizations201_response_from_dict = SystemPostSystemOrganizations201Response.from_dict(system_post_system_organizations201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


