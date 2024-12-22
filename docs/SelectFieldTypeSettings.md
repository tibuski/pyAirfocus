# SelectFieldTypeSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multi** | **bool** |  | 
**options** | [**List[SelectFieldTypeOption]**](SelectFieldTypeOption.md) |  | [optional] 

## Example

```python
from openapi_client.models.select_field_type_settings import SelectFieldTypeSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SelectFieldTypeSettings from a JSON string
select_field_type_settings_instance = SelectFieldTypeSettings.from_json(json)
# print the JSON string representation of the object
print(SelectFieldTypeSettings.to_json())

# convert the object into a dict
select_field_type_settings_dict = select_field_type_settings_instance.to_dict()
# create an instance of SelectFieldTypeSettings from a dict
select_field_type_settings_from_dict = SelectFieldTypeSettings.from_dict(select_field_type_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


