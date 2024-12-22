# ItemSearchQueryFilterCreatedAt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | [**ItemSearchQueryTimeMode**](ItemSearchQueryTimeMode.md) |  | 
**value** | [**ItemSearchQueryDateTimeFilterValue**](ItemSearchQueryDateTimeFilterValue.md) |  | 

## Example

```python
from openapi_client.models.item_search_query_filter_created_at import ItemSearchQueryFilterCreatedAt

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSearchQueryFilterCreatedAt from a JSON string
item_search_query_filter_created_at_instance = ItemSearchQueryFilterCreatedAt.from_json(json)
# print the JSON string representation of the object
print(ItemSearchQueryFilterCreatedAt.to_json())

# convert the object into a dict
item_search_query_filter_created_at_dict = item_search_query_filter_created_at_instance.to_dict()
# create an instance of ItemSearchQueryFilterCreatedAt from a dict
item_search_query_filter_created_at_from_dict = ItemSearchQueryFilterCreatedAt.from_dict(item_search_query_filter_created_at_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


