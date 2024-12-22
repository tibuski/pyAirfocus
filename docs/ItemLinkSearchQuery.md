# ItemLinkSearchQuery

Query-parameters for searching links.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_archived** | **bool** | Also include links which connect archived items. | [optional] [default to False]
**item_ids** | **List[str]** | Return only those links which connect the specified items. | [optional] 
**workspace_ids** | **List[str]** | Return only those links which connect items in the specified workspaces. | [optional] 

## Example

```python
from openapi_client.models.item_link_search_query import ItemLinkSearchQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ItemLinkSearchQuery from a JSON string
item_link_search_query_instance = ItemLinkSearchQuery.from_json(json)
# print the JSON string representation of the object
print(ItemLinkSearchQuery.to_json())

# convert the object into a dict
item_link_search_query_dict = item_link_search_query_instance.to_dict()
# create an instance of ItemLinkSearchQuery from a dict
item_link_search_query_from_dict = ItemLinkSearchQuery.from_dict(item_link_search_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


