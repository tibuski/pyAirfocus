# PortalFieldWithFieldEmbed


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
from openapi_client.models.portal_field_with_field_embed import PortalFieldWithFieldEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of PortalFieldWithFieldEmbed from a JSON string
portal_field_with_field_embed_instance = PortalFieldWithFieldEmbed.from_json(json)
# print the JSON string representation of the object
print(PortalFieldWithFieldEmbed.to_json())

# convert the object into a dict
portal_field_with_field_embed_dict = portal_field_with_field_embed_instance.to_dict()
# create an instance of PortalFieldWithFieldEmbed from a dict
portal_field_with_field_embed_from_dict = PortalFieldWithFieldEmbed.from_dict(portal_field_with_field_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


