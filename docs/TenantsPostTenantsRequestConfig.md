# TenantsPostTenantsRequestConfig

Tenant-level configuration controlling currencies, limits, and approval thresholds. Each tenant (organization) can define its own policies without changing the underlying code.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_currency** | **str** | Default currency for new wallets and operations | 
**allowed_currencies** | **List[str]** | Currencies this tenant can operate in. System accounts (pool, clearing, revenue, suspense) are created per currency on tenant creation. | 
**max_transaction_amount** | **float** | Per-transaction limit in the smallest currency unit. Transactions above this are rejected by the risk engine. | [optional] 
**require_approval_above** | **float** | Transactions above this amount require maker-checker approval before execution. | [optional] 

## Example

```python
from fwallet.models.tenants_post_tenants_request_config import TenantsPostTenantsRequestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TenantsPostTenantsRequestConfig from a JSON string
tenants_post_tenants_request_config_instance = TenantsPostTenantsRequestConfig.from_json(json)
# print the JSON string representation of the object
print(TenantsPostTenantsRequestConfig.to_json())

# convert the object into a dict
tenants_post_tenants_request_config_dict = tenants_post_tenants_request_config_instance.to_dict()
# create an instance of TenantsPostTenantsRequestConfig from a dict
tenants_post_tenants_request_config_from_dict = TenantsPostTenantsRequestConfig.from_dict(tenants_post_tenants_request_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


