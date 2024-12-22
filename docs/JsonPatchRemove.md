# JsonPatchRemove


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old** | **object** |  | [optional] 
**op** | **str** |  | 
**path** | **str** |  | 

## Example

```python
from openapi_client.models.json_patch_remove import JsonPatchRemove

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPatchRemove from a JSON string
json_patch_remove_instance = JsonPatchRemove.from_json(json)
# print the JSON string representation of the object
print(JsonPatchRemove.to_json())

# convert the object into a dict
json_patch_remove_dict = json_patch_remove_instance.to_dict()
# create an instance of JsonPatchRemove from a dict
json_patch_remove_from_dict = JsonPatchRemove.from_dict(json_patch_remove_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


