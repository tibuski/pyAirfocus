# ItemWithItemEmbedPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ItemWithItemEmbed]**](ItemWithItemEmbed.md) |  | [optional] 
**total_items** | **int** |  | 

## Example

```python
from openapi_client.models.item_with_item_embed_page import ItemWithItemEmbedPage

# TODO update the JSON string below
json = "{}"
# create an instance of ItemWithItemEmbedPage from a JSON string
item_with_item_embed_page_instance = ItemWithItemEmbedPage.from_json(json)
# print the JSON string representation of the object
print(ItemWithItemEmbedPage.to_json())

# convert the object into a dict
item_with_item_embed_page_dict = item_with_item_embed_page_instance.to_dict()
# create an instance of ItemWithItemEmbedPage from a dict
item_with_item_embed_page_from_dict = ItemWithItemEmbedPage.from_dict(item_with_item_embed_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


