# IoTraefikV1alpha1ServersTransportTCPSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dial_keep_alive** | **object** | DialKeepAlive is the interval between keep-alive probes for an active network connection. If zero, keep-alive probes are sent with a default value (currently 15 seconds), if supported by the protocol and operating system. Network protocols or operating systems that do not support keep-alives ignore this field. If negative, keep-alive probes are disabled. | [optional] 
**dial_timeout** | **object** | DialTimeout is the amount of time to wait until a connection to a backend server can be established. | [optional] 
**termination_delay** | **object** | TerminationDelay defines the delay to wait before fully terminating the connection, after one connected peer has closed its writing capability. | [optional] 
**tls** | [**IoTraefikV1alpha1ServersTransportTCPSpecTls**](IoTraefikV1alpha1ServersTransportTCPSpecTls.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


