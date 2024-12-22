# FormSourceFieldWithFieldEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**FieldEmbed**](FieldEmbed.md) |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | 
**id** | **str** |  | 
**is_team_field** | **bool** |  | 
**name** | **str** |  | 
**settings** | [**FormSourceFieldTypeSettings**](FormSourceFieldTypeSettings.md) |  | 
**team_id** | **str** |  | 
**type_id** | **str** |  | 

## Example

```python
from openapi_client.models.form_source_field_with_field_embed import FormSourceFieldWithFieldEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of FormSourceFieldWithFieldEmbed from a JSON string
form_source_field_with_field_embed_instance = FormSourceFieldWithFieldEmbed.from_json(json)
# print the JSON string representation of the object
print(FormSourceFieldWithFieldEmbed.to_json())

# convert the object into a dict
form_source_field_with_field_embed_dict = form_source_field_with_field_embed_instance.to_dict()
# create an instance of FormSourceFieldWithFieldEmbed from a dict
form_source_field_with_field_embed_from_dict = FormSourceFieldWithFieldEmbed.from_dict(form_source_field_with_field_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


