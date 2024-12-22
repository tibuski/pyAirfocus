# JsonPatchMove


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** |  | 
**op** | **str** |  | 
**path** | **str** |  | 

## Example

```python
from openapi_client.models.json_patch_move import JsonPatchMove

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPatchMove from a JSON string
json_patch_move_instance = JsonPatchMove.from_json(json)
# print the JSON string representation of the object
print(JsonPatchMove.to_json())

# convert the object into a dict
json_patch_move_dict = json_patch_move_instance.to_dict()
# create an instance of JsonPatchMove from a dict
json_patch_move_from_dict = JsonPatchMove.from_dict(json_patch_move_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


