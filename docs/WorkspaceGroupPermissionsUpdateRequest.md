# WorkspaceGroupPermissionsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**Dict[str, Permission]**](Permission.md) |  | 

## Example

```python
from openapi_client.models.workspace_group_permissions_update_request import WorkspaceGroupPermissionsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceGroupPermissionsUpdateRequest from a JSON string
workspace_group_permissions_update_request_instance = WorkspaceGroupPermissionsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceGroupPermissionsUpdateRequest.to_json())

# convert the object into a dict
workspace_group_permissions_update_request_dict = workspace_group_permissions_update_request_instance.to_dict()
# create an instance of WorkspaceGroupPermissionsUpdateRequest from a dict
workspace_group_permissions_update_request_from_dict = WorkspaceGroupPermissionsUpdateRequest.from_dict(workspace_group_permissions_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


