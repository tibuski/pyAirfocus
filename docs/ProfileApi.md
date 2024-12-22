# openapi_client.ProfileApi

All URIs are relative to *https://app.airfocus.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password**](ProfileApi.md#change_password) | **POST** /api/profile/change-password | 
[**create_api_key**](ProfileApi.md#create_api_key) | **POST** /api/profile/api-keys | 
[**delete_api_key**](ProfileApi.md#delete_api_key) | **DELETE** /api/profile/api-keys/{apiKeyId} | 
[**get_client_settings**](ProfileApi.md#get_client_settings) | **GET** /api/profile/client-settings | 
[**list_api_keys**](ProfileApi.md#list_api_keys) | **GET** /api/profile/api-keys | 
[**retrieve_profile**](ProfileApi.md#retrieve_profile) | **GET** /api/profile | 
[**set_client_settings**](ProfileApi.md#set_client_settings) | **PUT** /api/profile/client-settings | 
[**update_profile**](ProfileApi.md#update_profile) | **PUT** /api/profile | 


# **change_password**
> change_password(change_password_request, token=token)



Requirements:<br/>- auth-client scopes: \"profile\"

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.change_password_request import ChangePasswordRequest
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
    api_instance = openapi_client.ProfileApi(api_client)
    change_password_request = openapi_client.ChangePasswordRequest() # ChangePasswordRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)

    try:
        api_instance.change_password(change_password_request, token=token)
    except Exception as e:
        print("Exception when calling ProfileApi->change_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_password_request** | [**ChangePasswordRequest**](ChangePasswordRequest.md)|  | 
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

# **create_api_key**
> CreateApiKeyResponse create_api_key(create_api_key_request, token=token)



Requirements:<br/>- auth-client scopes: \"profile\"<br/>- team features: \"api-keys\"

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.create_api_key_request import CreateApiKeyRequest
from openapi_client.models.create_api_key_response import CreateApiKeyResponse
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
    api_instance = openapi_client.ProfileApi(api_client)
    create_api_key_request = openapi_client.CreateApiKeyRequest() # CreateApiKeyRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)

    try:
        api_response = api_instance.create_api_key(create_api_key_request, token=token)
        print("The response of ProfileApi->create_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->create_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_api_key_request** | [**CreateApiKeyRequest**](CreateApiKeyRequest.md)|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 

### Return type

[**CreateApiKeyResponse**](CreateApiKeyResponse.md)

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

# **delete_api_key**
> delete_api_key(api_key_id, token=token)



Requirements:<br/>- auth-client scopes: \"profile\"<br/>- team features: \"api-keys\"

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
    api_instance = openapi_client.ProfileApi(api_client)
    api_key_id = 'api_key_id_example' # str | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)

    try:
        api_instance.delete_api_key(api_key_id, token=token)
    except Exception as e:
        print("Exception when calling ProfileApi->delete_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **str**|  | 
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_settings**
> object get_client_settings(token=token, path=path)



Requirements:<br/>- auth-client scopes: \"profile:read\"

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
    api_instance = openapi_client.ProfileApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)
    path = 'path_example' # str |  (optional)

    try:
        api_response = api_instance.get_client_settings(token=token, path=path)
        print("The response of ProfileApi->get_client_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_client_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 
 **path** | **str**|  | [optional] 

### Return type

**object**

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

# **list_api_keys**
> List[ApiKey] list_api_keys(token=token)



Requirements:<br/>- auth-client scopes: \"profile\"<br/>- team features: \"api-keys\"

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.api_key import ApiKey
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
    api_instance = openapi_client.ProfileApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)

    try:
        api_response = api_instance.list_api_keys(token=token)
        print("The response of ProfileApi->list_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->list_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 

### Return type

[**List[ApiKey]**](ApiKey.md)

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

# **retrieve_profile**
> User retrieve_profile(token=token)



Requirements:<br/>- auth-client scopes: \"profile:read\"

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
    api_instance = openapi_client.ProfileApi(api_client)
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)

    try:
        api_response = api_instance.retrieve_profile(token=token)
        print("The response of ProfileApi->retrieve_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->retrieve_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Auth token as query parameter (alternative to Authorization header). | [optional] 

### Return type

[**User**](User.md)

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

# **set_client_settings**
> set_client_settings(set_client_settings_request, token=token)



Requirements:<br/>- auth-client scopes: \"profile\"

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.set_client_settings_request import SetClientSettingsRequest
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
    api_instance = openapi_client.ProfileApi(api_client)
    set_client_settings_request = openapi_client.SetClientSettingsRequest() # SetClientSettingsRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)

    try:
        api_instance.set_client_settings(set_client_settings_request, token=token)
    except Exception as e:
        print("Exception when calling ProfileApi->set_client_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_client_settings_request** | [**SetClientSettingsRequest**](SetClientSettingsRequest.md)|  | 
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

# **update_profile**
> User update_profile(update_user_request, token=token)



Requirements:<br/>- auth-client scopes: \"profile\"

### Example

* Bearer Authentication (httpAuth):

```python
import openapi_client
from openapi_client.models.update_user_request import UpdateUserRequest
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
    api_instance = openapi_client.ProfileApi(api_client)
    update_user_request = openapi_client.UpdateUserRequest() # UpdateUserRequest | 
    token = 'token_example' # str | Auth token as query parameter (alternative to Authorization header). (optional)

    try:
        api_response = api_instance.update_profile(update_user_request, token=token)
        print("The response of ProfileApi->update_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->update_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_user_request** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | 
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

