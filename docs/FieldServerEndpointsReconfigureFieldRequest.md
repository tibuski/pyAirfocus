# FieldServerEndpointsReconfigureFieldRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**is_team_field** | **bool** |  | 
**name** | **str** |  | 
**settings** | [**FieldServerEndpointsReconfigureFieldRequestSettings**](FieldServerEndpointsReconfigureFieldRequestSettings.md) |  | [optional] 

## Example

```python
from openapi_client.models.field_server_endpoints_reconfigure_field_request import FieldServerEndpointsReconfigureFieldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FieldServerEndpointsReconfigureFieldRequest from a JSON string
field_server_endpoints_reconfigure_field_request_instance = FieldServerEndpointsReconfigureFieldRequest.from_json(json)
# print the JSON string representation of the object
print(FieldServerEndpointsReconfigureFieldRequest.to_json())

# convert the object into a dict
field_server_endpoints_reconfigure_field_request_dict = field_server_endpoints_reconfigure_field_request_instance.to_dict()
# create an instance of FieldServerEndpointsReconfigureFieldRequest from a dict
field_server_endpoints_reconfigure_field_request_from_dict = FieldServerEndpointsReconfigureFieldRequest.from_dict(field_server_endpoints_reconfigure_field_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


