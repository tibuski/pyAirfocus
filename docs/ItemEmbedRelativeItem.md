# ItemEmbedRelativeItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** |  | [optional] 
**child_order** | **int** |  | 
**item** | [**Item**](Item.md) |  | [optional] 
**item_id** | **str** |  | 
**item_type** | [**ItemType**](ItemType.md) |  | [optional] 
**parent_order** | **int** |  | 
**relation_id** | **str** |  | 
**workspace_id** | **str** |  | 

## Example

```python
from openapi_client.models.item_embed_relative_item import ItemEmbedRelativeItem

# TODO update the JSON string below
json = "{}"
# create an instance of ItemEmbedRelativeItem from a JSON string
item_embed_relative_item_instance = ItemEmbedRelativeItem.from_json(json)
# print the JSON string representation of the object
print(ItemEmbedRelativeItem.to_json())

# convert the object into a dict
item_embed_relative_item_dict = item_embed_relative_item_instance.to_dict()
# create an instance of ItemEmbedRelativeItem from a dict
item_embed_relative_item_from_dict = ItemEmbedRelativeItem.from_dict(item_embed_relative_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


