# swagger_client.VersionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_code_version**](VersionApi.md#get_code_version) | **GET** /version/ | 


# **get_code_version**
> IoK8sApimachineryPkgVersionInfo get_code_version()



get the code version

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
api_instance = swagger_client.VersionApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_code_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionApi->get_code_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IoK8sApimachineryPkgVersionInfo**](IoK8sApimachineryPkgVersionInfo.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

