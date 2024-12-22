# WorkspaceGroupAssignWorkspaceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_group_id** | **str** |  | [optional] 
**workspace_id** | **str** |  | 

## Example

```python
from openapi_client.models.workspace_group_assign_workspace_request import WorkspaceGroupAssignWorkspaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceGroupAssignWorkspaceRequest from a JSON string
workspace_group_assign_workspace_request_instance = WorkspaceGroupAssignWorkspaceRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceGroupAssignWorkspaceRequest.to_json())

# convert the object into a dict
workspace_group_assign_workspace_request_dict = workspace_group_assign_workspace_request_instance.to_dict()
# create an instance of WorkspaceGroupAssignWorkspaceRequest from a dict
workspace_group_assign_workspace_request_from_dict = WorkspaceGroupAssignWorkspaceRequest.from_dict(workspace_group_assign_workspace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


