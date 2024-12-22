# ItemLinkBulkAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**ItemLink**](ItemLink.md) |  | 
**type** | **str** |  | 
**id** | **str** |  | 
**transform** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) | A JSON Patch document. See https://jsonpatch.com/ for more information. | 

## Example

```python
from openapi_client.models.item_link_bulk_action import ItemLinkBulkAction

# TODO update the JSON string below
json = "{}"
# create an instance of ItemLinkBulkAction from a JSON string
item_link_bulk_action_instance = ItemLinkBulkAction.from_json(json)
# print the JSON string representation of the object
print(ItemLinkBulkAction.to_json())

# convert the object into a dict
item_link_bulk_action_dict = item_link_bulk_action_instance.to_dict()
# create an instance of ItemLinkBulkAction from a dict
item_link_bulk_action_from_dict = ItemLinkBulkAction.from_dict(item_link_bulk_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


