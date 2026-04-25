# DeveloperGetDeveloperRequestLogs200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiRequestLog]**](ApiRequestLog.md) |  | 
**pagination** | [**ApiRequestLogPagination**](ApiRequestLogPagination.md) |  | 

## Example

```python
from fwallet.models.developer_get_developer_request_logs200_response import DeveloperGetDeveloperRequestLogs200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperGetDeveloperRequestLogs200Response from a JSON string
developer_get_developer_request_logs200_response_instance = DeveloperGetDeveloperRequestLogs200Response.from_json(json)
# print the JSON string representation of the object
print(DeveloperGetDeveloperRequestLogs200Response.to_json())

# convert the object into a dict
developer_get_developer_request_logs200_response_dict = developer_get_developer_request_logs200_response_instance.to_dict()
# create an instance of DeveloperGetDeveloperRequestLogs200Response from a dict
developer_get_developer_request_logs200_response_from_dict = DeveloperGetDeveloperRequestLogs200Response.from_dict(developer_get_developer_request_logs200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


