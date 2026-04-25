# HealthGetHealth200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**version** | **str** |  | 
**timestamp** | **str** |  | 

## Example

```python
from fwallet.models.health_get_health200_response import HealthGetHealth200Response

# TODO update the JSON string below
json = "{}"
# create an instance of HealthGetHealth200Response from a JSON string
health_get_health200_response_instance = HealthGetHealth200Response.from_json(json)
# print the JSON string representation of the object
print(HealthGetHealth200Response.to_json())

# convert the object into a dict
health_get_health200_response_dict = health_get_health200_response_instance.to_dict()
# create an instance of HealthGetHealth200Response from a dict
health_get_health200_response_from_dict = HealthGetHealth200Response.from_dict(health_get_health200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


