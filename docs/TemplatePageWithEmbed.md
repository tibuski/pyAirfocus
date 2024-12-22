# TemplatePageWithEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**TemplateSearchEmbed**](TemplateSearchEmbed.md) |  | 
**items** | [**List[Template]**](Template.md) |  | [optional] 
**total_items** | **int** |  | 

## Example

```python
from openapi_client.models.template_page_with_embed import TemplatePageWithEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatePageWithEmbed from a JSON string
template_page_with_embed_instance = TemplatePageWithEmbed.from_json(json)
# print the JSON string representation of the object
print(TemplatePageWithEmbed.to_json())

# convert the object into a dict
template_page_with_embed_dict = template_page_with_embed_instance.to_dict()
# create an instance of TemplatePageWithEmbed from a dict
template_page_with_embed_from_dict = TemplatePageWithEmbed.from_dict(template_page_with_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


