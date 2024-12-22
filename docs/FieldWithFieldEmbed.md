# FieldWithFieldEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**FieldEmbed**](FieldEmbed.md) |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | 
**id** | **str** |  | 
**is_team_field** | **bool** |  | 
**name** | **str** |  | 
**team_id** | **str** |  | 
**type_id** | **str** |  | 
**settings** | [**VotingAppScoreFieldTypeSettings**](VotingAppScoreFieldTypeSettings.md) |  | 

## Example

```python
from openapi_client.models.field_with_field_embed import FieldWithFieldEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of FieldWithFieldEmbed from a JSON string
field_with_field_embed_instance = FieldWithFieldEmbed.from_json(json)
# print the JSON string representation of the object
print(FieldWithFieldEmbed.to_json())

# convert the object into a dict
field_with_field_embed_dict = field_with_field_embed_instance.to_dict()
# create an instance of FieldWithFieldEmbed from a dict
field_with_field_embed_from_dict = FieldWithFieldEmbed.from_dict(field_with_field_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


