# fwallet.DeveloperApi

All URIs are relative to *https://api.fwallet.co.ug*

Method | HTTP request | Description
------------- | ------------- | -------------
[**developer_get_developer_api_keys**](DeveloperApi.md#developer_get_developer_api_keys) | **GET** /v1/developer/api-keys | Get Developer
[**developer_get_developer_apps**](DeveloperApi.md#developer_get_developer_apps) | **GET** /v1/developer/apps | Get Developer
[**developer_get_developer_request_logs**](DeveloperApi.md#developer_get_developer_request_logs) | **GET** /v1/developer/request-logs | Get Developer
[**developer_patch_developer_api_keys_by_id_restrictions**](DeveloperApi.md#developer_patch_developer_api_keys_by_id_restrictions) | **PATCH** /v1/developer/api-keys/{id}/restrictions | Update Developer
[**developer_patch_developer_apps_by_id**](DeveloperApi.md#developer_patch_developer_apps_by_id) | **PATCH** /v1/developer/apps/{id} | Update Developer
[**developer_post_developer_api_keys**](DeveloperApi.md#developer_post_developer_api_keys) | **POST** /v1/developer/api-keys | Create Developer
[**developer_post_developer_api_keys_by_id_revoke**](DeveloperApi.md#developer_post_developer_api_keys_by_id_revoke) | **POST** /v1/developer/api-keys/{id}/revoke | Create Developer
[**developer_post_developer_api_keys_by_id_rotate**](DeveloperApi.md#developer_post_developer_api_keys_by_id_rotate) | **POST** /v1/developer/api-keys/{id}/rotate | Create Developer
[**developer_post_developer_apps**](DeveloperApi.md#developer_post_developer_apps) | **POST** /v1/developer/apps | Create Developer


# **developer_get_developer_api_keys**
> DeveloperGetDeveloperApiKeys200Response developer_get_developer_api_keys()

Get Developer

### Example

* Api Key Authentication (hmacNonce):
* Api Key Authentication (apiKey):
* Api Key Authentication (hmacContentSha256):
* Api Key Authentication (hmacTimestamp):
* Api Key Authentication (hmacKeyId):
* Api Key Authentication (hmacSignature):

```python
import fwallet
from fwallet.models.developer_get_developer_api_keys200_response import DeveloperGetDeveloperApiKeys200Response
from fwallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fwallet.co.ug
# See configuration.py for a list of all supported configuration parameters.
configuration = fwallet.Configuration(
    host = "https://api.fwallet.co.ug"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: hmacNonce
configuration.api_key['hmacNonce'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacNonce'] = 'Bearer'

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: hmacContentSha256
configuration.api_key['hmacContentSha256'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacContentSha256'] = 'Bearer'

# Configure API key authorization: hmacTimestamp
configuration.api_key['hmacTimestamp'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacTimestamp'] = 'Bearer'

# Configure API key authorization: hmacKeyId
configuration.api_key['hmacKeyId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacKeyId'] = 'Bearer'

# Configure API key authorization: hmacSignature
configuration.api_key['hmacSignature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacSignature'] = 'Bearer'

# Enter a context with an instance of the API client
with fwallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fwallet.DeveloperApi(api_client)

    try:
        # Get Developer
        api_response = api_instance.developer_get_developer_api_keys()
        print("The response of DeveloperApi->developer_get_developer_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_get_developer_api_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DeveloperGetDeveloperApiKeys200Response**](DeveloperGetDeveloperApiKeys200Response.md)

### Authorization

[hmacNonce](../README.md#hmacNonce), [apiKey](../README.md#apiKey), [hmacContentSha256](../README.md#hmacContentSha256), [hmacTimestamp](../README.md#hmacTimestamp), [hmacKeyId](../README.md#hmacKeyId), [hmacSignature](../README.md#hmacSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API key metadata |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_get_developer_apps**
> DeveloperGetDeveloperApps200Response developer_get_developer_apps()

Get Developer

### Example

* Api Key Authentication (hmacNonce):
* Api Key Authentication (apiKey):
* Api Key Authentication (hmacContentSha256):
* Api Key Authentication (hmacTimestamp):
* Api Key Authentication (hmacKeyId):
* Api Key Authentication (hmacSignature):

```python
import fwallet
from fwallet.models.developer_get_developer_apps200_response import DeveloperGetDeveloperApps200Response
from fwallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fwallet.co.ug
# See configuration.py for a list of all supported configuration parameters.
configuration = fwallet.Configuration(
    host = "https://api.fwallet.co.ug"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: hmacNonce
configuration.api_key['hmacNonce'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacNonce'] = 'Bearer'

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: hmacContentSha256
configuration.api_key['hmacContentSha256'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacContentSha256'] = 'Bearer'

# Configure API key authorization: hmacTimestamp
configuration.api_key['hmacTimestamp'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacTimestamp'] = 'Bearer'

# Configure API key authorization: hmacKeyId
configuration.api_key['hmacKeyId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacKeyId'] = 'Bearer'

# Configure API key authorization: hmacSignature
configuration.api_key['hmacSignature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacSignature'] = 'Bearer'

# Enter a context with an instance of the API client
with fwallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fwallet.DeveloperApi(api_client)

    try:
        # Get Developer
        api_response = api_instance.developer_get_developer_apps()
        print("The response of DeveloperApi->developer_get_developer_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_get_developer_apps: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DeveloperGetDeveloperApps200Response**](DeveloperGetDeveloperApps200Response.md)

### Authorization

[hmacNonce](../README.md#hmacNonce), [apiKey](../README.md#apiKey), [hmacContentSha256](../README.md#hmacContentSha256), [hmacTimestamp](../README.md#hmacTimestamp), [hmacKeyId](../README.md#hmacKeyId), [hmacSignature](../README.md#hmacSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Developer applications |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_get_developer_request_logs**
> DeveloperGetDeveloperRequestLogs200Response developer_get_developer_request_logs(api_key_id=api_key_id, application_id=application_id, auth_mode=auth_mode, traffic=traffic, environment=environment, status_family=status_family, status_code=status_code, method=method, path=path, origin=origin, ip_address=ip_address, actor_type=actor_type, actor_id=actor_id, idempotency_key=idempotency_key, correlation_id=correlation_id, created_from=created_from, created_to=created_to, limit=limit, page=page)

Get Developer

### Example

* Api Key Authentication (hmacNonce):
* Api Key Authentication (apiKey):
* Api Key Authentication (hmacContentSha256):
* Api Key Authentication (hmacTimestamp):
* Api Key Authentication (hmacKeyId):
* Api Key Authentication (hmacSignature):

```python
import fwallet
from fwallet.models.developer_get_developer_request_logs200_response import DeveloperGetDeveloperRequestLogs200Response
from fwallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fwallet.co.ug
# See configuration.py for a list of all supported configuration parameters.
configuration = fwallet.Configuration(
    host = "https://api.fwallet.co.ug"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: hmacNonce
configuration.api_key['hmacNonce'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacNonce'] = 'Bearer'

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: hmacContentSha256
configuration.api_key['hmacContentSha256'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacContentSha256'] = 'Bearer'

# Configure API key authorization: hmacTimestamp
configuration.api_key['hmacTimestamp'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacTimestamp'] = 'Bearer'

# Configure API key authorization: hmacKeyId
configuration.api_key['hmacKeyId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacKeyId'] = 'Bearer'

# Configure API key authorization: hmacSignature
configuration.api_key['hmacSignature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacSignature'] = 'Bearer'

# Enter a context with an instance of the API client
with fwallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fwallet.DeveloperApi(api_client)
    api_key_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    application_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    auth_mode = 'auth_mode_example' # str |  (optional)
    traffic = api # str |  (optional) (default to api)
    environment = 'environment_example' # str |  (optional)
    status_family = 'status_family_example' # str |  (optional)
    status_code = 56 # int |  (optional)
    method = 'method_example' # str |  (optional)
    path = 'path_example' # str |  (optional)
    origin = 'origin_example' # str |  (optional)
    ip_address = 'ip_address_example' # str |  (optional)
    actor_type = 'actor_type_example' # str |  (optional)
    actor_id = 'actor_id_example' # str |  (optional)
    idempotency_key = 'idempotency_key_example' # str |  (optional)
    correlation_id = 'correlation_id_example' # str |  (optional)
    created_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    created_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    page = 1 # int |  (optional) (default to 1)

    try:
        # Get Developer
        api_response = api_instance.developer_get_developer_request_logs(api_key_id=api_key_id, application_id=application_id, auth_mode=auth_mode, traffic=traffic, environment=environment, status_family=status_family, status_code=status_code, method=method, path=path, origin=origin, ip_address=ip_address, actor_type=actor_type, actor_id=actor_id, idempotency_key=idempotency_key, correlation_id=correlation_id, created_from=created_from, created_to=created_to, limit=limit, page=page)
        print("The response of DeveloperApi->developer_get_developer_request_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_get_developer_request_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **UUID**|  | [optional] 
 **application_id** | **UUID**|  | [optional] 
 **auth_mode** | **str**|  | [optional] 
 **traffic** | **str**|  | [optional] [default to api]
 **environment** | **str**|  | [optional] 
 **status_family** | **str**|  | [optional] 
 **status_code** | **int**|  | [optional] 
 **method** | **str**|  | [optional] 
 **path** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 
 **ip_address** | **str**|  | [optional] 
 **actor_type** | **str**|  | [optional] 
 **actor_id** | **str**|  | [optional] 
 **idempotency_key** | **str**|  | [optional] 
 **correlation_id** | **str**|  | [optional] 
 **created_from** | **datetime**|  | [optional] 
 **created_to** | **datetime**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **page** | **int**|  | [optional] [default to 1]

### Return type

[**DeveloperGetDeveloperRequestLogs200Response**](DeveloperGetDeveloperRequestLogs200Response.md)

### Authorization

[hmacNonce](../README.md#hmacNonce), [apiKey](../README.md#apiKey), [hmacContentSha256](../README.md#hmacContentSha256), [hmacTimestamp](../README.md#hmacTimestamp), [hmacKeyId](../README.md#hmacKeyId), [hmacSignature](../README.md#hmacSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API request logs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_patch_developer_api_keys_by_id_restrictions**
> ApiKeyMetadata developer_patch_developer_api_keys_by_id_restrictions(id, developer_patch_developer_api_keys_by_id_restrictions_request=developer_patch_developer_api_keys_by_id_restrictions_request)

Update Developer

### Example

* Api Key Authentication (hmacNonce):
* Api Key Authentication (apiKey):
* Api Key Authentication (hmacContentSha256):
* Api Key Authentication (hmacTimestamp):
* Api Key Authentication (hmacKeyId):
* Api Key Authentication (hmacSignature):

```python
import fwallet
from fwallet.models.api_key_metadata import ApiKeyMetadata
from fwallet.models.developer_patch_developer_api_keys_by_id_restrictions_request import DeveloperPatchDeveloperApiKeysByIdRestrictionsRequest
from fwallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fwallet.co.ug
# See configuration.py for a list of all supported configuration parameters.
configuration = fwallet.Configuration(
    host = "https://api.fwallet.co.ug"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: hmacNonce
configuration.api_key['hmacNonce'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacNonce'] = 'Bearer'

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: hmacContentSha256
configuration.api_key['hmacContentSha256'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacContentSha256'] = 'Bearer'

# Configure API key authorization: hmacTimestamp
configuration.api_key['hmacTimestamp'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacTimestamp'] = 'Bearer'

# Configure API key authorization: hmacKeyId
configuration.api_key['hmacKeyId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacKeyId'] = 'Bearer'

# Configure API key authorization: hmacSignature
configuration.api_key['hmacSignature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacSignature'] = 'Bearer'

# Enter a context with an instance of the API client
with fwallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fwallet.DeveloperApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    developer_patch_developer_api_keys_by_id_restrictions_request = fwallet.DeveloperPatchDeveloperApiKeysByIdRestrictionsRequest() # DeveloperPatchDeveloperApiKeysByIdRestrictionsRequest |  (optional)

    try:
        # Update Developer
        api_response = api_instance.developer_patch_developer_api_keys_by_id_restrictions(id, developer_patch_developer_api_keys_by_id_restrictions_request=developer_patch_developer_api_keys_by_id_restrictions_request)
        print("The response of DeveloperApi->developer_patch_developer_api_keys_by_id_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_patch_developer_api_keys_by_id_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 
 **developer_patch_developer_api_keys_by_id_restrictions_request** | [**DeveloperPatchDeveloperApiKeysByIdRestrictionsRequest**](DeveloperPatchDeveloperApiKeysByIdRestrictionsRequest.md)|  | [optional] 

### Return type

[**ApiKeyMetadata**](ApiKeyMetadata.md)

### Authorization

[hmacNonce](../README.md#hmacNonce), [apiKey](../README.md#apiKey), [hmacContentSha256](../README.md#hmacContentSha256), [hmacTimestamp](../README.md#hmacTimestamp), [hmacKeyId](../README.md#hmacKeyId), [hmacSignature](../README.md#hmacSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API key restrictions updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_patch_developer_apps_by_id**
> DeveloperApplication developer_patch_developer_apps_by_id(id, developer_patch_developer_apps_by_id_request=developer_patch_developer_apps_by_id_request)

Update Developer

### Example

* Api Key Authentication (hmacNonce):
* Api Key Authentication (apiKey):
* Api Key Authentication (hmacContentSha256):
* Api Key Authentication (hmacTimestamp):
* Api Key Authentication (hmacKeyId):
* Api Key Authentication (hmacSignature):

```python
import fwallet
from fwallet.models.developer_application import DeveloperApplication
from fwallet.models.developer_patch_developer_apps_by_id_request import DeveloperPatchDeveloperAppsByIdRequest
from fwallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fwallet.co.ug
# See configuration.py for a list of all supported configuration parameters.
configuration = fwallet.Configuration(
    host = "https://api.fwallet.co.ug"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: hmacNonce
configuration.api_key['hmacNonce'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacNonce'] = 'Bearer'

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: hmacContentSha256
configuration.api_key['hmacContentSha256'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacContentSha256'] = 'Bearer'

# Configure API key authorization: hmacTimestamp
configuration.api_key['hmacTimestamp'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacTimestamp'] = 'Bearer'

# Configure API key authorization: hmacKeyId
configuration.api_key['hmacKeyId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacKeyId'] = 'Bearer'

# Configure API key authorization: hmacSignature
configuration.api_key['hmacSignature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacSignature'] = 'Bearer'

# Enter a context with an instance of the API client
with fwallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fwallet.DeveloperApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    developer_patch_developer_apps_by_id_request = fwallet.DeveloperPatchDeveloperAppsByIdRequest() # DeveloperPatchDeveloperAppsByIdRequest |  (optional)

    try:
        # Update Developer
        api_response = api_instance.developer_patch_developer_apps_by_id(id, developer_patch_developer_apps_by_id_request=developer_patch_developer_apps_by_id_request)
        print("The response of DeveloperApi->developer_patch_developer_apps_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_patch_developer_apps_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 
 **developer_patch_developer_apps_by_id_request** | [**DeveloperPatchDeveloperAppsByIdRequest**](DeveloperPatchDeveloperAppsByIdRequest.md)|  | [optional] 

### Return type

[**DeveloperApplication**](DeveloperApplication.md)

### Authorization

[hmacNonce](../README.md#hmacNonce), [apiKey](../README.md#apiKey), [hmacContentSha256](../README.md#hmacContentSha256), [hmacTimestamp](../README.md#hmacTimestamp), [hmacKeyId](../README.md#hmacKeyId), [hmacSignature](../README.md#hmacSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Developer application updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_post_developer_api_keys**
> DeveloperPostDeveloperApiKeys201Response developer_post_developer_api_keys(developer_post_developer_api_keys_request=developer_post_developer_api_keys_request)

Create Developer

### Example

* Api Key Authentication (hmacNonce):
* Api Key Authentication (apiKey):
* Api Key Authentication (hmacContentSha256):
* Api Key Authentication (hmacTimestamp):
* Api Key Authentication (hmacKeyId):
* Api Key Authentication (hmacSignature):

```python
import fwallet
from fwallet.models.developer_post_developer_api_keys201_response import DeveloperPostDeveloperApiKeys201Response
from fwallet.models.developer_post_developer_api_keys_request import DeveloperPostDeveloperApiKeysRequest
from fwallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fwallet.co.ug
# See configuration.py for a list of all supported configuration parameters.
configuration = fwallet.Configuration(
    host = "https://api.fwallet.co.ug"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: hmacNonce
configuration.api_key['hmacNonce'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacNonce'] = 'Bearer'

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: hmacContentSha256
configuration.api_key['hmacContentSha256'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacContentSha256'] = 'Bearer'

# Configure API key authorization: hmacTimestamp
configuration.api_key['hmacTimestamp'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacTimestamp'] = 'Bearer'

# Configure API key authorization: hmacKeyId
configuration.api_key['hmacKeyId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacKeyId'] = 'Bearer'

# Configure API key authorization: hmacSignature
configuration.api_key['hmacSignature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacSignature'] = 'Bearer'

# Enter a context with an instance of the API client
with fwallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fwallet.DeveloperApi(api_client)
    developer_post_developer_api_keys_request = fwallet.DeveloperPostDeveloperApiKeysRequest() # DeveloperPostDeveloperApiKeysRequest |  (optional)

    try:
        # Create Developer
        api_response = api_instance.developer_post_developer_api_keys(developer_post_developer_api_keys_request=developer_post_developer_api_keys_request)
        print("The response of DeveloperApi->developer_post_developer_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_post_developer_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **developer_post_developer_api_keys_request** | [**DeveloperPostDeveloperApiKeysRequest**](DeveloperPostDeveloperApiKeysRequest.md)|  | [optional] 

### Return type

[**DeveloperPostDeveloperApiKeys201Response**](DeveloperPostDeveloperApiKeys201Response.md)

### Authorization

[hmacNonce](../README.md#hmacNonce), [apiKey](../README.md#apiKey), [hmacContentSha256](../README.md#hmacContentSha256), [hmacTimestamp](../README.md#hmacTimestamp), [hmacKeyId](../README.md#hmacKeyId), [hmacSignature](../README.md#hmacSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | API key created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_post_developer_api_keys_by_id_revoke**
> ApiKeyMetadata developer_post_developer_api_keys_by_id_revoke(id)

Create Developer

### Example

* Api Key Authentication (hmacNonce):
* Api Key Authentication (apiKey):
* Api Key Authentication (hmacContentSha256):
* Api Key Authentication (hmacTimestamp):
* Api Key Authentication (hmacKeyId):
* Api Key Authentication (hmacSignature):

```python
import fwallet
from fwallet.models.api_key_metadata import ApiKeyMetadata
from fwallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fwallet.co.ug
# See configuration.py for a list of all supported configuration parameters.
configuration = fwallet.Configuration(
    host = "https://api.fwallet.co.ug"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: hmacNonce
configuration.api_key['hmacNonce'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacNonce'] = 'Bearer'

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: hmacContentSha256
configuration.api_key['hmacContentSha256'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacContentSha256'] = 'Bearer'

# Configure API key authorization: hmacTimestamp
configuration.api_key['hmacTimestamp'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacTimestamp'] = 'Bearer'

# Configure API key authorization: hmacKeyId
configuration.api_key['hmacKeyId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacKeyId'] = 'Bearer'

# Configure API key authorization: hmacSignature
configuration.api_key['hmacSignature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacSignature'] = 'Bearer'

# Enter a context with an instance of the API client
with fwallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fwallet.DeveloperApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Create Developer
        api_response = api_instance.developer_post_developer_api_keys_by_id_revoke(id)
        print("The response of DeveloperApi->developer_post_developer_api_keys_by_id_revoke:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_post_developer_api_keys_by_id_revoke: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

### Return type

[**ApiKeyMetadata**](ApiKeyMetadata.md)

### Authorization

[hmacNonce](../README.md#hmacNonce), [apiKey](../README.md#apiKey), [hmacContentSha256](../README.md#hmacContentSha256), [hmacTimestamp](../README.md#hmacTimestamp), [hmacKeyId](../README.md#hmacKeyId), [hmacSignature](../README.md#hmacSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API key revoked |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_post_developer_api_keys_by_id_rotate**
> DeveloperPostDeveloperApiKeysByIdRotate201Response developer_post_developer_api_keys_by_id_rotate(id)

Create Developer

### Example

* Api Key Authentication (hmacNonce):
* Api Key Authentication (apiKey):
* Api Key Authentication (hmacContentSha256):
* Api Key Authentication (hmacTimestamp):
* Api Key Authentication (hmacKeyId):
* Api Key Authentication (hmacSignature):

```python
import fwallet
from fwallet.models.developer_post_developer_api_keys_by_id_rotate201_response import DeveloperPostDeveloperApiKeysByIdRotate201Response
from fwallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fwallet.co.ug
# See configuration.py for a list of all supported configuration parameters.
configuration = fwallet.Configuration(
    host = "https://api.fwallet.co.ug"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: hmacNonce
configuration.api_key['hmacNonce'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacNonce'] = 'Bearer'

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: hmacContentSha256
configuration.api_key['hmacContentSha256'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacContentSha256'] = 'Bearer'

# Configure API key authorization: hmacTimestamp
configuration.api_key['hmacTimestamp'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacTimestamp'] = 'Bearer'

# Configure API key authorization: hmacKeyId
configuration.api_key['hmacKeyId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacKeyId'] = 'Bearer'

# Configure API key authorization: hmacSignature
configuration.api_key['hmacSignature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacSignature'] = 'Bearer'

# Enter a context with an instance of the API client
with fwallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fwallet.DeveloperApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Create Developer
        api_response = api_instance.developer_post_developer_api_keys_by_id_rotate(id)
        print("The response of DeveloperApi->developer_post_developer_api_keys_by_id_rotate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_post_developer_api_keys_by_id_rotate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

### Return type

[**DeveloperPostDeveloperApiKeysByIdRotate201Response**](DeveloperPostDeveloperApiKeysByIdRotate201Response.md)

### Authorization

[hmacNonce](../README.md#hmacNonce), [apiKey](../README.md#apiKey), [hmacContentSha256](../README.md#hmacContentSha256), [hmacTimestamp](../README.md#hmacTimestamp), [hmacKeyId](../README.md#hmacKeyId), [hmacSignature](../README.md#hmacSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | API key rotated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_post_developer_apps**
> DeveloperApplication developer_post_developer_apps(developer_post_developer_apps_request=developer_post_developer_apps_request)

Create Developer

### Example

* Api Key Authentication (hmacNonce):
* Api Key Authentication (apiKey):
* Api Key Authentication (hmacContentSha256):
* Api Key Authentication (hmacTimestamp):
* Api Key Authentication (hmacKeyId):
* Api Key Authentication (hmacSignature):

```python
import fwallet
from fwallet.models.developer_application import DeveloperApplication
from fwallet.models.developer_post_developer_apps_request import DeveloperPostDeveloperAppsRequest
from fwallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fwallet.co.ug
# See configuration.py for a list of all supported configuration parameters.
configuration = fwallet.Configuration(
    host = "https://api.fwallet.co.ug"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: hmacNonce
configuration.api_key['hmacNonce'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacNonce'] = 'Bearer'

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: hmacContentSha256
configuration.api_key['hmacContentSha256'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacContentSha256'] = 'Bearer'

# Configure API key authorization: hmacTimestamp
configuration.api_key['hmacTimestamp'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacTimestamp'] = 'Bearer'

# Configure API key authorization: hmacKeyId
configuration.api_key['hmacKeyId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacKeyId'] = 'Bearer'

# Configure API key authorization: hmacSignature
configuration.api_key['hmacSignature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacSignature'] = 'Bearer'

# Enter a context with an instance of the API client
with fwallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fwallet.DeveloperApi(api_client)
    developer_post_developer_apps_request = fwallet.DeveloperPostDeveloperAppsRequest() # DeveloperPostDeveloperAppsRequest |  (optional)

    try:
        # Create Developer
        api_response = api_instance.developer_post_developer_apps(developer_post_developer_apps_request=developer_post_developer_apps_request)
        print("The response of DeveloperApi->developer_post_developer_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_post_developer_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **developer_post_developer_apps_request** | [**DeveloperPostDeveloperAppsRequest**](DeveloperPostDeveloperAppsRequest.md)|  | [optional] 

### Return type

[**DeveloperApplication**](DeveloperApplication.md)

### Authorization

[hmacNonce](../README.md#hmacNonce), [apiKey](../README.md#apiKey), [hmacContentSha256](../README.md#hmacContentSha256), [hmacTimestamp](../README.md#hmacTimestamp), [hmacKeyId](../README.md#hmacKeyId), [hmacSignature](../README.md#hmacSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Developer application created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

