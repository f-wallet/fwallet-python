# TeamGetTeam200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**org_role** | **str** |  | 
**branch_id** | **str** |  | 
**created_at** | **str** |  | 

## Example

```python
from fwallet.models.team_get_team200_response_data_inner import TeamGetTeam200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of TeamGetTeam200ResponseDataInner from a JSON string
team_get_team200_response_data_inner_instance = TeamGetTeam200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(TeamGetTeam200ResponseDataInner.to_json())

# convert the object into a dict
team_get_team200_response_data_inner_dict = team_get_team200_response_data_inner_instance.to_dict()
# create an instance of TeamGetTeam200ResponseDataInner from a dict
team_get_team200_response_data_inner_from_dict = TeamGetTeam200ResponseDataInner.from_dict(team_get_team200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


