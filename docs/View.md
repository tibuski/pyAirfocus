# View


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**id** | **str** |  | 
**item_filter** | [**ItemSearchQueryFilter**](ItemSearchQueryFilter.md) |  | [optional] 
**item_sort** | [**List[ItemSearchQuerySort]**](ItemSearchQuerySort.md) |  | [optional] 
**name** | **str** |  | 
**order** | **int** |  | 
**pinned_to_position** | **int** |  | [optional] 
**private_owner_id** | **str** |  | [optional] 
**required_permission** | [**Permission**](Permission.md) |  | [optional] 
**settings** | **object** |  | 
**type_id** | **str** |  | 
**workspace_id** | **str** |  | 

## Example

```python
from openapi_client.models.view import View

# TODO update the JSON string below
json = "{}"
# create an instance of View from a JSON string
view_instance = View.from_json(json)
# print the JSON string representation of the object
print(View.to_json())

# convert the object into a dict
view_dict = view_instance.to_dict()
# create an instance of View from a dict
view_from_dict = View.from_dict(view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


