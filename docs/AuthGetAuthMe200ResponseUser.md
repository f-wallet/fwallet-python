# AuthGetAuthMe200ResponseUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**org_role** | **str** |  | 
**tenant_id** | **str** |  | 
**branch_id** | **str** |  | 

## Example

```python
from fwallet.models.auth_get_auth_me200_response_user import AuthGetAuthMe200ResponseUser

# TODO update the JSON string below
json = "{}"
# create an instance of AuthGetAuthMe200ResponseUser from a JSON string
auth_get_auth_me200_response_user_instance = AuthGetAuthMe200ResponseUser.from_json(json)
# print the JSON string representation of the object
print(AuthGetAuthMe200ResponseUser.to_json())

# convert the object into a dict
auth_get_auth_me200_response_user_dict = auth_get_auth_me200_response_user_instance.to_dict()
# create an instance of AuthGetAuthMe200ResponseUser from a dict
auth_get_auth_me200_response_user_from_dict = AuthGetAuthMe200ResponseUser.from_dict(auth_get_auth_me200_response_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


