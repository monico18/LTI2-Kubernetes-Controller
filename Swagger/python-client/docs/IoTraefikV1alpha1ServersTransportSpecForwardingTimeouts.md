# IoTraefikV1alpha1ServersTransportSpecForwardingTimeouts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dial_timeout** | **object** | DialTimeout is the amount of time to wait until a connection to a backend server can be established. | [optional] 
**idle_conn_timeout** | **object** | IdleConnTimeout is the maximum period for which an idle HTTP keep-alive connection will remain open before closing itself. | [optional] 
**ping_timeout** | **object** | PingTimeout is the timeout after which the HTTP/2 connection will be closed if a response to ping is not received. | [optional] 
**read_idle_timeout** | **object** | ReadIdleTimeout is the timeout after which a health check using ping frame will be carried out if no frame is received on the HTTP/2 connection. | [optional] 
**response_header_timeout** | **object** | ResponseHeaderTimeout is the amount of time to wait for a server&#39;s response headers after fully writing the request (including its body, if any). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


