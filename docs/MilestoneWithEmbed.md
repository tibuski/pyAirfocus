# MilestoneWithEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | **object** |  | 
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
from openapi_client.models.milestone_with_embed import MilestoneWithEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of MilestoneWithEmbed from a JSON string
milestone_with_embed_instance = MilestoneWithEmbed.from_json(json)
# print the JSON string representation of the object
print(MilestoneWithEmbed.to_json())

# convert the object into a dict
milestone_with_embed_dict = milestone_with_embed_instance.to_dict()
# create an instance of MilestoneWithEmbed from a dict
milestone_with_embed_from_dict = MilestoneWithEmbed.from_dict(milestone_with_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


