# ItemRelationSearchQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**ItemRelationSearchQueryFilter**](ItemRelationSearchQueryFilter.md) |  | [optional] 

## Example

```python
from openapi_client.models.item_relation_search_query import ItemRelationSearchQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ItemRelationSearchQuery from a JSON string
item_relation_search_query_instance = ItemRelationSearchQuery.from_json(json)
# print the JSON string representation of the object
print(ItemRelationSearchQuery.to_json())

# convert the object into a dict
item_relation_search_query_dict = item_relation_search_query_instance.to_dict()
# create an instance of ItemRelationSearchQuery from a dict
item_relation_search_query_from_dict = ItemRelationSearchQuery.from_dict(item_relation_search_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


