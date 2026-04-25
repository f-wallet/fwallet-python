# WalletsGetWallets200ResponseDataInnerBalance

Wallet balance breakdown. All values are strings representing bigint amounts in the smallest currency unit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **str** | Spendable balance in the smallest currency unit. For UGX this is the shilling; for USD this is cents. | 
**pending** | **str** | Amount currently held (e.g. pending payout approval). Not available for spending. | 

## Example

```python
from fwallet.models.wallets_get_wallets200_response_data_inner_balance import WalletsGetWallets200ResponseDataInnerBalance

# TODO update the JSON string below
json = "{}"
# create an instance of WalletsGetWallets200ResponseDataInnerBalance from a JSON string
wallets_get_wallets200_response_data_inner_balance_instance = WalletsGetWallets200ResponseDataInnerBalance.from_json(json)
# print the JSON string representation of the object
print(WalletsGetWallets200ResponseDataInnerBalance.to_json())

# convert the object into a dict
wallets_get_wallets200_response_data_inner_balance_dict = wallets_get_wallets200_response_data_inner_balance_instance.to_dict()
# create an instance of WalletsGetWallets200ResponseDataInnerBalance from a dict
wallets_get_wallets200_response_data_inner_balance_from_dict = WalletsGetWallets200ResponseDataInnerBalance.from_dict(wallets_get_wallets200_response_data_inner_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


