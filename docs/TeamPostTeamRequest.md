# TeamPostTeamRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 
**password** | **str** |  | 
**org_role** | **str** |  | 
**branch_id** | **str** |  | [optional] 

## Example

```python
from fwallet.models.team_post_team_request import TeamPostTeamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TeamPostTeamRequest from a JSON string
team_post_team_request_instance = TeamPostTeamRequest.from_json(json)
# print the JSON string representation of the object
print(TeamPostTeamRequest.to_json())

# convert the object into a dict
team_post_team_request_dict = team_post_team_request_instance.to_dict()
# create an instance of TeamPostTeamRequest from a dict
team_post_team_request_from_dict = TeamPostTeamRequest.from_dict(team_post_team_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


