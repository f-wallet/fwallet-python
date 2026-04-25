# fwallet.HealthApi

All URIs are relative to *https://api.fwallet.co.ug*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_get_health**](HealthApi.md#health_get_health) | **GET** /v1/health | Get Health


# **health_get_health**
> HealthGetHealth200Response health_get_health()

Get Health

### Example


```python
import fwallet
from fwallet.models.health_get_health200_response import HealthGetHealth200Response
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
    api_instance = fwallet.HealthApi(api_client)

    try:
        # Get Health
        api_response = api_instance.health_get_health()
        print("The response of HealthApi->health_get_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->health_get_health: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthGetHealth200Response**](HealthGetHealth200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service is healthy |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

