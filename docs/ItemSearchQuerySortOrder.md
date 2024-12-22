# ItemSearchQuerySortOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**ItemSearchQuerySortDirection**](ItemSearchQuerySortDirection.md) |  | 

## Example

```python
from openapi_client.models.item_search_query_sort_order import ItemSearchQuerySortOrder

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSearchQuerySortOrder from a JSON string
item_search_query_sort_order_instance = ItemSearchQuerySortOrder.from_json(json)
# print the JSON string representation of the object
print(ItemSearchQuerySortOrder.to_json())

# convert the object into a dict
item_search_query_sort_order_dict = item_search_query_sort_order_instance.to_dict()
# create an instance of ItemSearchQuerySortOrder from a dict
item_search_query_sort_order_from_dict = ItemSearchQuerySortOrder.from_dict(item_search_query_sort_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


