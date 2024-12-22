# CommentReaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emoji** | [**CommentReactionEmoji**](CommentReactionEmoji.md) |  | 
**user_ids** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.comment_reaction import CommentReaction

# TODO update the JSON string below
json = "{}"
# create an instance of CommentReaction from a JSON string
comment_reaction_instance = CommentReaction.from_json(json)
# print the JSON string representation of the object
print(CommentReaction.to_json())

# convert the object into a dict
comment_reaction_dict = comment_reaction_instance.to_dict()
# create an instance of CommentReaction from a dict
comment_reaction_from_dict = CommentReaction.from_dict(comment_reaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


