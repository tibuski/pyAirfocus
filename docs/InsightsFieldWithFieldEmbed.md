# InsightsFieldWithFieldEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**FieldEmbed**](FieldEmbed.md) |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | 
**id** | **str** |  | 
**is_team_field** | **bool** |  | 
**name** | **str** |  | 
**settings** | [**InsightsFieldTypeSettings**](InsightsFieldTypeSettings.md) |  | 
**team_id** | **str** |  | 
**type_id** | **str** |  | 

## Example

```python
from openapi_client.models.insights_field_with_field_embed import InsightsFieldWithFieldEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsFieldWithFieldEmbed from a JSON string
insights_field_with_field_embed_instance = InsightsFieldWithFieldEmbed.from_json(json)
# print the JSON string representation of the object
print(InsightsFieldWithFieldEmbed.to_json())

# convert the object into a dict
insights_field_with_field_embed_dict = insights_field_with_field_embed_instance.to_dict()
# create an instance of InsightsFieldWithFieldEmbed from a dict
insights_field_with_field_embed_from_dict = InsightsFieldWithFieldEmbed.from_dict(insights_field_with_field_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


