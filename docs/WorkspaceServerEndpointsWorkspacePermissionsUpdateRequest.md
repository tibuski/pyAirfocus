# WorkspaceServerEndpointsWorkspacePermissionsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_permission** | [**Permission**](Permission.md) |  | [optional] 
**permissions** | [**Dict[str, Permission]**](Permission.md) | Explicit permissions for specific users in the team. | 

## Example

```python
from openapi_client.models.workspace_server_endpoints_workspace_permissions_update_request import WorkspaceServerEndpointsWorkspacePermissionsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceServerEndpointsWorkspacePermissionsUpdateRequest from a JSON string
workspace_server_endpoints_workspace_permissions_update_request_instance = WorkspaceServerEndpointsWorkspacePermissionsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceServerEndpointsWorkspacePermissionsUpdateRequest.to_json())

# convert the object into a dict
workspace_server_endpoints_workspace_permissions_update_request_dict = workspace_server_endpoints_workspace_permissions_update_request_instance.to_dict()
# create an instance of WorkspaceServerEndpointsWorkspacePermissionsUpdateRequest from a dict
workspace_server_endpoints_workspace_permissions_update_request_from_dict = WorkspaceServerEndpointsWorkspacePermissionsUpdateRequest.from_dict(workspace_server_endpoints_workspace_permissions_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


