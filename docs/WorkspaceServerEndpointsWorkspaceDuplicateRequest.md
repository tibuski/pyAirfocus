# WorkspaceServerEndpointsWorkspaceDuplicateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duplicate_permissions** | **bool** | Whether to also duplicate all user-permissions to the new workspace. | 

## Example

```python
from openapi_client.models.workspace_server_endpoints_workspace_duplicate_request import WorkspaceServerEndpointsWorkspaceDuplicateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceServerEndpointsWorkspaceDuplicateRequest from a JSON string
workspace_server_endpoints_workspace_duplicate_request_instance = WorkspaceServerEndpointsWorkspaceDuplicateRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceServerEndpointsWorkspaceDuplicateRequest.to_json())

# convert the object into a dict
workspace_server_endpoints_workspace_duplicate_request_dict = workspace_server_endpoints_workspace_duplicate_request_instance.to_dict()
# create an instance of WorkspaceServerEndpointsWorkspaceDuplicateRequest from a dict
workspace_server_endpoints_workspace_duplicate_request_from_dict = WorkspaceServerEndpointsWorkspaceDuplicateRequest.from_dict(workspace_server_endpoints_workspace_duplicate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


