# ItemRelationBulkCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**ItemRelation**](ItemRelation.md) |  | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.item_relation_bulk_create import ItemRelationBulkCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ItemRelationBulkCreate from a JSON string
item_relation_bulk_create_instance = ItemRelationBulkCreate.from_json(json)
# print the JSON string representation of the object
print(ItemRelationBulkCreate.to_json())

# convert the object into a dict
item_relation_bulk_create_dict = item_relation_bulk_create_instance.to_dict()
# create an instance of ItemRelationBulkCreate from a dict
item_relation_bulk_create_from_dict = ItemRelationBulkCreate.from_dict(item_relation_bulk_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


