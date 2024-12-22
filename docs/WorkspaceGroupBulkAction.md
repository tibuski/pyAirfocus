# WorkspaceGroupBulkAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**WorkspaceGroup**](WorkspaceGroup.md) |  | 
**type** | **str** |  | 
**id** | **str** |  | 
**transform** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) | A JSON Patch document. See https://jsonpatch.com/ for more information. | 

## Example

```python
from openapi_client.models.workspace_group_bulk_action import WorkspaceGroupBulkAction

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceGroupBulkAction from a JSON string
workspace_group_bulk_action_instance = WorkspaceGroupBulkAction.from_json(json)
# print the JSON string representation of the object
print(WorkspaceGroupBulkAction.to_json())

# convert the object into a dict
workspace_group_bulk_action_dict = workspace_group_bulk_action_instance.to_dict()
# create an instance of WorkspaceGroupBulkAction from a dict
workspace_group_bulk_action_from_dict = WorkspaceGroupBulkAction.from_dict(workspace_group_bulk_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


