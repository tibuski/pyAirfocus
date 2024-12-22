# WorkspaceRelationBulkCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**WorkspaceRelation**](WorkspaceRelation.md) |  | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.workspace_relation_bulk_create import WorkspaceRelationBulkCreate

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceRelationBulkCreate from a JSON string
workspace_relation_bulk_create_instance = WorkspaceRelationBulkCreate.from_json(json)
# print the JSON string representation of the object
print(WorkspaceRelationBulkCreate.to_json())

# convert the object into a dict
workspace_relation_bulk_create_dict = workspace_relation_bulk_create_instance.to_dict()
# create an instance of WorkspaceRelationBulkCreate from a dict
workspace_relation_bulk_create_from_dict = WorkspaceRelationBulkCreate.from_dict(workspace_relation_bulk_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


