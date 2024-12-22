# CommentBulkUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**resource** | [**Comment**](Comment.md) |  | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.comment_bulk_update import CommentBulkUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CommentBulkUpdate from a JSON string
comment_bulk_update_instance = CommentBulkUpdate.from_json(json)
# print the JSON string representation of the object
print(CommentBulkUpdate.to_json())

# convert the object into a dict
comment_bulk_update_dict = comment_bulk_update_instance.to_dict()
# create an instance of CommentBulkUpdate from a dict
comment_bulk_update_from_dict = CommentBulkUpdate.from_dict(comment_bulk_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


