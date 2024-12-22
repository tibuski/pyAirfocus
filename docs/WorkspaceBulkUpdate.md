# WorkspaceBulkUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**resource** | [**Workspace**](Workspace.md) |  | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.workspace_bulk_update import WorkspaceBulkUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceBulkUpdate from a JSON string
workspace_bulk_update_instance = WorkspaceBulkUpdate.from_json(json)
# print the JSON string representation of the object
print(WorkspaceBulkUpdate.to_json())

# convert the object into a dict
workspace_bulk_update_dict = workspace_bulk_update_instance.to_dict()
# create an instance of WorkspaceBulkUpdate from a dict
workspace_bulk_update_from_dict = WorkspaceBulkUpdate.from_dict(workspace_bulk_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


