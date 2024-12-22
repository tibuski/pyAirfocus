# openapi_client.DefaultApi

All URIs are relative to *https://app.airfocus.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_inbox_counters**](DefaultApi.md#retrieve_inbox_counters) | **POST** /api/workspaces/extensions/views/inbox/{viewId}/counters | 


# **retrieve_inbox_counters**
> List[InboxCounter] retrieve_inbox_counters(view_id, inbox_view_endpoints_inbox_counters_request, token=token, act_as_admin=act_as_admin)



Returns counters for each.

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.inbox_counter import InboxCounter
from openapi_client.models.inbox_view_endpoints_inbox_counters_request import InboxViewEndpointsInboxCountersRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.airfocus.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://app.airfocus.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: httpAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    view_id = 'view_id_example' # str | 
    inbox_view_endpoints_inbox_counters_request = openapi_client.InboxViewEndpointsInboxCountersRequest() # InboxViewEndpointsInboxCountersRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        api_response = api_instance.retrieve_inbox_counters(view_id, inbox_view_endpoints_inbox_counters_request, token=token, act_as_admin=act_as_admin)
        print("The response of DefaultApi->retrieve_inbox_counters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->retrieve_inbox_counters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**|  | 
 **inbox_view_endpoints_inbox_counters_request** | [**InboxViewEndpointsInboxCountersRequest**](InboxViewEndpointsInboxCountersRequest.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**List[InboxCounter]**](InboxCounter.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

