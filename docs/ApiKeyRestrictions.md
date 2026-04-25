# ApiKeyRestrictions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_origins** | **List[str]** |  | [optional] 
**allowed_ips** | **List[str]** |  | [optional] 
**allowed_currencies** | **List[str]** |  | [optional] 
**allowed_owner_types** | **List[str]** |  | [optional] 
**allowed_wallet_ids** | **List[UUID]** |  | [optional] 
**max_amount_minor** | **str** |  | [optional] 
**require_actor_headers** | **bool** |  | [optional] 
**require_request_signing** | **bool** |  | [optional] 

## Example

```python
from fwallet.models.api_key_restrictions import ApiKeyRestrictions

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyRestrictions from a JSON string
api_key_restrictions_instance = ApiKeyRestrictions.from_json(json)
# print the JSON string representation of the object
print(ApiKeyRestrictions.to_json())

# convert the object into a dict
api_key_restrictions_dict = api_key_restrictions_instance.to_dict()
# create an instance of ApiKeyRestrictions from a dict
api_key_restrictions_from_dict = ApiKeyRestrictions.from_dict(api_key_restrictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


