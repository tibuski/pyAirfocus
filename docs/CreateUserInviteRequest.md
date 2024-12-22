# CreateUserInviteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 

## Example

```python
from openapi_client.models.create_user_invite_request import CreateUserInviteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserInviteRequest from a JSON string
create_user_invite_request_instance = CreateUserInviteRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUserInviteRequest.to_json())

# convert the object into a dict
create_user_invite_request_dict = create_user_invite_request_instance.to_dict()
# create an instance of CreateUserInviteRequest from a dict
create_user_invite_request_from_dict = CreateUserInviteRequest.from_dict(create_user_invite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


