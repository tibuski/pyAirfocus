# ItemSearchQueryDateTimeFilterValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | 
**time** | **str** |  | [optional] 
**zone_id** | **str** |  | 

## Example

```python
from openapi_client.models.item_search_query_date_time_filter_value import ItemSearchQueryDateTimeFilterValue

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSearchQueryDateTimeFilterValue from a JSON string
item_search_query_date_time_filter_value_instance = ItemSearchQueryDateTimeFilterValue.from_json(json)
# print the JSON string representation of the object
print(ItemSearchQueryDateTimeFilterValue.to_json())

# convert the object into a dict
item_search_query_date_time_filter_value_dict = item_search_query_date_time_filter_value_instance.to_dict()
# create an instance of ItemSearchQueryDateTimeFilterValue from a dict
item_search_query_date_time_filter_value_from_dict = ItemSearchQueryDateTimeFilterValue.from_dict(item_search_query_date_time_filter_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


