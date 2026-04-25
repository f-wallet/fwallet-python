# WalletsGetWallets200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WalletsGetWallets200ResponseDataInner]**](WalletsGetWallets200ResponseDataInner.md) |  | 

## Example

```python
from fwallet.models.wallets_get_wallets200_response import WalletsGetWallets200Response

# TODO update the JSON string below
json = "{}"
# create an instance of WalletsGetWallets200Response from a JSON string
wallets_get_wallets200_response_instance = WalletsGetWallets200Response.from_json(json)
# print the JSON string representation of the object
print(WalletsGetWallets200Response.to_json())

# convert the object into a dict
wallets_get_wallets200_response_dict = wallets_get_wallets200_response_instance.to_dict()
# create an instance of WalletsGetWallets200Response from a dict
wallets_get_wallets200_response_from_dict = WalletsGetWallets200Response.from_dict(wallets_get_wallets200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


