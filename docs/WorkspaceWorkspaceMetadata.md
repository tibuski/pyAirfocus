# WorkspaceWorkspaceMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duplicated** | **bool** |  | 
**template_id** | **str** |  | [optional] 
**template_workspace_ref** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.workspace_workspace_metadata import WorkspaceWorkspaceMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceWorkspaceMetadata from a JSON string
workspace_workspace_metadata_instance = WorkspaceWorkspaceMetadata.from_json(json)
# print the JSON string representation of the object
print(WorkspaceWorkspaceMetadata.to_json())

# convert the object into a dict
workspace_workspace_metadata_dict = workspace_workspace_metadata_instance.to_dict()
# create an instance of WorkspaceWorkspaceMetadata from a dict
workspace_workspace_metadata_from_dict = WorkspaceWorkspaceMetadata.from_dict(workspace_workspace_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


