# BankSlipVerifyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **UUID** | Wallet to credit if the slip is verified | 
**reference** | **str** | Bank slip reference number. Matched against imported bank statement lines. | 
**amount** | **float** | Deposit amount in human-readable units | 
**currency_code** | **str** | Deposit currency | 

## Example

```python
from fwallet.models.bank_slip_verify_request import BankSlipVerifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BankSlipVerifyRequest from a JSON string
bank_slip_verify_request_instance = BankSlipVerifyRequest.from_json(json)
# print the JSON string representation of the object
print(BankSlipVerifyRequest.to_json())

# convert the object into a dict
bank_slip_verify_request_dict = bank_slip_verify_request_instance.to_dict()
# create an instance of BankSlipVerifyRequest from a dict
bank_slip_verify_request_from_dict = BankSlipVerifyRequest.from_dict(bank_slip_verify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


