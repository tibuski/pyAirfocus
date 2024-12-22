# RichTextBlockAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment_id** | **str** |  | 
**caption** | **str** |  | [optional] 
**content_type** | **str** |  | 
**width** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.rich_text_block_attachment import RichTextBlockAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of RichTextBlockAttachment from a JSON string
rich_text_block_attachment_instance = RichTextBlockAttachment.from_json(json)
# print the JSON string representation of the object
print(RichTextBlockAttachment.to_json())

# convert the object into a dict
rich_text_block_attachment_dict = rich_text_block_attachment_instance.to_dict()
# create an instance of RichTextBlockAttachment from a dict
rich_text_block_attachment_from_dict = RichTextBlockAttachment.from_dict(rich_text_block_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


