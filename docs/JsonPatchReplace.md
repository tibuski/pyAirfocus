# JsonPatchReplace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old** | **object** |  | [optional] 
**op** | **str** |  | 
**path** | **str** |  | 
**value** | **object** |  | 

## Example

```python
from openapi_client.models.json_patch_replace import JsonPatchReplace

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPatchReplace from a JSON string
json_patch_replace_instance = JsonPatchReplace.from_json(json)
# print the JSON string representation of the object
print(JsonPatchReplace.to_json())

# convert the object into a dict
json_patch_replace_dict = json_patch_replace_instance.to_dict()
# create an instance of JsonPatchReplace from a dict
json_patch_replace_from_dict = JsonPatchReplace.from_dict(json_patch_replace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


