# ItemSearchQueryFilterAssignees


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserRef**](UserRef.md) |  | 
**users** | [**List[UserRef]**](UserRef.md) |  | [optional] 

## Example

```python
from openapi_client.models.item_search_query_filter_assignees import ItemSearchQueryFilterAssignees

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSearchQueryFilterAssignees from a JSON string
item_search_query_filter_assignees_instance = ItemSearchQueryFilterAssignees.from_json(json)
# print the JSON string representation of the object
print(ItemSearchQueryFilterAssignees.to_json())

# convert the object into a dict
item_search_query_filter_assignees_dict = item_search_query_filter_assignees_instance.to_dict()
# create an instance of ItemSearchQueryFilterAssignees from a dict
item_search_query_filter_assignees_from_dict = ItemSearchQueryFilterAssignees.from_dict(item_search_query_filter_assignees_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


