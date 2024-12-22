# TimePeriodFieldWithFieldEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**FieldEmbed**](FieldEmbed.md) |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | 
**id** | **str** |  | 
**is_team_field** | **bool** |  | 
**name** | **str** |  | 
**settings** | [**TimePeriodFieldSettings**](TimePeriodFieldSettings.md) |  | 
**team_id** | **str** |  | 
**type_id** | **str** |  | 

## Example

```python
from openapi_client.models.time_period_field_with_field_embed import TimePeriodFieldWithFieldEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of TimePeriodFieldWithFieldEmbed from a JSON string
time_period_field_with_field_embed_instance = TimePeriodFieldWithFieldEmbed.from_json(json)
# print the JSON string representation of the object
print(TimePeriodFieldWithFieldEmbed.to_json())

# convert the object into a dict
time_period_field_with_field_embed_dict = time_period_field_with_field_embed_instance.to_dict()
# create an instance of TimePeriodFieldWithFieldEmbed from a dict
time_period_field_with_field_embed_from_dict = TimePeriodFieldWithFieldEmbed.from_dict(time_period_field_with_field_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


