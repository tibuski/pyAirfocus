# Workspace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from openapi_client.models.workspace import Workspace

# TODO update the JSON string below
json = "{}"
# create an instance of Workspace from a JSON string
workspace_instance = Workspace.from_json(json)
# print the JSON string representation of the object
print(Workspace.to_json())

# convert the object into a dict
workspace_dict = workspace_instance.to_dict()
# create an instance of Workspace from a dict
workspace_from_dict = Workspace.from_dict(workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


