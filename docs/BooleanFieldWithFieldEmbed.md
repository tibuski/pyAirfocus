# BooleanFieldWithFieldEmbed


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
from openapi_client.models.boolean_field_with_field_embed import BooleanFieldWithFieldEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of BooleanFieldWithFieldEmbed from a JSON string
boolean_field_with_field_embed_instance = BooleanFieldWithFieldEmbed.from_json(json)
# print the JSON string representation of the object
print(BooleanFieldWithFieldEmbed.to_json())

# convert the object into a dict
boolean_field_with_field_embed_dict = boolean_field_with_field_embed_instance.to_dict()
# create an instance of BooleanFieldWithFieldEmbed from a dict
boolean_field_with_field_embed_from_dict = BooleanFieldWithFieldEmbed.from_dict(boolean_field_with_field_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


