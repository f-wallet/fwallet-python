# AdminGetAdminDashboard200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **UUID** |  | 
**tenant_name** | **str** |  | 
**wallet_count** | **float** |  | 
**total_transactions** | **float** |  | 
**revenue_byurrency** | [**List[AdminGetAdminDashboard200ResponseRevenueByurrencyInner]**](AdminGetAdminDashboard200ResponseRevenueByurrencyInner.md) |  | 
**tvl_by_currency** | [**List[AdminGetAdminDashboard200ResponseTvlByCurrencyInner]**](AdminGetAdminDashboard200ResponseTvlByCurrencyInner.md) |  | 
**pool_balances** | [**List[AdminGetAdminDashboard200ResponsePoolBalancesInner]**](AdminGetAdminDashboard200ResponsePoolBalancesInner.md) |  | 

## Example

```python
from fwallet.models.admin_get_admin_dashboard200_response import AdminGetAdminDashboard200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGetAdminDashboard200Response from a JSON string
admin_get_admin_dashboard200_response_instance = AdminGetAdminDashboard200Response.from_json(json)
# print the JSON string representation of the object
print(AdminGetAdminDashboard200Response.to_json())

# convert the object into a dict
admin_get_admin_dashboard200_response_dict = admin_get_admin_dashboard200_response_instance.to_dict()
# create an instance of AdminGetAdminDashboard200Response from a dict
admin_get_admin_dashboard200_response_from_dict = AdminGetAdminDashboard200Response.from_dict(admin_get_admin_dashboard200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


