# DeveloperPostDeveloperApiKeysByIdRotate201Response


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
**key** | **str** | The rotated bearer API key. Only returned for secret auth mode. | 
**signing_secret** | **str** | The rotated HMAC signing secret. Only returned for hmac auth mode. | 

## Example

```python
from fwallet.models.developer_post_developer_api_keys_by_id_rotate201_response import DeveloperPostDeveloperApiKeysByIdRotate201Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperPostDeveloperApiKeysByIdRotate201Response from a JSON string
developer_post_developer_api_keys_by_id_rotate201_response_instance = DeveloperPostDeveloperApiKeysByIdRotate201Response.from_json(json)
# print the JSON string representation of the object
print(DeveloperPostDeveloperApiKeysByIdRotate201Response.to_json())

# convert the object into a dict
developer_post_developer_api_keys_by_id_rotate201_response_dict = developer_post_developer_api_keys_by_id_rotate201_response_instance.to_dict()
# create an instance of DeveloperPostDeveloperApiKeysByIdRotate201Response from a dict
developer_post_developer_api_keys_by_id_rotate201_response_from_dict = DeveloperPostDeveloperApiKeysByIdRotate201Response.from_dict(developer_post_developer_api_keys_by_id_rotate201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


