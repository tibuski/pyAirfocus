# InstallTextFieldRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | User-readable field description. | [optional] [default to '']
**is_team_field** | **bool** | Whether the field should be installed as a team-field or a workspace-specific field. | [optional] [default to False]
**name** | **str** | User-readable field name. | 
**type_id** | **str** |  | 
**workspace_ids** | **List[str]** | If isTeamField&#x3D;false then exactly one workspace ID should be provided. If isTeamField&#x3D;true then any amount of workspace IDs can be provided to be linked to the newly installed field. | [optional] 

## Example

```python
from openapi_client.models.install_text_field_request import InstallTextFieldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstallTextFieldRequest from a JSON string
install_text_field_request_instance = InstallTextFieldRequest.from_json(json)
# print the JSON string representation of the object
print(InstallTextFieldRequest.to_json())

# convert the object into a dict
install_text_field_request_dict = install_text_field_request_instance.to_dict()
# create an instance of InstallTextFieldRequest from a dict
install_text_field_request_from_dict = InstallTextFieldRequest.from_dict(install_text_field_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


