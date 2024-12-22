# CommentBulkAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**Comment**](Comment.md) |  | 
**type** | **str** |  | 
**id** | **str** |  | 
**transform** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) | A JSON Patch document. See https://jsonpatch.com/ for more information. | 

## Example

```python
from openapi_client.models.comment_bulk_action import CommentBulkAction

# TODO update the JSON string below
json = "{}"
# create an instance of CommentBulkAction from a JSON string
comment_bulk_action_instance = CommentBulkAction.from_json(json)
# print the JSON string representation of the object
print(CommentBulkAction.to_json())

# convert the object into a dict
comment_bulk_action_dict = comment_bulk_action_instance.to_dict()
# create an instance of CommentBulkAction from a dict
comment_bulk_action_from_dict = CommentBulkAction.from_dict(comment_bulk_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


