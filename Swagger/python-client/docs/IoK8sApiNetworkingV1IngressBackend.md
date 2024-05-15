# IoK8sApiNetworkingV1IngressBackend

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**IoK8sApiCoreV1TypedLocalObjectReference**](IoK8sApiCoreV1TypedLocalObjectReference.md) | resource is an ObjectRef to another Kubernetes resource in the namespace of the Ingress object. If resource is specified, a service.Name and service.Port must not be specified. This is a mutually exclusive setting with \&quot;Service\&quot;. | [optional] 
**service** | [**IoK8sApiNetworkingV1IngressServiceBackend**](IoK8sApiNetworkingV1IngressServiceBackend.md) | service references a service as a backend. This is a mutually exclusive setting with \&quot;Resource\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


