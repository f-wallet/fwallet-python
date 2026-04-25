# fwallet.TenantsApi

All URIs are relative to *https://api.fwallet.co.ug*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenants_get_tenants_by_id**](TenantsApi.md#tenants_get_tenants_by_id) | **GET** /v1/tenants/{id} | Get Tenants
[**tenants_post_tenants**](TenantsApi.md#tenants_post_tenants) | **POST** /v1/tenants | Create Tenants
[**tenants_post_tenants_by_id_api_keys**](TenantsApi.md#tenants_post_tenants_by_id_api_keys) | **POST** /v1/tenants/{id}/api-keys | Create Tenants


# **tenants_get_tenants_by_id**
> TenantsPostTenants201Response tenants_get_tenants_by_id(id)

Get Tenants

### Example


```python
import fwallet
from fwallet.models.tenants_post_tenants201_response import TenantsPostTenants201Response
from fwallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fwallet.co.ug
# See configuration.py for a list of all supported configuration parameters.
configuration = fwallet.Configuration(
    host = "https://api.fwallet.co.ug"
)


# Enter a context with an instance of the API client
with fwallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fwallet.TenantsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Tenants
        api_response = api_instance.tenants_get_tenants_by_id(id)
        print("The response of TenantsApi->tenants_get_tenants_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->tenants_get_tenants_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

### Return type

[**TenantsPostTenants201Response**](TenantsPostTenants201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tenant details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_post_tenants**
> TenantsPostTenants201Response tenants_post_tenants(tenants_post_tenants_request=tenants_post_tenants_request)

Create Tenants

### Example


```python
import fwallet
from fwallet.models.tenants_post_tenants201_response import TenantsPostTenants201Response
from fwallet.models.tenants_post_tenants_request import TenantsPostTenantsRequest
from fwallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fwallet.co.ug
# See configuration.py for a list of all supported configuration parameters.
configuration = fwallet.Configuration(
    host = "https://api.fwallet.co.ug"
)


# Enter a context with an instance of the API client
with fwallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fwallet.TenantsApi(api_client)
    tenants_post_tenants_request = fwallet.TenantsPostTenantsRequest() # TenantsPostTenantsRequest |  (optional)

    try:
        # Create Tenants
        api_response = api_instance.tenants_post_tenants(tenants_post_tenants_request=tenants_post_tenants_request)
        print("The response of TenantsApi->tenants_post_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->tenants_post_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenants_post_tenants_request** | [**TenantsPostTenantsRequest**](TenantsPostTenantsRequest.md)|  | [optional] 

### Return type

[**TenantsPostTenants201Response**](TenantsPostTenants201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tenant created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_post_tenants_by_id_api_keys**
> TenantsPostTenantsByIdApiKeys201Response tenants_post_tenants_by_id_api_keys(id, tenants_post_tenants_by_id_api_keys_request=tenants_post_tenants_by_id_api_keys_request)

Create Tenants

### Example


```python
import fwallet
from fwallet.models.tenants_post_tenants_by_id_api_keys201_response import TenantsPostTenantsByIdApiKeys201Response
from fwallet.models.tenants_post_tenants_by_id_api_keys_request import TenantsPostTenantsByIdApiKeysRequest
from fwallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fwallet.co.ug
# See configuration.py for a list of all supported configuration parameters.
configuration = fwallet.Configuration(
    host = "https://api.fwallet.co.ug"
)


# Enter a context with an instance of the API client
with fwallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fwallet.TenantsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    tenants_post_tenants_by_id_api_keys_request = fwallet.TenantsPostTenantsByIdApiKeysRequest() # TenantsPostTenantsByIdApiKeysRequest |  (optional)

    try:
        # Create Tenants
        api_response = api_instance.tenants_post_tenants_by_id_api_keys(id, tenants_post_tenants_by_id_api_keys_request=tenants_post_tenants_by_id_api_keys_request)
        print("The response of TenantsApi->tenants_post_tenants_by_id_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->tenants_post_tenants_by_id_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 
 **tenants_post_tenants_by_id_api_keys_request** | [**TenantsPostTenantsByIdApiKeysRequest**](TenantsPostTenantsByIdApiKeysRequest.md)|  | [optional] 

### Return type

[**TenantsPostTenantsByIdApiKeys201Response**](TenantsPostTenantsByIdApiKeys201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | API key created. The key value is only shown once. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

