# JournalLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Line item ID | 
**account_id** | **UUID** | The ledger account this line posts to | 
**amount** | **str** | Amount in the smallest currency unit (always positive — direction is indicated by the direction field) | 
**direction** | **str** | Debit increases asset/expense accounts and decreases liability/revenue/equity. Credit is the reverse. Every journal entry&#39;s debits must equal its credits. | 
**currency_code** | **str** | ISO 4217 currency code | 

## Example

```python
from fwallet.models.journal_line import JournalLine

# TODO update the JSON string below
json = "{}"
# create an instance of JournalLine from a JSON string
journal_line_instance = JournalLine.from_json(json)
# print the JSON string representation of the object
print(JournalLine.to_json())

# convert the object into a dict
journal_line_dict = journal_line_instance.to_dict()
# create an instance of JournalLine from a dict
journal_line_from_dict = JournalLine.from_dict(journal_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


