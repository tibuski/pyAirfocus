# SelectFieldWithFieldEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**FieldEmbed**](FieldEmbed.md) |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | 
**id** | **str** |  | 
**is_team_field** | **bool** |  | 
**name** | **str** |  | 
**settings** | [**SelectFieldTypeSettings**](SelectFieldTypeSettings.md) |  | 
**team_id** | **str** |  | 
**type_id** | **str** |  | 

## Example

```python
from openapi_client.models.select_field_with_field_embed import SelectFieldWithFieldEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of SelectFieldWithFieldEmbed from a JSON string
select_field_with_field_embed_instance = SelectFieldWithFieldEmbed.from_json(json)
# print the JSON string representation of the object
print(SelectFieldWithFieldEmbed.to_json())

# convert the object into a dict
select_field_with_field_embed_dict = select_field_with_field_embed_instance.to_dict()
# create an instance of SelectFieldWithFieldEmbed from a dict
select_field_with_field_embed_from_dict = SelectFieldWithFieldEmbed.from_dict(select_field_with_field_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


