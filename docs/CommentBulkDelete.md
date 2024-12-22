# CommentBulkDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.comment_bulk_delete import CommentBulkDelete

# TODO update the JSON string below
json = "{}"
# create an instance of CommentBulkDelete from a JSON string
comment_bulk_delete_instance = CommentBulkDelete.from_json(json)
# print the JSON string representation of the object
print(CommentBulkDelete.to_json())

# convert the object into a dict
comment_bulk_delete_dict = comment_bulk_delete_instance.to_dict()
# create an instance of CommentBulkDelete from a dict
comment_bulk_delete_from_dict = CommentBulkDelete.from_dict(comment_bulk_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


