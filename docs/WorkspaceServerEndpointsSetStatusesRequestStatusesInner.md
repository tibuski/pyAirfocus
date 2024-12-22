# WorkspaceServerEndpointsSetStatusesRequestStatusesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**StatusCategory**](StatusCategory.md) |  | 
**color** | [**StatusColor**](StatusColor.md) |  | [optional] 
**default** | **bool** | Whether this status should be applied by default to newly created items. There can be only one default status in each workspace. | 
**name** | **str** | Name of this status in UI. | 
**order** | **int** | Order of this status comparing to other statuses in the same workspace. | 
**id** | **str** |  | 

## Example

```python
from openapi_client.models.workspace_server_endpoints_set_statuses_request_statuses_inner import WorkspaceServerEndpointsSetStatusesRequestStatusesInner

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceServerEndpointsSetStatusesRequestStatusesInner from a JSON string
workspace_server_endpoints_set_statuses_request_statuses_inner_instance = WorkspaceServerEndpointsSetStatusesRequestStatusesInner.from_json(json)
# print the JSON string representation of the object
print(WorkspaceServerEndpointsSetStatusesRequestStatusesInner.to_json())

# convert the object into a dict
workspace_server_endpoints_set_statuses_request_statuses_inner_dict = workspace_server_endpoints_set_statuses_request_statuses_inner_instance.to_dict()
# create an instance of WorkspaceServerEndpointsSetStatusesRequestStatusesInner from a dict
workspace_server_endpoints_set_statuses_request_statuses_inner_from_dict = WorkspaceServerEndpointsSetStatusesRequestStatusesInner.from_dict(workspace_server_endpoints_set_statuses_request_statuses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


