# AuthGetAuthMe200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**AuthGetAuthMe200ResponseUser**](AuthGetAuthMe200ResponseUser.md) |  | 

## Example

```python
from fwallet.models.auth_get_auth_me200_response import AuthGetAuthMe200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthGetAuthMe200Response from a JSON string
auth_get_auth_me200_response_instance = AuthGetAuthMe200Response.from_json(json)
# print the JSON string representation of the object
print(AuthGetAuthMe200Response.to_json())

# convert the object into a dict
auth_get_auth_me200_response_dict = auth_get_auth_me200_response_instance.to_dict()
# create an instance of AuthGetAuthMe200Response from a dict
auth_get_auth_me200_response_from_dict = AuthGetAuthMe200Response.from_dict(auth_get_auth_me200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


