# SystemGetSystemOverview200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_organizations** | **float** |  | 
**total_wallets** | **float** |  | 
**total_transactions** | **float** |  | 
**organizations** | [**List[SystemGetSystemOverview200ResponseOrganizationsInner]**](SystemGetSystemOverview200ResponseOrganizationsInner.md) |  | 
**platform_revenue_by_currency** | [**List[AdminGetAdminDashboard200ResponseRevenueByurrencyInner]**](AdminGetAdminDashboard200ResponseRevenueByurrencyInner.md) |  | 
**platform_tvl_by_currency** | [**List[SystemGetSystemOverview200ResponsePlatformTvlByCurrencyInner]**](SystemGetSystemOverview200ResponsePlatformTvlByCurrencyInner.md) |  | 

## Example

```python
from fwallet.models.system_get_system_overview200_response import SystemGetSystemOverview200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SystemGetSystemOverview200Response from a JSON string
system_get_system_overview200_response_instance = SystemGetSystemOverview200Response.from_json(json)
# print the JSON string representation of the object
print(SystemGetSystemOverview200Response.to_json())

# convert the object into a dict
system_get_system_overview200_response_dict = system_get_system_overview200_response_instance.to_dict()
# create an instance of SystemGetSystemOverview200Response from a dict
system_get_system_overview200_response_from_dict = SystemGetSystemOverview200Response.from_dict(system_get_system_overview200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


