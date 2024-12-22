# DateRangeFieldWithFieldEmbed


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

## Example

```python
from openapi_client.models.date_range_field_with_field_embed import DateRangeFieldWithFieldEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of DateRangeFieldWithFieldEmbed from a JSON string
date_range_field_with_field_embed_instance = DateRangeFieldWithFieldEmbed.from_json(json)
# print the JSON string representation of the object
print(DateRangeFieldWithFieldEmbed.to_json())

# convert the object into a dict
date_range_field_with_field_embed_dict = date_range_field_with_field_embed_instance.to_dict()
# create an instance of DateRangeFieldWithFieldEmbed from a dict
date_range_field_with_field_embed_from_dict = DateRangeFieldWithFieldEmbed.from_dict(date_range_field_with_field_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


