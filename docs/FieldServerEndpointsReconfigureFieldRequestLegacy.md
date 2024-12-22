# FieldServerEndpointsReconfigureFieldRequestLegacy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**field_id** | **str** |  | 
**is_team_field** | **bool** |  | 
**name** | **str** |  | 
**settings** | **object** |  | 

## Example

```python
from openapi_client.models.field_server_endpoints_reconfigure_field_request_legacy import FieldServerEndpointsReconfigureFieldRequestLegacy

# TODO update the JSON string below
json = "{}"
# create an instance of FieldServerEndpointsReconfigureFieldRequestLegacy from a JSON string
field_server_endpoints_reconfigure_field_request_legacy_instance = FieldServerEndpointsReconfigureFieldRequestLegacy.from_json(json)
# print the JSON string representation of the object
print(FieldServerEndpointsReconfigureFieldRequestLegacy.to_json())

# convert the object into a dict
field_server_endpoints_reconfigure_field_request_legacy_dict = field_server_endpoints_reconfigure_field_request_legacy_instance.to_dict()
# create an instance of FieldServerEndpointsReconfigureFieldRequestLegacy from a dict
field_server_endpoints_reconfigure_field_request_legacy_from_dict = FieldServerEndpointsReconfigureFieldRequestLegacy.from_dict(field_server_endpoints_reconfigure_field_request_legacy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


