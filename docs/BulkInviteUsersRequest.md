# BulkInviteUsersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[BulkInviteUsersRequestUser]**](BulkInviteUsersRequestUser.md) |  | [optional] 

## Example

```python
from openapi_client.models.bulk_invite_users_request import BulkInviteUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkInviteUsersRequest from a JSON string
bulk_invite_users_request_instance = BulkInviteUsersRequest.from_json(json)
# print the JSON string representation of the object
print(BulkInviteUsersRequest.to_json())

# convert the object into a dict
bulk_invite_users_request_dict = bulk_invite_users_request_instance.to_dict()
# create an instance of BulkInviteUsersRequest from a dict
bulk_invite_users_request_from_dict = BulkInviteUsersRequest.from_dict(bulk_invite_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


