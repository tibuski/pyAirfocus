# GlobalSearchResultItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** |  | [optional] 
**value** | [**Item**](Item.md) |  | 

## Example

```python
from openapi_client.models.global_search_result_item import GlobalSearchResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalSearchResultItem from a JSON string
global_search_result_item_instance = GlobalSearchResultItem.from_json(json)
# print the JSON string representation of the object
print(GlobalSearchResultItem.to_json())

# convert the object into a dict
global_search_result_item_dict = global_search_result_item_instance.to_dict()
# create an instance of GlobalSearchResultItem from a dict
global_search_result_item_from_dict = GlobalSearchResultItem.from_dict(global_search_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


