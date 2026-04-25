# SystemPostSystemOrganizationsRequest

Create a new tenant (organization). On creation, the system auto-provisions: system ledger accounts (pool, MoMo clearing, bank clearing, payout clearing, fee revenue, suspense) for each allowed currency, and a default fee schedule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name of the organization | 
**slug** | **str** | URL-safe unique identifier for the tenant | 
**config** | [**TenantsPostTenantsRequestConfig**](TenantsPostTenantsRequestConfig.md) |  | 
**admin** | [**SystemPostSystemOrganizationsRequestAdmin**](SystemPostSystemOrganizationsRequestAdmin.md) |  | 

## Example

```python
from fwallet.models.system_post_system_organizations_request import SystemPostSystemOrganizationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SystemPostSystemOrganizationsRequest from a JSON string
system_post_system_organizations_request_instance = SystemPostSystemOrganizationsRequest.from_json(json)
# print the JSON string representation of the object
print(SystemPostSystemOrganizationsRequest.to_json())

# convert the object into a dict
system_post_system_organizations_request_dict = system_post_system_organizations_request_instance.to_dict()
# create an instance of SystemPostSystemOrganizationsRequest from a dict
system_post_system_organizations_request_from_dict = SystemPostSystemOrganizationsRequest.from_dict(system_post_system_organizations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


