# NumberFieldWithFieldEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**FieldEmbed**](FieldEmbed.md) |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | 
**id** | **str** |  | 
**is_team_field** | **bool** |  | 
**name** | **str** |  | 
**settings** | [**NumberFieldTypeSettings**](NumberFieldTypeSettings.md) |  | 
**team_id** | **str** |  | 
**type_id** | **str** |  | 

## Example

```python
from openapi_client.models.number_field_with_field_embed import NumberFieldWithFieldEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of NumberFieldWithFieldEmbed from a JSON string
number_field_with_field_embed_instance = NumberFieldWithFieldEmbed.from_json(json)
# print the JSON string representation of the object
print(NumberFieldWithFieldEmbed.to_json())

# convert the object into a dict
number_field_with_field_embed_dict = number_field_with_field_embed_instance.to_dict()
# create an instance of NumberFieldWithFieldEmbed from a dict
number_field_with_field_embed_from_dict = NumberFieldWithFieldEmbed.from_dict(number_field_with_field_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


