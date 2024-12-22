# OkrTimePeriodFieldWithFieldEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**FieldEmbed**](FieldEmbed.md) |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | 
**id** | **str** |  | 
**is_team_field** | **bool** |  | 
**name** | **str** |  | 
**settings** | [**OkrTimePeriodFieldSettings**](OkrTimePeriodFieldSettings.md) |  | 
**team_id** | **str** |  | 
**type_id** | **str** |  | 

## Example

```python
from openapi_client.models.okr_time_period_field_with_field_embed import OkrTimePeriodFieldWithFieldEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of OkrTimePeriodFieldWithFieldEmbed from a JSON string
okr_time_period_field_with_field_embed_instance = OkrTimePeriodFieldWithFieldEmbed.from_json(json)
# print the JSON string representation of the object
print(OkrTimePeriodFieldWithFieldEmbed.to_json())

# convert the object into a dict
okr_time_period_field_with_field_embed_dict = okr_time_period_field_with_field_embed_instance.to_dict()
# create an instance of OkrTimePeriodFieldWithFieldEmbed from a dict
okr_time_period_field_with_field_embed_from_dict = OkrTimePeriodFieldWithFieldEmbed.from_dict(okr_time_period_field_with_field_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


