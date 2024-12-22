# ItemBulkPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**transform** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) | A JSON Patch document. See https://jsonpatch.com/ for more information. | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.item_bulk_patch import ItemBulkPatch

# TODO update the JSON string below
json = "{}"
# create an instance of ItemBulkPatch from a JSON string
item_bulk_patch_instance = ItemBulkPatch.from_json(json)
# print the JSON string representation of the object
print(ItemBulkPatch.to_json())

# convert the object into a dict
item_bulk_patch_dict = item_bulk_patch_instance.to_dict()
# create an instance of ItemBulkPatch from a dict
item_bulk_patch_from_dict = ItemBulkPatch.from_dict(item_bulk_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


