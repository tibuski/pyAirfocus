# JsonPatchTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | 
**path** | **str** |  | 
**value** | **object** |  | 

## Example

```python
from openapi_client.models.json_patch_test import JsonPatchTest

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPatchTest from a JSON string
json_patch_test_instance = JsonPatchTest.from_json(json)
# print the JSON string representation of the object
print(JsonPatchTest.to_json())

# convert the object into a dict
json_patch_test_dict = json_patch_test_instance.to_dict()
# create an instance of JsonPatchTest from a dict
json_patch_test_from_dict = JsonPatchTest.from_dict(json_patch_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


