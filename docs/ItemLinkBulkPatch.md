# ItemLinkBulkPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**transform** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) | A JSON Patch document. See https://jsonpatch.com/ for more information. | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.item_link_bulk_patch import ItemLinkBulkPatch

# TODO update the JSON string below
json = "{}"
# create an instance of ItemLinkBulkPatch from a JSON string
item_link_bulk_patch_instance = ItemLinkBulkPatch.from_json(json)
# print the JSON string representation of the object
print(ItemLinkBulkPatch.to_json())

# convert the object into a dict
item_link_bulk_patch_dict = item_link_bulk_patch_instance.to_dict()
# create an instance of ItemLinkBulkPatch from a dict
item_link_bulk_patch_from_dict = ItemLinkBulkPatch.from_dict(item_link_bulk_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


