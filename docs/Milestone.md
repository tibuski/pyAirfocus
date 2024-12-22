# Milestone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**var_date** | **date** |  | 
**description** | **str** |  | 
**id** | **str** |  | 
**last_updated_at** | **datetime** |  | 
**name** | **str** |  | 
**timezone** | **str** |  | [optional] 
**workspace_id** | **str** |  | 

## Example

```python
from openapi_client.models.milestone import Milestone

# TODO update the JSON string below
json = "{}"
# create an instance of Milestone from a JSON string
milestone_instance = Milestone.from_json(json)
# print the JSON string representation of the object
print(Milestone.to_json())

# convert the object into a dict
milestone_dict = milestone_instance.to_dict()
# create an instance of Milestone from a dict
milestone_from_dict = Milestone.from_dict(milestone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


