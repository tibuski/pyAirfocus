# SetClientSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] 
**value** | **object** |  | 

## Example

```python
from openapi_client.models.set_client_settings_request import SetClientSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetClientSettingsRequest from a JSON string
set_client_settings_request_instance = SetClientSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(SetClientSettingsRequest.to_json())

# convert the object into a dict
set_client_settings_request_dict = set_client_settings_request_instance.to_dict()
# create an instance of SetClientSettingsRequest from a dict
set_client_settings_request_from_dict = SetClientSettingsRequest.from_dict(set_client_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


