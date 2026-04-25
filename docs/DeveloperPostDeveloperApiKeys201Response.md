# DeveloperPostDeveloperApiKeys201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**application_id** | **UUID** |  | 
**application_name** | **str** |  | 
**key_prefix** | **str** |  | 
**name** | **str** |  | 
**scopes** | **List[str]** |  | 
**environment** | **str** |  | 
**status** | **str** |  | 
**auth_mode** | **str** |  | 
**restrictions** | [**ApiKeyRestrictions**](ApiKeyRestrictions.md) |  | 
**expires_at** | **str** |  | 
**revoked_at** | **str** |  | 
**last_used_at** | **str** |  | 
**last_used_ip** | **str** |  | 
**last_used_origin** | **str** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 
**key** | **str** | The full bearer API key. Only returned once for secret auth mode. | 
**signing_secret** | **str** | The HMAC signing secret. Only returned once for hmac auth mode. | 

## Example

```python
from fwallet.models.developer_post_developer_api_keys201_response import DeveloperPostDeveloperApiKeys201Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperPostDeveloperApiKeys201Response from a JSON string
developer_post_developer_api_keys201_response_instance = DeveloperPostDeveloperApiKeys201Response.from_json(json)
# print the JSON string representation of the object
print(DeveloperPostDeveloperApiKeys201Response.to_json())

# convert the object into a dict
developer_post_developer_api_keys201_response_dict = developer_post_developer_api_keys201_response_instance.to_dict()
# create an instance of DeveloperPostDeveloperApiKeys201Response from a dict
developer_post_developer_api_keys201_response_from_dict = DeveloperPostDeveloperApiKeys201Response.from_dict(developer_post_developer_api_keys201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


