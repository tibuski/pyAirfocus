# ItemRelationWithEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | **object** |  | 
**child_id** | **str** |  | 
**child_order** | **int** |  | 
**id** | **str** |  | 
**parent_id** | **str** |  | 
**parent_order** | **int** |  | 

## Example

```python
from openapi_client.models.item_relation_with_embed import ItemRelationWithEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of ItemRelationWithEmbed from a JSON string
item_relation_with_embed_instance = ItemRelationWithEmbed.from_json(json)
# print the JSON string representation of the object
print(ItemRelationWithEmbed.to_json())

# convert the object into a dict
item_relation_with_embed_dict = item_relation_with_embed_instance.to_dict()
# create an instance of ItemRelationWithEmbed from a dict
item_relation_with_embed_from_dict = ItemRelationWithEmbed.from_dict(item_relation_with_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


