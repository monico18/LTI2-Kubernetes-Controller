# IoTraefikV1alpha1MiddlewareSpecBuffering

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_request_body_bytes** | **int** | MaxRequestBodyBytes defines the maximum allowed body size for the request (in bytes). If the request exceeds the allowed size, it is not forwarded to the service, and the client gets a 413 (Request Entity Too Large) response. Default: 0 (no maximum). | [optional] 
**max_response_body_bytes** | **int** | MaxResponseBodyBytes defines the maximum allowed response size from the service (in bytes). If the response exceeds the allowed size, it is not forwarded to the client. The client gets a 500 (Internal Server Error) response instead. Default: 0 (no maximum). | [optional] 
**mem_request_body_bytes** | **int** | MemRequestBodyBytes defines the threshold (in bytes) from which the request will be buffered on disk instead of in memory. Default: 1048576 (1Mi). | [optional] 
**mem_response_body_bytes** | **int** | MemResponseBodyBytes defines the threshold (in bytes) from which the response will be buffered on disk instead of in memory. Default: 1048576 (1Mi). | [optional] 
**retry_expression** | **str** | RetryExpression defines the retry conditions. It is a logical combination of functions with operators AND (&amp;&amp;) and OR (||). More info: https://doc.traefik.io/traefik/v2.10/middlewares/http/buffering/#retryexpression | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


