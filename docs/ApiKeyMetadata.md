# ApiKeyMetadata


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

## Example

```python
from fwallet.models.api_key_metadata import ApiKeyMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyMetadata from a JSON string
api_key_metadata_instance = ApiKeyMetadata.from_json(json)
# print the JSON string representation of the object
print(ApiKeyMetadata.to_json())

# convert the object into a dict
api_key_metadata_dict = api_key_metadata_instance.to_dict()
# create an instance of ApiKeyMetadata from a dict
api_key_metadata_from_dict = ApiKeyMetadata.from_dict(api_key_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


