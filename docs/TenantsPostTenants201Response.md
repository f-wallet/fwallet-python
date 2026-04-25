# TenantsPostTenants201Response

A tenant represents an organization using FWallet (e.g. a betting platform, a remittance company). Tenants are fully isolated — each has its own wallets, ledger, fee schedules, and approval policies.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique tenant identifier | 
**name** | **str** | Display name | 
**slug** | **str** | URL-safe identifier | 
**status** | **str** | Tenant lifecycle status. Suspended tenants cannot process transactions; deactivated tenants cannot authenticate. | 
**created_at** | **str** | ISO 8601 creation timestamp | 

## Example

```python
from fwallet.models.tenants_post_tenants201_response import TenantsPostTenants201Response

# TODO update the JSON string below
json = "{}"
# create an instance of TenantsPostTenants201Response from a JSON string
tenants_post_tenants201_response_instance = TenantsPostTenants201Response.from_json(json)
# print the JSON string representation of the object
print(TenantsPostTenants201Response.to_json())

# convert the object into a dict
tenants_post_tenants201_response_dict = tenants_post_tenants201_response_instance.to_dict()
# create an instance of TenantsPostTenants201Response from a dict
tenants_post_tenants201_response_from_dict = TenantsPostTenants201Response.from_dict(tenants_post_tenants201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


