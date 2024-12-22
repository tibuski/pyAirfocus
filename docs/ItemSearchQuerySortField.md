# ItemSearchQuerySortField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**ItemSearchQuerySortDirection**](ItemSearchQuerySortDirection.md) |  | 
**field_id** | **str** |  | 

## Example

```python
from openapi_client.models.item_search_query_sort_field import ItemSearchQuerySortField

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSearchQuerySortField from a JSON string
item_search_query_sort_field_instance = ItemSearchQuerySortField.from_json(json)
# print the JSON string representation of the object
print(ItemSearchQuerySortField.to_json())

# convert the object into a dict
item_search_query_sort_field_dict = item_search_query_sort_field_instance.to_dict()
# create an instance of ItemSearchQuerySortField from a dict
item_search_query_sort_field_from_dict = ItemSearchQuerySortField.from_dict(item_search_query_sort_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


