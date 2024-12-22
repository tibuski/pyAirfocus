# ItemSearchQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived** | **bool** |  | 
**filter** | [**ItemSearchQueryFilter**](ItemSearchQueryFilter.md) |  | [optional] 
**sort** | [**ItemSearchQuerySort**](ItemSearchQuerySort.md) |  | 

## Example

```python
from openapi_client.models.item_search_query import ItemSearchQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSearchQuery from a JSON string
item_search_query_instance = ItemSearchQuery.from_json(json)
# print the JSON string representation of the object
print(ItemSearchQuery.to_json())

# convert the object into a dict
item_search_query_dict = item_search_query_instance.to_dict()
# create an instance of ItemSearchQuery from a dict
item_search_query_from_dict = ItemSearchQuery.from_dict(item_search_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


