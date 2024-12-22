# MilestoneBulkAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**Milestone**](Milestone.md) |  | 
**type** | **str** |  | 
**id** | **str** |  | 
**transform** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) | A JSON Patch document. See https://jsonpatch.com/ for more information. | 

## Example

```python
from openapi_client.models.milestone_bulk_action import MilestoneBulkAction

# TODO update the JSON string below
json = "{}"
# create an instance of MilestoneBulkAction from a JSON string
milestone_bulk_action_instance = MilestoneBulkAction.from_json(json)
# print the JSON string representation of the object
print(MilestoneBulkAction.to_json())

# convert the object into a dict
milestone_bulk_action_dict = milestone_bulk_action_instance.to_dict()
# create an instance of MilestoneBulkAction from a dict
milestone_bulk_action_from_dict = MilestoneBulkAction.from_dict(milestone_bulk_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


