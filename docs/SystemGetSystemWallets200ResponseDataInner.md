# SystemGetSystemWallets200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**tenant_name** | **str** |  | 
**tenant_slug** | **str** |  | 
**owner_type** | **str** |  | 
**owner_id** | **str** |  | 
**currency_code** | **str** |  | 
**status** | **str** |  | 
**available** | **str** |  | 
**pending** | **str** |  | 
**created_at** | **str** |  | 

## Example

```python
from fwallet.models.system_get_system_wallets200_response_data_inner import SystemGetSystemWallets200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of SystemGetSystemWallets200ResponseDataInner from a JSON string
system_get_system_wallets200_response_data_inner_instance = SystemGetSystemWallets200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(SystemGetSystemWallets200ResponseDataInner.to_json())

# convert the object into a dict
system_get_system_wallets200_response_data_inner_dict = system_get_system_wallets200_response_data_inner_instance.to_dict()
# create an instance of SystemGetSystemWallets200ResponseDataInner from a dict
system_get_system_wallets200_response_data_inner_from_dict = SystemGetSystemWallets200ResponseDataInner.from_dict(system_get_system_wallets200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


