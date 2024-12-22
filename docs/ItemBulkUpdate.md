# ItemBulkUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**resource** | [**Item**](Item.md) |  | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.item_bulk_update import ItemBulkUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ItemBulkUpdate from a JSON string
item_bulk_update_instance = ItemBulkUpdate.from_json(json)
# print the JSON string representation of the object
print(ItemBulkUpdate.to_json())

# convert the object into a dict
item_bulk_update_dict = item_bulk_update_instance.to_dict()
# create an instance of ItemBulkUpdate from a dict
item_bulk_update_from_dict = ItemBulkUpdate.from_dict(item_bulk_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


