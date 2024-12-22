# PeopleFieldWithFieldEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**FieldEmbed**](FieldEmbed.md) |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | 
**id** | **str** |  | 
**is_team_field** | **bool** |  | 
**name** | **str** |  | 
**settings** | [**PeopleFieldTypeSettings**](PeopleFieldTypeSettings.md) |  | 
**team_id** | **str** |  | 
**type_id** | **str** |  | 

## Example

```python
from openapi_client.models.people_field_with_field_embed import PeopleFieldWithFieldEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleFieldWithFieldEmbed from a JSON string
people_field_with_field_embed_instance = PeopleFieldWithFieldEmbed.from_json(json)
# print the JSON string representation of the object
print(PeopleFieldWithFieldEmbed.to_json())

# convert the object into a dict
people_field_with_field_embed_dict = people_field_with_field_embed_instance.to_dict()
# create an instance of PeopleFieldWithFieldEmbed from a dict
people_field_with_field_embed_from_dict = PeopleFieldWithFieldEmbed.from_dict(people_field_with_field_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


