# BulkInviteUsersRequestUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**full_name** | **str** |  | [optional] 
**role** | [**Role**](Role.md) |  | 

## Example

```python
from openapi_client.models.bulk_invite_users_request_user import BulkInviteUsersRequestUser

# TODO update the JSON string below
json = "{}"
# create an instance of BulkInviteUsersRequestUser from a JSON string
bulk_invite_users_request_user_instance = BulkInviteUsersRequestUser.from_json(json)
# print the JSON string representation of the object
print(BulkInviteUsersRequestUser.to_json())

# convert the object into a dict
bulk_invite_users_request_user_dict = bulk_invite_users_request_user_instance.to_dict()
# create an instance of BulkInviteUsersRequestUser from a dict
bulk_invite_users_request_user_from_dict = BulkInviteUsersRequestUser.from_dict(bulk_invite_users_request_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


