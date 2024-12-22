# TeamFlags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_ai** | [**TeamFlag**](TeamFlag.md) |  | 
**enable_okr_app** | [**TeamFlag**](TeamFlag.md) |  | 
**remove_branding** | [**TeamFlag**](TeamFlag.md) |  | 
**require_portal_password** | [**TeamFlag**](TeamFlag.md) |  | 
**require_share_link_password** | [**TeamFlag**](TeamFlag.md) |  | 
**restrict_share_link_creation** | [**TeamFlag**](TeamFlag.md) |  | 

## Example

```python
from openapi_client.models.team_flags import TeamFlags

# TODO update the JSON string below
json = "{}"
# create an instance of TeamFlags from a JSON string
team_flags_instance = TeamFlags.from_json(json)
# print the JSON string representation of the object
print(TeamFlags.to_json())

# convert the object into a dict
team_flags_dict = team_flags_instance.to_dict()
# create an instance of TeamFlags from a dict
team_flags_from_dict = TeamFlags.from_dict(team_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


