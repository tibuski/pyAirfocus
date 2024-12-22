# WorkspaceGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**default_permission** | [**Permission**](Permission.md) |  | [optional] 
**id** | **str** |  | 
**last_updated_at** | **datetime** |  | 
**name** | **str** |  | 
**team_id** | **str** |  | 

## Example

```python
from openapi_client.models.workspace_group import WorkspaceGroup

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceGroup from a JSON string
workspace_group_instance = WorkspaceGroup.from_json(json)
# print the JSON string representation of the object
print(WorkspaceGroup.to_json())

# convert the object into a dict
workspace_group_dict = workspace_group_instance.to_dict()
# create an instance of WorkspaceGroup from a dict
workspace_group_from_dict = WorkspaceGroup.from_dict(workspace_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


