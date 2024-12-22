# ItemSearchQueryFilterLastUpdatedAt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | [**ItemSearchQueryTimeMode**](ItemSearchQueryTimeMode.md) |  | 
**var_property** | [**ModelProperty**](ModelProperty.md) |  | [optional] 
**value** | [**ItemSearchQueryDateTimeFilterValue**](ItemSearchQueryDateTimeFilterValue.md) |  | 

## Example

```python
from openapi_client.models.item_search_query_filter_last_updated_at import ItemSearchQueryFilterLastUpdatedAt

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSearchQueryFilterLastUpdatedAt from a JSON string
item_search_query_filter_last_updated_at_instance = ItemSearchQueryFilterLastUpdatedAt.from_json(json)
# print the JSON string representation of the object
print(ItemSearchQueryFilterLastUpdatedAt.to_json())

# convert the object into a dict
item_search_query_filter_last_updated_at_dict = item_search_query_filter_last_updated_at_instance.to_dict()
# create an instance of ItemSearchQueryFilterLastUpdatedAt from a dict
item_search_query_filter_last_updated_at_from_dict = ItemSearchQueryFilterLastUpdatedAt.from_dict(item_search_query_filter_last_updated_at_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


