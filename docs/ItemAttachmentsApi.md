# openapi_client.ItemAttachmentsApi

All URIs are relative to *https://app.airfocus.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_item_attachments**](ItemAttachmentsApi.md#bulk_item_attachments) | **POST** /api/workspaces/{workspaceId}/attachments/bulk | Perform multiple operations with attachments
[**create_item_attachment**](ItemAttachmentsApi.md#create_item_attachment) | **POST** /api/workspaces/{workspaceId}/attachments | Create a new attachment
[**delete_item_attachment**](ItemAttachmentsApi.md#delete_item_attachment) | **DELETE** /api/workspaces/{workspaceId}/attachments/{itemAttachmentId} | Delete an existing attachment
[**list_item_attachments**](ItemAttachmentsApi.md#list_item_attachments) | **POST** /api/workspaces/{workspaceId}/attachments/list | Retrieve multiple attachments by their IDs
[**patch_item_attachment**](ItemAttachmentsApi.md#patch_item_attachment) | **PATCH** /api/workspaces/{workspaceId}/attachments/{itemAttachmentId} | Patch an existing attachment
[**retrieve_item_attachment**](ItemAttachmentsApi.md#retrieve_item_attachment) | **GET** /api/workspaces/{workspaceId}/attachments/{itemAttachmentId} | Retrieve a single attachment by its ID
[**search_item_attachments**](ItemAttachmentsApi.md#search_item_attachments) | **POST** /api/workspaces/{workspaceId}/attachments/search | Retrieve or search attachments
[**update_item_attachment**](ItemAttachmentsApi.md#update_item_attachment) | **PUT** /api/workspaces/{workspaceId}/attachments/{itemAttachmentId} | Update an existing attachment


# **bulk_item_attachments**
> List[ItemAttachmentWithEmbed] bulk_item_attachments(workspace_id, token=token, act_as_admin=act_as_admin, item_attachment_bulk_action=item_attachment_bulk_action)

Perform multiple operations with attachments

Accepts a list of create/update/patch/delete operations (see the request model for more details).<br/> Each operations can target a single or multiple attachments.<br/> Returns a list of results for each input operation including errors.<br/> Guarantees that the size and order of the returned results matches the input list of operations.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.item_attachment_bulk_action import ItemAttachmentBulkAction
from openapi_client.models.item_attachment_with_embed import ItemAttachmentWithEmbed
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
    api_instance = openapi_client.ItemAttachmentsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed links.
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    item_attachment_bulk_action = [openapi_client.ItemAttachmentBulkAction()] # List[ItemAttachmentBulkAction] |  (optional)

    try:
        # Perform multiple operations with attachments
        api_response = api_instance.bulk_item_attachments(workspace_id, token=token, act_as_admin=act_as_admin, item_attachment_bulk_action=item_attachment_bulk_action)
        print("The response of ItemAttachmentsApi->bulk_item_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemAttachmentsApi->bulk_item_attachments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed links. | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **item_attachment_bulk_action** | [**List[ItemAttachmentBulkAction]**](ItemAttachmentBulkAction.md)|  | [optional] 

### Return type

[**List[ItemAttachmentWithEmbed]**](ItemAttachmentWithEmbed.md)

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

# **create_item_attachment**
> ItemAttachmentWithEmbed create_item_attachment(workspace_id, item_attachment, token=token, act_as_admin=act_as_admin)

Create a new attachment

Returns newly created attachment with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.item_attachment import ItemAttachment
from openapi_client.models.item_attachment_with_embed import ItemAttachmentWithEmbed
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
    api_instance = openapi_client.ItemAttachmentsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed links.
    item_attachment = openapi_client.ItemAttachment() # ItemAttachment | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Create a new attachment
        api_response = api_instance.create_item_attachment(workspace_id, item_attachment, token=token, act_as_admin=act_as_admin)
        print("The response of ItemAttachmentsApi->create_item_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemAttachmentsApi->create_item_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed links. | 
 **item_attachment** | [**ItemAttachment**](ItemAttachment.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemAttachmentWithEmbed**](ItemAttachmentWithEmbed.md)

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

# **delete_item_attachment**
> delete_item_attachment(workspace_id, item_attachment_id, token=token, act_as_admin=act_as_admin)

Delete an existing attachment

Returns empty result if the attachment was successfully deleted.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

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
    api_instance = openapi_client.ItemAttachmentsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed links.
    item_attachment_id = 'item_attachment_id_example' # str | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Delete an existing attachment
        api_instance.delete_item_attachment(workspace_id, item_attachment_id, token=token, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling ItemAttachmentsApi->delete_item_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed links. | 
 **item_attachment_id** | **str**|  | 
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

# **list_item_attachments**
> List[ItemAttachmentWithEmbed] list_item_attachments(workspace_id, token=token, act_as_admin=act_as_admin, request_body=request_body)

Retrieve multiple attachments by their IDs

Returns a list of attachments.<br/> Returns null for those attachments which are not found or not accessible.<br/> Guarantees that the size and order of the returned list matches the requested IDs.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.item_attachment_with_embed import ItemAttachmentWithEmbed
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
    api_instance = openapi_client.ItemAttachmentsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed links.
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Retrieve multiple attachments by their IDs
        api_response = api_instance.list_item_attachments(workspace_id, token=token, act_as_admin=act_as_admin, request_body=request_body)
        print("The response of ItemAttachmentsApi->list_item_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemAttachmentsApi->list_item_attachments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed links. | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ItemAttachmentWithEmbed]**](ItemAttachmentWithEmbed.md)

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

# **patch_item_attachment**
> ItemAttachmentWithEmbed patch_item_attachment(workspace_id, item_attachment_id, json_patch_operation, token=token, act_as_admin=act_as_admin)

Patch an existing attachment

Returns the whole updated attachment with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.item_attachment_with_embed import ItemAttachmentWithEmbed
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
    api_instance = openapi_client.ItemAttachmentsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed links.
    item_attachment_id = 'item_attachment_id_example' # str | 
    json_patch_operation = [openapi_client.JsonPatchOperation()] # List[JsonPatchOperation] | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Patch an existing attachment
        api_response = api_instance.patch_item_attachment(workspace_id, item_attachment_id, json_patch_operation, token=token, act_as_admin=act_as_admin)
        print("The response of ItemAttachmentsApi->patch_item_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemAttachmentsApi->patch_item_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed links. | 
 **item_attachment_id** | **str**|  | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemAttachmentWithEmbed**](ItemAttachmentWithEmbed.md)

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

# **retrieve_item_attachment**
> ItemAttachmentWithEmbed retrieve_item_attachment(workspace_id, item_attachment_id, token=token, act_as_admin=act_as_admin)

Retrieve a single attachment by its ID

Returns found attachment.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.item_attachment_with_embed import ItemAttachmentWithEmbed
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
    api_instance = openapi_client.ItemAttachmentsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed links.
    item_attachment_id = 'item_attachment_id_example' # str | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Retrieve a single attachment by its ID
        api_response = api_instance.retrieve_item_attachment(workspace_id, item_attachment_id, token=token, act_as_admin=act_as_admin)
        print("The response of ItemAttachmentsApi->retrieve_item_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemAttachmentsApi->retrieve_item_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed links. | 
 **item_attachment_id** | **str**|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemAttachmentWithEmbed**](ItemAttachmentWithEmbed.md)

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

# **search_item_attachments**
> ItemAttachmentWithEmbedPage search_item_attachments(workspace_id, token=token, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, attachment_search_query=attachment_search_query)

Retrieve or search attachments

Returns all attachments or searches attachments by query. Always returns only attachments which are accessible by the current user.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.attachment_search_query import AttachmentSearchQuery
from openapi_client.models.item_attachment_with_embed_page import ItemAttachmentWithEmbedPage
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
    api_instance = openapi_client.ItemAttachmentsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed links.
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    offset = 0 # int | How many elements to skip. (optional) (default to 0)
    limit = 1000 # int | How many elements to return. (optional) (default to 1000)
    var_from = 0 # int | From which element the page should start. (optional) (default to 0)
    to = 56 # int | At which element the page should end (excluding it). (optional)
    attachment_search_query = openapi_client.AttachmentSearchQuery() # AttachmentSearchQuery |  (optional)

    try:
        # Retrieve or search attachments
        api_response = api_instance.search_item_attachments(workspace_id, token=token, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, attachment_search_query=attachment_search_query)
        print("The response of ItemAttachmentsApi->search_item_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemAttachmentsApi->search_item_attachments: %s\n" % e)
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
 **attachment_search_query** | [**AttachmentSearchQuery**](AttachmentSearchQuery.md)|  | [optional] 

### Return type

[**ItemAttachmentWithEmbedPage**](ItemAttachmentWithEmbedPage.md)

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

# **update_item_attachment**
> ItemAttachmentWithEmbed update_item_attachment(workspace_id, item_attachment_id, item_attachment, token=token, act_as_admin=act_as_admin)

Update an existing attachment

Returns updated attachment with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.item_attachment import ItemAttachment
from openapi_client.models.item_attachment_with_embed import ItemAttachmentWithEmbed
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
    api_instance = openapi_client.ItemAttachmentsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed links.
    item_attachment_id = 'item_attachment_id_example' # str | 
    item_attachment = openapi_client.ItemAttachment() # ItemAttachment | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update an existing attachment
        api_response = api_instance.update_item_attachment(workspace_id, item_attachment_id, item_attachment, token=token, act_as_admin=act_as_admin)
        print("The response of ItemAttachmentsApi->update_item_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemAttachmentsApi->update_item_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed links. | 
 **item_attachment_id** | **str**|  | 
 **item_attachment** | [**ItemAttachment**](ItemAttachment.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemAttachmentWithEmbed**](ItemAttachmentWithEmbed.md)

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

