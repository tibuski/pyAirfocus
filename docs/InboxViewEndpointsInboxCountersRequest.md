# InboxViewEndpointsInboxCountersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived** | **bool** |  | 
**count_assigned** | **bool** |  | 
**filter** | [**ItemSearchQueryFilter**](ItemSearchQueryFilter.md) |  | [optional] 

## Example

```python
from openapi_client.models.inbox_view_endpoints_inbox_counters_request import InboxViewEndpointsInboxCountersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InboxViewEndpointsInboxCountersRequest from a JSON string
inbox_view_endpoints_inbox_counters_request_instance = InboxViewEndpointsInboxCountersRequest.from_json(json)
# print the JSON string representation of the object
print(InboxViewEndpointsInboxCountersRequest.to_json())

# convert the object into a dict
inbox_view_endpoints_inbox_counters_request_dict = inbox_view_endpoints_inbox_counters_request_instance.to_dict()
# create an instance of InboxViewEndpointsInboxCountersRequest from a dict
inbox_view_endpoints_inbox_counters_request_from_dict = InboxViewEndpointsInboxCountersRequest.from_dict(inbox_view_endpoints_inbox_counters_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


