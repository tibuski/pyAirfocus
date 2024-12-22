# TimePeriodFieldSettingsIterations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_id** | **str** |  | 
**multi** | **bool** |  | 
**time_periods** | [**List[TimePeriod]**](TimePeriod.md) |  | [optional] 

## Example

```python
from openapi_client.models.time_period_field_settings_iterations import TimePeriodFieldSettingsIterations

# TODO update the JSON string below
json = "{}"
# create an instance of TimePeriodFieldSettingsIterations from a JSON string
time_period_field_settings_iterations_instance = TimePeriodFieldSettingsIterations.from_json(json)
# print the JSON string representation of the object
print(TimePeriodFieldSettingsIterations.to_json())

# convert the object into a dict
time_period_field_settings_iterations_dict = time_period_field_settings_iterations_instance.to_dict()
# create an instance of TimePeriodFieldSettingsIterations from a dict
time_period_field_settings_iterations_from_dict = TimePeriodFieldSettingsIterations.from_dict(time_period_field_settings_iterations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


