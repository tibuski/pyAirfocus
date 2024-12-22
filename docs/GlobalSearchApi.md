# openapi_client.GlobalSearchApi

All URIs are relative to *https://app.airfocus.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_global**](GlobalSearchApi.md#search_global) | **POST** /api/workspaces/global-search | 


# **search_global**
> GlobalSearchResultPage search_global(token=token, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, global_search_query=global_search_query)



Requirements:<br/>- auth-client scopes: \"workspace:read\"

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.global_search_query import GlobalSearchQuery
from openapi_client.models.global_search_result_page import GlobalSearchResultPage
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
    api_instance = openapi_client.GlobalSearchApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    offset = 0 # int | How many elements to skip. (optional) (default to 0)
    limit = 25 # int | How many elements to return. (optional) (default to 25)
    var_from = 0 # int | From which element the page should start. (optional) (default to 0)
    to = 56 # int | At which element the page should end (excluding it). (optional)
    global_search_query = openapi_client.GlobalSearchQuery() # GlobalSearchQuery |  (optional)

    try:
        api_response = api_instance.search_global(token=token, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, global_search_query=global_search_query)
        print("The response of GlobalSearchApi->search_global:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalSearchApi->search_global: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **offset** | **int**| How many elements to skip. | [optional] [default to 0]
 **limit** | **int**| How many elements to return. | [optional] [default to 25]
 **var_from** | **int**| From which element the page should start. | [optional] [default to 0]
 **to** | **int**| At which element the page should end (excluding it). | [optional] 
 **global_search_query** | [**GlobalSearchQuery**](GlobalSearchQuery.md)|  | [optional] 

### Return type

[**GlobalSearchResultPage**](GlobalSearchResultPage.md)

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

