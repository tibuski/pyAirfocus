# ItemSearchQuerySort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**ItemSearchQuerySortDirection**](ItemSearchQuerySortDirection.md) |  | 
**field_id** | **str** |  | 

## Example

```python
from openapi_client.models.item_search_query_sort import ItemSearchQuerySort

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSearchQuerySort from a JSON string
item_search_query_sort_instance = ItemSearchQuerySort.from_json(json)
# print the JSON string representation of the object
print(ItemSearchQuerySort.to_json())

# convert the object into a dict
item_search_query_sort_dict = item_search_query_sort_instance.to_dict()
# create an instance of ItemSearchQuerySort from a dict
item_search_query_sort_from_dict = ItemSearchQuerySort.from_dict(item_search_query_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


