# ItemRelationWithEmbedPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ItemRelationWithEmbed]**](ItemRelationWithEmbed.md) |  | [optional] 
**total_items** | **int** |  | 

## Example

```python
from openapi_client.models.item_relation_with_embed_page import ItemRelationWithEmbedPage

# TODO update the JSON string below
json = "{}"
# create an instance of ItemRelationWithEmbedPage from a JSON string
item_relation_with_embed_page_instance = ItemRelationWithEmbedPage.from_json(json)
# print the JSON string representation of the object
print(ItemRelationWithEmbedPage.to_json())

# convert the object into a dict
item_relation_with_embed_page_dict = item_relation_with_embed_page_instance.to_dict()
# create an instance of ItemRelationWithEmbedPage from a dict
item_relation_with_embed_page_from_dict = ItemRelationWithEmbedPage.from_dict(item_relation_with_embed_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


