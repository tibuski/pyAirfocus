# TimePeriodFieldSettingsSimple


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multi** | **bool** |  | 
**time_periods** | [**List[TimePeriod]**](TimePeriod.md) |  | [optional] 

## Example

```python
from openapi_client.models.time_period_field_settings_simple import TimePeriodFieldSettingsSimple

# TODO update the JSON string below
json = "{}"
# create an instance of TimePeriodFieldSettingsSimple from a JSON string
time_period_field_settings_simple_instance = TimePeriodFieldSettingsSimple.from_json(json)
# print the JSON string representation of the object
print(TimePeriodFieldSettingsSimple.to_json())

# convert the object into a dict
time_period_field_settings_simple_dict = time_period_field_settings_simple_instance.to_dict()
# create an instance of TimePeriodFieldSettingsSimple from a dict
time_period_field_settings_simple_from_dict = TimePeriodFieldSettingsSimple.from_dict(time_period_field_settings_simple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


