# IntegrationSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**IntegrationCapabilities**](IntegrationCapabilities.md) |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**last_sync_at** | **datetime** |  | [optional] 
**last_sync_state** | [**IntegrationSyncState**](IntegrationSyncState.md) |  | [optional] 
**settings** | **object** |  | 
**type_id** | **str** |  | 

## Example

```python
from openapi_client.models.integration_summary import IntegrationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationSummary from a JSON string
integration_summary_instance = IntegrationSummary.from_json(json)
# print the JSON string representation of the object
print(IntegrationSummary.to_json())

# convert the object into a dict
integration_summary_dict = integration_summary_instance.to_dict()
# create an instance of IntegrationSummary from a dict
integration_summary_from_dict = IntegrationSummary.from_dict(integration_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


