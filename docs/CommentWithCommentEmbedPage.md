# CommentWithCommentEmbedPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CommentWithCommentEmbed]**](CommentWithCommentEmbed.md) |  | [optional] 
**total_items** | **int** |  | 

## Example

```python
from openapi_client.models.comment_with_comment_embed_page import CommentWithCommentEmbedPage

# TODO update the JSON string below
json = "{}"
# create an instance of CommentWithCommentEmbedPage from a JSON string
comment_with_comment_embed_page_instance = CommentWithCommentEmbedPage.from_json(json)
# print the JSON string representation of the object
print(CommentWithCommentEmbedPage.to_json())

# convert the object into a dict
comment_with_comment_embed_page_dict = comment_with_comment_embed_page_instance.to_dict()
# create an instance of CommentWithCommentEmbedPage from a dict
comment_with_comment_embed_page_from_dict = CommentWithCommentEmbedPage.from_dict(comment_with_comment_embed_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


