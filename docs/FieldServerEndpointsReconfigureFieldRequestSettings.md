# FieldServerEndpointsReconfigureFieldRequestSettings

The settings object which corresponds to the type of the requested field, or it can be skipped if the requested field does not have any settings. This schema shows all the available field-settings. See also the Field schema to learn about settings of each specific field type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximum** | **float** |  | [optional] 
**minimum** | **float** |  | [optional] 
**overflow** | **bool** |  | 
**stepping** | [**NumberFieldTypeSettingsStepping**](NumberFieldTypeSettingsStepping.md) |  | [optional] 
**unit** | [**NumberFieldTypeSettingsUnit**](NumberFieldTypeSettingsUnit.md) |  | [optional] 
**low** | **int** |  | 
**medium** | **int** |  | 
**time_periods** | [**List[TimePeriod]**](TimePeriod.md) |  | [optional] 
**auto_assign** | **bool** |  | 
**multi** | **bool** |  | 
**options** | [**List[SelectFieldTypeOption]**](SelectFieldTypeOption.md) |  | [optional] 

## Example

```python
from openapi_client.models.field_server_endpoints_reconfigure_field_request_settings import FieldServerEndpointsReconfigureFieldRequestSettings

# TODO update the JSON string below
json = "{}"
# create an instance of FieldServerEndpointsReconfigureFieldRequestSettings from a JSON string
field_server_endpoints_reconfigure_field_request_settings_instance = FieldServerEndpointsReconfigureFieldRequestSettings.from_json(json)
# print the JSON string representation of the object
print(FieldServerEndpointsReconfigureFieldRequestSettings.to_json())

# convert the object into a dict
field_server_endpoints_reconfigure_field_request_settings_dict = field_server_endpoints_reconfigure_field_request_settings_instance.to_dict()
# create an instance of FieldServerEndpointsReconfigureFieldRequestSettings from a dict
field_server_endpoints_reconfigure_field_request_settings_from_dict = FieldServerEndpointsReconfigureFieldRequestSettings.from_dict(field_server_endpoints_reconfigure_field_request_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


