# fwallet.TeamApi

All URIs are relative to *https://api.fwallet.co.ug*

Method | HTTP request | Description
------------- | ------------- | -------------
[**team_get_team**](TeamApi.md#team_get_team) | **GET** /v1/team | Get Team
[**team_post_team**](TeamApi.md#team_post_team) | **POST** /v1/team | Create Team


# **team_get_team**
> TeamGetTeam200Response team_get_team()

Get Team

List all users in the authenticated tenant.

### Example

* Api Key Authentication (hmacNonce):
* Api Key Authentication (apiKey):
* Api Key Authentication (hmacContentSha256):
* Api Key Authentication (hmacTimestamp):
* Api Key Authentication (hmacKeyId):
* Api Key Authentication (hmacSignature):

```python
import fwallet
from fwallet.models.team_get_team200_response import TeamGetTeam200Response
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
    api_instance = fwallet.TeamApi(api_client)

    try:
        # Get Team
        api_response = api_instance.team_get_team()
        print("The response of TeamApi->team_get_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->team_get_team: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TeamGetTeam200Response**](TeamGetTeam200Response.md)

### Authorization

[hmacNonce](../README.md#hmacNonce), [apiKey](../README.md#apiKey), [hmacContentSha256](../README.md#hmacContentSha256), [hmacTimestamp](../README.md#hmacTimestamp), [hmacKeyId](../README.md#hmacKeyId), [hmacSignature](../README.md#hmacSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of team members |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_post_team**
> TeamPostTeam201Response team_post_team(team_post_team_request=team_post_team_request)

Create Team

Create a new user in the tenant with a specific role.

### Example

* Api Key Authentication (hmacNonce):
* Api Key Authentication (apiKey):
* Api Key Authentication (hmacContentSha256):
* Api Key Authentication (hmacTimestamp):
* Api Key Authentication (hmacKeyId):
* Api Key Authentication (hmacSignature):

```python
import fwallet
from fwallet.models.team_post_team201_response import TeamPostTeam201Response
from fwallet.models.team_post_team_request import TeamPostTeamRequest
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
    api_instance = fwallet.TeamApi(api_client)
    team_post_team_request = fwallet.TeamPostTeamRequest() # TeamPostTeamRequest |  (optional)

    try:
        # Create Team
        api_response = api_instance.team_post_team(team_post_team_request=team_post_team_request)
        print("The response of TeamApi->team_post_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->team_post_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_post_team_request** | [**TeamPostTeamRequest**](TeamPostTeamRequest.md)|  | [optional] 

### Return type

[**TeamPostTeam201Response**](TeamPostTeam201Response.md)

### Authorization

[hmacNonce](../README.md#hmacNonce), [apiKey](../README.md#apiKey), [hmacContentSha256](../README.md#hmacContentSha256), [hmacTimestamp](../README.md#hmacTimestamp), [hmacKeyId](../README.md#hmacKeyId), [hmacSignature](../README.md#hmacSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Team member created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

