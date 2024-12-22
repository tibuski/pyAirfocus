# openapi_client.ItemLinksApi

All URIs are relative to *https://app.airfocus.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_item_links**](ItemLinksApi.md#bulk_item_links) | **POST** /api/workspaces/{workspaceId}/links/bulk | Perform multiple operations with item links
[**create_item_link**](ItemLinksApi.md#create_item_link) | **POST** /api/workspaces/{workspaceId}/links | Create a new item link
[**delete_item_link**](ItemLinksApi.md#delete_item_link) | **DELETE** /api/workspaces/{workspaceId}/links/{itemLinkId} | Delete an existing item link
[**list_item_links**](ItemLinksApi.md#list_item_links) | **POST** /api/workspaces/{workspaceId}/links/list | Retrieve multiple item links by their IDs
[**patch_item_link**](ItemLinksApi.md#patch_item_link) | **PATCH** /api/workspaces/{workspaceId}/links/{itemLinkId} | Patch an existing item link
[**retrieve_item_link**](ItemLinksApi.md#retrieve_item_link) | **GET** /api/workspaces/{workspaceId}/links/{itemLinkId} | Retrieve a single item link by its ID
[**search_item_links**](ItemLinksApi.md#search_item_links) | **POST** /api/workspaces/{workspaceId}/links/search | Retrieve or search item links
[**update_item_link**](ItemLinksApi.md#update_item_link) | **PUT** /api/workspaces/{workspaceId}/links/{itemLinkId} | Update an existing item link


# **bulk_item_links**
> List[ItemLinkWithItemLinkEmbed] bulk_item_links(workspace_id, token=token, act_as_admin=act_as_admin, item_link_bulk_action=item_link_bulk_action)

Perform multiple operations with item links

Accepts a list of create/update/patch/delete operations (see the request model for more details).<br/> Each operations can target a single or multiple item links.<br/> Returns a list of results for each input operation including errors.<br/> Guarantees that the size and order of the returned results matches the input list of operations.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.item_link_bulk_action import ItemLinkBulkAction
from openapi_client.models.item_link_with_item_link_embed import ItemLinkWithItemLinkEmbed
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
    api_instance = openapi_client.ItemLinksApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed links.
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    item_link_bulk_action = [openapi_client.ItemLinkBulkAction()] # List[ItemLinkBulkAction] |  (optional)

    try:
        # Perform multiple operations with item links
        api_response = api_instance.bulk_item_links(workspace_id, token=token, act_as_admin=act_as_admin, item_link_bulk_action=item_link_bulk_action)
        print("The response of ItemLinksApi->bulk_item_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLinksApi->bulk_item_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed links. | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **item_link_bulk_action** | [**List[ItemLinkBulkAction]**](ItemLinkBulkAction.md)|  | [optional] 

### Return type

[**List[ItemLinkWithItemLinkEmbed]**](ItemLinkWithItemLinkEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_item_link**
> ItemLinkWithItemLinkEmbed create_item_link(workspace_id, item_link, token=token, act_as_admin=act_as_admin)

Create a new item link

Returns newly created item link with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.item_link import ItemLink
from openapi_client.models.item_link_with_item_link_embed import ItemLinkWithItemLinkEmbed
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
    api_instance = openapi_client.ItemLinksApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed links.
    item_link = openapi_client.ItemLink() # ItemLink | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Create a new item link
        api_response = api_instance.create_item_link(workspace_id, item_link, token=token, act_as_admin=act_as_admin)
        print("The response of ItemLinksApi->create_item_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLinksApi->create_item_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed links. | 
 **item_link** | [**ItemLink**](ItemLink.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemLinkWithItemLinkEmbed**](ItemLinkWithItemLinkEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_link**
> delete_item_link(workspace_id, item_link_id, token=token, act_as_admin=act_as_admin)

Delete an existing item link

Returns empty result if the item link was successfully deleted.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
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
    api_instance = openapi_client.ItemLinksApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed links.
    item_link_id = 'item_link_id_example' # str | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Delete an existing item link
        api_instance.delete_item_link(workspace_id, item_link_id, token=token, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling ItemLinksApi->delete_item_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed links. | 
 **item_link_id** | **str**|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

void (empty response body)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_item_links**
> List[ItemLinkWithItemLinkEmbed] list_item_links(workspace_id, token=token, act_as_admin=act_as_admin, request_body=request_body)

Retrieve multiple item links by their IDs

Returns a list of item links.<br/> Returns null for those item links which are not found or not accessible.<br/> Guarantees that the size and order of the returned list matches the requested IDs.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.item_link_with_item_link_embed import ItemLinkWithItemLinkEmbed
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
    api_instance = openapi_client.ItemLinksApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed links.
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Retrieve multiple item links by their IDs
        api_response = api_instance.list_item_links(workspace_id, token=token, act_as_admin=act_as_admin, request_body=request_body)
        print("The response of ItemLinksApi->list_item_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLinksApi->list_item_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed links. | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ItemLinkWithItemLinkEmbed]**](ItemLinkWithItemLinkEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_item_link**
> ItemLinkWithItemLinkEmbed patch_item_link(workspace_id, item_link_id, json_patch_operation, token=token, act_as_admin=act_as_admin)

Patch an existing item link

Returns the whole updated item link with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.item_link_with_item_link_embed import ItemLinkWithItemLinkEmbed
from openapi_client.models.json_patch_operation import JsonPatchOperation
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
    api_instance = openapi_client.ItemLinksApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed links.
    item_link_id = 'item_link_id_example' # str | 
    json_patch_operation = [openapi_client.JsonPatchOperation()] # List[JsonPatchOperation] | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Patch an existing item link
        api_response = api_instance.patch_item_link(workspace_id, item_link_id, json_patch_operation, token=token, act_as_admin=act_as_admin)
        print("The response of ItemLinksApi->patch_item_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLinksApi->patch_item_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed links. | 
 **item_link_id** | **str**|  | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemLinkWithItemLinkEmbed**](ItemLinkWithItemLinkEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_item_link**
> ItemLinkWithItemLinkEmbed retrieve_item_link(workspace_id, item_link_id, token=token, act_as_admin=act_as_admin)

Retrieve a single item link by its ID

Returns found item link.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.item_link_with_item_link_embed import ItemLinkWithItemLinkEmbed
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
    api_instance = openapi_client.ItemLinksApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed links.
    item_link_id = 'item_link_id_example' # str | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Retrieve a single item link by its ID
        api_response = api_instance.retrieve_item_link(workspace_id, item_link_id, token=token, act_as_admin=act_as_admin)
        print("The response of ItemLinksApi->retrieve_item_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLinksApi->retrieve_item_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed links. | 
 **item_link_id** | **str**|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemLinkWithItemLinkEmbed**](ItemLinkWithItemLinkEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_item_links**
> ItemLinkWithItemLinkEmbedPage search_item_links(workspace_id, token=token, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, item_link_search_query=item_link_search_query)

Retrieve or search item links

Returns all item links or searches item links by query. Always returns only item links which are accessible by the current user.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.item_link_search_query import ItemLinkSearchQuery
from openapi_client.models.item_link_with_item_link_embed_page import ItemLinkWithItemLinkEmbedPage
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
    api_instance = openapi_client.ItemLinksApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed links.
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    offset = 0 # int | How many elements to skip. (optional) (default to 0)
    limit = 1000 # int | How many elements to return. (optional) (default to 1000)
    var_from = 0 # int | From which element the page should start. (optional) (default to 0)
    to = 56 # int | At which element the page should end (excluding it). (optional)
    item_link_search_query = openapi_client.ItemLinkSearchQuery() # ItemLinkSearchQuery |  (optional)

    try:
        # Retrieve or search item links
        api_response = api_instance.search_item_links(workspace_id, token=token, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, item_link_search_query=item_link_search_query)
        print("The response of ItemLinksApi->search_item_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLinksApi->search_item_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed links. | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **offset** | **int**| How many elements to skip. | [optional] [default to 0]
 **limit** | **int**| How many elements to return. | [optional] [default to 1000]
 **var_from** | **int**| From which element the page should start. | [optional] [default to 0]
 **to** | **int**| At which element the page should end (excluding it). | [optional] 
 **item_link_search_query** | [**ItemLinkSearchQuery**](ItemLinkSearchQuery.md)|  | [optional] 

### Return type

[**ItemLinkWithItemLinkEmbedPage**](ItemLinkWithItemLinkEmbedPage.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_link**
> ItemLinkWithItemLinkEmbed update_item_link(workspace_id, item_link_id, item_link, token=token, act_as_admin=act_as_admin)

Update an existing item link

Returns updated item link with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.item_link import ItemLink
from openapi_client.models.item_link_with_item_link_embed import ItemLinkWithItemLinkEmbed
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
    api_instance = openapi_client.ItemLinksApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed links.
    item_link_id = 'item_link_id_example' # str | 
    item_link = openapi_client.ItemLink() # ItemLink | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update an existing item link
        api_response = api_instance.update_item_link(workspace_id, item_link_id, item_link, token=token, act_as_admin=act_as_admin)
        print("The response of ItemLinksApi->update_item_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLinksApi->update_item_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed links. | 
 **item_link_id** | **str**|  | 
 **item_link** | [**ItemLink**](ItemLink.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemLinkWithItemLinkEmbed**](ItemLinkWithItemLinkEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

