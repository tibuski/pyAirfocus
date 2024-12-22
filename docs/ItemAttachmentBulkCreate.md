# ItemAttachmentBulkCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**ItemAttachment**](ItemAttachment.md) |  | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.item_attachment_bulk_create import ItemAttachmentBulkCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ItemAttachmentBulkCreate from a JSON string
item_attachment_bulk_create_instance = ItemAttachmentBulkCreate.from_json(json)
# print the JSON string representation of the object
print(ItemAttachmentBulkCreate.to_json())

# convert the object into a dict
item_attachment_bulk_create_dict = item_attachment_bulk_create_instance.to_dict()
# create an instance of ItemAttachmentBulkCreate from a dict
item_attachment_bulk_create_from_dict = ItemAttachmentBulkCreate.from_dict(item_attachment_bulk_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


