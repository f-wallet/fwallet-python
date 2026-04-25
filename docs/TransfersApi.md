# fwallet.TransfersApi

All URIs are relative to *https://api.fwallet.co.ug*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transfers_post_transfers**](TransfersApi.md#transfers_post_transfers) | **POST** /v1/transfers | Create Transfers
[**transfers_post_transfers_simulate_fee**](TransfersApi.md#transfers_post_transfers_simulate_fee) | **POST** /v1/transfers/simulate-fee | Create Transfers


# **transfers_post_transfers**
> TransfersPostTransfers200Response transfers_post_transfers(idempotency_key, transfers_post_transfers_request=transfers_post_transfers_request)

Create Transfers

### Example

* Api Key Authentication (hmacNonce):
* Api Key Authentication (apiKey):
* Api Key Authentication (hmacContentSha256):
* Api Key Authentication (hmacTimestamp):
* Api Key Authentication (hmacKeyId):
* Api Key Authentication (hmacSignature):

```python
import fwallet
from fwallet.models.transfers_post_transfers200_response import TransfersPostTransfers200Response
from fwallet.models.transfers_post_transfers_request import TransfersPostTransfersRequest
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
    api_instance = fwallet.TransfersApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key for idempotent financial writes. Reusing the same key with the same request returns the original result.
    transfers_post_transfers_request = fwallet.TransfersPostTransfersRequest() # TransfersPostTransfersRequest |  (optional)

    try:
        # Create Transfers
        api_response = api_instance.transfers_post_transfers(idempotency_key, transfers_post_transfers_request=transfers_post_transfers_request)
        print("The response of TransfersApi->transfers_post_transfers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->transfers_post_transfers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key for idempotent financial writes. Reusing the same key with the same request returns the original result. | 
 **transfers_post_transfers_request** | [**TransfersPostTransfersRequest**](TransfersPostTransfersRequest.md)|  | [optional] 

### Return type

[**TransfersPostTransfers200Response**](TransfersPostTransfers200Response.md)

### Authorization

[hmacNonce](../README.md#hmacNonce), [apiKey](../README.md#apiKey), [hmacContentSha256](../README.md#hmacContentSha256), [hmacTimestamp](../README.md#hmacTimestamp), [hmacKeyId](../README.md#hmacKeyId), [hmacSignature](../README.md#hmacSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transfer executed (or replayed if idempotent) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfers_post_transfers_simulate_fee**
> TransfersPostTransfersSimulateFee200Response transfers_post_transfers_simulate_fee(idempotency_key, transfers_post_transfers_simulate_fee_request=transfers_post_transfers_simulate_fee_request)

Create Transfers

### Example

* Api Key Authentication (hmacNonce):
* Api Key Authentication (apiKey):
* Api Key Authentication (hmacContentSha256):
* Api Key Authentication (hmacTimestamp):
* Api Key Authentication (hmacKeyId):
* Api Key Authentication (hmacSignature):

```python
import fwallet
from fwallet.models.transfers_post_transfers_simulate_fee200_response import TransfersPostTransfersSimulateFee200Response
from fwallet.models.transfers_post_transfers_simulate_fee_request import TransfersPostTransfersSimulateFeeRequest
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
    api_instance = fwallet.TransfersApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Required for financial writes. Reusing the same key with the same request returns the original result; reusing it with a different body returns an idempotency conflict.
    transfers_post_transfers_simulate_fee_request = fwallet.TransfersPostTransfersSimulateFeeRequest() # TransfersPostTransfersSimulateFeeRequest |  (optional)

    try:
        # Create Transfers
        api_response = api_instance.transfers_post_transfers_simulate_fee(idempotency_key, transfers_post_transfers_simulate_fee_request=transfers_post_transfers_simulate_fee_request)
        print("The response of TransfersApi->transfers_post_transfers_simulate_fee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->transfers_post_transfers_simulate_fee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Required for financial writes. Reusing the same key with the same request returns the original result; reusing it with a different body returns an idempotency conflict. | 
 **transfers_post_transfers_simulate_fee_request** | [**TransfersPostTransfersSimulateFeeRequest**](TransfersPostTransfersSimulateFeeRequest.md)|  | [optional] 

### Return type

[**TransfersPostTransfersSimulateFee200Response**](TransfersPostTransfersSimulateFee200Response.md)

### Authorization

[hmacNonce](../README.md#hmacNonce), [apiKey](../README.md#apiKey), [hmacContentSha256](../README.md#hmacContentSha256), [hmacTimestamp](../README.md#hmacTimestamp), [hmacKeyId](../README.md#hmacKeyId), [hmacSignature](../README.md#hmacSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fee simulation result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

