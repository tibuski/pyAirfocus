# FieldWithFieldEmbedPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[FieldWithFieldEmbed]**](FieldWithFieldEmbed.md) |  | [optional] 
**total_items** | **int** |  | 

## Example

```python
from openapi_client.models.field_with_field_embed_page import FieldWithFieldEmbedPage

# TODO update the JSON string below
json = "{}"
# create an instance of FieldWithFieldEmbedPage from a JSON string
field_with_field_embed_page_instance = FieldWithFieldEmbedPage.from_json(json)
# print the JSON string representation of the object
print(FieldWithFieldEmbedPage.to_json())

# convert the object into a dict
field_with_field_embed_page_dict = field_with_field_embed_page_instance.to_dict()
# create an instance of FieldWithFieldEmbedPage from a dict
field_with_field_embed_page_from_dict = FieldWithFieldEmbedPage.from_dict(field_with_field_embed_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


