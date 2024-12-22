# openapi_client.CommentsApi

All URIs are relative to *https://app.airfocus.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_comment_reaction**](CommentsApi.md#add_comment_reaction) | **POST** /api/workspaces/{workspaceId}/comments/{commentId}/reactions/{emojiCode} | Add a reaction to the specified comment.
[**bulk_comments**](CommentsApi.md#bulk_comments) | **POST** /api/workspaces/{workspaceId}/comments/bulk | Perform multiple operations with comments
[**create_comment**](CommentsApi.md#create_comment) | **POST** /api/workspaces/{workspaceId}/comments | Create a new comment
[**delete_comment**](CommentsApi.md#delete_comment) | **DELETE** /api/workspaces/{workspaceId}/comments/{commentId} | Delete an existing comment
[**list_comments**](CommentsApi.md#list_comments) | **POST** /api/workspaces/{workspaceId}/comments/list | Retrieve multiple comments by their IDs
[**patch_comment**](CommentsApi.md#patch_comment) | **PATCH** /api/workspaces/{workspaceId}/comments/{commentId} | Patch an existing comment
[**remove_comment_reaction**](CommentsApi.md#remove_comment_reaction) | **DELETE** /api/workspaces/{workspaceId}/comments/{commentId}/reactions/{emojiCode} | Remove a reaction from the specified comment.
[**retrieve_comment**](CommentsApi.md#retrieve_comment) | **GET** /api/workspaces/{workspaceId}/comments/{commentId} | Retrieve a single comment by its ID
[**search_comments**](CommentsApi.md#search_comments) | **POST** /api/workspaces/{workspaceId}/comments/search | Retrieve or search comments
[**update_comment**](CommentsApi.md#update_comment) | **PUT** /api/workspaces/{workspaceId}/comments/{commentId} | Update an existing comment


# **add_comment_reaction**
> add_comment_reaction(workspace_id, comment_id, emoji_code, token=token, act_as_admin=act_as_admin)

Add a reaction to the specified comment.

This action can be performed only as a real authenticated user<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.comment_reaction_emoji import CommentReactionEmoji
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
    api_instance = openapi_client.CommentsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    emoji_code = openapi_client.CommentReactionEmoji() # CommentReactionEmoji | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Add a reaction to the specified comment.
        api_instance.add_comment_reaction(workspace_id, comment_id, emoji_code, token=token, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling CommentsApi->add_comment_reaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **emoji_code** | [**CommentReactionEmoji**](.md)|  | 
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

# **bulk_comments**
> List[CommentWithCommentEmbed] bulk_comments(workspace_id, token=token, act_as_admin=act_as_admin, comment_bulk_action=comment_bulk_action)

Perform multiple operations with comments

Accepts a list of create/update/patch/delete operations (see the request model for more details).<br/> Each operations can target a single or multiple comments.<br/> Returns a list of results for each input operation including errors.<br/> Guarantees that the size and order of the returned results matches the input list of operations.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.comment_bulk_action import CommentBulkAction
from openapi_client.models.comment_with_comment_embed import CommentWithCommentEmbed
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
    api_instance = openapi_client.CommentsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    comment_bulk_action = [openapi_client.CommentBulkAction()] # List[CommentBulkAction] |  (optional)

    try:
        # Perform multiple operations with comments
        api_response = api_instance.bulk_comments(workspace_id, token=token, act_as_admin=act_as_admin, comment_bulk_action=comment_bulk_action)
        print("The response of CommentsApi->bulk_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->bulk_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **comment_bulk_action** | [**List[CommentBulkAction]**](CommentBulkAction.md)|  | [optional] 

### Return type

[**List[CommentWithCommentEmbed]**](CommentWithCommentEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/json+markdown
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_comment**
> CommentWithCommentEmbed create_comment(workspace_id, comment, token=token, act_as_admin=act_as_admin)

Create a new comment

Returns newly created comment with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.comment import Comment
from openapi_client.models.comment_with_comment_embed import CommentWithCommentEmbed
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
    api_instance = openapi_client.CommentsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    comment = openapi_client.Comment() # Comment | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Create a new comment
        api_response = api_instance.create_comment(workspace_id, comment, token=token, act_as_admin=act_as_admin)
        print("The response of CommentsApi->create_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->create_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **comment** | [**Comment**](Comment.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**CommentWithCommentEmbed**](CommentWithCommentEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/json+markdown
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment**
> delete_comment(workspace_id, comment_id, token=token, act_as_admin=act_as_admin)

Delete an existing comment

Returns empty result if the comment was successfully deleted.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

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
    api_instance = openapi_client.CommentsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Delete an existing comment
        api_instance.delete_comment(workspace_id, comment_id, token=token, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling CommentsApi->delete_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **comment_id** | **str**|  | 
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

# **list_comments**
> List[CommentWithCommentEmbed] list_comments(workspace_id, token=token, act_as_admin=act_as_admin, request_body=request_body)

Retrieve multiple comments by their IDs

Returns a list of comments.<br/> Returns null for those comments which are not found or not accessible.<br/> Guarantees that the size and order of the returned list matches the requested IDs.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.comment_with_comment_embed import CommentWithCommentEmbed
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
    api_instance = openapi_client.CommentsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Retrieve multiple comments by their IDs
        api_response = api_instance.list_comments(workspace_id, token=token, act_as_admin=act_as_admin, request_body=request_body)
        print("The response of CommentsApi->list_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->list_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[CommentWithCommentEmbed]**](CommentWithCommentEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_comment**
> CommentWithCommentEmbed patch_comment(workspace_id, comment_id, json_patch_operation, token=token, act_as_admin=act_as_admin)

Patch an existing comment

Returns the whole updated comment with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.comment_with_comment_embed import CommentWithCommentEmbed
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
    api_instance = openapi_client.CommentsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    json_patch_operation = [openapi_client.JsonPatchOperation()] # List[JsonPatchOperation] | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Patch an existing comment
        api_response = api_instance.patch_comment(workspace_id, comment_id, json_patch_operation, token=token, act_as_admin=act_as_admin)
        print("The response of CommentsApi->patch_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->patch_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**CommentWithCommentEmbed**](CommentWithCommentEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_comment_reaction**
> remove_comment_reaction(workspace_id, comment_id, emoji_code, token=token, act_as_admin=act_as_admin)

Remove a reaction from the specified comment.

This action can be performed only as a real authenticated user<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.comment_reaction_emoji import CommentReactionEmoji
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
    api_instance = openapi_client.CommentsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    emoji_code = openapi_client.CommentReactionEmoji() # CommentReactionEmoji | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Remove a reaction from the specified comment.
        api_instance.remove_comment_reaction(workspace_id, comment_id, emoji_code, token=token, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling CommentsApi->remove_comment_reaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **emoji_code** | [**CommentReactionEmoji**](.md)|  | 
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

# **retrieve_comment**
> CommentWithCommentEmbed retrieve_comment(workspace_id, comment_id, token=token, act_as_admin=act_as_admin)

Retrieve a single comment by its ID

Returns found comment.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.comment_with_comment_embed import CommentWithCommentEmbed
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
    api_instance = openapi_client.CommentsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Retrieve a single comment by its ID
        api_response = api_instance.retrieve_comment(workspace_id, comment_id, token=token, act_as_admin=act_as_admin)
        print("The response of CommentsApi->retrieve_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->retrieve_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**CommentWithCommentEmbed**](CommentWithCommentEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_comments**
> CommentWithCommentEmbedPage search_comments(workspace_id, token=token, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, comment_search_query=comment_search_query)

Retrieve or search comments

Returns all comments or searches comments by query. Always returns only comments which are accessible by the current user.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.comment_search_query import CommentSearchQuery
from openapi_client.models.comment_with_comment_embed_page import CommentWithCommentEmbedPage
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
    api_instance = openapi_client.CommentsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    offset = 0 # int | How many elements to skip. (optional) (default to 0)
    limit = 1000 # int | How many elements to return. (optional) (default to 1000)
    var_from = 0 # int | From which element the page should start. (optional) (default to 0)
    to = 56 # int | At which element the page should end (excluding it). (optional)
    comment_search_query = openapi_client.CommentSearchQuery() # CommentSearchQuery |  (optional)

    try:
        # Retrieve or search comments
        api_response = api_instance.search_comments(workspace_id, token=token, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, comment_search_query=comment_search_query)
        print("The response of CommentsApi->search_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->search_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **offset** | **int**| How many elements to skip. | [optional] [default to 0]
 **limit** | **int**| How many elements to return. | [optional] [default to 1000]
 **var_from** | **int**| From which element the page should start. | [optional] [default to 0]
 **to** | **int**| At which element the page should end (excluding it). | [optional] 
 **comment_search_query** | [**CommentSearchQuery**](CommentSearchQuery.md)|  | [optional] 

### Return type

[**CommentWithCommentEmbedPage**](CommentWithCommentEmbedPage.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comment**
> CommentWithCommentEmbed update_comment(workspace_id, comment_id, comment, token=token, act_as_admin=act_as_admin)

Update an existing comment

Returns updated comment with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"write\" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.comment import Comment
from openapi_client.models.comment_with_comment_embed import CommentWithCommentEmbed
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
    api_instance = openapi_client.CommentsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    comment = openapi_client.Comment() # Comment | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update an existing comment
        api_response = api_instance.update_comment(workspace_id, comment_id, comment, token=token, act_as_admin=act_as_admin)
        print("The response of CommentsApi->update_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->update_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **comment** | [**Comment**](Comment.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**CommentWithCommentEmbed**](CommentWithCommentEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/json+markdown
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

