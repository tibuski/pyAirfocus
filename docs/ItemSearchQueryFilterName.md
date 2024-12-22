# ItemSearchQueryFilterName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_sensitive** | **bool** |  | 
**text** | **str** |  | 

## Example

```python
from openapi_client.models.item_search_query_filter_name import ItemSearchQueryFilterName

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSearchQueryFilterName from a JSON string
item_search_query_filter_name_instance = ItemSearchQueryFilterName.from_json(json)
# print the JSON string representation of the object
print(ItemSearchQueryFilterName.to_json())

# convert the object into a dict
item_search_query_filter_name_dict = item_search_query_filter_name_instance.to_dict()
# create an instance of ItemSearchQueryFilterName from a dict
item_search_query_filter_name_from_dict = ItemSearchQueryFilterName.from_dict(item_search_query_filter_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


