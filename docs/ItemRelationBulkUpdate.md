# ItemRelationBulkUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**resource** | [**ItemRelation**](ItemRelation.md) |  | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.item_relation_bulk_update import ItemRelationBulkUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ItemRelationBulkUpdate from a JSON string
item_relation_bulk_update_instance = ItemRelationBulkUpdate.from_json(json)
# print the JSON string representation of the object
print(ItemRelationBulkUpdate.to_json())

# convert the object into a dict
item_relation_bulk_update_dict = item_relation_bulk_update_instance.to_dict()
# create an instance of ItemRelationBulkUpdate from a dict
item_relation_bulk_update_from_dict = ItemRelationBulkUpdate.from_dict(item_relation_bulk_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


