# openapi_client.WorkspaceRelationsApi

All URIs are relative to *https://app.airfocus.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_workspace_relations**](WorkspaceRelationsApi.md#bulk_workspace_relations) | **POST** /api/workspaces/workspace-relations/bulk | Perform multiple operations with workspace relations
[**create_workspace_relation**](WorkspaceRelationsApi.md#create_workspace_relation) | **POST** /api/workspaces/workspace-relations | Create a new workspace relation
[**delete_workspace_relation**](WorkspaceRelationsApi.md#delete_workspace_relation) | **DELETE** /api/workspaces/workspace-relations/{workspaceRelationId} | Delete an existing workspace relation
[**list_workspace_relations**](WorkspaceRelationsApi.md#list_workspace_relations) | **POST** /api/workspaces/workspace-relations/list | Retrieve multiple workspace relations by their IDs
[**patch_workspace_relation**](WorkspaceRelationsApi.md#patch_workspace_relation) | **PATCH** /api/workspaces/workspace-relations/{workspaceRelationId} | Patch an existing workspace relation
[**put_api_workspaces_workspace_relations_set**](WorkspaceRelationsApi.md#put_api_workspaces_workspace_relations_set) | **PUT** /api/workspaces/workspace-relations/set | 
[**retrieve_workspace_relation**](WorkspaceRelationsApi.md#retrieve_workspace_relation) | **GET** /api/workspaces/workspace-relations/{workspaceRelationId} | Retrieve a single workspace relation by its ID
[**search_workspace_relations**](WorkspaceRelationsApi.md#search_workspace_relations) | **POST** /api/workspaces/workspace-relations/search | Retrieve or search workspace relations
[**update_workspace_relation**](WorkspaceRelationsApi.md#update_workspace_relation) | **PUT** /api/workspaces/workspace-relations/{workspaceRelationId} | Update an existing workspace relation


# **bulk_workspace_relations**
> List[WorkspaceRelationWithEmbed] bulk_workspace_relations(token=token, act_as_admin=act_as_admin, workspace_relation_bulk_action=workspace_relation_bulk_action)

Perform multiple operations with workspace relations

Accepts a list of create/update/patch/delete operations (see the request model for more details).<br/> Each operations can target a single or multiple workspace relations.<br/> Returns a list of results for each input operation including errors.<br/> Guarantees that the size and order of the returned results matches the input list of operations.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace_relation_bulk_action import WorkspaceRelationBulkAction
from openapi_client.models.workspace_relation_with_embed import WorkspaceRelationWithEmbed
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
    api_instance = openapi_client.WorkspaceRelationsApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    workspace_relation_bulk_action = [openapi_client.WorkspaceRelationBulkAction()] # List[WorkspaceRelationBulkAction] |  (optional)

    try:
        # Perform multiple operations with workspace relations
        api_response = api_instance.bulk_workspace_relations(token=token, act_as_admin=act_as_admin, workspace_relation_bulk_action=workspace_relation_bulk_action)
        print("The response of WorkspaceRelationsApi->bulk_workspace_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceRelationsApi->bulk_workspace_relations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **workspace_relation_bulk_action** | [**List[WorkspaceRelationBulkAction]**](WorkspaceRelationBulkAction.md)|  | [optional] 

### Return type

[**List[WorkspaceRelationWithEmbed]**](WorkspaceRelationWithEmbed.md)

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

# **create_workspace_relation**
> WorkspaceRelationWithEmbed create_workspace_relation(workspace_relation, token=token, act_as_admin=act_as_admin)

Create a new workspace relation

Returns newly created workspace relation with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace_relation import WorkspaceRelation
from openapi_client.models.workspace_relation_with_embed import WorkspaceRelationWithEmbed
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
    api_instance = openapi_client.WorkspaceRelationsApi(api_client)
    workspace_relation = openapi_client.WorkspaceRelation() # WorkspaceRelation | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Create a new workspace relation
        api_response = api_instance.create_workspace_relation(workspace_relation, token=token, act_as_admin=act_as_admin)
        print("The response of WorkspaceRelationsApi->create_workspace_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceRelationsApi->create_workspace_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_relation** | [**WorkspaceRelation**](WorkspaceRelation.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceRelationWithEmbed**](WorkspaceRelationWithEmbed.md)

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

# **delete_workspace_relation**
> delete_workspace_relation(workspace_relation_id, token=token, act_as_admin=act_as_admin)

Delete an existing workspace relation

Returns empty result if the workspace relation was successfully deleted.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

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
    api_instance = openapi_client.WorkspaceRelationsApi(api_client)
    workspace_relation_id = 'workspace_relation_id_example' # str | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Delete an existing workspace relation
        api_instance.delete_workspace_relation(workspace_relation_id, token=token, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling WorkspaceRelationsApi->delete_workspace_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_relation_id** | **str**|  | 
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

# **list_workspace_relations**
> List[WorkspaceRelationWithEmbed] list_workspace_relations(token=token, act_as_admin=act_as_admin, request_body=request_body)

Retrieve multiple workspace relations by their IDs

Returns a list of workspace relations.<br/> Returns null for those workspace relations which are not found or not accessible.<br/> Guarantees that the size and order of the returned list matches the requested IDs.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace_relation_with_embed import WorkspaceRelationWithEmbed
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
    api_instance = openapi_client.WorkspaceRelationsApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Retrieve multiple workspace relations by their IDs
        api_response = api_instance.list_workspace_relations(token=token, act_as_admin=act_as_admin, request_body=request_body)
        print("The response of WorkspaceRelationsApi->list_workspace_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceRelationsApi->list_workspace_relations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[WorkspaceRelationWithEmbed]**](WorkspaceRelationWithEmbed.md)

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

# **patch_workspace_relation**
> WorkspaceRelationWithEmbed patch_workspace_relation(workspace_relation_id, json_patch_operation, token=token, act_as_admin=act_as_admin)

Patch an existing workspace relation

Returns the whole updated workspace relation with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.json_patch_operation import JsonPatchOperation
from openapi_client.models.workspace_relation_with_embed import WorkspaceRelationWithEmbed
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
    api_instance = openapi_client.WorkspaceRelationsApi(api_client)
    workspace_relation_id = 'workspace_relation_id_example' # str | 
    json_patch_operation = [openapi_client.JsonPatchOperation()] # List[JsonPatchOperation] | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Patch an existing workspace relation
        api_response = api_instance.patch_workspace_relation(workspace_relation_id, json_patch_operation, token=token, act_as_admin=act_as_admin)
        print("The response of WorkspaceRelationsApi->patch_workspace_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceRelationsApi->patch_workspace_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_relation_id** | **str**|  | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceRelationWithEmbed**](WorkspaceRelationWithEmbed.md)

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

# **put_api_workspaces_workspace_relations_set**
> WorkspaceWithWorkspaceEmbed put_api_workspaces_workspace_relations_set(workspace_relations_set_request, token=token, act_as_admin=act_as_admin)





### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace_relations_set_request import WorkspaceRelationsSetRequest
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
    api_instance = openapi_client.WorkspaceRelationsApi(api_client)
    workspace_relations_set_request = openapi_client.WorkspaceRelationsSetRequest() # WorkspaceRelationsSetRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        api_response = api_instance.put_api_workspaces_workspace_relations_set(workspace_relations_set_request, token=token, act_as_admin=act_as_admin)
        print("The response of WorkspaceRelationsApi->put_api_workspaces_workspace_relations_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceRelationsApi->put_api_workspaces_workspace_relations_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_relations_set_request** | [**WorkspaceRelationsSetRequest**](WorkspaceRelationsSetRequest.md)|  | 
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

# **retrieve_workspace_relation**
> WorkspaceRelationWithEmbed retrieve_workspace_relation(workspace_relation_id, token=token, act_as_admin=act_as_admin)

Retrieve a single workspace relation by its ID

Returns found workspace relation.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace_relation_with_embed import WorkspaceRelationWithEmbed
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
    api_instance = openapi_client.WorkspaceRelationsApi(api_client)
    workspace_relation_id = 'workspace_relation_id_example' # str | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Retrieve a single workspace relation by its ID
        api_response = api_instance.retrieve_workspace_relation(workspace_relation_id, token=token, act_as_admin=act_as_admin)
        print("The response of WorkspaceRelationsApi->retrieve_workspace_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceRelationsApi->retrieve_workspace_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_relation_id** | **str**|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceRelationWithEmbed**](WorkspaceRelationWithEmbed.md)

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

# **search_workspace_relations**
> WorkspaceRelationWithEmbedPage search_workspace_relations(token=token, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, workspace_relation_search_query=workspace_relation_search_query)

Retrieve or search workspace relations

Returns all workspace relations or searches workspace relations by query. Always returns only workspace relations which are accessible by the current user.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace_relation_search_query import WorkspaceRelationSearchQuery
from openapi_client.models.workspace_relation_with_embed_page import WorkspaceRelationWithEmbedPage
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
    api_instance = openapi_client.WorkspaceRelationsApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    offset = 0 # int | How many elements to skip. (optional) (default to 0)
    limit = 1000 # int | How many elements to return. (optional) (default to 1000)
    var_from = 0 # int | From which element the page should start. (optional) (default to 0)
    to = 56 # int | At which element the page should end (excluding it). (optional)
    workspace_relation_search_query = openapi_client.WorkspaceRelationSearchQuery() # WorkspaceRelationSearchQuery |  (optional)

    try:
        # Retrieve or search workspace relations
        api_response = api_instance.search_workspace_relations(token=token, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, workspace_relation_search_query=workspace_relation_search_query)
        print("The response of WorkspaceRelationsApi->search_workspace_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceRelationsApi->search_workspace_relations: %s\n" % e)
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
 **workspace_relation_search_query** | [**WorkspaceRelationSearchQuery**](WorkspaceRelationSearchQuery.md)|  | [optional] 

### Return type

[**WorkspaceRelationWithEmbedPage**](WorkspaceRelationWithEmbedPage.md)

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

# **update_workspace_relation**
> WorkspaceRelationWithEmbed update_workspace_relation(workspace_relation_id, workspace_relation, token=token, act_as_admin=act_as_admin)

Update an existing workspace relation

Returns updated workspace relation with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.workspace_relation import WorkspaceRelation
from openapi_client.models.workspace_relation_with_embed import WorkspaceRelationWithEmbed
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
    api_instance = openapi_client.WorkspaceRelationsApi(api_client)
    workspace_relation_id = 'workspace_relation_id_example' # str | 
    workspace_relation = openapi_client.WorkspaceRelation() # WorkspaceRelation | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update an existing workspace relation
        api_response = api_instance.update_workspace_relation(workspace_relation_id, workspace_relation, token=token, act_as_admin=act_as_admin)
        print("The response of WorkspaceRelationsApi->update_workspace_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceRelationsApi->update_workspace_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_relation_id** | **str**|  | 
 **workspace_relation** | [**WorkspaceRelation**](WorkspaceRelation.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceRelationWithEmbed**](WorkspaceRelationWithEmbed.md)

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

