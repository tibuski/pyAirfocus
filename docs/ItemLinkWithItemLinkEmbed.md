# ItemLinkWithItemLinkEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**ItemLinkEmbed**](ItemLinkEmbed.md) |  | 
**from_item_id** | **str** |  | 
**from_order** | **int** | How this link is ordered in the list of links of the \&quot;fromItem\&quot;. | 
**id** | **str** |  | 
**to_item_id** | **str** |  | 
**to_order** | **int** | How this link is ordered in the list of links of the \&quot;toItem\&quot;. | 
**type** | [**ItemLinkType**](ItemLinkType.md) |  | 

## Example

```python
from openapi_client.models.item_link_with_item_link_embed import ItemLinkWithItemLinkEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of ItemLinkWithItemLinkEmbed from a JSON string
item_link_with_item_link_embed_instance = ItemLinkWithItemLinkEmbed.from_json(json)
# print the JSON string representation of the object
print(ItemLinkWithItemLinkEmbed.to_json())

# convert the object into a dict
item_link_with_item_link_embed_dict = item_link_with_item_link_embed_instance.to_dict()
# create an instance of ItemLinkWithItemLinkEmbed from a dict
item_link_with_item_link_embed_from_dict = ItemLinkWithItemLinkEmbed.from_dict(item_link_with_item_link_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


