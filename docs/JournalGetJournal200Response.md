# JournalGetJournal200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[JournalGetJournal200ResponseDataInner]**](JournalGetJournal200ResponseDataInner.md) |  | 
**next_cursor** | **str** | Pass this as the cursor param to fetch the next page. Null when no more results. | 
**has_more** | **bool** | True if there are more entries after this page | 

## Example

```python
from fwallet.models.journal_get_journal200_response import JournalGetJournal200Response

# TODO update the JSON string below
json = "{}"
# create an instance of JournalGetJournal200Response from a JSON string
journal_get_journal200_response_instance = JournalGetJournal200Response.from_json(json)
# print the JSON string representation of the object
print(JournalGetJournal200Response.to_json())

# convert the object into a dict
journal_get_journal200_response_dict = journal_get_journal200_response_instance.to_dict()
# create an instance of JournalGetJournal200Response from a dict
journal_get_journal200_response_from_dict = JournalGetJournal200Response.from_dict(journal_get_journal200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


