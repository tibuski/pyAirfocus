# TemplateView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**icon_name** | **str** |  | [optional] 
**image_url** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from openapi_client.models.template_view import TemplateView

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateView from a JSON string
template_view_instance = TemplateView.from_json(json)
# print the JSON string representation of the object
print(TemplateView.to_json())

# convert the object into a dict
template_view_dict = template_view_instance.to_dict()
# create an instance of TemplateView from a dict
template_view_from_dict = TemplateView.from_dict(template_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


