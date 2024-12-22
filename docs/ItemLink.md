# ItemLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_item_id** | **str** |  | 
**from_order** | **int** | How this link is ordered in the list of links of the \&quot;fromItem\&quot;. | 
**id** | **str** |  | 
**to_item_id** | **str** |  | 
**to_order** | **int** | How this link is ordered in the list of links of the \&quot;toItem\&quot;. | 
**type** | [**ItemLinkType**](ItemLinkType.md) |  | 

## Example

```python
from openapi_client.models.item_link import ItemLink

# TODO update the JSON string below
json = "{}"
# create an instance of ItemLink from a JSON string
item_link_instance = ItemLink.from_json(json)
# print the JSON string representation of the object
print(ItemLink.to_json())

# convert the object into a dict
item_link_dict = item_link_instance.to_dict()
# create an instance of ItemLink from a dict
item_link_from_dict = ItemLink.from_dict(item_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


