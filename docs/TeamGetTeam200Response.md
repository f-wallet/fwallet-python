# TeamGetTeam200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TeamGetTeam200ResponseDataInner]**](TeamGetTeam200ResponseDataInner.md) |  | 

## Example

```python
from fwallet.models.team_get_team200_response import TeamGetTeam200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TeamGetTeam200Response from a JSON string
team_get_team200_response_instance = TeamGetTeam200Response.from_json(json)
# print the JSON string representation of the object
print(TeamGetTeam200Response.to_json())

# convert the object into a dict
team_get_team200_response_dict = team_get_team200_response_instance.to_dict()
# create an instance of TeamGetTeam200Response from a dict
team_get_team200_response_from_dict = TeamGetTeam200Response.from_dict(team_get_team200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


