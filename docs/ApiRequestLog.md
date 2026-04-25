# ApiRequestLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**application_id** | **UUID** |  | 
**api_key_id** | **UUID** |  | 
**auth_mode** | **str** |  | 
**environment** | **str** |  | 
**method** | **str** |  | 
**path** | **str** |  | 
**route_pattern** | **str** |  | 
**status_code** | **int** |  | 
**error_code** | **str** |  | 
**duration_ms** | **int** |  | 
**correlation_id** | **str** |  | 
**idempotency_key** | **str** |  | 
**origin** | **str** |  | 
**ip_address** | **str** |  | 
**user_agent_hash** | **str** |  | 
**actor_type** | **str** |  | 
**actor_id** | **str** |  | 
**request_body_hash** | **str** |  | 
**request_signature_verified** | **bool** |  | 
**created_at** | **str** |  | 

## Example

```python
from fwallet.models.api_request_log import ApiRequestLog

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRequestLog from a JSON string
api_request_log_instance = ApiRequestLog.from_json(json)
# print the JSON string representation of the object
print(ApiRequestLog.to_json())

# convert the object into a dict
api_request_log_dict = api_request_log_instance.to_dict()
# create an instance of ApiRequestLog from a dict
api_request_log_from_dict = ApiRequestLog.from_dict(api_request_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


