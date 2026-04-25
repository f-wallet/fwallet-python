# ApiRequestLogPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**limit** | **int** |  | 
**has_next_page** | **bool** |  | 
**has_previous_page** | **bool** |  | 

## Example

```python
from fwallet.models.api_request_log_pagination import ApiRequestLogPagination

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRequestLogPagination from a JSON string
api_request_log_pagination_instance = ApiRequestLogPagination.from_json(json)
# print the JSON string representation of the object
print(ApiRequestLogPagination.to_json())

# convert the object into a dict
api_request_log_pagination_dict = api_request_log_pagination_instance.to_dict()
# create an instance of ApiRequestLogPagination from a dict
api_request_log_pagination_from_dict = ApiRequestLogPagination.from_dict(api_request_log_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


