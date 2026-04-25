# fwallet.PayoutsApi

All URIs are relative to *https://api.fwallet.co.ug*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payouts_get_payouts_cases**](PayoutsApi.md#payouts_get_payouts_cases) | **GET** /v1/payouts/cases | Get Payouts
[**payouts_post_payouts**](PayoutsApi.md#payouts_post_payouts) | **POST** /v1/payouts | Create Payouts
[**payouts_post_payouts_by_case_id_approve**](PayoutsApi.md#payouts_post_payouts_by_case_id_approve) | **POST** /v1/payouts/{caseId}/approve | Create Payouts
[**payouts_post_payouts_by_case_id_reject**](PayoutsApi.md#payouts_post_payouts_by_case_id_reject) | **POST** /v1/payouts/{caseId}/reject | Create Payouts


# **payouts_get_payouts_cases**
> PayoutsGetPayoutsCases200Response payouts_get_payouts_cases(status=status)

Get Payouts

List payout approval cases. Filter by status to see pending cases that need action, or historical approved/rejected cases.

### Example

* Api Key Authentication (hmacNonce):
* Api Key Authentication (apiKey):
* Api Key Authentication (hmacContentSha256):
* Api Key Authentication (hmacTimestamp):
* Api Key Authentication (hmacKeyId):
* Api Key Authentication (hmacSignature):

```python
import fwallet
from fwallet.models.payouts_get_payouts_cases200_response import PayoutsGetPayoutsCases200Response
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
    api_instance = fwallet.PayoutsApi(api_client)
    status = 'status_example' # str |  (optional)

    try:
        # Get Payouts
        api_response = api_instance.payouts_get_payouts_cases(status=status)
        print("The response of PayoutsApi->payouts_get_payouts_cases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->payouts_get_payouts_cases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] 

### Return type

[**PayoutsGetPayoutsCases200Response**](PayoutsGetPayoutsCases200Response.md)

### Authorization

[hmacNonce](../README.md#hmacNonce), [apiKey](../README.md#apiKey), [hmacContentSha256](../README.md#hmacContentSha256), [hmacTimestamp](../README.md#hmacTimestamp), [hmacKeyId](../README.md#hmacKeyId), [hmacSignature](../README.md#hmacSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of payout approval cases |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payouts_post_payouts**
> PayoutsPostPayouts200Response payouts_post_payouts(idempotency_key, payout_request=payout_request)

Create Payouts

Request a payout (withdrawal). This immediately places a hold on the user's wallet (available balance decreases, funds move to suspense) and creates an approval case. The payout is NOT settled until approved by a different person (maker-checker pattern). If rejected, the hold is reversed and the balance restored.

### Example

* Api Key Authentication (hmacNonce):
* Api Key Authentication (apiKey):
* Api Key Authentication (hmacContentSha256):
* Api Key Authentication (hmacTimestamp):
* Api Key Authentication (hmacKeyId):
* Api Key Authentication (hmacSignature):

```python
import fwallet
from fwallet.models.payout_request import PayoutRequest
from fwallet.models.payouts_post_payouts200_response import PayoutsPostPayouts200Response
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
    api_instance = fwallet.PayoutsApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key for idempotent financial writes. Reusing the same key with the same request returns the original result.
    payout_request = fwallet.PayoutRequest() # PayoutRequest |  (optional)

    try:
        # Create Payouts
        api_response = api_instance.payouts_post_payouts(idempotency_key, payout_request=payout_request)
        print("The response of PayoutsApi->payouts_post_payouts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->payouts_post_payouts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key for idempotent financial writes. Reusing the same key with the same request returns the original result. | 
 **payout_request** | [**PayoutRequest**](PayoutRequest.md)|  | [optional] 

### Return type

[**PayoutsPostPayouts200Response**](PayoutsPostPayouts200Response.md)

### Authorization

[hmacNonce](../README.md#hmacNonce), [apiKey](../README.md#apiKey), [hmacContentSha256](../README.md#hmacContentSha256), [hmacTimestamp](../README.md#hmacTimestamp), [hmacKeyId](../README.md#hmacKeyId), [hmacSignature](../README.md#hmacSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payout requested — funds held, awaiting approval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payouts_post_payouts_by_case_id_approve**
> PayoutSettlement payouts_post_payouts_by_case_id_approve(case_id, idempotency_key, payouts_post_payouts_by_case_id_approve_request=payouts_post_payouts_by_case_id_approve_request)

Create Payouts

Approve a pending payout. Settles the payout by moving funds from suspense to the payout-clearing account. The actorId must differ from the requestor (maker-checker). Returns MAKER_CHECKER_VIOLATION (422) if the same person tries to approve their own request.

### Example

* Api Key Authentication (hmacNonce):
* Api Key Authentication (apiKey):
* Api Key Authentication (hmacContentSha256):
* Api Key Authentication (hmacTimestamp):
* Api Key Authentication (hmacKeyId):
* Api Key Authentication (hmacSignature):

```python
import fwallet
from fwallet.models.payout_settlement import PayoutSettlement
from fwallet.models.payouts_post_payouts_by_case_id_approve_request import PayoutsPostPayoutsByCaseIdApproveRequest
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
    api_instance = fwallet.PayoutsApi(api_client)
    case_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str | Required for financial writes. Reusing the same key with the same request returns the original result; reusing it with a different body returns an idempotency conflict.
    payouts_post_payouts_by_case_id_approve_request = fwallet.PayoutsPostPayoutsByCaseIdApproveRequest() # PayoutsPostPayoutsByCaseIdApproveRequest |  (optional)

    try:
        # Create Payouts
        api_response = api_instance.payouts_post_payouts_by_case_id_approve(case_id, idempotency_key, payouts_post_payouts_by_case_id_approve_request=payouts_post_payouts_by_case_id_approve_request)
        print("The response of PayoutsApi->payouts_post_payouts_by_case_id_approve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->payouts_post_payouts_by_case_id_approve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **UUID**|  | 
 **idempotency_key** | **str**| Required for financial writes. Reusing the same key with the same request returns the original result; reusing it with a different body returns an idempotency conflict. | 
 **payouts_post_payouts_by_case_id_approve_request** | [**PayoutsPostPayoutsByCaseIdApproveRequest**](PayoutsPostPayoutsByCaseIdApproveRequest.md)|  | [optional] 

### Return type

[**PayoutSettlement**](PayoutSettlement.md)

### Authorization

[hmacNonce](../README.md#hmacNonce), [apiKey](../README.md#apiKey), [hmacContentSha256](../README.md#hmacContentSha256), [hmacTimestamp](../README.md#hmacTimestamp), [hmacKeyId](../README.md#hmacKeyId), [hmacSignature](../README.md#hmacSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payout approved and settled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payouts_post_payouts_by_case_id_reject**
> PayoutCancellation payouts_post_payouts_by_case_id_reject(case_id, idempotency_key, payouts_post_payouts_by_case_id_reject_request=payouts_post_payouts_by_case_id_reject_request)

Create Payouts

Reject a pending payout. Reverses the balance hold by posting a reversing journal entry (funds move from suspense back to the user's wallet). The user's available balance is restored.

### Example

* Api Key Authentication (hmacNonce):
* Api Key Authentication (apiKey):
* Api Key Authentication (hmacContentSha256):
* Api Key Authentication (hmacTimestamp):
* Api Key Authentication (hmacKeyId):
* Api Key Authentication (hmacSignature):

```python
import fwallet
from fwallet.models.payout_cancellation import PayoutCancellation
from fwallet.models.payouts_post_payouts_by_case_id_reject_request import PayoutsPostPayoutsByCaseIdRejectRequest
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
    api_instance = fwallet.PayoutsApi(api_client)
    case_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str | Required for financial writes. Reusing the same key with the same request returns the original result; reusing it with a different body returns an idempotency conflict.
    payouts_post_payouts_by_case_id_reject_request = fwallet.PayoutsPostPayoutsByCaseIdRejectRequest() # PayoutsPostPayoutsByCaseIdRejectRequest |  (optional)

    try:
        # Create Payouts
        api_response = api_instance.payouts_post_payouts_by_case_id_reject(case_id, idempotency_key, payouts_post_payouts_by_case_id_reject_request=payouts_post_payouts_by_case_id_reject_request)
        print("The response of PayoutsApi->payouts_post_payouts_by_case_id_reject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->payouts_post_payouts_by_case_id_reject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **UUID**|  | 
 **idempotency_key** | **str**| Required for financial writes. Reusing the same key with the same request returns the original result; reusing it with a different body returns an idempotency conflict. | 
 **payouts_post_payouts_by_case_id_reject_request** | [**PayoutsPostPayoutsByCaseIdRejectRequest**](PayoutsPostPayoutsByCaseIdRejectRequest.md)|  | [optional] 

### Return type

[**PayoutCancellation**](PayoutCancellation.md)

### Authorization

[hmacNonce](../README.md#hmacNonce), [apiKey](../README.md#apiKey), [hmacContentSha256](../README.md#hmacContentSha256), [hmacTimestamp](../README.md#hmacTimestamp), [hmacKeyId](../README.md#hmacKeyId), [hmacSignature](../README.md#hmacSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payout rejected — hold reversed, balance restored |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

