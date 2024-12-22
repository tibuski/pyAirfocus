# RichTextBlockPanel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color_hex** | **str** |  | 
**content** | [**RichTextBlock**](RichTextBlock.md) |  | 

## Example

```python
from openapi_client.models.rich_text_block_panel import RichTextBlockPanel

# TODO update the JSON string below
json = "{}"
# create an instance of RichTextBlockPanel from a JSON string
rich_text_block_panel_instance = RichTextBlockPanel.from_json(json)
# print the JSON string representation of the object
print(RichTextBlockPanel.to_json())

# convert the object into a dict
rich_text_block_panel_dict = rich_text_block_panel_instance.to_dict()
# create an instance of RichTextBlockPanel from a dict
rich_text_block_panel_from_dict = RichTextBlockPanel.from_dict(rich_text_block_panel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


