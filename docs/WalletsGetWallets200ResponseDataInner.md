# WalletsGetWallets200ResponseDataInner

A wallet represents a user-facing balance in a single currency. Under the hood, each wallet maps to a ledger account where all movements are recorded as double-entry journal postings. Balances are materialized and updated atomically with each posting.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique wallet identifier | 
**tenant_id** | **UUID** | Tenant this wallet belongs to | 
**owner_type** | **str** | Owner entity type | 
**owner_id** | **str** | External owner identifier | 
**currency_code** | **str** | Wallet currency (ISO 4217) | 
**status** | **str** | Wallet lifecycle status. Frozen wallets cannot send but can receive; closed wallets are fully inactive. | 
**balance** | [**WalletsGetWallets200ResponseDataInnerBalance**](WalletsGetWallets200ResponseDataInnerBalance.md) |  | 
**created_at** | **str** | ISO 8601 creation timestamp | 

## Example

```python
from fwallet.models.wallets_get_wallets200_response_data_inner import WalletsGetWallets200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of WalletsGetWallets200ResponseDataInner from a JSON string
wallets_get_wallets200_response_data_inner_instance = WalletsGetWallets200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(WalletsGetWallets200ResponseDataInner.to_json())

# convert the object into a dict
wallets_get_wallets200_response_data_inner_dict = wallets_get_wallets200_response_data_inner_instance.to_dict()
# create an instance of WalletsGetWallets200ResponseDataInner from a dict
wallets_get_wallets200_response_data_inner_from_dict = WalletsGetWallets200ResponseDataInner.from_dict(wallets_get_wallets200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


