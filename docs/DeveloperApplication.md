# DeveloperApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**environment** | **str** |  | 
**status** | **str** |  | 
**owner_user_id** | **str** |  | 
**created_by_user_id** | **str** |  | 
**disabled_at** | **str** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from fwallet.models.developer_application import DeveloperApplication

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperApplication from a JSON string
developer_application_instance = DeveloperApplication.from_json(json)
# print the JSON string representation of the object
print(DeveloperApplication.to_json())

# convert the object into a dict
developer_application_dict = developer_application_instance.to_dict()
# create an instance of DeveloperApplication from a dict
developer_application_from_dict = DeveloperApplication.from_dict(developer_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


