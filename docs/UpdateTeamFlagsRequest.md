# UpdateTeamFlagsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_ai** | **bool** |  | [optional] 
**enable_okr_app** | **bool** |  | [optional] 
**remove_branding** | **bool** |  | [optional] 
**require_portal_password** | **bool** |  | [optional] 
**require_share_link_password** | **bool** |  | [optional] 
**restrict_share_link_creation** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.update_team_flags_request import UpdateTeamFlagsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTeamFlagsRequest from a JSON string
update_team_flags_request_instance = UpdateTeamFlagsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTeamFlagsRequest.to_json())

# convert the object into a dict
update_team_flags_request_dict = update_team_flags_request_instance.to_dict()
# create an instance of UpdateTeamFlagsRequest from a dict
update_team_flags_request_from_dict = UpdateTeamFlagsRequest.from_dict(update_team_flags_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


