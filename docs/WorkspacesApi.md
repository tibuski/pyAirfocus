# openapi_client.WorkspacesApi

All URIs are relative to *https://app.airfocus.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_workspaces**](WorkspacesApi.md#bulk_workspaces) | **POST** /api/workspaces/bulk | Perform multiple operations with workspaces
[**count_workspaces**](WorkspacesApi.md#count_workspaces) | **GET** /api/workspaces/count | Count workspaces in the current team.
[**create_workspace**](WorkspacesApi.md#create_workspace) | **POST** /api/workspaces | Create a new workspace
[**delete_workspace**](WorkspacesApi.md#delete_workspace) | **DELETE** /api/workspaces/{workspaceId} | Delete an existing workspace
[**duplicate_workspace**](WorkspacesApi.md#duplicate_workspace) | **POST** /api/workspaces/{workspaceId}/duplicate | Duplicate workspace with all its items and apps.
[**list_workspaces**](WorkspacesApi.md#list_workspaces) | **POST** /api/workspaces/list | Retrieve multiple workspaces by their IDs
[**patch_workspace**](WorkspacesApi.md#patch_workspace) | **PATCH** /api/workspaces/{workspaceId} | Patch an existing workspace
[**retrieve_workspace**](WorkspacesApi.md#retrieve_workspace) | **GET** /api/workspaces/{workspaceId} | Retrieve a single workspace by its ID
[**search_workspaces**](WorkspacesApi.md#search_workspaces) | **POST** /api/workspaces/search | Retrieve or search workspaces
[**set_workspace_statuses**](WorkspacesApi.md#set_workspace_statuses) | **POST** /api/workspaces/{workspaceId}/statuses | 
[**update_workspace**](WorkspacesApi.md#update_workspace) | **PUT** /api/workspaces/{workspaceId} | Update an existing workspace
[**update_workspace_permissions**](WorkspacesApi.md#update_workspace_permissions) | **POST** /api/workspaces/{workspaceId}/permissions | Update workspace permissions.
[**workspace_background_activity_sse**](WorkspacesApi.md#workspace_background_activity_sse) | **GET** /api/workspaces/{workspaceId}/background-activity/sse | Server-sent-events for background activity in workspace.
[**workspace_events_by_workspace_id_sse**](WorkspacesApi.md#workspace_events_by_workspace_id_sse) | **GET** /api/workspaces/{workspaceId}/events/sse | Server-side-events for updates in a single workspace.
[**workspace_events_sse**](WorkspacesApi.md#workspace_events_sse) | **GET** /api/workspaces/events/sse | Server-side-events for updates in all workspaces.


# **bulk_workspaces**
> List[WorkspaceWithWorkspaceEmbed] bulk_workspaces(token=token, act_as_admin=act_as_admin, workspace_bulk_action=workspace_bulk_action)

Perform multiple operations with workspaces

Accepts a list of create/update/patch/delete operations (see the request model for more details).<br/> Each operations can target a single or multiple workspaces.<br/> Returns a list of results for each input operation including errors.<br/> Guarantees that the size and order of the returned results matches the input list of operations.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace_bulk_action import WorkspaceBulkAction
from openapi_client.models.workspace_with_workspace_embed import WorkspaceWithWorkspaceEmbed
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
    api_instance = openapi_client.WorkspacesApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    workspace_bulk_action = [openapi_client.WorkspaceBulkAction()] # List[WorkspaceBulkAction] |  (optional)

    try:
        # Perform multiple operations with workspaces
        api_response = api_instance.bulk_workspaces(token=token, act_as_admin=act_as_admin, workspace_bulk_action=workspace_bulk_action)
        print("The response of WorkspacesApi->bulk_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->bulk_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **workspace_bulk_action** | [**List[WorkspaceBulkAction]**](WorkspaceBulkAction.md)|  | [optional] 

### Return type

[**List[WorkspaceWithWorkspaceEmbed]**](WorkspaceWithWorkspaceEmbed.md)

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

# **count_workspaces**
> int count_workspaces(token=token, act_as_admin=act_as_admin)

Count workspaces in the current team.

Returns the total counter number.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>Returns:<br/>403 if user does not have the required permission

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
    api_instance = openapi_client.WorkspacesApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Count workspaces in the current team.
        api_response = api_instance.count_workspaces(token=token, act_as_admin=act_as_admin)
        print("The response of WorkspacesApi->count_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->count_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

**int**

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

# **create_workspace**
> WorkspaceWithWorkspaceEmbed create_workspace(workspace, token=token, act_as_admin=act_as_admin)

Create a new workspace

Returns newly created workspace with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace import Workspace
from openapi_client.models.workspace_with_workspace_embed import WorkspaceWithWorkspaceEmbed
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
    api_instance = openapi_client.WorkspacesApi(api_client)
    workspace = openapi_client.Workspace() # Workspace | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Create a new workspace
        api_response = api_instance.create_workspace(workspace, token=token, act_as_admin=act_as_admin)
        print("The response of WorkspacesApi->create_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->create_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | [**Workspace**](Workspace.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceWithWorkspaceEmbed**](WorkspaceWithWorkspaceEmbed.md)

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

# **delete_workspace**
> delete_workspace(workspace_id, token=token, act_as_admin=act_as_admin)

Delete an existing workspace

Returns empty result if the workspace was successfully deleted.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

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
    api_instance = openapi_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Delete an existing workspace
        api_instance.delete_workspace(workspace_id, token=token, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling WorkspacesApi->delete_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
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

# **duplicate_workspace**
> WorkspaceWithWorkspaceEmbed duplicate_workspace(workspace_id, workspace_server_endpoints_workspace_duplicate_request, token=token, act_as_admin=act_as_admin)

Duplicate workspace with all its items and apps.

Returns the newly created workspace with embedded data.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace_server_endpoints_workspace_duplicate_request import WorkspaceServerEndpointsWorkspaceDuplicateRequest
from openapi_client.models.workspace_with_workspace_embed import WorkspaceWithWorkspaceEmbed
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
    api_instance = openapi_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    workspace_server_endpoints_workspace_duplicate_request = openapi_client.WorkspaceServerEndpointsWorkspaceDuplicateRequest() # WorkspaceServerEndpointsWorkspaceDuplicateRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Duplicate workspace with all its items and apps.
        api_response = api_instance.duplicate_workspace(workspace_id, workspace_server_endpoints_workspace_duplicate_request, token=token, act_as_admin=act_as_admin)
        print("The response of WorkspacesApi->duplicate_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->duplicate_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **workspace_server_endpoints_workspace_duplicate_request** | [**WorkspaceServerEndpointsWorkspaceDuplicateRequest**](WorkspaceServerEndpointsWorkspaceDuplicateRequest.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceWithWorkspaceEmbed**](WorkspaceWithWorkspaceEmbed.md)

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

# **list_workspaces**
> List[WorkspaceWithWorkspaceEmbed] list_workspaces(token=token, act_as_admin=act_as_admin, request_body=request_body)

Retrieve multiple workspaces by their IDs

Returns a list of workspaces.<br/> Returns null for those workspaces which are not found or not accessible.<br/> Guarantees that the size and order of the returned list matches the requested IDs.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace_with_workspace_embed import WorkspaceWithWorkspaceEmbed
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
    api_instance = openapi_client.WorkspacesApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Retrieve multiple workspaces by their IDs
        api_response = api_instance.list_workspaces(token=token, act_as_admin=act_as_admin, request_body=request_body)
        print("The response of WorkspacesApi->list_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->list_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[WorkspaceWithWorkspaceEmbed]**](WorkspaceWithWorkspaceEmbed.md)

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

# **patch_workspace**
> WorkspaceWithWorkspaceEmbed patch_workspace(workspace_id, json_patch_operation, token=token, act_as_admin=act_as_admin)

Patch an existing workspace

Returns the whole updated workspace with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.json_patch_operation import JsonPatchOperation
from openapi_client.models.workspace_with_workspace_embed import WorkspaceWithWorkspaceEmbed
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
    api_instance = openapi_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    json_patch_operation = [openapi_client.JsonPatchOperation()] # List[JsonPatchOperation] | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Patch an existing workspace
        api_response = api_instance.patch_workspace(workspace_id, json_patch_operation, token=token, act_as_admin=act_as_admin)
        print("The response of WorkspacesApi->patch_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->patch_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceWithWorkspaceEmbed**](WorkspaceWithWorkspaceEmbed.md)

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

# **retrieve_workspace**
> WorkspaceWithWorkspaceEmbed retrieve_workspace(workspace_id, token=token, act_as_admin=act_as_admin)

Retrieve a single workspace by its ID

Returns found workspace.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace_with_workspace_embed import WorkspaceWithWorkspaceEmbed
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
    api_instance = openapi_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Retrieve a single workspace by its ID
        api_response = api_instance.retrieve_workspace(workspace_id, token=token, act_as_admin=act_as_admin)
        print("The response of WorkspacesApi->retrieve_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->retrieve_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceWithWorkspaceEmbed**](WorkspaceWithWorkspaceEmbed.md)

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

# **search_workspaces**
> WorkspaceWithWorkspaceSearchEmbedPage search_workspaces(token=token, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, workspace_search_query=workspace_search_query)

Retrieve or search workspaces

Returns all workspaces or searches workspaces by query. Always returns only workspaces which are accessible by the current user.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace_search_query import WorkspaceSearchQuery
from openapi_client.models.workspace_with_workspace_search_embed_page import WorkspaceWithWorkspaceSearchEmbedPage
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
    api_instance = openapi_client.WorkspacesApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    offset = 0 # int | How many elements to skip. (optional) (default to 0)
    limit = 1000 # int | How many elements to return. (optional) (default to 1000)
    var_from = 0 # int | From which element the page should start. (optional) (default to 0)
    to = 56 # int | At which element the page should end (excluding it). (optional)
    workspace_search_query = openapi_client.WorkspaceSearchQuery() # WorkspaceSearchQuery |  (optional)

    try:
        # Retrieve or search workspaces
        api_response = api_instance.search_workspaces(token=token, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, workspace_search_query=workspace_search_query)
        print("The response of WorkspacesApi->search_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->search_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **offset** | **int**| How many elements to skip. | [optional] [default to 0]
 **limit** | **int**| How many elements to return. | [optional] [default to 1000]
 **var_from** | **int**| From which element the page should start. | [optional] [default to 0]
 **to** | **int**| At which element the page should end (excluding it). | [optional] 
 **workspace_search_query** | [**WorkspaceSearchQuery**](WorkspaceSearchQuery.md)|  | [optional] 

### Return type

[**WorkspaceWithWorkspaceSearchEmbedPage**](WorkspaceWithWorkspaceSearchEmbedPage.md)

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

# **set_workspace_statuses**
> set_workspace_statuses(workspace_id, workspace_server_endpoints_set_statuses_request, token=token, act_as_admin=act_as_admin)



Set statuses all at once for the specified workspace. New statuses in the list will be added to the database, missing statuses will be removed from the database, all other statuses will be updated. Each workspace must have at least one status in each category: 'draft', 'active', 'closed'<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"full\"<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace_server_endpoints_set_statuses_request import WorkspaceServerEndpointsSetStatusesRequest
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
    api_instance = openapi_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    workspace_server_endpoints_set_statuses_request = openapi_client.WorkspaceServerEndpointsSetStatusesRequest() # WorkspaceServerEndpointsSetStatusesRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        api_instance.set_workspace_statuses(workspace_id, workspace_server_endpoints_set_statuses_request, token=token, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling WorkspacesApi->set_workspace_statuses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **workspace_server_endpoints_set_statuses_request** | [**WorkspaceServerEndpointsSetStatusesRequest**](WorkspaceServerEndpointsSetStatusesRequest.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

void (empty response body)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace**
> WorkspaceWithWorkspaceEmbed update_workspace(workspace_id, workspace, token=token, act_as_admin=act_as_admin)

Update an existing workspace

Returns updated workspace with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace import Workspace
from openapi_client.models.workspace_with_workspace_embed import WorkspaceWithWorkspaceEmbed
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
    api_instance = openapi_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    workspace = openapi_client.Workspace() # Workspace | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update an existing workspace
        api_response = api_instance.update_workspace(workspace_id, workspace, token=token, act_as_admin=act_as_admin)
        print("The response of WorkspacesApi->update_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->update_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **workspace** | [**Workspace**](Workspace.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceWithWorkspaceEmbed**](WorkspaceWithWorkspaceEmbed.md)

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

# **update_workspace_permissions**
> Permission update_workspace_permissions(workspace_id, workspace_server_endpoints_workspace_permissions_update_request, token=token, act_as_admin=act_as_admin)

Update workspace permissions.

Returns effective permission for the current user.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.permission import Permission
from openapi_client.models.workspace_server_endpoints_workspace_permissions_update_request import WorkspaceServerEndpointsWorkspacePermissionsUpdateRequest
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
    api_instance = openapi_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    workspace_server_endpoints_workspace_permissions_update_request = openapi_client.WorkspaceServerEndpointsWorkspacePermissionsUpdateRequest() # WorkspaceServerEndpointsWorkspacePermissionsUpdateRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update workspace permissions.
        api_response = api_instance.update_workspace_permissions(workspace_id, workspace_server_endpoints_workspace_permissions_update_request, token=token, act_as_admin=act_as_admin)
        print("The response of WorkspacesApi->update_workspace_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->update_workspace_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **workspace_server_endpoints_workspace_permissions_update_request** | [**WorkspaceServerEndpointsWorkspacePermissionsUpdateRequest**](WorkspaceServerEndpointsWorkspacePermissionsUpdateRequest.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**Permission**](Permission.md)

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

# **workspace_background_activity_sse**
> str workspace_background_activity_sse(workspace_id, token=token, act_as_admin=act_as_admin)

Server-sent-events for background activity in workspace.

Creates an SSE connection which sends an event every time something changes in the background activity of this workspace.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>Returns:<br/>403 if user does not have the required permission

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
    api_instance = openapi_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Server-sent-events for background activity in workspace.
        api_response = api_instance.workspace_background_activity_sse(workspace_id, token=token, act_as_admin=act_as_admin)
        print("The response of WorkspacesApi->workspace_background_activity_sse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->workspace_background_activity_sse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

**str**

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspace_events_by_workspace_id_sse**
> str workspace_events_by_workspace_id_sse(workspace_id, token=token, act_as_admin=act_as_admin)

Server-side-events for updates in a single workspace.

Creates an SSE connection which sends a events every time when something in the workspace has happened.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>Returns:<br/>403 if user does not have the required permission

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
    api_instance = openapi_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Server-side-events for updates in a single workspace.
        api_response = api_instance.workspace_events_by_workspace_id_sse(workspace_id, token=token, act_as_admin=act_as_admin)
        print("The response of WorkspacesApi->workspace_events_by_workspace_id_sse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->workspace_events_by_workspace_id_sse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

**str**

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspace_events_sse**
> str workspace_events_sse(token=token, act_as_admin=act_as_admin)

Server-side-events for updates in all workspaces.

Creates an SSE connection which sends a events every time when something has happened in any workspace.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>Returns:<br/>403 if user does not have the required permission

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
    api_instance = openapi_client.WorkspacesApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Server-side-events for updates in all workspaces.
        api_response = api_instance.workspace_events_sse(token=token, act_as_admin=act_as_admin)
        print("The response of WorkspacesApi->workspace_events_sse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->workspace_events_sse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

**str**

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

