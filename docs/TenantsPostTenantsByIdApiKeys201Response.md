# TenantsPostTenantsByIdApiKeys201Response

API key metadata. The actual key value is only included on creation (see the key field in the creation response).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | API key record ID | 
**key_prefix** | **str** | First 16 characters of the key, for display/identification | 
**name** | **str** | Human-readable label | 
**scopes** | **List[str]** | Granted permission scopes | 
**environment** | **str** | Key environment | 
**created_at** | **str** | ISO 8601 creation timestamp | 
**key** | **str** | The full API key. Only returned on creation. | 

## Example

```python
from fwallet.models.tenants_post_tenants_by_id_api_keys201_response import TenantsPostTenantsByIdApiKeys201Response

# TODO update the JSON string below
json = "{}"
# create an instance of TenantsPostTenantsByIdApiKeys201Response from a JSON string
tenants_post_tenants_by_id_api_keys201_response_instance = TenantsPostTenantsByIdApiKeys201Response.from_json(json)
# print the JSON string representation of the object
print(TenantsPostTenantsByIdApiKeys201Response.to_json())

# convert the object into a dict
tenants_post_tenants_by_id_api_keys201_response_dict = tenants_post_tenants_by_id_api_keys201_response_instance.to_dict()
# create an instance of TenantsPostTenantsByIdApiKeys201Response from a dict
tenants_post_tenants_by_id_api_keys201_response_from_dict = TenantsPostTenantsByIdApiKeys201Response.from_dict(tenants_post_tenants_by_id_api_keys201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


