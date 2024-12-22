# WorkspaceServerEndpointsSetStatusesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replacements** | **Dict[str, str]** | A map of status replacements, where key is and OLD status-id and value is a NEW status-id. Replacements must be specified for each status being deleted from the workspace.This mapping will be used to migrate all items in the workspace to new statuses before deleting the old ones. | 
**statuses** | [**List[WorkspaceServerEndpointsSetStatusesRequestStatusesInner]**](WorkspaceServerEndpointsSetStatusesRequestStatusesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.workspace_server_endpoints_set_statuses_request import WorkspaceServerEndpointsSetStatusesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceServerEndpointsSetStatusesRequest from a JSON string
workspace_server_endpoints_set_statuses_request_instance = WorkspaceServerEndpointsSetStatusesRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceServerEndpointsSetStatusesRequest.to_json())

# convert the object into a dict
workspace_server_endpoints_set_statuses_request_dict = workspace_server_endpoints_set_statuses_request_instance.to_dict()
# create an instance of WorkspaceServerEndpointsSetStatusesRequest from a dict
workspace_server_endpoints_set_statuses_request_from_dict = WorkspaceServerEndpointsSetStatusesRequest.from_dict(workspace_server_endpoints_set_statuses_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


