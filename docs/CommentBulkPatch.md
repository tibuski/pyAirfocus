# CommentBulkPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**transform** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) | A JSON Patch document. See https://jsonpatch.com/ for more information. | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.comment_bulk_patch import CommentBulkPatch

# TODO update the JSON string below
json = "{}"
# create an instance of CommentBulkPatch from a JSON string
comment_bulk_patch_instance = CommentBulkPatch.from_json(json)
# print the JSON string representation of the object
print(CommentBulkPatch.to_json())

# convert the object into a dict
comment_bulk_patch_dict = comment_bulk_patch_instance.to_dict()
# create an instance of CommentBulkPatch from a dict
comment_bulk_patch_from_dict = CommentBulkPatch.from_dict(comment_bulk_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


