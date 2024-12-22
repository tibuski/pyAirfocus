# FieldSearchQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_team_field** | **bool** | Return only fields with the specified isTeamField value. | [optional] 
**workspace_ids** | **List[str]** | Return only fields which are installed in the specified workspaces. | [optional] 

## Example

```python
from openapi_client.models.field_search_query import FieldSearchQuery

# TODO update the JSON string below
json = "{}"
# create an instance of FieldSearchQuery from a JSON string
field_search_query_instance = FieldSearchQuery.from_json(json)
# print the JSON string representation of the object
print(FieldSearchQuery.to_json())

# convert the object into a dict
field_search_query_dict = field_search_query_instance.to_dict()
# create an instance of FieldSearchQuery from a dict
field_search_query_from_dict = FieldSearchQuery.from_dict(field_search_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


