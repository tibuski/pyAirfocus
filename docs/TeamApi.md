# openapi_client.TeamApi

All URIs are relative to *https://app.airfocus.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_terms_of_service**](TeamApi.md#accept_terms_of_service) | **POST** /api/team/tos | 
[**change_user_disabled**](TeamApi.md#change_user_disabled) | **POST** /api/team/users/disabled | 
[**change_user_role**](TeamApi.md#change_user_role) | **POST** /api/team/users/role | 
[**create_user_invite**](TeamApi.md#create_user_invite) | **POST** /api/team/users/invite/create | 
[**kick_user**](TeamApi.md#kick_user) | **POST** /api/team/users/kick | 
[**list_users**](TeamApi.md#list_users) | **GET** /api/team/users | 
[**resend_user_invite**](TeamApi.md#resend_user_invite) | **POST** /api/team/users/invite/resend | 
[**retrieve_team**](TeamApi.md#retrieve_team) | **GET** /api/team | 
[**send_bulk_user_invites**](TeamApi.md#send_bulk_user_invites) | **POST** /api/team/users/invite/bulk | 
[**send_user_invite**](TeamApi.md#send_user_invite) | **POST** /api/team/users/invite | 
[**update_team_flags**](TeamApi.md#update_team_flags) | **PATCH** /api/team/flags | 


# **accept_terms_of_service**
> accept_terms_of_service(store_accepted_tos_request, token=token)



Requirements:<br/>- auth-client scopes: \"team\"<br/>- user role: \"admin\"<br/>Returns:<br/>- 403 if user does not match the required role

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.store_accepted_tos_request import StoreAcceptedTosRequest
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
    api_instance = openapi_client.TeamApi(api_client)
    store_accepted_tos_request = openapi_client.StoreAcceptedTosRequest() # StoreAcceptedTosRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)

    try:
        api_instance.accept_terms_of_service(store_accepted_tos_request, token=token)
    except Exception as e:
        print("Exception when calling TeamApi->accept_terms_of_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_accepted_tos_request** | [**StoreAcceptedTosRequest**](StoreAcceptedTosRequest.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_disabled**
> change_user_disabled(change_user_disabled_request, token=token)



Requirements:<br/>- auth-client scopes: \"team\"<br/>- user role: \"admin\"<br/>Returns:<br/>- 403 if user does not match the required role

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.change_user_disabled_request import ChangeUserDisabledRequest
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
    api_instance = openapi_client.TeamApi(api_client)
    change_user_disabled_request = openapi_client.ChangeUserDisabledRequest() # ChangeUserDisabledRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)

    try:
        api_instance.change_user_disabled(change_user_disabled_request, token=token)
    except Exception as e:
        print("Exception when calling TeamApi->change_user_disabled: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_user_disabled_request** | [**ChangeUserDisabledRequest**](ChangeUserDisabledRequest.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_role**
> change_user_role(change_user_role_request, token=token)



Requirements:<br/>- auth-client scopes: \"team\"<br/>- user role: \"admin\"<br/>Returns:<br/>- 403 if user does not match the required role

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.change_user_role_request import ChangeUserRoleRequest
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
    api_instance = openapi_client.TeamApi(api_client)
    change_user_role_request = openapi_client.ChangeUserRoleRequest() # ChangeUserRoleRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)

    try:
        api_instance.change_user_role(change_user_role_request, token=token)
    except Exception as e:
        print("Exception when calling TeamApi->change_user_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_user_role_request** | [**ChangeUserRoleRequest**](ChangeUserRoleRequest.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_invite**
> str create_user_invite(create_user_invite_request, token=token)



Requirements:<br/>- auth-client scopes: \"team\"<br/>- user role: \"admin\"<br/>Returns:<br/>- 403 if user does not match the required role

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.create_user_invite_request import CreateUserInviteRequest
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
    api_instance = openapi_client.TeamApi(api_client)
    create_user_invite_request = openapi_client.CreateUserInviteRequest() # CreateUserInviteRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)

    try:
        api_response = api_instance.create_user_invite(create_user_invite_request, token=token)
        print("The response of TeamApi->create_user_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->create_user_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_invite_request** | [**CreateUserInviteRequest**](CreateUserInviteRequest.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 

### Return type

**str**

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

# **kick_user**
> kick_user(kick_user_request, token=token)



Requirements:<br/>- auth-client scopes: \"team\"<br/>- user role: \"admin\"<br/>Returns:<br/>- 403 if user does not match the required role

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.kick_user_request import KickUserRequest
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
    api_instance = openapi_client.TeamApi(api_client)
    kick_user_request = openapi_client.KickUserRequest() # KickUserRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)

    try:
        api_instance.kick_user(kick_user_request, token=token)
    except Exception as e:
        print("Exception when calling TeamApi->kick_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kick_user_request** | [**KickUserRequest**](KickUserRequest.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> List[User] list_users(token=token, query=query)



List team users.<br/>Requirements:<br/>- auth-client scopes: \"team:read\"

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.user import User
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
    api_instance = openapi_client.TeamApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    query = 'query_example' # str |  (optional)

    try:
        api_response = api_instance.list_users(token=token, query=query)
        print("The response of TeamApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **query** | **str**|  | [optional] 

### Return type

[**List[User]**](User.md)

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

# **resend_user_invite**
> resend_user_invite(resend_user_invite_request, token=token)



Requirements:<br/>- auth-client scopes: \"team\"<br/>- user role: \"admin\"<br/>Returns:<br/>- 403 if user does not match the required role

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.resend_user_invite_request import ResendUserInviteRequest
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
    api_instance = openapi_client.TeamApi(api_client)
    resend_user_invite_request = openapi_client.ResendUserInviteRequest() # ResendUserInviteRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)

    try:
        api_instance.resend_user_invite(resend_user_invite_request, token=token)
    except Exception as e:
        print("Exception when calling TeamApi->resend_user_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resend_user_invite_request** | [**ResendUserInviteRequest**](ResendUserInviteRequest.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_team**
> Team retrieve_team(token=token)



Requirements:<br/>- auth-client scopes: \"team:read\"

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.team import Team
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
    api_instance = openapi_client.TeamApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)

    try:
        api_response = api_instance.retrieve_team(token=token)
        print("The response of TeamApi->retrieve_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->retrieve_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 

### Return type

[**Team**](Team.md)

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

# **send_bulk_user_invites**
> List[User] send_bulk_user_invites(bulk_invite_users_request, token=token)



Requirements:<br/>- auth-client scopes: \"team\"<br/>- user role: \"admin\"<br/>Returns:<br/>- 403 if user does not match the required role

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.bulk_invite_users_request import BulkInviteUsersRequest
from openapi_client.models.user import User
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
    api_instance = openapi_client.TeamApi(api_client)
    bulk_invite_users_request = openapi_client.BulkInviteUsersRequest() # BulkInviteUsersRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)

    try:
        api_response = api_instance.send_bulk_user_invites(bulk_invite_users_request, token=token)
        print("The response of TeamApi->send_bulk_user_invites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->send_bulk_user_invites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_invite_users_request** | [**BulkInviteUsersRequest**](BulkInviteUsersRequest.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 

### Return type

[**List[User]**](User.md)

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

# **send_user_invite**
> User send_user_invite(invite_user_request, token=token)



Requirements:<br/>- auth-client scopes: \"team\"<br/>- user role: \"admin\"<br/>Returns:<br/>- 403 if user does not match the required role

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.invite_user_request import InviteUserRequest
from openapi_client.models.user import User
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
    api_instance = openapi_client.TeamApi(api_client)
    invite_user_request = openapi_client.InviteUserRequest() # InviteUserRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)

    try:
        api_response = api_instance.send_user_invite(invite_user_request, token=token)
        print("The response of TeamApi->send_user_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->send_user_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_user_request** | [**InviteUserRequest**](InviteUserRequest.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 

### Return type

[**User**](User.md)

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

# **update_team_flags**
> TeamFlags update_team_flags(update_team_flags_request, token=token)



Requirements:<br/>- auth-client scopes: \"team\"<br/>- user role: \"admin\"<br/>Returns:<br/>- 403 if user does not match the required role

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.team_flags import TeamFlags
from openapi_client.models.update_team_flags_request import UpdateTeamFlagsRequest
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
    api_instance = openapi_client.TeamApi(api_client)
    update_team_flags_request = openapi_client.UpdateTeamFlagsRequest() # UpdateTeamFlagsRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)

    try:
        api_response = api_instance.update_team_flags(update_team_flags_request, token=token)
        print("The response of TeamApi->update_team_flags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->update_team_flags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_team_flags_request** | [**UpdateTeamFlagsRequest**](UpdateTeamFlagsRequest.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 

### Return type

[**TeamFlags**](TeamFlags.md)

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

