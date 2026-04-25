# WalletsPostWalletsRequest

Create a new wallet. Each wallet is backed by a dedicated ledger account (asset:wallet:{ownerType}:{ownerId}:{currency}) with a zero initial balance. A user can have one wallet per currency.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_type** | **str** | Type of entity that owns this wallet. Users hold personal balances; branches manage cash-assisted operations; companies hold operating pools. | 
**owner_id** | **str** | External identifier for the wallet owner (e.g. user ID, branch code). Combined with ownerType and currencyCode, this must be unique per tenant. | 
**currency_code** | **str** | ISO 4217 currency code. UGX and TSH have no decimal subdivisions; KES, USD, CNY, GBP use cents (1/100). | 

## Example

```python
from fwallet.models.wallets_post_wallets_request import WalletsPostWalletsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WalletsPostWalletsRequest from a JSON string
wallets_post_wallets_request_instance = WalletsPostWalletsRequest.from_json(json)
# print the JSON string representation of the object
print(WalletsPostWalletsRequest.to_json())

# convert the object into a dict
wallets_post_wallets_request_dict = wallets_post_wallets_request_instance.to_dict()
# create an instance of WalletsPostWalletsRequest from a dict
wallets_post_wallets_request_from_dict = WalletsPostWalletsRequest.from_dict(wallets_post_wallets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


