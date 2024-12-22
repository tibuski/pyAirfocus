# ItemLinkEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | [**Dict[str, ItemLinkEmbedApp]**](ItemLinkEmbedApp.md) |  | 
**constraints** | [**List[LinkConstraint]**](LinkConstraint.md) |  | [optional] 
**from_workspace_id** | **str** |  | 
**to_workspace_id** | **str** |  | 

## Example

```python
from openapi_client.models.item_link_embed import ItemLinkEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of ItemLinkEmbed from a JSON string
item_link_embed_instance = ItemLinkEmbed.from_json(json)
# print the JSON string representation of the object
print(ItemLinkEmbed.to_json())

# convert the object into a dict
item_link_embed_dict = item_link_embed_instance.to_dict()
# create an instance of ItemLinkEmbed from a dict
item_link_embed_from_dict = ItemLinkEmbed.from_dict(item_link_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


