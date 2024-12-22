# RichTextListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**RichTextBlock**](RichTextBlock.md) |  | 

## Example

```python
from openapi_client.models.rich_text_list_item import RichTextListItem

# TODO update the JSON string below
json = "{}"
# create an instance of RichTextListItem from a JSON string
rich_text_list_item_instance = RichTextListItem.from_json(json)
# print the JSON string representation of the object
print(RichTextListItem.to_json())

# convert the object into a dict
rich_text_list_item_dict = rich_text_list_item_instance.to_dict()
# create an instance of RichTextListItem from a dict
rich_text_list_item_from_dict = RichTextListItem.from_dict(rich_text_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


