# TeamPostTeam201ResponseUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**org_role** | **str** |  | 
**branch_id** | **str** |  | 

## Example

```python
from fwallet.models.team_post_team201_response_user import TeamPostTeam201ResponseUser

# TODO update the JSON string below
json = "{}"
# create an instance of TeamPostTeam201ResponseUser from a JSON string
team_post_team201_response_user_instance = TeamPostTeam201ResponseUser.from_json(json)
# print the JSON string representation of the object
print(TeamPostTeam201ResponseUser.to_json())

# convert the object into a dict
team_post_team201_response_user_dict = team_post_team201_response_user_instance.to_dict()
# create an instance of TeamPostTeam201ResponseUser from a dict
team_post_team201_response_user_from_dict = TeamPostTeam201ResponseUser.from_dict(team_post_team201_response_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


