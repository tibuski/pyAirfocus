# ItemBulkAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**Item**](Item.md) |  | 
**type** | **str** |  | 
**id** | **str** |  | 
**transform** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) | A JSON Patch document. See https://jsonpatch.com/ for more information. | 

## Example

```python
from openapi_client.models.item_bulk_action import ItemBulkAction

# TODO update the JSON string below
json = "{}"
# create an instance of ItemBulkAction from a JSON string
item_bulk_action_instance = ItemBulkAction.from_json(json)
# print the JSON string representation of the object
print(ItemBulkAction.to_json())

# convert the object into a dict
item_bulk_action_dict = item_bulk_action_instance.to_dict()
# create an instance of ItemBulkAction from a dict
item_bulk_action_from_dict = ItemBulkAction.from_dict(item_bulk_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


