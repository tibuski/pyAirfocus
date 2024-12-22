# ItemAttachmentWithEmbed

A connection link between an item and an uploaded attachment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | **object** |  | 
**content_type** | **str** | Type of updated content. | 
**created_at** | **datetime** | When this attachment link has been created. | 
**id** | **str** | ID of an item-attachment link. | 
**item_id** | **str** | ID of the item to which the attachment is linked. | 
**last_updated_at** | **datetime** | When this attachment link has been updated for the last time. | 
**name** | **str** | Name of the attachment, e.g. its file name (to be displayed in UI). | 
**uri** | **str** | URI of the attachment contents. It can be any URI, but conventionally it&#39;s a relative URI like &#39;attachment:1ecb9ecd-8a97-403a-a74a-741eb4b8fb69&#39; with UUID of a file uploaded to airfocus file-storage. Such URI is then resolved by clients into a full HTTPS URL. | 

## Example

```python
from openapi_client.models.item_attachment_with_embed import ItemAttachmentWithEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of ItemAttachmentWithEmbed from a JSON string
item_attachment_with_embed_instance = ItemAttachmentWithEmbed.from_json(json)
# print the JSON string representation of the object
print(ItemAttachmentWithEmbed.to_json())

# convert the object into a dict
item_attachment_with_embed_dict = item_attachment_with_embed_instance.to_dict()
# create an instance of ItemAttachmentWithEmbed from a dict
item_attachment_with_embed_from_dict = ItemAttachmentWithEmbed.from_dict(item_attachment_with_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


