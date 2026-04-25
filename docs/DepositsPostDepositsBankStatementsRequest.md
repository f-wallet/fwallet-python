# DepositsPostDepositsBankStatementsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lines** | [**List[BankStatementLine]**](BankStatementLine.md) | Bank statement lines to import | 

## Example

```python
from fwallet.models.deposits_post_deposits_bank_statements_request import DepositsPostDepositsBankStatementsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DepositsPostDepositsBankStatementsRequest from a JSON string
deposits_post_deposits_bank_statements_request_instance = DepositsPostDepositsBankStatementsRequest.from_json(json)
# print the JSON string representation of the object
print(DepositsPostDepositsBankStatementsRequest.to_json())

# convert the object into a dict
deposits_post_deposits_bank_statements_request_dict = deposits_post_deposits_bank_statements_request_instance.to_dict()
# create an instance of DepositsPostDepositsBankStatementsRequest from a dict
deposits_post_deposits_bank_statements_request_from_dict = DepositsPostDepositsBankStatementsRequest.from_dict(deposits_post_deposits_bank_statements_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


