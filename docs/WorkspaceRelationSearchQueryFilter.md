# WorkspaceRelationSearchQueryFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inner** | [**WorkspaceRelationSearchQueryFilter**](WorkspaceRelationSearchQueryFilter.md) |  | 
**workspace_ids** | **List[str]** |  | [optional] 
**workspace_id** | **str** |  | 

## Example

```python
from openapi_client.models.workspace_relation_search_query_filter import WorkspaceRelationSearchQueryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceRelationSearchQueryFilter from a JSON string
workspace_relation_search_query_filter_instance = WorkspaceRelationSearchQueryFilter.from_json(json)
# print the JSON string representation of the object
print(WorkspaceRelationSearchQueryFilter.to_json())

# convert the object into a dict
workspace_relation_search_query_filter_dict = workspace_relation_search_query_filter_instance.to_dict()
# create an instance of WorkspaceRelationSearchQueryFilter from a dict
workspace_relation_search_query_filter_from_dict = WorkspaceRelationSearchQueryFilter.from_dict(workspace_relation_search_query_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


