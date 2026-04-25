# MoMoDepositResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**journal_entry_id** | **UUID** | The ledger journal entry recording this deposit | 
**wallet_id** | **UUID** | The wallet that was credited | 
**amount** | **str** | Credited amount in smallest currency unit | 
**currency_code** | **str** | Deposit currency | 
**replayed** | **bool** | True if this transactionId was already processed. The original result is returned without double-crediting. | 

## Example

```python
from fwallet.models.mo_mo_deposit_result import MoMoDepositResult

# TODO update the JSON string below
json = "{}"
# create an instance of MoMoDepositResult from a JSON string
mo_mo_deposit_result_instance = MoMoDepositResult.from_json(json)
# print the JSON string representation of the object
print(MoMoDepositResult.to_json())

# convert the object into a dict
mo_mo_deposit_result_dict = mo_mo_deposit_result_instance.to_dict()
# create an instance of MoMoDepositResult from a dict
mo_mo_deposit_result_from_dict = MoMoDepositResult.from_dict(mo_mo_deposit_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


