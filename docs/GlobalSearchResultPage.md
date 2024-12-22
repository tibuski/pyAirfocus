# GlobalSearchResultPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[GlobalSearchResult]**](GlobalSearchResult.md) |  | [optional] 
**total_items** | **int** |  | 

## Example

```python
from openapi_client.models.global_search_result_page import GlobalSearchResultPage

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalSearchResultPage from a JSON string
global_search_result_page_instance = GlobalSearchResultPage.from_json(json)
# print the JSON string representation of the object
print(GlobalSearchResultPage.to_json())

# convert the object into a dict
global_search_result_page_dict = global_search_result_page_instance.to_dict()
# create an instance of GlobalSearchResultPage from a dict
global_search_result_page_from_dict = GlobalSearchResultPage.from_dict(global_search_result_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


