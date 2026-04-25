# TenantsPostTenantsRequest

Create a new tenant (organization). On creation, the system auto-provisions: system ledger accounts (pool, MoMo clearing, bank clearing, payout clearing, fee revenue, suspense) for each allowed currency, and a default fee schedule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name of the organization | 
**slug** | **str** | URL-safe unique identifier for the tenant | 
**config** | [**TenantsPostTenantsRequestConfig**](TenantsPostTenantsRequestConfig.md) |  | 

## Example

```python
from fwallet.models.tenants_post_tenants_request import TenantsPostTenantsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TenantsPostTenantsRequest from a JSON string
tenants_post_tenants_request_instance = TenantsPostTenantsRequest.from_json(json)
# print the JSON string representation of the object
print(TenantsPostTenantsRequest.to_json())

# convert the object into a dict
tenants_post_tenants_request_dict = tenants_post_tenants_request_instance.to_dict()
# create an instance of TenantsPostTenantsRequest from a dict
tenants_post_tenants_request_from_dict = TenantsPostTenantsRequest.from_dict(tenants_post_tenants_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


