# IoTraefikV1alpha1TraefikServiceSpecMirroring

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Kind defines the kind of the Service. | [optional] 
**max_body_size** | **int** | MaxBodySize defines the maximum size allowed for the body of the request. If the body is larger, the request is not mirrored. Default value is -1, which means unlimited size. | [optional] 
**mirrors** | [**list[IoTraefikV1alpha1TraefikServiceSpecMirroringMirrors]**](IoTraefikV1alpha1TraefikServiceSpecMirroringMirrors.md) | Mirrors defines the list of mirrors where Traefik will duplicate the traffic. | [optional] 
**name** | **str** | Name defines the name of the referenced Kubernetes Service or TraefikService. The differentiation between the two is specified in the Kind field. | 
**namespace** | **str** | Namespace defines the namespace of the referenced Kubernetes Service or TraefikService. | [optional] 
**native_lb** | **bool** | NativeLB controls, when creating the load-balancer, whether the LB&#39;s children are directly the pods IPs or if the only child is the Kubernetes Service clusterIP. The Kubernetes Service itself does load-balance to the pods. By default, NativeLB is false. | [optional] 
**pass_host_header** | **bool** | PassHostHeader defines whether the client Host header is forwarded to the upstream Kubernetes Service. By default, passHostHeader is true. | [optional] 
**port** | **object** | Port defines the port of a Kubernetes Service. This can be a reference to a named port. | [optional] 
**response_forwarding** | [**IoTraefikV1alpha1IngressRouteSpecResponseForwarding**](IoTraefikV1alpha1IngressRouteSpecResponseForwarding.md) |  | [optional] 
**scheme** | **str** | Scheme defines the scheme to use for the request to the upstream Kubernetes Service. It defaults to https when Kubernetes Service port is 443, http otherwise. | [optional] 
**servers_transport** | **str** | ServersTransport defines the name of ServersTransport resource to use. It allows to configure the transport between Traefik and your servers. Can only be used on a Kubernetes Service. | [optional] 
**sticky** | [**IoTraefikV1alpha1IngressRouteSpecSticky**](IoTraefikV1alpha1IngressRouteSpecSticky.md) |  | [optional] 
**strategy** | **str** | Strategy defines the load balancing strategy between the servers. RoundRobin is the only supported value at the moment. | [optional] 
**weight** | **int** | Weight defines the weight and should only be specified when Name references a TraefikService object (and to be precise, one that embeds a Weighted Round Robin). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


