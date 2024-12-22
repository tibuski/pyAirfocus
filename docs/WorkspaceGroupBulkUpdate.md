# WorkspaceGroupBulkUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**resource** | [**WorkspaceGroup**](WorkspaceGroup.md) |  | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.workspace_group_bulk_update import WorkspaceGroupBulkUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceGroupBulkUpdate from a JSON string
workspace_group_bulk_update_instance = WorkspaceGroupBulkUpdate.from_json(json)
# print the JSON string representation of the object
print(WorkspaceGroupBulkUpdate.to_json())

# convert the object into a dict
workspace_group_bulk_update_dict = workspace_group_bulk_update_instance.to_dict()
# create an instance of WorkspaceGroupBulkUpdate from a dict
workspace_group_bulk_update_from_dict = WorkspaceGroupBulkUpdate.from_dict(workspace_group_bulk_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


