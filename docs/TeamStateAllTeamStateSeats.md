# TeamStateAllTeamStateSeats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin** | [**TeamStateSeats**](TeamStateSeats.md) |  | [optional] 
**any** | [**TeamStateSeats**](TeamStateSeats.md) |  | [optional] 
**contributor** | [**TeamStateSeats**](TeamStateSeats.md) |  | [optional] 
**editor** | [**TeamStateSeats**](TeamStateSeats.md) |  | [optional] 

## Example

```python
from openapi_client.models.team_state_all_team_state_seats import TeamStateAllTeamStateSeats

# TODO update the JSON string below
json = "{}"
# create an instance of TeamStateAllTeamStateSeats from a JSON string
team_state_all_team_state_seats_instance = TeamStateAllTeamStateSeats.from_json(json)
# print the JSON string representation of the object
print(TeamStateAllTeamStateSeats.to_json())

# convert the object into a dict
team_state_all_team_state_seats_dict = team_state_all_team_state_seats_instance.to_dict()
# create an instance of TeamStateAllTeamStateSeats from a dict
team_state_all_team_state_seats_from_dict = TeamStateAllTeamStateSeats.from_dict(team_state_all_team_state_seats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


