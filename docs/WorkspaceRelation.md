# WorkspaceRelation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_id** | **str** |  | 
**id** | **str** |  | 
**parent_id** | **str** |  | 

## Example

```python
from openapi_client.models.workspace_relation import WorkspaceRelation

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceRelation from a JSON string
workspace_relation_instance = WorkspaceRelation.from_json(json)
# print the JSON string representation of the object
print(WorkspaceRelation.to_json())

# convert the object into a dict
workspace_relation_dict = workspace_relation_instance.to_dict()
# create an instance of WorkspaceRelation from a dict
workspace_relation_from_dict = WorkspaceRelation.from_dict(workspace_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


