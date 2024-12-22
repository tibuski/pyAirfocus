# WorkspaceRelationBulkUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**resource** | [**WorkspaceRelation**](WorkspaceRelation.md) |  | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.workspace_relation_bulk_update import WorkspaceRelationBulkUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceRelationBulkUpdate from a JSON string
workspace_relation_bulk_update_instance = WorkspaceRelationBulkUpdate.from_json(json)
# print the JSON string representation of the object
print(WorkspaceRelationBulkUpdate.to_json())

# convert the object into a dict
workspace_relation_bulk_update_dict = workspace_relation_bulk_update_instance.to_dict()
# create an instance of WorkspaceRelationBulkUpdate from a dict
workspace_relation_bulk_update_from_dict = WorkspaceRelationBulkUpdate.from_dict(workspace_relation_bulk_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


