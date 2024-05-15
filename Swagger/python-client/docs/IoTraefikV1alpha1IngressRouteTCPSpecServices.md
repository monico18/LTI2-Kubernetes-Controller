# IoTraefikV1alpha1IngressRouteTCPSpecServices

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name defines the name of the referenced Kubernetes Service. | 
**namespace** | **str** | Namespace defines the namespace of the referenced Kubernetes Service. | [optional] 
**native_lb** | **bool** | NativeLB controls, when creating the load-balancer, whether the LB&#39;s children are directly the pods IPs or if the only child is the Kubernetes Service clusterIP. The Kubernetes Service itself does load-balance to the pods. By default, NativeLB is false. | [optional] 
**port** | **object** | Port defines the port of a Kubernetes Service. This can be a reference to a named port. | 
**proxy_protocol** | [**IoTraefikV1alpha1IngressRouteTCPSpecProxyProtocol**](IoTraefikV1alpha1IngressRouteTCPSpecProxyProtocol.md) |  | [optional] 
**termination_delay** | **int** | TerminationDelay defines the deadline that the proxy sets, after one of its connected peers indicates it has closed the writing capability of its connection, to close the reading capability as well, hence fully terminating the connection. It is a duration in milliseconds, defaulting to 100. A negative value means an infinite deadline (i.e. the reading capability is never closed). | [optional] 
**weight** | **int** | Weight defines the weight used when balancing requests between multiple Kubernetes Service. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


