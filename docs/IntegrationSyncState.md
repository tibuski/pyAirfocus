# IntegrationSyncState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_count** | **int** |  | 
**success_count** | **int** |  | 

## Example

```python
from openapi_client.models.integration_sync_state import IntegrationSyncState

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationSyncState from a JSON string
integration_sync_state_instance = IntegrationSyncState.from_json(json)
# print the JSON string representation of the object
print(IntegrationSyncState.to_json())

# convert the object into a dict
integration_sync_state_dict = integration_sync_state_instance.to_dict()
# create an instance of IntegrationSyncState from a dict
integration_sync_state_from_dict = IntegrationSyncState.from_dict(integration_sync_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


