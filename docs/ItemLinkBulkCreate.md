# ItemLinkBulkCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**ItemLink**](ItemLink.md) |  | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.item_link_bulk_create import ItemLinkBulkCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ItemLinkBulkCreate from a JSON string
item_link_bulk_create_instance = ItemLinkBulkCreate.from_json(json)
# print the JSON string representation of the object
print(ItemLinkBulkCreate.to_json())

# convert the object into a dict
item_link_bulk_create_dict = item_link_bulk_create_instance.to_dict()
# create an instance of ItemLinkBulkCreate from a dict
item_link_bulk_create_from_dict = ItemLinkBulkCreate.from_dict(item_link_bulk_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


