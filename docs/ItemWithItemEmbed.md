# ItemWithItemEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**ItemEmbed**](ItemEmbed.md) |  | 
**archived** | **bool** |  | 
**assignee_user_ids** | **List[str]** |  | [optional] 
**color** | [**ItemColor**](ItemColor.md) |  | 
**created_at** | **datetime** |  | 
**description** | [**RichText**](RichText.md) |  | 
**fields** | **Dict[str, object]** | Values of custom fields, where each key is a custom-field ID and each value is a JSON-formatted value of the corresponding field. | 
**id** | **str** |  | 
**last_updated_at** | **datetime** |  | 
**name** | **str** |  | 
**number** | **int** |  | [optional] 
**order** | **int** |  | 
**status_category_updated_at** | **datetime** |  | [optional] 
**status_id** | **str** |  | 
**status_updated_at** | **datetime** |  | [optional] 
**workspace_id** | **str** |  | 

## Example

```python
from openapi_client.models.item_with_item_embed import ItemWithItemEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of ItemWithItemEmbed from a JSON string
item_with_item_embed_instance = ItemWithItemEmbed.from_json(json)
# print the JSON string representation of the object
print(ItemWithItemEmbed.to_json())

# convert the object into a dict
item_with_item_embed_dict = item_with_item_embed_instance.to_dict()
# create an instance of ItemWithItemEmbed from a dict
item_with_item_embed_from_dict = ItemWithItemEmbed.from_dict(item_with_item_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


