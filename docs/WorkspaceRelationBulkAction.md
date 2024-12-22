# WorkspaceRelationBulkAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**WorkspaceRelation**](WorkspaceRelation.md) |  | 
**type** | **str** |  | 
**id** | **str** |  | 
**transform** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) | A JSON Patch document. See https://jsonpatch.com/ for more information. | 

## Example

```python
from openapi_client.models.workspace_relation_bulk_action import WorkspaceRelationBulkAction

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceRelationBulkAction from a JSON string
workspace_relation_bulk_action_instance = WorkspaceRelationBulkAction.from_json(json)
# print the JSON string representation of the object
print(WorkspaceRelationBulkAction.to_json())

# convert the object into a dict
workspace_relation_bulk_action_dict = workspace_relation_bulk_action_instance.to_dict()
# create an instance of WorkspaceRelationBulkAction from a dict
workspace_relation_bulk_action_from_dict = WorkspaceRelationBulkAction.from_dict(workspace_relation_bulk_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


