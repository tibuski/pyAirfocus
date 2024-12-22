# RichTextBlockHeadline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[RichTextInline]**](RichTextInline.md) |  | [optional] 
**level** | **int** |  | 

## Example

```python
from openapi_client.models.rich_text_block_headline import RichTextBlockHeadline

# TODO update the JSON string below
json = "{}"
# create an instance of RichTextBlockHeadline from a JSON string
rich_text_block_headline_instance = RichTextBlockHeadline.from_json(json)
# print the JSON string representation of the object
print(RichTextBlockHeadline.to_json())

# convert the object into a dict
rich_text_block_headline_dict = rich_text_block_headline_instance.to_dict()
# create an instance of RichTextBlockHeadline from a dict
rich_text_block_headline_from_dict = RichTextBlockHeadline.from_dict(rich_text_block_headline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


