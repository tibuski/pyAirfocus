# TemplateCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**slug** | **str** |  | 
**template_ids** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.template_category import TemplateCategory

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateCategory from a JSON string
template_category_instance = TemplateCategory.from_json(json)
# print the JSON string representation of the object
print(TemplateCategory.to_json())

# convert the object into a dict
template_category_dict = template_category_instance.to_dict()
# create an instance of TemplateCategory from a dict
template_category_from_dict = TemplateCategory.from_dict(template_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


