# ItemAttachmentBulkAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**ItemAttachment**](ItemAttachment.md) |  | 
**type** | **str** |  | 
**id** | **str** |  | 
**transform** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) | A JSON Patch document. See https://jsonpatch.com/ for more information. | 

## Example

```python
from openapi_client.models.item_attachment_bulk_action import ItemAttachmentBulkAction

# TODO update the JSON string below
json = "{}"
# create an instance of ItemAttachmentBulkAction from a JSON string
item_attachment_bulk_action_instance = ItemAttachmentBulkAction.from_json(json)
# print the JSON string representation of the object
print(ItemAttachmentBulkAction.to_json())

# convert the object into a dict
item_attachment_bulk_action_dict = item_attachment_bulk_action_instance.to_dict()
# create an instance of ItemAttachmentBulkAction from a dict
item_attachment_bulk_action_from_dict = ItemAttachmentBulkAction.from_dict(item_attachment_bulk_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


