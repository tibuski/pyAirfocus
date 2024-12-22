# ItemAttachmentBulkUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**resource** | [**ItemAttachment**](ItemAttachment.md) |  | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.item_attachment_bulk_update import ItemAttachmentBulkUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ItemAttachmentBulkUpdate from a JSON string
item_attachment_bulk_update_instance = ItemAttachmentBulkUpdate.from_json(json)
# print the JSON string representation of the object
print(ItemAttachmentBulkUpdate.to_json())

# convert the object into a dict
item_attachment_bulk_update_dict = item_attachment_bulk_update_instance.to_dict()
# create an instance of ItemAttachmentBulkUpdate from a dict
item_attachment_bulk_update_from_dict = ItemAttachmentBulkUpdate.from_dict(item_attachment_bulk_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


