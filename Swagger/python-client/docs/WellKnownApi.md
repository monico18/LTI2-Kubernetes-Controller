# swagger_client.WellKnownApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_account_issuer_open_id_configuration**](WellKnownApi.md#get_service_account_issuer_open_id_configuration) | **GET** /.well-known/openid-configuration/ | 


# **get_service_account_issuer_open_id_configuration**
> str get_service_account_issuer_open_id_configuration()



get service account issuer OpenID configuration, also known as the 'OIDC discovery doc'

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = swagger_client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WellKnownApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_service_account_issuer_open_id_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WellKnownApi->get_service_account_issuer_open_id_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

