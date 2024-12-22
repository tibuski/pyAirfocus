# CommentWithCommentEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | **object** |  | 
**content** | [**RichText**](RichText.md) |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**item_id** | **str** |  | 
**last_updated_at** | **datetime** |  | 
**reactions** | [**List[CommentReaction]**](CommentReaction.md) |  | [optional] 
**user_id** | **str** |  | 

## Example

```python
from openapi_client.models.comment_with_comment_embed import CommentWithCommentEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of CommentWithCommentEmbed from a JSON string
comment_with_comment_embed_instance = CommentWithCommentEmbed.from_json(json)
# print the JSON string representation of the object
print(CommentWithCommentEmbed.to_json())

# convert the object into a dict
comment_with_comment_embed_dict = comment_with_comment_embed_instance.to_dict()
# create an instance of CommentWithCommentEmbed from a dict
comment_with_comment_embed_from_dict = CommentWithCommentEmbed.from_dict(comment_with_comment_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


