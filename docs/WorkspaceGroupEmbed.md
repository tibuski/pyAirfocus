# WorkspaceGroupEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_permission** | [**Permission**](Permission.md) |  | [optional] 
**permissions** | [**Dict[str, Permission]**](Permission.md) |  | 
**workspaces** | [**List[Workspace]**](Workspace.md) |  | [optional] 

## Example

```python
from openapi_client.models.workspace_group_embed import WorkspaceGroupEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceGroupEmbed from a JSON string
workspace_group_embed_instance = WorkspaceGroupEmbed.from_json(json)
# print the JSON string representation of the object
print(WorkspaceGroupEmbed.to_json())

# convert the object into a dict
workspace_group_embed_dict = workspace_group_embed_instance.to_dict()
# create an instance of WorkspaceGroupEmbed from a dict
workspace_group_embed_from_dict = WorkspaceGroupEmbed.from_dict(workspace_group_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


