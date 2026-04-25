# fwallet.SystemApi

All URIs are relative to *https://api.fwallet.co.ug*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_get_system_organizations**](SystemApi.md#system_get_system_organizations) | **GET** /v1/system/organizations | Get System
[**system_get_system_overview**](SystemApi.md#system_get_system_overview) | **GET** /v1/system/overview | Get System
[**system_get_system_transactions**](SystemApi.md#system_get_system_transactions) | **GET** /v1/system/transactions | Get System
[**system_get_system_wallets**](SystemApi.md#system_get_system_wallets) | **GET** /v1/system/wallets | Get System
[**system_post_system_organizations**](SystemApi.md#system_post_system_organizations) | **POST** /v1/system/organizations | Create System


# **system_get_system_organizations**
> SystemGetSystemOrganizations200Response system_get_system_organizations()

Get System

### Example

* Api Key Authentication (systemKey):

```python
import fwallet
from fwallet.models.system_get_system_organizations200_response import SystemGetSystemOrganizations200Response
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

# Configure API key authorization: systemKey
configuration.api_key['systemKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['systemKey'] = 'Bearer'

# Enter a context with an instance of the API client
with fwallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fwallet.SystemApi(api_client)

    try:
        # Get System
        api_response = api_instance.system_get_system_organizations()
        print("The response of SystemApi->system_get_system_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->system_get_system_organizations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemGetSystemOrganizations200Response**](SystemGetSystemOrganizations200Response.md)

### Authorization

[systemKey](../README.md#systemKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All organizations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_get_system_overview**
> SystemGetSystemOverview200Response system_get_system_overview()

Get System

### Example

* Api Key Authentication (systemKey):

```python
import fwallet
from fwallet.models.system_get_system_overview200_response import SystemGetSystemOverview200Response
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

# Configure API key authorization: systemKey
configuration.api_key['systemKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['systemKey'] = 'Bearer'

# Enter a context with an instance of the API client
with fwallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fwallet.SystemApi(api_client)

    try:
        # Get System
        api_response = api_instance.system_get_system_overview()
        print("The response of SystemApi->system_get_system_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->system_get_system_overview: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemGetSystemOverview200Response**](SystemGetSystemOverview200Response.md)

### Authorization

[systemKey](../README.md#systemKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | System-wide overview across all organizations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_get_system_transactions**
> SystemGetSystemTransactions200Response system_get_system_transactions(limit=limit)

Get System

### Example

* Api Key Authentication (systemKey):

```python
import fwallet
from fwallet.models.system_get_system_transactions200_response import SystemGetSystemTransactions200Response
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

# Configure API key authorization: systemKey
configuration.api_key['systemKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['systemKey'] = 'Bearer'

# Enter a context with an instance of the API client
with fwallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fwallet.SystemApi(api_client)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # Get System
        api_response = api_instance.system_get_system_transactions(limit=limit)
        print("The response of SystemApi->system_get_system_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->system_get_system_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**SystemGetSystemTransactions200Response**](SystemGetSystemTransactions200Response.md)

### Authorization

[systemKey](../README.md#systemKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recent ledger transactions across all organizations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_get_system_wallets**
> SystemGetSystemWallets200Response system_get_system_wallets(limit=limit)

Get System

### Example

* Api Key Authentication (systemKey):

```python
import fwallet
from fwallet.models.system_get_system_wallets200_response import SystemGetSystemWallets200Response
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

# Configure API key authorization: systemKey
configuration.api_key['systemKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['systemKey'] = 'Bearer'

# Enter a context with an instance of the API client
with fwallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fwallet.SystemApi(api_client)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # Get System
        api_response = api_instance.system_get_system_wallets(limit=limit)
        print("The response of SystemApi->system_get_system_wallets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->system_get_system_wallets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**SystemGetSystemWallets200Response**](SystemGetSystemWallets200Response.md)

### Authorization

[systemKey](../README.md#systemKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recent wallets across all organizations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_post_system_organizations**
> SystemPostSystemOrganizations201Response system_post_system_organizations(system_post_system_organizations_request=system_post_system_organizations_request)

Create System

### Example

* Api Key Authentication (systemKey):

```python
import fwallet
from fwallet.models.system_post_system_organizations201_response import SystemPostSystemOrganizations201Response
from fwallet.models.system_post_system_organizations_request import SystemPostSystemOrganizationsRequest
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

# Configure API key authorization: systemKey
configuration.api_key['systemKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['systemKey'] = 'Bearer'

# Enter a context with an instance of the API client
with fwallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fwallet.SystemApi(api_client)
    system_post_system_organizations_request = fwallet.SystemPostSystemOrganizationsRequest() # SystemPostSystemOrganizationsRequest |  (optional)

    try:
        # Create System
        api_response = api_instance.system_post_system_organizations(system_post_system_organizations_request=system_post_system_organizations_request)
        print("The response of SystemApi->system_post_system_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->system_post_system_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_post_system_organizations_request** | [**SystemPostSystemOrganizationsRequest**](SystemPostSystemOrganizationsRequest.md)|  | [optional] 

### Return type

[**SystemPostSystemOrganizations201Response**](SystemPostSystemOrganizations201Response.md)

### Authorization

[systemKey](../README.md#systemKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Organization created and tenant admin invited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

