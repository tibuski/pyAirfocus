# WorkspaceRelationSearchQueryFilterParent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_ids** | **List[str]** |  | [optional] 
**workspace_id** | **str** |  | 

## Example

```python
from openapi_client.models.workspace_relation_search_query_filter_parent import WorkspaceRelationSearchQueryFilterParent

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceRelationSearchQueryFilterParent from a JSON string
workspace_relation_search_query_filter_parent_instance = WorkspaceRelationSearchQueryFilterParent.from_json(json)
# print the JSON string representation of the object
print(WorkspaceRelationSearchQueryFilterParent.to_json())

# convert the object into a dict
workspace_relation_search_query_filter_parent_dict = workspace_relation_search_query_filter_parent_instance.to_dict()
# create an instance of WorkspaceRelationSearchQueryFilterParent from a dict
workspace_relation_search_query_filter_parent_from_dict = WorkspaceRelationSearchQueryFilterParent.from_dict(workspace_relation_search_query_filter_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


