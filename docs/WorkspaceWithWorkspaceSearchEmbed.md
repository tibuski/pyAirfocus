# WorkspaceWithWorkspaceSearchEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**WorkspaceSearchEmbed**](WorkspaceSearchEmbed.md) |  | 
**alias** | **str** |  | [optional] 
**archived** | **bool** |  | 
**created_at** | **datetime** |  | 
**default_permission** | [**Permission**](Permission.md) |  | [optional] 
**description** | [**RichText**](RichText.md) |  | 
**id** | **str** |  | 
**item_color** | [**ItemColor**](ItemColor.md) |  | [optional] 
**item_type** | [**ItemType**](ItemType.md) |  | [optional] 
**last_updated_at** | **datetime** |  | 
**legacy_id** | **str** |  | [optional] 
**metadata** | [**WorkspaceWorkspaceMetadata**](WorkspaceWorkspaceMetadata.md) |  | [optional] 
**name** | **str** |  | 
**namespace** | [**WorkspaceNamespace**](WorkspaceNamespace.md) |  | 
**progress_mode** | [**WorkspaceProgressMode**](WorkspaceProgressMode.md) |  | 
**team_id** | **str** |  | 

## Example

```python
from openapi_client.models.workspace_with_workspace_search_embed import WorkspaceWithWorkspaceSearchEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceWithWorkspaceSearchEmbed from a JSON string
workspace_with_workspace_search_embed_instance = WorkspaceWithWorkspaceSearchEmbed.from_json(json)
# print the JSON string representation of the object
print(WorkspaceWithWorkspaceSearchEmbed.to_json())

# convert the object into a dict
workspace_with_workspace_search_embed_dict = workspace_with_workspace_search_embed_instance.to_dict()
# create an instance of WorkspaceWithWorkspaceSearchEmbed from a dict
workspace_with_workspace_search_embed_from_dict = WorkspaceWithWorkspaceSearchEmbed.from_dict(workspace_with_workspace_search_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


