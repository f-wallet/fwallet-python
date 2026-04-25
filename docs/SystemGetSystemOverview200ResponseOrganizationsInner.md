# SystemGetSystemOverview200ResponseOrganizationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**status** | **str** |  | 
**wallet_count** | **float** |  | 
**transaction_count** | **float** |  | 
**revenue_by_currency** | [**List[SystemGetSystemOverview200ResponseOrganizationsInnerRevenueByCurrencyInner]**](SystemGetSystemOverview200ResponseOrganizationsInnerRevenueByCurrencyInner.md) |  | 
**tvl_by_currency** | [**List[SystemGetSystemOverview200ResponseOrganizationsInnerTvlByCurrencyInner]**](SystemGetSystemOverview200ResponseOrganizationsInnerTvlByCurrencyInner.md) |  | 

## Example

```python
from fwallet.models.system_get_system_overview200_response_organizations_inner import SystemGetSystemOverview200ResponseOrganizationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SystemGetSystemOverview200ResponseOrganizationsInner from a JSON string
system_get_system_overview200_response_organizations_inner_instance = SystemGetSystemOverview200ResponseOrganizationsInner.from_json(json)
# print the JSON string representation of the object
print(SystemGetSystemOverview200ResponseOrganizationsInner.to_json())

# convert the object into a dict
system_get_system_overview200_response_organizations_inner_dict = system_get_system_overview200_response_organizations_inner_instance.to_dict()
# create an instance of SystemGetSystemOverview200ResponseOrganizationsInner from a dict
system_get_system_overview200_response_organizations_inner_from_dict = SystemGetSystemOverview200ResponseOrganizationsInner.from_dict(system_get_system_overview200_response_organizations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


