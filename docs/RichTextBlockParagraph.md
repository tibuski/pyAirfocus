# RichTextBlockParagraph


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[RichTextInline]**](RichTextInline.md) |  | [optional] 

## Example

```python
from openapi_client.models.rich_text_block_paragraph import RichTextBlockParagraph

# TODO update the JSON string below
json = "{}"
# create an instance of RichTextBlockParagraph from a JSON string
rich_text_block_paragraph_instance = RichTextBlockParagraph.from_json(json)
# print the JSON string representation of the object
print(RichTextBlockParagraph.to_json())

# convert the object into a dict
rich_text_block_paragraph_dict = rich_text_block_paragraph_instance.to_dict()
# create an instance of RichTextBlockParagraph from a dict
rich_text_block_paragraph_from_dict = RichTextBlockParagraph.from_dict(rich_text_block_paragraph_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


