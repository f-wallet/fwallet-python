# SystemGetSystemTransactions200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**tenant_name** | **str** |  | 
**tenant_slug** | **str** |  | 
**entry_type** | **str** |  | 
**description** | **str** |  | 
**idempotency_key** | **str** |  | 
**posted_at** | **str** |  | 
**lines** | [**List[SystemGetSystemTransactions200ResponseDataInnerLinesInner]**](SystemGetSystemTransactions200ResponseDataInnerLinesInner.md) |  | 

## Example

```python
from fwallet.models.system_get_system_transactions200_response_data_inner import SystemGetSystemTransactions200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of SystemGetSystemTransactions200ResponseDataInner from a JSON string
system_get_system_transactions200_response_data_inner_instance = SystemGetSystemTransactions200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(SystemGetSystemTransactions200ResponseDataInner.to_json())

# convert the object into a dict
system_get_system_transactions200_response_data_inner_dict = system_get_system_transactions200_response_data_inner_instance.to_dict()
# create an instance of SystemGetSystemTransactions200ResponseDataInner from a dict
system_get_system_transactions200_response_data_inner_from_dict = SystemGetSystemTransactions200ResponseDataInner.from_dict(system_get_system_transactions200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


