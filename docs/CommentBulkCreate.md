# CommentBulkCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**Comment**](Comment.md) |  | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.comment_bulk_create import CommentBulkCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CommentBulkCreate from a JSON string
comment_bulk_create_instance = CommentBulkCreate.from_json(json)
# print the JSON string representation of the object
print(CommentBulkCreate.to_json())

# convert the object into a dict
comment_bulk_create_dict = comment_bulk_create_instance.to_dict()
# create an instance of CommentBulkCreate from a dict
comment_bulk_create_from_dict = CommentBulkCreate.from_dict(comment_bulk_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


