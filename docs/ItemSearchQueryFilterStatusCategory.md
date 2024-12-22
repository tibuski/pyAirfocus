# ItemSearchQueryFilterStatusCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[StatusCategory]**](StatusCategory.md) |  | [optional] 
**value** | [**ItemSearchQueryTimeAnchor**](ItemSearchQueryTimeAnchor.md) |  | 

## Example

```python
from openapi_client.models.item_search_query_filter_status_category import ItemSearchQueryFilterStatusCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSearchQueryFilterStatusCategory from a JSON string
item_search_query_filter_status_category_instance = ItemSearchQueryFilterStatusCategory.from_json(json)
# print the JSON string representation of the object
print(ItemSearchQueryFilterStatusCategory.to_json())

# convert the object into a dict
item_search_query_filter_status_category_dict = item_search_query_filter_status_category_instance.to_dict()
# create an instance of ItemSearchQueryFilterStatusCategory from a dict
item_search_query_filter_status_category_from_dict = ItemSearchQueryFilterStatusCategory.from_dict(item_search_query_filter_status_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


