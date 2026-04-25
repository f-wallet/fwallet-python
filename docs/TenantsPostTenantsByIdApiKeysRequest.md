# TenantsPostTenantsByIdApiKeysRequest

Create a new API key for a tenant. The full key value is returned only once on creation — store it securely. All subsequent API calls use this key in the X-API-Key header.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable label for the key | 
**scopes** | **List[str]** | Permission scopes granted to this key. Available: ledger:read, ledger:write, wallet:transfer, wallet:deposit, tenant:manage, webhook:manage | 
**environment** | **str** | Environment scope. Test keys can only access test data. | [optional] [default to 'live']

## Example

```python
from fwallet.models.tenants_post_tenants_by_id_api_keys_request import TenantsPostTenantsByIdApiKeysRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TenantsPostTenantsByIdApiKeysRequest from a JSON string
tenants_post_tenants_by_id_api_keys_request_instance = TenantsPostTenantsByIdApiKeysRequest.from_json(json)
# print the JSON string representation of the object
print(TenantsPostTenantsByIdApiKeysRequest.to_json())

# convert the object into a dict
tenants_post_tenants_by_id_api_keys_request_dict = tenants_post_tenants_by_id_api_keys_request_instance.to_dict()
# create an instance of TenantsPostTenantsByIdApiKeysRequest from a dict
tenants_post_tenants_by_id_api_keys_request_from_dict = TenantsPostTenantsByIdApiKeysRequest.from_dict(tenants_post_tenants_by_id_api_keys_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


