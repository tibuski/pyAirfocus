# MilestoneBulkCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**Milestone**](Milestone.md) |  | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.milestone_bulk_create import MilestoneBulkCreate

# TODO update the JSON string below
json = "{}"
# create an instance of MilestoneBulkCreate from a JSON string
milestone_bulk_create_instance = MilestoneBulkCreate.from_json(json)
# print the JSON string representation of the object
print(MilestoneBulkCreate.to_json())

# convert the object into a dict
milestone_bulk_create_dict = milestone_bulk_create_instance.to_dict()
# create an instance of MilestoneBulkCreate from a dict
milestone_bulk_create_from_dict = MilestoneBulkCreate.from_dict(milestone_bulk_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


