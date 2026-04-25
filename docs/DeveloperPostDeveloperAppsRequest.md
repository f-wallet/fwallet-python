# DeveloperPostDeveloperAppsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**environment** | **str** |  | [optional] [default to 'test']
**owner_user_id** | **str** |  | [optional] 

## Example

```python
from fwallet.models.developer_post_developer_apps_request import DeveloperPostDeveloperAppsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperPostDeveloperAppsRequest from a JSON string
developer_post_developer_apps_request_instance = DeveloperPostDeveloperAppsRequest.from_json(json)
# print the JSON string representation of the object
print(DeveloperPostDeveloperAppsRequest.to_json())

# convert the object into a dict
developer_post_developer_apps_request_dict = developer_post_developer_apps_request_instance.to_dict()
# create an instance of DeveloperPostDeveloperAppsRequest from a dict
developer_post_developer_apps_request_from_dict = DeveloperPostDeveloperAppsRequest.from_dict(developer_post_developer_apps_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


