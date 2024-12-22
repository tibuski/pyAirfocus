# NumberFieldTypeSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximum** | **float** |  | [optional] 
**minimum** | **float** |  | [optional] 
**overflow** | **bool** |  | 
**stepping** | [**NumberFieldTypeSettingsStepping**](NumberFieldTypeSettingsStepping.md) |  | [optional] 
**unit** | [**NumberFieldTypeSettingsUnit**](NumberFieldTypeSettingsUnit.md) |  | [optional] 

## Example

```python
from openapi_client.models.number_field_type_settings import NumberFieldTypeSettings

# TODO update the JSON string below
json = "{}"
# create an instance of NumberFieldTypeSettings from a JSON string
number_field_type_settings_instance = NumberFieldTypeSettings.from_json(json)
# print the JSON string representation of the object
print(NumberFieldTypeSettings.to_json())

# convert the object into a dict
number_field_type_settings_dict = number_field_type_settings_instance.to_dict()
# create an instance of NumberFieldTypeSettings from a dict
number_field_type_settings_from_dict = NumberFieldTypeSettings.from_dict(number_field_type_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


