# WalletsGetWalletsLookup200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**found** | **bool** |  | 
**user** | [**WalletsGetWalletsLookup200ResponseUser**](WalletsGetWalletsLookup200ResponseUser.md) |  | [optional] 
**wallet** | [**WalletsGetWalletsLookup200ResponseWallet**](WalletsGetWalletsLookup200ResponseWallet.md) |  | [optional] 

## Example

```python
from fwallet.models.wallets_get_wallets_lookup200_response import WalletsGetWalletsLookup200Response

# TODO update the JSON string below
json = "{}"
# create an instance of WalletsGetWalletsLookup200Response from a JSON string
wallets_get_wallets_lookup200_response_instance = WalletsGetWalletsLookup200Response.from_json(json)
# print the JSON string representation of the object
print(WalletsGetWalletsLookup200Response.to_json())

# convert the object into a dict
wallets_get_wallets_lookup200_response_dict = wallets_get_wallets_lookup200_response_instance.to_dict()
# create an instance of WalletsGetWalletsLookup200Response from a dict
wallets_get_wallets_lookup200_response_from_dict = WalletsGetWalletsLookup200Response.from_dict(wallets_get_wallets_lookup200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


