# JournalGetJournal200ResponseDataInner


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

## Example

```python
from fwallet.models.journal_get_journal200_response_data_inner import JournalGetJournal200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of JournalGetJournal200ResponseDataInner from a JSON string
journal_get_journal200_response_data_inner_instance = JournalGetJournal200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(JournalGetJournal200ResponseDataInner.to_json())

# convert the object into a dict
journal_get_journal200_response_data_inner_dict = journal_get_journal200_response_data_inner_instance.to_dict()
# create an instance of JournalGetJournal200ResponseDataInner from a dict
journal_get_journal200_response_data_inner_from_dict = JournalGetJournal200ResponseDataInner.from_dict(journal_get_journal200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


