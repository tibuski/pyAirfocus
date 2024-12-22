# ChangeUserRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**Role**](Role.md) |  | 
**user_id** | **str** |  | 

## Example

```python
from openapi_client.models.change_user_role_request import ChangeUserRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeUserRoleRequest from a JSON string
change_user_role_request_instance = ChangeUserRoleRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeUserRoleRequest.to_json())

# convert the object into a dict
change_user_role_request_dict = change_user_role_request_instance.to_dict()
# create an instance of ChangeUserRoleRequest from a dict
change_user_role_request_from_dict = ChangeUserRoleRequest.from_dict(change_user_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


