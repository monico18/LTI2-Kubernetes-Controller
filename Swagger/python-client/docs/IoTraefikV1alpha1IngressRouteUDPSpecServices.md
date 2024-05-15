# IoTraefikV1alpha1IngressRouteUDPSpecServices

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name defines the name of the referenced Kubernetes Service. | 
**namespace** | **str** | Namespace defines the namespace of the referenced Kubernetes Service. | [optional] 
**native_lb** | **bool** | NativeLB controls, when creating the load-balancer, whether the LB&#39;s children are directly the pods IPs or if the only child is the Kubernetes Service clusterIP. The Kubernetes Service itself does load-balance to the pods. By default, NativeLB is false. | [optional] 
**port** | **object** | Port defines the port of a Kubernetes Service. This can be a reference to a named port. | 
**weight** | **int** | Weight defines the weight used when balancing requests between multiple Kubernetes Service. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


