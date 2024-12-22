# FieldServerEndpointsInstallFieldRequestLegacy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**is_team_field** | **bool** |  | 
**name** | **str** |  | 
**settings** | **object** |  | 
**type_id** | **str** |  | 
**workspace_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.field_server_endpoints_install_field_request_legacy import FieldServerEndpointsInstallFieldRequestLegacy

# TODO update the JSON string below
json = "{}"
# create an instance of FieldServerEndpointsInstallFieldRequestLegacy from a JSON string
field_server_endpoints_install_field_request_legacy_instance = FieldServerEndpointsInstallFieldRequestLegacy.from_json(json)
# print the JSON string representation of the object
print(FieldServerEndpointsInstallFieldRequestLegacy.to_json())

# convert the object into a dict
field_server_endpoints_install_field_request_legacy_dict = field_server_endpoints_install_field_request_legacy_instance.to_dict()
# create an instance of FieldServerEndpointsInstallFieldRequestLegacy from a dict
field_server_endpoints_install_field_request_legacy_from_dict = FieldServerEndpointsInstallFieldRequestLegacy.from_dict(field_server_endpoints_install_field_request_legacy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


