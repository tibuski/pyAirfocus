# GlobalSearchQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived** | **bool** | Search only archived or only non-archived items (only non-archived by default) | [optional] 
**assignee_user_ids** | **List[str]** | Narrow down the search to items which are assigned to the specified users | [optional] 
**context_query** | **str** | Context-string for AI to match items by similarity | [optional] 
**search_query** | **str** | Text to search in contents of items | [optional] 
**status_categories** | [**List[StatusCategory]**](StatusCategory.md) | Narrow down the search to items with status in the specified status-categories | [optional] 
**workspace_ids** | **List[str]** | Narrow down the search to specific workspaces | [optional] 

## Example

```python
from openapi_client.models.global_search_query import GlobalSearchQuery

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalSearchQuery from a JSON string
global_search_query_instance = GlobalSearchQuery.from_json(json)
# print the JSON string representation of the object
print(GlobalSearchQuery.to_json())

# convert the object into a dict
global_search_query_dict = global_search_query_instance.to_dict()
# create an instance of GlobalSearchQuery from a dict
global_search_query_from_dict = GlobalSearchQuery.from_dict(global_search_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


