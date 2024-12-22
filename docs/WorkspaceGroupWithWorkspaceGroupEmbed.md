# WorkspaceGroupWithWorkspaceGroupEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**WorkspaceGroupEmbed**](WorkspaceGroupEmbed.md) |  | 
**created_at** | **datetime** |  | 
**default_permission** | [**Permission**](Permission.md) |  | [optional] 
**id** | **str** |  | 
**last_updated_at** | **datetime** |  | 
**name** | **str** |  | 
**team_id** | **str** |  | 

## Example

```python
from openapi_client.models.workspace_group_with_workspace_group_embed import WorkspaceGroupWithWorkspaceGroupEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceGroupWithWorkspaceGroupEmbed from a JSON string
workspace_group_with_workspace_group_embed_instance = WorkspaceGroupWithWorkspaceGroupEmbed.from_json(json)
# print the JSON string representation of the object
print(WorkspaceGroupWithWorkspaceGroupEmbed.to_json())

# convert the object into a dict
workspace_group_with_workspace_group_embed_dict = workspace_group_with_workspace_group_embed_instance.to_dict()
# create an instance of WorkspaceGroupWithWorkspaceGroupEmbed from a dict
workspace_group_with_workspace_group_embed_from_dict = WorkspaceGroupWithWorkspaceGroupEmbed.from_dict(workspace_group_with_workspace_group_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


