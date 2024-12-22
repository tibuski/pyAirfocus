# IntegrationCapabilities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debug** | **bool** |  | 
**hierarchy** | **bool** |  | 
**push** | **bool** |  | 
**sync** | **bool** |  | 

## Example

```python
from openapi_client.models.integration_capabilities import IntegrationCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationCapabilities from a JSON string
integration_capabilities_instance = IntegrationCapabilities.from_json(json)
# print the JSON string representation of the object
print(IntegrationCapabilities.to_json())

# convert the object into a dict
integration_capabilities_dict = integration_capabilities_instance.to_dict()
# create an instance of IntegrationCapabilities from a dict
integration_capabilities_from_dict = IntegrationCapabilities.from_dict(integration_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


