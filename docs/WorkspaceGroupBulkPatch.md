# WorkspaceGroupBulkPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**transform** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) | A JSON Patch document. See https://jsonpatch.com/ for more information. | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.workspace_group_bulk_patch import WorkspaceGroupBulkPatch

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceGroupBulkPatch from a JSON string
workspace_group_bulk_patch_instance = WorkspaceGroupBulkPatch.from_json(json)
# print the JSON string representation of the object
print(WorkspaceGroupBulkPatch.to_json())

# convert the object into a dict
workspace_group_bulk_patch_dict = workspace_group_bulk_patch_instance.to_dict()
# create an instance of WorkspaceGroupBulkPatch from a dict
workspace_group_bulk_patch_from_dict = WorkspaceGroupBulkPatch.from_dict(workspace_group_bulk_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


