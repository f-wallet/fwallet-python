# JournalGetJournalById200Response

An immutable ledger journal entry representing a financial event. Every money movement (deposit, transfer, payout, fee) is recorded as a journal entry with two or more lines that must balance. Entries are never updated or deleted — corrections are posted as new reversing entries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique journal entry identifier | 
**tenant_id** | **UUID** | Tenant this entry belongs to | 
**idempotency_key** | **str** | Client-provided key that prevents duplicate postings. If the same key is sent twice, the original entry is returned. | 
**entry_type** | **str** | Type of financial event: deposit (MoMo/bank), transfer (wallet-to-wallet), payout_hold (funds held pending approval), payout_settlement (approved payout), payout_reversal (rejected payout hold reversal), reversal (generic correction) | 
**description** | **str** | Human-readable description of the entry | 
**posted_at** | **str** | ISO 8601 timestamp when the entry was posted to the ledger | 
**created_at** | **str** | ISO 8601 creation timestamp | 
**lines** | [**List[JournalLine]**](JournalLine.md) | The individual debit/credit postings. For every entry, SUM(debit amounts) &#x3D; SUM(credit amounts) — this is the double-entry invariant. | 

## Example

```python
from fwallet.models.journal_get_journal_by_id200_response import JournalGetJournalById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of JournalGetJournalById200Response from a JSON string
journal_get_journal_by_id200_response_instance = JournalGetJournalById200Response.from_json(json)
# print the JSON string representation of the object
print(JournalGetJournalById200Response.to_json())

# convert the object into a dict
journal_get_journal_by_id200_response_dict = journal_get_journal_by_id200_response_instance.to_dict()
# create an instance of JournalGetJournalById200Response from a dict
journal_get_journal_by_id200_response_from_dict = JournalGetJournalById200Response.from_dict(journal_get_journal_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


