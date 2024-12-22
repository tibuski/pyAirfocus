# WorkspaceGroupBulkCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**WorkspaceGroup**](WorkspaceGroup.md) |  | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.workspace_group_bulk_create import WorkspaceGroupBulkCreate

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceGroupBulkCreate from a JSON string
workspace_group_bulk_create_instance = WorkspaceGroupBulkCreate.from_json(json)
# print the JSON string representation of the object
print(WorkspaceGroupBulkCreate.to_json())

# convert the object into a dict
workspace_group_bulk_create_dict = workspace_group_bulk_create_instance.to_dict()
# create an instance of WorkspaceGroupBulkCreate from a dict
workspace_group_bulk_create_from_dict = WorkspaceGroupBulkCreate.from_dict(workspace_group_bulk_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


