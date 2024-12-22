# WorkspaceEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | [**Dict[str, App]**](App.md) |  | 
**children** | [**List[WorkspaceEmbedRelation]**](WorkspaceEmbedRelation.md) |  | [optional] 
**current_permission** | [**Permission**](Permission.md) |  | [optional] 
**fields** | [**Dict[str, FieldWithFieldEmbed]**](FieldWithFieldEmbed.md) |  | 
**integrations** | [**Dict[str, IntegrationSummary]**](IntegrationSummary.md) |  | 
**item_count** | **int** |  | 
**item_status_count** | **Dict[str, int]** |  | 
**item_status_count_archived** | **Dict[str, int]** |  | 
**parents** | [**List[WorkspaceEmbedRelation]**](WorkspaceEmbedRelation.md) |  | [optional] 
**permissions** | [**Dict[str, Permission]**](Permission.md) |  | 
**statuses** | [**Dict[str, Status]**](Status.md) |  | 
**views** | [**Dict[str, View]**](View.md) |  | 

## Example

```python
from openapi_client.models.workspace_embed import WorkspaceEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceEmbed from a JSON string
workspace_embed_instance = WorkspaceEmbed.from_json(json)
# print the JSON string representation of the object
print(WorkspaceEmbed.to_json())

# convert the object into a dict
workspace_embed_dict = workspace_embed_instance.to_dict()
# create an instance of WorkspaceEmbed from a dict
workspace_embed_from_dict = WorkspaceEmbed.from_dict(workspace_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


