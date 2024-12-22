# JsonPatchCopy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** |  | 
**op** | **str** |  | 
**path** | **str** |  | 

## Example

```python
from openapi_client.models.json_patch_copy import JsonPatchCopy

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPatchCopy from a JSON string
json_patch_copy_instance = JsonPatchCopy.from_json(json)
# print the JSON string representation of the object
print(JsonPatchCopy.to_json())

# convert the object into a dict
json_patch_copy_dict = json_patch_copy_instance.to_dict()
# create an instance of JsonPatchCopy from a dict
json_patch_copy_from_dict = JsonPatchCopy.from_dict(json_patch_copy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


