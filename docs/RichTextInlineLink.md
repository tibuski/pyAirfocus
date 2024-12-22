# RichTextInlineLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**RichTextInline**](RichTextInline.md) |  | 
**url** | **str** |  | 

## Example

```python
from openapi_client.models.rich_text_inline_link import RichTextInlineLink

# TODO update the JSON string below
json = "{}"
# create an instance of RichTextInlineLink from a JSON string
rich_text_inline_link_instance = RichTextInlineLink.from_json(json)
# print the JSON string representation of the object
print(RichTextInlineLink.to_json())

# convert the object into a dict
rich_text_inline_link_dict = rich_text_inline_link_instance.to_dict()
# create an instance of RichTextInlineLink from a dict
rich_text_inline_link_from_dict = RichTextInlineLink.from_dict(rich_text_inline_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


