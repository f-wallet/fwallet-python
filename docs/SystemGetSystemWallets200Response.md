# SystemGetSystemWallets200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SystemGetSystemWallets200ResponseDataInner]**](SystemGetSystemWallets200ResponseDataInner.md) |  | 

## Example

```python
from fwallet.models.system_get_system_wallets200_response import SystemGetSystemWallets200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SystemGetSystemWallets200Response from a JSON string
system_get_system_wallets200_response_instance = SystemGetSystemWallets200Response.from_json(json)
# print the JSON string representation of the object
print(SystemGetSystemWallets200Response.to_json())

# convert the object into a dict
system_get_system_wallets200_response_dict = system_get_system_wallets200_response_instance.to_dict()
# create an instance of SystemGetSystemWallets200Response from a dict
system_get_system_wallets200_response_from_dict = SystemGetSystemWallets200Response.from_dict(system_get_system_wallets200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


