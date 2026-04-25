# fwallet.AuthApi

All URIs are relative to *https://api.fwallet.co.ug*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_get_auth_me**](AuthApi.md#auth_get_auth_me) | **GET** /v1/auth/me | Get Auth


# **auth_get_auth_me**
> AuthGetAuthMe200Response auth_get_auth_me()

Get Auth

Get the current session's user info. Used by the dashboard to validate sessions via HTTP.

### Example


```python
import fwallet
from fwallet.models.auth_get_auth_me200_response import AuthGetAuthMe200Response
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
    api_instance = fwallet.AuthApi(api_client)

    try:
        # Get Auth
        api_response = api_instance.auth_get_auth_me()
        print("The response of AuthApi->auth_get_auth_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_get_auth_me: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthGetAuthMe200Response**](AuthGetAuthMe200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current user session |  -  |
**401** | No valid session |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

