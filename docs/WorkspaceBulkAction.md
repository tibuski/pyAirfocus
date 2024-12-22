# WorkspaceBulkAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**Workspace**](Workspace.md) |  | 
**type** | **str** |  | 
**id** | **str** |  | 
**transform** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) | A JSON Patch document. See https://jsonpatch.com/ for more information. | 

## Example

```python
from openapi_client.models.workspace_bulk_action import WorkspaceBulkAction

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceBulkAction from a JSON string
workspace_bulk_action_instance = WorkspaceBulkAction.from_json(json)
# print the JSON string representation of the object
print(WorkspaceBulkAction.to_json())

# convert the object into a dict
workspace_bulk_action_dict = workspace_bulk_action_instance.to_dict()
# create an instance of WorkspaceBulkAction from a dict
workspace_bulk_action_from_dict = WorkspaceBulkAction.from_dict(workspace_bulk_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


