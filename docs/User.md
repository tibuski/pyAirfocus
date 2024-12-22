# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_attachment_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**disabled** | **bool** |  | 
**email** | **str** |  | 
**email_verified** | **bool** |  | 
**full_name** | **str** |  | 
**is_team_creator** | **bool** |  | 
**last_seen_at** | **datetime** |  | [optional] 
**role** | [**Role**](Role.md) |  | 
**state** | [**UserState**](UserState.md) |  | 
**team_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**user_id** | **str** |  | 

## Example

```python
from openapi_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


