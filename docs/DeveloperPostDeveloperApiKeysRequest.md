# DeveloperPostDeveloperApiKeysRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**scopes** | **List[str]** |  | 
**environment** | **str** |  | [optional] [default to 'test']
**application_id** | **UUID** |  | [optional] 
**auth_mode** | **str** |  | [optional] [default to 'secret']
**restrictions** | [**ApiKeyRestrictions**](ApiKeyRestrictions.md) |  | [optional] 
**expires_at** | **datetime** |  | [optional] 

## Example

```python
from fwallet.models.developer_post_developer_api_keys_request import DeveloperPostDeveloperApiKeysRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperPostDeveloperApiKeysRequest from a JSON string
developer_post_developer_api_keys_request_instance = DeveloperPostDeveloperApiKeysRequest.from_json(json)
# print the JSON string representation of the object
print(DeveloperPostDeveloperApiKeysRequest.to_json())

# convert the object into a dict
developer_post_developer_api_keys_request_dict = developer_post_developer_api_keys_request_instance.to_dict()
# create an instance of DeveloperPostDeveloperApiKeysRequest from a dict
developer_post_developer_api_keys_request_from_dict = DeveloperPostDeveloperApiKeysRequest.from_dict(developer_post_developer_api_keys_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


