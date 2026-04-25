# BankSlipResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | verified: reference + amount matched a bank statement line, user has been credited. pending: no matching statement line found yet (bank feed may be delayed). mismatch: reference found but amount differs — flagged for manual review. | 
**journal_entry_id** | **UUID** | Journal entry ID (only present when result is &#39;verified&#39;) | [optional] 

## Example

```python
from fwallet.models.bank_slip_result import BankSlipResult

# TODO update the JSON string below
json = "{}"
# create an instance of BankSlipResult from a JSON string
bank_slip_result_instance = BankSlipResult.from_json(json)
# print the JSON string representation of the object
print(BankSlipResult.to_json())

# convert the object into a dict
bank_slip_result_dict = bank_slip_result_instance.to_dict()
# create an instance of BankSlipResult from a dict
bank_slip_result_from_dict = BankSlipResult.from_dict(bank_slip_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


