# WorkspaceBulkCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**Workspace**](Workspace.md) |  | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.workspace_bulk_create import WorkspaceBulkCreate

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceBulkCreate from a JSON string
workspace_bulk_create_instance = WorkspaceBulkCreate.from_json(json)
# print the JSON string representation of the object
print(WorkspaceBulkCreate.to_json())

# convert the object into a dict
workspace_bulk_create_dict = workspace_bulk_create_instance.to_dict()
# create an instance of WorkspaceBulkCreate from a dict
workspace_bulk_create_from_dict = WorkspaceBulkCreate.from_dict(workspace_bulk_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


