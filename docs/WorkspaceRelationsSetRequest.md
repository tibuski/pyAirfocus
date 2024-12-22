# WorkspaceRelationsSetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_ids** | **List[str]** |  | [optional] 
**parent_ids** | **List[str]** |  | [optional] 
**workspace_id** | **str** |  | 

## Example

```python
from openapi_client.models.workspace_relations_set_request import WorkspaceRelationsSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceRelationsSetRequest from a JSON string
workspace_relations_set_request_instance = WorkspaceRelationsSetRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceRelationsSetRequest.to_json())

# convert the object into a dict
workspace_relations_set_request_dict = workspace_relations_set_request_instance.to_dict()
# create an instance of WorkspaceRelationsSetRequest from a dict
workspace_relations_set_request_from_dict = WorkspaceRelationsSetRequest.from_dict(workspace_relations_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


