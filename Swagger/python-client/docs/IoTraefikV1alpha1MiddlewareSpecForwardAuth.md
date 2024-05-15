# IoTraefikV1alpha1MiddlewareSpecForwardAuth

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address defines the authentication server address. | [optional] 
**auth_request_headers** | **list[str]** | AuthRequestHeaders defines the list of the headers to copy from the request to the authentication server. If not set or empty then all request headers are passed. | [optional] 
**auth_response_headers** | **list[str]** | AuthResponseHeaders defines the list of headers to copy from the authentication server response and set on forwarded request, replacing any existing conflicting headers. | [optional] 
**auth_response_headers_regex** | **str** | AuthResponseHeadersRegex defines the regex to match headers to copy from the authentication server response and set on forwarded request, after stripping all headers that match the regex. More info: https://doc.traefik.io/traefik/v2.10/middlewares/http/forwardauth/#authresponseheadersregex | [optional] 
**tls** | [**IoTraefikV1alpha1MiddlewareSpecForwardAuthTls**](IoTraefikV1alpha1MiddlewareSpecForwardAuthTls.md) |  | [optional] 
**trust_forward_header** | **bool** | TrustForwardHeader defines whether to trust (ie: forward) all X-Forwarded-* headers. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


