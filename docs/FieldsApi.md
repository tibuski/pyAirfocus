# openapi_client.FieldsApi

All URIs are relative to *https://app.airfocus.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_field**](FieldsApi.md#delete_field) | **DELETE** /api/fields/{fieldId} | Delete field
[**get_all_team_fields_legacy**](FieldsApi.md#get_all_team_fields_legacy) | **GET** /api/workspaces/fields/team-fields | List team-fields
[**install_field**](FieldsApi.md#install_field) | **POST** /api/fields | Install a new field
[**install_field_legacy**](FieldsApi.md#install_field_legacy) | **POST** /api/workspaces/fields/install-field | Install a new field
[**install_field_legacy_with_workspace_id**](FieldsApi.md#install_field_legacy_with_workspace_id) | **POST** /api/workspaces/{workspaceId}/install-field | Install a new field
[**link_team_fields_to_workspaces**](FieldsApi.md#link_team_fields_to_workspaces) | **POST** /api/fields/workspaces | Link team-fields to workspaces
[**link_team_fields_to_workspaces_legacy**](FieldsApi.md#link_team_fields_to_workspaces_legacy) | **POST** /api/workspaces/fields/add-team-field | Add team-field to workspace
[**list_field_types**](FieldsApi.md#list_field_types) | **GET** /api/fields/types | List all available field types
[**list_field_types_legacy**](FieldsApi.md#list_field_types_legacy) | **GET** /api/workspaces/extensions/fields | List all available field types
[**reconfigure_field**](FieldsApi.md#reconfigure_field) | **PUT** /api/fields/{fieldId} | Reconfigure field
[**reconfigure_field_legacy**](FieldsApi.md#reconfigure_field_legacy) | **POST** /api/workspaces/fields/reconfigure-field | Reconfigure field
[**reconfigure_field_legacy_with_workspace_id**](FieldsApi.md#reconfigure_field_legacy_with_workspace_id) | **POST** /api/workspaces/{workspaceId}/reconfigure-field | Reconfigure field
[**reorder_fields**](FieldsApi.md#reorder_fields) | **POST** /api/fields/reorder | Reorder fields
[**reorder_fields_legacy**](FieldsApi.md#reorder_fields_legacy) | **POST** /api/workspaces/{workspaceId}/reorder-fields | Reorder fields
[**retrieve_field**](FieldsApi.md#retrieve_field) | **GET** /api/fields/{fieldId} | Retrieve a single field
[**search_fields**](FieldsApi.md#search_fields) | **POST** /api/fields/search | Search fields
[**uninstall_field_completely_legacy**](FieldsApi.md#uninstall_field_completely_legacy) | **POST** /api/workspaces/uninstall-field | Completely delete field
[**uninstall_field_legacy**](FieldsApi.md#uninstall_field_legacy) | **POST** /api/workspaces/{workspaceId}/uninstall-field | Delete field
[**unlink_team_fields_from_workspaces**](FieldsApi.md#unlink_team_fields_from_workspaces) | **DELETE** /api/fields/workspaces | Unlink team-fields from workspaces


# **delete_field**
> delete_field(field_id, token=token, act_as_admin=act_as_admin)

Delete field

Deletes the requested field together with all its connections to workspaces and its values in the corresponding workspaces<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"full\"<br/>  - team features: \"team-fields\" when operating with team-fields<br/>  - user role: \"admin\" when operating with team-fields<br/>Returns:<br/>403 if user does not have the required permission

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
    api_instance = openapi_client.FieldsApi(api_client)
    field_id = 'field_id_example' # str | ID of the target field.
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Delete field
        api_instance.delete_field(field_id, token=token, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling FieldsApi->delete_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_id** | **str**| ID of the target field. | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

void (empty response body)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_team_fields_legacy**
> FieldWithFieldEmbedPage get_all_team_fields_legacy(token=token, act_as_admin=act_as_admin)

List team-fields

Returns all team-fields installed for the current team.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>  - team features: \"team-fields\" when operating with team-fields<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.field_with_field_embed_page import FieldWithFieldEmbedPage
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
    api_instance = openapi_client.FieldsApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # List team-fields
        api_response = api_instance.get_all_team_fields_legacy(token=token, act_as_admin=act_as_admin)
        print("The response of FieldsApi->get_all_team_fields_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldsApi->get_all_team_fields_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**FieldWithFieldEmbedPage**](FieldWithFieldEmbedPage.md)

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

# **install_field**
> FieldWithFieldEmbed install_field(field_server_endpoints_install_field_request, token=token, act_as_admin=act_as_admin)

Install a new field

Installs a new field. If it's a team-field, then it's possible to install it with empty or any non-empty amount of linked workspaces. Otherwise, if it's not a team-field, then exactly one linked workspace should be specified.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"full\"<br/>  - team features: \"team-fields\" when operating with team-fields<br/>  - user role: \"admin\" when operating with team-fields<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.field_server_endpoints_install_field_request import FieldServerEndpointsInstallFieldRequest
from openapi_client.models.field_with_field_embed import FieldWithFieldEmbed
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
    api_instance = openapi_client.FieldsApi(api_client)
    field_server_endpoints_install_field_request = openapi_client.FieldServerEndpointsInstallFieldRequest() # FieldServerEndpointsInstallFieldRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Install a new field
        api_response = api_instance.install_field(field_server_endpoints_install_field_request, token=token, act_as_admin=act_as_admin)
        print("The response of FieldsApi->install_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldsApi->install_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_server_endpoints_install_field_request** | [**FieldServerEndpointsInstallFieldRequest**](FieldServerEndpointsInstallFieldRequest.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**FieldWithFieldEmbed**](FieldWithFieldEmbed.md)

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

# **install_field_legacy**
> FieldWithFieldEmbed install_field_legacy(field_server_endpoints_install_field_request_legacy, token=token, act_as_admin=act_as_admin)

Install a new field

Installs a new field. If it's a team-field, then it's possible to install it with empty or any non-empty amount of linked workspaces. Otherwise, if it's not a team-field, then exactly one linked workspace should be specified.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"full\"<br/>  - team features: \"team-fields\" when operating with team-fields<br/>  - user role: \"admin\" when operating with team-fields<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.field_server_endpoints_install_field_request_legacy import FieldServerEndpointsInstallFieldRequestLegacy
from openapi_client.models.field_with_field_embed import FieldWithFieldEmbed
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
    api_instance = openapi_client.FieldsApi(api_client)
    field_server_endpoints_install_field_request_legacy = openapi_client.FieldServerEndpointsInstallFieldRequestLegacy() # FieldServerEndpointsInstallFieldRequestLegacy | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Install a new field
        api_response = api_instance.install_field_legacy(field_server_endpoints_install_field_request_legacy, token=token, act_as_admin=act_as_admin)
        print("The response of FieldsApi->install_field_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldsApi->install_field_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_server_endpoints_install_field_request_legacy** | [**FieldServerEndpointsInstallFieldRequestLegacy**](FieldServerEndpointsInstallFieldRequestLegacy.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**FieldWithFieldEmbed**](FieldWithFieldEmbed.md)

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

# **install_field_legacy_with_workspace_id**
> FieldWithFieldEmbed install_field_legacy_with_workspace_id(workspace_id, field_server_endpoints_install_field_request_legacy, token=token, act_as_admin=act_as_admin)

Install a new field

Installs a new field. If it's a team-field, then it's possible to install it with empty or any non-empty amount of linked workspaces. Otherwise, if it's not a team-field, then exactly one linked workspace should be specified.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"full\"<br/>  - team features: \"team-fields\" when operating with team-fields<br/>  - user role: \"admin\" when operating with team-fields<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.field_server_endpoints_install_field_request_legacy import FieldServerEndpointsInstallFieldRequestLegacy
from openapi_client.models.field_with_field_embed import FieldWithFieldEmbed
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
    api_instance = openapi_client.FieldsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed fields.
    field_server_endpoints_install_field_request_legacy = openapi_client.FieldServerEndpointsInstallFieldRequestLegacy() # FieldServerEndpointsInstallFieldRequestLegacy | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Install a new field
        api_response = api_instance.install_field_legacy_with_workspace_id(workspace_id, field_server_endpoints_install_field_request_legacy, token=token, act_as_admin=act_as_admin)
        print("The response of FieldsApi->install_field_legacy_with_workspace_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldsApi->install_field_legacy_with_workspace_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed fields. | 
 **field_server_endpoints_install_field_request_legacy** | [**FieldServerEndpointsInstallFieldRequestLegacy**](FieldServerEndpointsInstallFieldRequestLegacy.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**FieldWithFieldEmbed**](FieldWithFieldEmbed.md)

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

# **link_team_fields_to_workspaces**
> List[FieldWithFieldEmbed] link_team_fields_to_workspaces(token=token, act_as_admin=act_as_admin, field_server_endpoints_field_to_workspace_link=field_server_endpoints_field_to_workspace_link)

Link team-fields to workspaces

Links existing team-fields to existing workspaces. Returns updated fields with their linked workspaces embedded. Returns an error if either of the requested fields is not a team-field. Ignores existing links. <br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"full\"<br/>  - team features: \"team-fields\" when operating with team-fields<br/>  - user role: \"admin\" when operating with team-fields<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.field_server_endpoints_field_to_workspace_link import FieldServerEndpointsFieldToWorkspaceLink
from openapi_client.models.field_with_field_embed import FieldWithFieldEmbed
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
    api_instance = openapi_client.FieldsApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    field_server_endpoints_field_to_workspace_link = [openapi_client.FieldServerEndpointsFieldToWorkspaceLink()] # List[FieldServerEndpointsFieldToWorkspaceLink] |  (optional)

    try:
        # Link team-fields to workspaces
        api_response = api_instance.link_team_fields_to_workspaces(token=token, act_as_admin=act_as_admin, field_server_endpoints_field_to_workspace_link=field_server_endpoints_field_to_workspace_link)
        print("The response of FieldsApi->link_team_fields_to_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldsApi->link_team_fields_to_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **field_server_endpoints_field_to_workspace_link** | [**List[FieldServerEndpointsFieldToWorkspaceLink]**](FieldServerEndpointsFieldToWorkspaceLink.md)|  | [optional] 

### Return type

[**List[FieldWithFieldEmbed]**](FieldWithFieldEmbed.md)

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

# **link_team_fields_to_workspaces_legacy**
> FieldWithFieldEmbed link_team_fields_to_workspaces_legacy(field_server_endpoints_field_to_workspace_link, token=token, act_as_admin=act_as_admin)

Add team-field to workspace

Links existing team-fields to existing workspaces. Returns updated fields with their linked workspaces embedded. Returns an error if either of the requested fields is not a team-field. Ignores existing links. <br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"full\"<br/>  - team features: \"team-fields\" when operating with team-fields<br/>  - user role: \"admin\" when operating with team-fields<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.field_server_endpoints_field_to_workspace_link import FieldServerEndpointsFieldToWorkspaceLink
from openapi_client.models.field_with_field_embed import FieldWithFieldEmbed
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
    api_instance = openapi_client.FieldsApi(api_client)
    field_server_endpoints_field_to_workspace_link = openapi_client.FieldServerEndpointsFieldToWorkspaceLink() # FieldServerEndpointsFieldToWorkspaceLink | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Add team-field to workspace
        api_response = api_instance.link_team_fields_to_workspaces_legacy(field_server_endpoints_field_to_workspace_link, token=token, act_as_admin=act_as_admin)
        print("The response of FieldsApi->link_team_fields_to_workspaces_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldsApi->link_team_fields_to_workspaces_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_server_endpoints_field_to_workspace_link** | [**FieldServerEndpointsFieldToWorkspaceLink**](FieldServerEndpointsFieldToWorkspaceLink.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**FieldWithFieldEmbed**](FieldWithFieldEmbed.md)

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

# **list_field_types**
> List[FieldServerEndpointsFieldTypeInfo] list_field_types(token=token, act_as_admin=act_as_admin)

List all available field types

Returns all field-types available in the system.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>  - team features: \"team-fields\" when operating with team-fields<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.field_server_endpoints_field_type_info import FieldServerEndpointsFieldTypeInfo
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
    api_instance = openapi_client.FieldsApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # List all available field types
        api_response = api_instance.list_field_types(token=token, act_as_admin=act_as_admin)
        print("The response of FieldsApi->list_field_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldsApi->list_field_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**List[FieldServerEndpointsFieldTypeInfo]**](FieldServerEndpointsFieldTypeInfo.md)

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

# **list_field_types_legacy**
> List[FieldServerEndpointsFieldTypeInfo] list_field_types_legacy(token=token, act_as_admin=act_as_admin)

List all available field types

Returns all field-types available in the system.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>  - team features: \"team-fields\" when operating with team-fields<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.field_server_endpoints_field_type_info import FieldServerEndpointsFieldTypeInfo
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
    api_instance = openapi_client.FieldsApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # List all available field types
        api_response = api_instance.list_field_types_legacy(token=token, act_as_admin=act_as_admin)
        print("The response of FieldsApi->list_field_types_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldsApi->list_field_types_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**List[FieldServerEndpointsFieldTypeInfo]**](FieldServerEndpointsFieldTypeInfo.md)

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

# **reconfigure_field**
> FieldWithFieldEmbed reconfigure_field(field_id, field_server_endpoints_reconfigure_field_request, token=token, act_as_admin=act_as_admin)

Reconfigure field

Updates configuration properties of an existing field.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"full\"<br/>  - team features: \"team-fields\" when operating with team-fields<br/>  - user role: \"admin\" when operating with team-fields<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.field_server_endpoints_reconfigure_field_request import FieldServerEndpointsReconfigureFieldRequest
from openapi_client.models.field_with_field_embed import FieldWithFieldEmbed
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
    api_instance = openapi_client.FieldsApi(api_client)
    field_id = 'field_id_example' # str | ID of the target field.
    field_server_endpoints_reconfigure_field_request = openapi_client.FieldServerEndpointsReconfigureFieldRequest() # FieldServerEndpointsReconfigureFieldRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Reconfigure field
        api_response = api_instance.reconfigure_field(field_id, field_server_endpoints_reconfigure_field_request, token=token, act_as_admin=act_as_admin)
        print("The response of FieldsApi->reconfigure_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldsApi->reconfigure_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_id** | **str**| ID of the target field. | 
 **field_server_endpoints_reconfigure_field_request** | [**FieldServerEndpointsReconfigureFieldRequest**](FieldServerEndpointsReconfigureFieldRequest.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**FieldWithFieldEmbed**](FieldWithFieldEmbed.md)

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

# **reconfigure_field_legacy**
> FieldWithFieldEmbed reconfigure_field_legacy(field_server_endpoints_reconfigure_field_request_legacy, token=token, act_as_admin=act_as_admin)

Reconfigure field

Updates configuration properties of an existing field.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"full\"<br/>  - team features: \"team-fields\" when operating with team-fields<br/>  - user role: \"admin\" when operating with team-fields<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.field_server_endpoints_reconfigure_field_request_legacy import FieldServerEndpointsReconfigureFieldRequestLegacy
from openapi_client.models.field_with_field_embed import FieldWithFieldEmbed
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
    api_instance = openapi_client.FieldsApi(api_client)
    field_server_endpoints_reconfigure_field_request_legacy = openapi_client.FieldServerEndpointsReconfigureFieldRequestLegacy() # FieldServerEndpointsReconfigureFieldRequestLegacy | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Reconfigure field
        api_response = api_instance.reconfigure_field_legacy(field_server_endpoints_reconfigure_field_request_legacy, token=token, act_as_admin=act_as_admin)
        print("The response of FieldsApi->reconfigure_field_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldsApi->reconfigure_field_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_server_endpoints_reconfigure_field_request_legacy** | [**FieldServerEndpointsReconfigureFieldRequestLegacy**](FieldServerEndpointsReconfigureFieldRequestLegacy.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**FieldWithFieldEmbed**](FieldWithFieldEmbed.md)

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

# **reconfigure_field_legacy_with_workspace_id**
> FieldWithFieldEmbed reconfigure_field_legacy_with_workspace_id(workspace_id, field_server_endpoints_reconfigure_field_request_legacy, token=token, act_as_admin=act_as_admin)

Reconfigure field

Updates configuration properties of an existing field.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"full\"<br/>  - team features: \"team-fields\" when operating with team-fields<br/>  - user role: \"admin\" when operating with team-fields<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.field_server_endpoints_reconfigure_field_request_legacy import FieldServerEndpointsReconfigureFieldRequestLegacy
from openapi_client.models.field_with_field_embed import FieldWithFieldEmbed
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
    api_instance = openapi_client.FieldsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed fields.
    field_server_endpoints_reconfigure_field_request_legacy = openapi_client.FieldServerEndpointsReconfigureFieldRequestLegacy() # FieldServerEndpointsReconfigureFieldRequestLegacy | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Reconfigure field
        api_response = api_instance.reconfigure_field_legacy_with_workspace_id(workspace_id, field_server_endpoints_reconfigure_field_request_legacy, token=token, act_as_admin=act_as_admin)
        print("The response of FieldsApi->reconfigure_field_legacy_with_workspace_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldsApi->reconfigure_field_legacy_with_workspace_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed fields. | 
 **field_server_endpoints_reconfigure_field_request_legacy** | [**FieldServerEndpointsReconfigureFieldRequestLegacy**](FieldServerEndpointsReconfigureFieldRequestLegacy.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**FieldWithFieldEmbed**](FieldWithFieldEmbed.md)

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

# **reorder_fields**
> reorder_fields(field_server_endpoints_reorder_fields_request, token=token, act_as_admin=act_as_admin)

Reorder fields

Updates the order of fields in the specified workspace.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"full\"<br/>  - team features: \"team-fields\" when operating with team-fields<br/>  - user role: \"admin\" when operating with team-fields<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.field_server_endpoints_reorder_fields_request import FieldServerEndpointsReorderFieldsRequest
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
    api_instance = openapi_client.FieldsApi(api_client)
    field_server_endpoints_reorder_fields_request = openapi_client.FieldServerEndpointsReorderFieldsRequest() # FieldServerEndpointsReorderFieldsRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Reorder fields
        api_instance.reorder_fields(field_server_endpoints_reorder_fields_request, token=token, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling FieldsApi->reorder_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_server_endpoints_reorder_fields_request** | [**FieldServerEndpointsReorderFieldsRequest**](FieldServerEndpointsReorderFieldsRequest.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

void (empty response body)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reorder_fields_legacy**
> reorder_fields_legacy(workspace_id, token=token, act_as_admin=act_as_admin, request_body=request_body)

Reorder fields

Updates the order of fields in the specified workspace.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"full\"<br/>  - team features: \"team-fields\" when operating with team-fields<br/>  - user role: \"admin\" when operating with team-fields<br/>Returns:<br/>403 if user does not have the required permission

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
    api_instance = openapi_client.FieldsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed fields.
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Reorder fields
        api_instance.reorder_fields_legacy(workspace_id, token=token, act_as_admin=act_as_admin, request_body=request_body)
    except Exception as e:
        print("Exception when calling FieldsApi->reorder_fields_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed fields. | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_field**
> FieldWithFieldEmbed retrieve_field(field_id, token=token, act_as_admin=act_as_admin)

Retrieve a single field

Returns a found field with its embedded data. The field is accessible by the current user only if it's a team-field, or if it belongs to an accessible workspace.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>  - team features: \"team-fields\" when operating with team-fields<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.field_with_field_embed import FieldWithFieldEmbed
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
    api_instance = openapi_client.FieldsApi(api_client)
    field_id = 'field_id_example' # str | ID of the target field.
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Retrieve a single field
        api_response = api_instance.retrieve_field(field_id, token=token, act_as_admin=act_as_admin)
        print("The response of FieldsApi->retrieve_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldsApi->retrieve_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_id** | **str**| ID of the target field. | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**FieldWithFieldEmbed**](FieldWithFieldEmbed.md)

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

# **search_fields**
> FieldWithFieldEmbedPage search_fields(field_search_query, token=token, act_as_admin=act_as_admin)

Search fields

Searches fields in the current team based on the specified filters.<br/>Requirements:<br/>  - auth-client scopes: \"workspace:read\"<br/>  - user permission: \"read\" or higher<br/>  - team features: \"team-fields\" when operating with team-fields<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.field_search_query import FieldSearchQuery
from openapi_client.models.field_with_field_embed_page import FieldWithFieldEmbedPage
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
    api_instance = openapi_client.FieldsApi(api_client)
    field_search_query = openapi_client.FieldSearchQuery() # FieldSearchQuery | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Search fields
        api_response = api_instance.search_fields(field_search_query, token=token, act_as_admin=act_as_admin)
        print("The response of FieldsApi->search_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldsApi->search_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_search_query** | [**FieldSearchQuery**](FieldSearchQuery.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**FieldWithFieldEmbedPage**](FieldWithFieldEmbedPage.md)

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

# **uninstall_field_completely_legacy**
> uninstall_field_completely_legacy(field_server_endpoints_uninstall_field_request, token=token, act_as_admin=act_as_admin)

Completely delete field

Removes the field and all its connections to workspaces, regardless whether it's a team-field or not.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"full\"<br/>  - team features: \"team-fields\" when operating with team-fields<br/>  - user role: \"admin\" when operating with team-fields<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.field_server_endpoints_uninstall_field_request import FieldServerEndpointsUninstallFieldRequest
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
    api_instance = openapi_client.FieldsApi(api_client)
    field_server_endpoints_uninstall_field_request = openapi_client.FieldServerEndpointsUninstallFieldRequest() # FieldServerEndpointsUninstallFieldRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Completely delete field
        api_instance.uninstall_field_completely_legacy(field_server_endpoints_uninstall_field_request, token=token, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling FieldsApi->uninstall_field_completely_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_server_endpoints_uninstall_field_request** | [**FieldServerEndpointsUninstallFieldRequest**](FieldServerEndpointsUninstallFieldRequest.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

void (empty response body)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uninstall_field_legacy**
> uninstall_field_legacy(workspace_id, field_server_endpoints_uninstall_field_request, token=token, act_as_admin=act_as_admin)

Delete field

Uninstalls a field from the specified workspace. For team-fields it results in just removing the field<>workspace connection, but the field itself won't be removed. For non-team-fields it additionally results in removing the field.<br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"full\"<br/>  - team features: \"team-fields\" when operating with team-fields<br/>  - user role: \"admin\" when operating with team-fields<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.field_server_endpoints_uninstall_field_request import FieldServerEndpointsUninstallFieldRequest
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
    api_instance = openapi_client.FieldsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed fields.
    field_server_endpoints_uninstall_field_request = openapi_client.FieldServerEndpointsUninstallFieldRequest() # FieldServerEndpointsUninstallFieldRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Delete field
        api_instance.uninstall_field_legacy(workspace_id, field_server_endpoints_uninstall_field_request, token=token, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling FieldsApi->uninstall_field_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed fields. | 
 **field_server_endpoints_uninstall_field_request** | [**FieldServerEndpointsUninstallFieldRequest**](FieldServerEndpointsUninstallFieldRequest.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

void (empty response body)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_team_fields_from_workspaces**
> List[FieldWithFieldEmbed] unlink_team_fields_from_workspaces(token=token, act_as_admin=act_as_admin, field_server_endpoints_field_to_workspace_link=field_server_endpoints_field_to_workspace_link)

Unlink team-fields from workspaces

Removes existing links between team-fields and workspaces. Returns updated fields with their linked workspaces embedded. Returns an error if either of the requested fields is not a team-field. Ignores when trying to delete non-existing links. <br/>Requirements:<br/>  - auth-client scopes: \"workspace\"<br/>  - user permission: \"full\"<br/>  - team features: \"team-fields\" when operating with team-fields<br/>  - user role: \"admin\" when operating with team-fields<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.field_server_endpoints_field_to_workspace_link import FieldServerEndpointsFieldToWorkspaceLink
from openapi_client.models.field_with_field_embed import FieldWithFieldEmbed
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
    api_instance = openapi_client.FieldsApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    field_server_endpoints_field_to_workspace_link = [openapi_client.FieldServerEndpointsFieldToWorkspaceLink()] # List[FieldServerEndpointsFieldToWorkspaceLink] |  (optional)

    try:
        # Unlink team-fields from workspaces
        api_response = api_instance.unlink_team_fields_from_workspaces(token=token, act_as_admin=act_as_admin, field_server_endpoints_field_to_workspace_link=field_server_endpoints_field_to_workspace_link)
        print("The response of FieldsApi->unlink_team_fields_from_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldsApi->unlink_team_fields_from_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **field_server_endpoints_field_to_workspace_link** | [**List[FieldServerEndpointsFieldToWorkspaceLink]**](FieldServerEndpointsFieldToWorkspaceLink.md)|  | [optional] 

### Return type

[**List[FieldWithFieldEmbed]**](FieldWithFieldEmbed.md)

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

