# BankStatementLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | Bank transaction reference | 
**amount** | **float** | Transaction amount in human-readable units | 
**currency_code** | **str** | Transaction currency | 
**var_date** | **str** | Transaction date (YYYY-MM-DD) | 
**description** | **str** | Optional bank description | [optional] 

## Example

```python
from fwallet.models.bank_statement_line import BankStatementLine

# TODO update the JSON string below
json = "{}"
# create an instance of BankStatementLine from a JSON string
bank_statement_line_instance = BankStatementLine.from_json(json)
# print the JSON string representation of the object
print(BankStatementLine.to_json())

# convert the object into a dict
bank_statement_line_dict = bank_statement_line_instance.to_dict()
# create an instance of BankStatementLine from a dict
bank_statement_line_from_dict = BankStatementLine.from_dict(bank_statement_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


