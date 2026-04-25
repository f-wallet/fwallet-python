# DeveloperPatchDeveloperAppsByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 

## Example

```python
from fwallet.models.developer_patch_developer_apps_by_id_request import DeveloperPatchDeveloperAppsByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperPatchDeveloperAppsByIdRequest from a JSON string
developer_patch_developer_apps_by_id_request_instance = DeveloperPatchDeveloperAppsByIdRequest.from_json(json)
# print the JSON string representation of the object
print(DeveloperPatchDeveloperAppsByIdRequest.to_json())

# convert the object into a dict
developer_patch_developer_apps_by_id_request_dict = developer_patch_developer_apps_by_id_request_instance.to_dict()
# create an instance of DeveloperPatchDeveloperAppsByIdRequest from a dict
developer_patch_developer_apps_by_id_request_from_dict = DeveloperPatchDeveloperAppsByIdRequest.from_dict(developer_patch_developer_apps_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


