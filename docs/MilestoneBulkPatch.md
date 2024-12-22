# MilestoneBulkPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**transform** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) | A JSON Patch document. See https://jsonpatch.com/ for more information. | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.milestone_bulk_patch import MilestoneBulkPatch

# TODO update the JSON string below
json = "{}"
# create an instance of MilestoneBulkPatch from a JSON string
milestone_bulk_patch_instance = MilestoneBulkPatch.from_json(json)
# print the JSON string representation of the object
print(MilestoneBulkPatch.to_json())

# convert the object into a dict
milestone_bulk_patch_dict = milestone_bulk_patch_instance.to_dict()
# create an instance of MilestoneBulkPatch from a dict
milestone_bulk_patch_from_dict = MilestoneBulkPatch.from_dict(milestone_bulk_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


