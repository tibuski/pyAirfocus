# MilestoneBulkUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**resource** | [**Milestone**](Milestone.md) |  | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.milestone_bulk_update import MilestoneBulkUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of MilestoneBulkUpdate from a JSON string
milestone_bulk_update_instance = MilestoneBulkUpdate.from_json(json)
# print the JSON string representation of the object
print(MilestoneBulkUpdate.to_json())

# convert the object into a dict
milestone_bulk_update_dict = milestone_bulk_update_instance.to_dict()
# create an instance of MilestoneBulkUpdate from a dict
milestone_bulk_update_from_dict = MilestoneBulkUpdate.from_dict(milestone_bulk_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


