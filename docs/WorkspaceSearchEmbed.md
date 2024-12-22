# WorkspaceSearchEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_permission** | [**Permission**](Permission.md) |  | [optional] 
**item_count** | **int** |  | 
**permissions** | [**Dict[str, Permission]**](Permission.md) |  | 
**statuses** | [**Dict[str, Status]**](Status.md) |  | 

## Example

```python
from openapi_client.models.workspace_search_embed import WorkspaceSearchEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceSearchEmbed from a JSON string
workspace_search_embed_instance = WorkspaceSearchEmbed.from_json(json)
# print the JSON string representation of the object
print(WorkspaceSearchEmbed.to_json())

# convert the object into a dict
workspace_search_embed_dict = workspace_search_embed_instance.to_dict()
# create an instance of WorkspaceSearchEmbed from a dict
workspace_search_embed_from_dict = WorkspaceSearchEmbed.from_dict(workspace_search_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


