# VotingScoreFieldWithFieldEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**FieldEmbed**](FieldEmbed.md) |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | 
**id** | **str** |  | 
**is_team_field** | **bool** |  | 
**name** | **str** |  | 
**settings** | [**VotingAppScoreFieldTypeSettings**](VotingAppScoreFieldTypeSettings.md) |  | 
**team_id** | **str** |  | 
**type_id** | **str** |  | 

## Example

```python
from openapi_client.models.voting_score_field_with_field_embed import VotingScoreFieldWithFieldEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of VotingScoreFieldWithFieldEmbed from a JSON string
voting_score_field_with_field_embed_instance = VotingScoreFieldWithFieldEmbed.from_json(json)
# print the JSON string representation of the object
print(VotingScoreFieldWithFieldEmbed.to_json())

# convert the object into a dict
voting_score_field_with_field_embed_dict = voting_score_field_with_field_embed_instance.to_dict()
# create an instance of VotingScoreFieldWithFieldEmbed from a dict
voting_score_field_with_field_embed_from_dict = VotingScoreFieldWithFieldEmbed.from_dict(voting_score_field_with_field_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


