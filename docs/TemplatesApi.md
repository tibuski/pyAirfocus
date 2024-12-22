# openapi_client.TemplatesApi

All URIs are relative to *https://app.airfocus.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**install_template**](TemplatesApi.md#install_template) | **POST** /api/templates/{templateId} | Install template
[**install_template_legacy**](TemplatesApi.md#install_template_legacy) | **POST** /api/workspaces/templates/{templateId} | Install template
[**list_templates**](TemplatesApi.md#list_templates) | **GET** /api/templates | List templates
[**list_templates_legacy**](TemplatesApi.md#list_templates_legacy) | **GET** /api/workspaces/templates | List templates


# **install_template**
> WorkspaceWithWorkspaceEmbed install_template(template_id, apply_template_request, token=token, act_as_admin=act_as_admin)

Install template

Installs the requested template with the given parameters. Returns a newly created workspace. If the template creates multiple workspaces - then it still returns a single workspace which is considered by the template as \"main\".<br/>Requirements:<br/>- auth-client scopes: \"workspace\"

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.apply_template_request import ApplyTemplateRequest
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
    api_instance = openapi_client.TemplatesApi(api_client)
    template_id = 'template_id_example' # str | 
    apply_template_request = openapi_client.ApplyTemplateRequest() # ApplyTemplateRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Install template
        api_response = api_instance.install_template(template_id, apply_template_request, token=token, act_as_admin=act_as_admin)
        print("The response of TemplatesApi->install_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->install_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **apply_template_request** | [**ApplyTemplateRequest**](ApplyTemplateRequest.md)|  | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_template_legacy**
> WorkspaceWithWorkspaceEmbed install_template_legacy(template_id, apply_template_request, token=token, act_as_admin=act_as_admin)

Install template

Installs the requested template with the given parameters. Returns a newly created workspace. If the template creates multiple workspaces - then it still returns a single workspace which is considered by the template as \"main\".<br/>Requirements:<br/>- auth-client scopes: \"workspace\"

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.apply_template_request import ApplyTemplateRequest
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
    api_instance = openapi_client.TemplatesApi(api_client)
    template_id = 'template_id_example' # str | 
    apply_template_request = openapi_client.ApplyTemplateRequest() # ApplyTemplateRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Install template
        api_response = api_instance.install_template_legacy(template_id, apply_template_request, token=token, act_as_admin=act_as_admin)
        print("The response of TemplatesApi->install_template_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->install_template_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **apply_template_request** | [**ApplyTemplateRequest**](ApplyTemplateRequest.md)|  | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_templates**
> TemplatePageWithEmbed list_templates(token=token, act_as_admin=act_as_admin, offset=offset, limit=limit)

List templates

Returns all workspace-templates available to the current team.<br/>Requirements:<br/>- auth-client scopes: \"workspace:read\"

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.template_page_with_embed import TemplatePageWithEmbed
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
    api_instance = openapi_client.TemplatesApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    offset = 0 # int | How many elements to skip. (optional) (default to 0)
    limit = 100 # int | How many elements to return. (optional) (default to 100)

    try:
        # List templates
        api_response = api_instance.list_templates(token=token, act_as_admin=act_as_admin, offset=offset, limit=limit)
        print("The response of TemplatesApi->list_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->list_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **offset** | **int**| How many elements to skip. | [optional] [default to 0]
 **limit** | **int**| How many elements to return. | [optional] [default to 100]

### Return type

[**TemplatePageWithEmbed**](TemplatePageWithEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_templates_legacy**
> TemplatePageWithEmbed list_templates_legacy(token=token, act_as_admin=act_as_admin, offset=offset, limit=limit)

List templates

Returns all workspace-templates available to the current team.<br/>Requirements:<br/>- auth-client scopes: \"workspace:read\"

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.template_page_with_embed import TemplatePageWithEmbed
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
    api_instance = openapi_client.TemplatesApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    offset = 0 # int | How many elements to skip. (optional) (default to 0)
    limit = 100 # int | How many elements to return. (optional) (default to 100)

    try:
        # List templates
        api_response = api_instance.list_templates_legacy(token=token, act_as_admin=act_as_admin, offset=offset, limit=limit)
        print("The response of TemplatesApi->list_templates_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->list_templates_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **offset** | **int**| How many elements to skip. | [optional] [default to 0]
 **limit** | **int**| How many elements to return. | [optional] [default to 100]

### Return type

[**TemplatePageWithEmbed**](TemplatePageWithEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

