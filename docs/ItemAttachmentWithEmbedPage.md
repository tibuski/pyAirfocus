# ItemAttachmentWithEmbedPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ItemAttachmentWithEmbed]**](ItemAttachmentWithEmbed.md) |  | [optional] 
**total_items** | **int** |  | 

## Example

```python
from openapi_client.models.item_attachment_with_embed_page import ItemAttachmentWithEmbedPage

# TODO update the JSON string below
json = "{}"
# create an instance of ItemAttachmentWithEmbedPage from a JSON string
item_attachment_with_embed_page_instance = ItemAttachmentWithEmbedPage.from_json(json)
# print the JSON string representation of the object
print(ItemAttachmentWithEmbedPage.to_json())

# convert the object into a dict
item_attachment_with_embed_page_dict = item_attachment_with_embed_page_instance.to_dict()
# create an instance of ItemAttachmentWithEmbedPage from a dict
item_attachment_with_embed_page_from_dict = ItemAttachmentWithEmbedPage.from_dict(item_attachment_with_embed_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


