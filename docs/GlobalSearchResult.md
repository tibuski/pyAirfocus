# GlobalSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** |  | [optional] 
**value** | [**Item**](Item.md) |  | 

## Example

```python
from openapi_client.models.global_search_result import GlobalSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalSearchResult from a JSON string
global_search_result_instance = GlobalSearchResult.from_json(json)
# print the JSON string representation of the object
print(GlobalSearchResult.to_json())

# convert the object into a dict
global_search_result_dict = global_search_result_instance.to_dict()
# create an instance of GlobalSearchResult from a dict
global_search_result_from_dict = GlobalSearchResult.from_dict(global_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


