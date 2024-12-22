# JsonPatchAdd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | 
**path** | **str** |  | 
**value** | **object** |  | 

## Example

```python
from openapi_client.models.json_patch_add import JsonPatchAdd

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPatchAdd from a JSON string
json_patch_add_instance = JsonPatchAdd.from_json(json)
# print the JSON string representation of the object
print(JsonPatchAdd.to_json())

# convert the object into a dict
json_patch_add_dict = json_patch_add_instance.to_dict()
# create an instance of JsonPatchAdd from a dict
json_patch_add_from_dict = JsonPatchAdd.from_dict(json_patch_add_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


