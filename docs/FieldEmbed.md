# FieldEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspaces** | [**List[FieldFieldWorkspaceEmbed]**](FieldFieldWorkspaceEmbed.md) | List of all workspaces where this field is used. | [optional] 

## Example

```python
from openapi_client.models.field_embed import FieldEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of FieldEmbed from a JSON string
field_embed_instance = FieldEmbed.from_json(json)
# print the JSON string representation of the object
print(FieldEmbed.to_json())

# convert the object into a dict
field_embed_dict = field_embed_instance.to_dict()
# create an instance of FieldEmbed from a dict
field_embed_from_dict = FieldEmbed.from_dict(field_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


