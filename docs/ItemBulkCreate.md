# ItemBulkCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**Item**](Item.md) |  | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.item_bulk_create import ItemBulkCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ItemBulkCreate from a JSON string
item_bulk_create_instance = ItemBulkCreate.from_json(json)
# print the JSON string representation of the object
print(ItemBulkCreate.to_json())

# convert the object into a dict
item_bulk_create_dict = item_bulk_create_instance.to_dict()
# create an instance of ItemBulkCreate from a dict
item_bulk_create_from_dict = ItemBulkCreate.from_dict(item_bulk_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


