# ItemLinkBulkUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**resource** | [**ItemLink**](ItemLink.md) |  | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.item_link_bulk_update import ItemLinkBulkUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ItemLinkBulkUpdate from a JSON string
item_link_bulk_update_instance = ItemLinkBulkUpdate.from_json(json)
# print the JSON string representation of the object
print(ItemLinkBulkUpdate.to_json())

# convert the object into a dict
item_link_bulk_update_dict = item_link_bulk_update_instance.to_dict()
# create an instance of ItemLinkBulkUpdate from a dict
item_link_bulk_update_from_dict = ItemLinkBulkUpdate.from_dict(item_link_bulk_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


