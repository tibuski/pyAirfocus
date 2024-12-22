# ItemSearchQueryFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inner** | [**ItemSearchQueryFilter**](ItemSearchQueryFilter.md) |  | 
**mode** | [**ItemSearchQueryTimeMode**](ItemSearchQueryTimeMode.md) |  | 
**value** | [**ItemSearchQueryTimeAnchor**](ItemSearchQueryTimeAnchor.md) |  | 
**field_id** | **str** |  | 
**filter** | **object** |  | 
**integration_id** | **str** |  | 
**var_property** | [**ModelProperty**](ModelProperty.md) |  | [optional] 
**case_sensitive** | **bool** |  | 
**text** | **str** |  | 
**item_id** | **str** |  | 
**workspace_id** | **str** |  | 
**status_ids** | **List[str]** |  | [optional] 
**categories** | [**List[StatusCategory]**](StatusCategory.md) |  | [optional] 
**timestamp** | **datetime** |  | 

## Example

```python
from openapi_client.models.item_search_query_filter import ItemSearchQueryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSearchQueryFilter from a JSON string
item_search_query_filter_instance = ItemSearchQueryFilter.from_json(json)
# print the JSON string representation of the object
print(ItemSearchQueryFilter.to_json())

# convert the object into a dict
item_search_query_filter_dict = item_search_query_filter_instance.to_dict()
# create an instance of ItemSearchQueryFilter from a dict
item_search_query_filter_from_dict = ItemSearchQueryFilter.from_dict(item_search_query_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


