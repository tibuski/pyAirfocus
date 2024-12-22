# openapi_client.WorkspaceGroupsApi

All URIs are relative to *https://app.airfocus.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_workspace_to_group**](WorkspaceGroupsApi.md#assign_workspace_to_group) | **POST** /api/workspaces/groups/assign | Update workspace-group permissions.
[**bulk_workspace_groups**](WorkspaceGroupsApi.md#bulk_workspace_groups) | **POST** /api/workspaces/groups/bulk | Perform multiple operations with workspace groups
[**create_workspace_group**](WorkspaceGroupsApi.md#create_workspace_group) | **POST** /api/workspaces/groups | Create a new workspace group
[**delete_workspace_group**](WorkspaceGroupsApi.md#delete_workspace_group) | **DELETE** /api/workspaces/groups/{workspaceGroupId} | Delete an existing workspace group
[**list_workspace_groups**](WorkspaceGroupsApi.md#list_workspace_groups) | **POST** /api/workspaces/groups/list | Retrieve multiple workspace groups by their IDs
[**patch_workspace_group**](WorkspaceGroupsApi.md#patch_workspace_group) | **PATCH** /api/workspaces/groups/{workspaceGroupId} | Patch an existing workspace group
[**retrieve_workspace_group**](WorkspaceGroupsApi.md#retrieve_workspace_group) | **GET** /api/workspaces/groups/{workspaceGroupId} | Retrieve a single workspace group by its ID
[**search_workspace_groups**](WorkspaceGroupsApi.md#search_workspace_groups) | **POST** /api/workspaces/groups/search | Retrieve or search workspace groups
[**update_workspace_group**](WorkspaceGroupsApi.md#update_workspace_group) | **PUT** /api/workspaces/groups/{workspaceGroupId} | Update an existing workspace group
[**update_workspace_group_permissions**](WorkspaceGroupsApi.md#update_workspace_group_permissions) | **POST** /api/workspaces/groups/{workspaceGroupId}/permissions | Update workspace-group permissions.


# **assign_workspace_to_group**
> assign_workspace_to_group(workspace_group_assign_workspace_request, token=token, act_as_admin=act_as_admin)

Update workspace-group permissions.

<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace_group_assign_workspace_request import WorkspaceGroupAssignWorkspaceRequest
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
    api_instance = openapi_client.WorkspaceGroupsApi(api_client)
    workspace_group_assign_workspace_request = openapi_client.WorkspaceGroupAssignWorkspaceRequest() # WorkspaceGroupAssignWorkspaceRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update workspace-group permissions.
        api_instance.assign_workspace_to_group(workspace_group_assign_workspace_request, token=token, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling WorkspaceGroupsApi->assign_workspace_to_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_group_assign_workspace_request** | [**WorkspaceGroupAssignWorkspaceRequest**](WorkspaceGroupAssignWorkspaceRequest.md)|  | 
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

# **bulk_workspace_groups**
> List[WorkspaceGroupWithWorkspaceGroupEmbed] bulk_workspace_groups(token=token, act_as_admin=act_as_admin, workspace_group_bulk_action=workspace_group_bulk_action)

Perform multiple operations with workspace groups

Accepts a list of create/update/patch/delete operations (see the request model for more details).<br/> Each operations can target a single or multiple workspace groups.<br/> Returns a list of results for each input operation including errors.<br/> Guarantees that the size and order of the returned results matches the input list of operations.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace_group_bulk_action import WorkspaceGroupBulkAction
from openapi_client.models.workspace_group_with_workspace_group_embed import WorkspaceGroupWithWorkspaceGroupEmbed
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
    api_instance = openapi_client.WorkspaceGroupsApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    workspace_group_bulk_action = [openapi_client.WorkspaceGroupBulkAction()] # List[WorkspaceGroupBulkAction] |  (optional)

    try:
        # Perform multiple operations with workspace groups
        api_response = api_instance.bulk_workspace_groups(token=token, act_as_admin=act_as_admin, workspace_group_bulk_action=workspace_group_bulk_action)
        print("The response of WorkspaceGroupsApi->bulk_workspace_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceGroupsApi->bulk_workspace_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **workspace_group_bulk_action** | [**List[WorkspaceGroupBulkAction]**](WorkspaceGroupBulkAction.md)|  | [optional] 

### Return type

[**List[WorkspaceGroupWithWorkspaceGroupEmbed]**](WorkspaceGroupWithWorkspaceGroupEmbed.md)

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

# **create_workspace_group**
> WorkspaceGroupWithWorkspaceGroupEmbed create_workspace_group(workspace_group, token=token, act_as_admin=act_as_admin)

Create a new workspace group

Returns newly created workspace group with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace_group import WorkspaceGroup
from openapi_client.models.workspace_group_with_workspace_group_embed import WorkspaceGroupWithWorkspaceGroupEmbed
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
    api_instance = openapi_client.WorkspaceGroupsApi(api_client)
    workspace_group = openapi_client.WorkspaceGroup() # WorkspaceGroup | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Create a new workspace group
        api_response = api_instance.create_workspace_group(workspace_group, token=token, act_as_admin=act_as_admin)
        print("The response of WorkspaceGroupsApi->create_workspace_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceGroupsApi->create_workspace_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_group** | [**WorkspaceGroup**](WorkspaceGroup.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceGroupWithWorkspaceGroupEmbed**](WorkspaceGroupWithWorkspaceGroupEmbed.md)

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

# **delete_workspace_group**
> delete_workspace_group(workspace_group_id, token=token, act_as_admin=act_as_admin)

Delete an existing workspace group

Returns empty result if the workspace group was successfully deleted.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

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
    api_instance = openapi_client.WorkspaceGroupsApi(api_client)
    workspace_group_id = 'workspace_group_id_example' # str | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Delete an existing workspace group
        api_instance.delete_workspace_group(workspace_group_id, token=token, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling WorkspaceGroupsApi->delete_workspace_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_group_id** | **str**|  | 
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

# **list_workspace_groups**
> List[WorkspaceGroupWithWorkspaceGroupEmbed] list_workspace_groups(token=token, act_as_admin=act_as_admin, request_body=request_body)

Retrieve multiple workspace groups by their IDs

Returns a list of workspace groups.<br/> Returns null for those workspace groups which are not found or not accessible.<br/> Guarantees that the size and order of the returned list matches the requested IDs.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace_group_with_workspace_group_embed import WorkspaceGroupWithWorkspaceGroupEmbed
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
    api_instance = openapi_client.WorkspaceGroupsApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Retrieve multiple workspace groups by their IDs
        api_response = api_instance.list_workspace_groups(token=token, act_as_admin=act_as_admin, request_body=request_body)
        print("The response of WorkspaceGroupsApi->list_workspace_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceGroupsApi->list_workspace_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[WorkspaceGroupWithWorkspaceGroupEmbed]**](WorkspaceGroupWithWorkspaceGroupEmbed.md)

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

# **patch_workspace_group**
> WorkspaceGroupWithWorkspaceGroupEmbed patch_workspace_group(workspace_group_id, json_patch_operation, token=token, act_as_admin=act_as_admin)

Patch an existing workspace group

Returns the whole updated workspace group with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.json_patch_operation import JsonPatchOperation
from openapi_client.models.workspace_group_with_workspace_group_embed import WorkspaceGroupWithWorkspaceGroupEmbed
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
    api_instance = openapi_client.WorkspaceGroupsApi(api_client)
    workspace_group_id = 'workspace_group_id_example' # str | 
    json_patch_operation = [openapi_client.JsonPatchOperation()] # List[JsonPatchOperation] | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Patch an existing workspace group
        api_response = api_instance.patch_workspace_group(workspace_group_id, json_patch_operation, token=token, act_as_admin=act_as_admin)
        print("The response of WorkspaceGroupsApi->patch_workspace_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceGroupsApi->patch_workspace_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_group_id** | **str**|  | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceGroupWithWorkspaceGroupEmbed**](WorkspaceGroupWithWorkspaceGroupEmbed.md)

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

# **retrieve_workspace_group**
> WorkspaceGroupWithWorkspaceGroupEmbed retrieve_workspace_group(workspace_group_id, token=token, act_as_admin=act_as_admin)

Retrieve a single workspace group by its ID

Returns found workspace group.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace_group_with_workspace_group_embed import WorkspaceGroupWithWorkspaceGroupEmbed
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
    api_instance = openapi_client.WorkspaceGroupsApi(api_client)
    workspace_group_id = 'workspace_group_id_example' # str | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Retrieve a single workspace group by its ID
        api_response = api_instance.retrieve_workspace_group(workspace_group_id, token=token, act_as_admin=act_as_admin)
        print("The response of WorkspaceGroupsApi->retrieve_workspace_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceGroupsApi->retrieve_workspace_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_group_id** | **str**|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceGroupWithWorkspaceGroupEmbed**](WorkspaceGroupWithWorkspaceGroupEmbed.md)

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

# **search_workspace_groups**
> WorkspaceGroupWithWorkspaceGroupEmbedPage search_workspace_groups(token=token, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, body=body)

Retrieve or search workspace groups

Returns all workspace groups or searches workspace groups by query. Always returns only workspace groups which are accessible by the current user.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace_group_with_workspace_group_embed_page import WorkspaceGroupWithWorkspaceGroupEmbedPage
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
    api_instance = openapi_client.WorkspaceGroupsApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    offset = 0 # int | How many elements to skip. (optional) (default to 0)
    limit = 1000 # int | How many elements to return. (optional) (default to 1000)
    var_from = 0 # int | From which element the page should start. (optional) (default to 0)
    to = 56 # int | At which element the page should end (excluding it). (optional)
    body = None # object |  (optional)

    try:
        # Retrieve or search workspace groups
        api_response = api_instance.search_workspace_groups(token=token, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, body=body)
        print("The response of WorkspaceGroupsApi->search_workspace_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceGroupsApi->search_workspace_groups: %s\n" % e)
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
 **body** | **object**|  | [optional] 

### Return type

[**WorkspaceGroupWithWorkspaceGroupEmbedPage**](WorkspaceGroupWithWorkspaceGroupEmbedPage.md)

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

# **update_workspace_group**
> WorkspaceGroupWithWorkspaceGroupEmbed update_workspace_group(workspace_group_id, workspace_group, token=token, act_as_admin=act_as_admin)

Update an existing workspace group

Returns updated workspace group with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace_group import WorkspaceGroup
from openapi_client.models.workspace_group_with_workspace_group_embed import WorkspaceGroupWithWorkspaceGroupEmbed
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
    api_instance = openapi_client.WorkspaceGroupsApi(api_client)
    workspace_group_id = 'workspace_group_id_example' # str | 
    workspace_group = openapi_client.WorkspaceGroup() # WorkspaceGroup | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update an existing workspace group
        api_response = api_instance.update_workspace_group(workspace_group_id, workspace_group, token=token, act_as_admin=act_as_admin)
        print("The response of WorkspaceGroupsApi->update_workspace_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceGroupsApi->update_workspace_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_group_id** | **str**|  | 
 **workspace_group** | [**WorkspaceGroup**](WorkspaceGroup.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceGroupWithWorkspaceGroupEmbed**](WorkspaceGroupWithWorkspaceGroupEmbed.md)

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

# **update_workspace_group_permissions**
> update_workspace_group_permissions(workspace_group_id, workspace_group_permissions_update_request, token=token, act_as_admin=act_as_admin)

Update workspace-group permissions.

<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace_group_permissions_update_request import WorkspaceGroupPermissionsUpdateRequest
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
    api_instance = openapi_client.WorkspaceGroupsApi(api_client)
    workspace_group_id = 'workspace_group_id_example' # str | 
    workspace_group_permissions_update_request = openapi_client.WorkspaceGroupPermissionsUpdateRequest() # WorkspaceGroupPermissionsUpdateRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update workspace-group permissions.
        api_instance.update_workspace_group_permissions(workspace_group_id, workspace_group_permissions_update_request, token=token, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling WorkspaceGroupsApi->update_workspace_group_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_group_id** | **str**|  | 
 **workspace_group_permissions_update_request** | [**WorkspaceGroupPermissionsUpdateRequest**](WorkspaceGroupPermissionsUpdateRequest.md)|  | 
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

