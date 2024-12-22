# WorkspaceEmbedRelation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relation_id** | **str** |  | 
**workspace** | [**Workspace**](Workspace.md) |  | [optional] 
**workspace_id** | **str** |  | 

## Example

```python
from openapi_client.models.workspace_embed_relation import WorkspaceEmbedRelation

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceEmbedRelation from a JSON string
workspace_embed_relation_instance = WorkspaceEmbedRelation.from_json(json)
# print the JSON string representation of the object
print(WorkspaceEmbedRelation.to_json())

# convert the object into a dict
workspace_embed_relation_dict = workspace_embed_relation_instance.to_dict()
# create an instance of WorkspaceEmbedRelation from a dict
workspace_embed_relation_from_dict = WorkspaceEmbedRelation.from_dict(workspace_embed_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


