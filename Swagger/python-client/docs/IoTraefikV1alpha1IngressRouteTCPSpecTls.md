# IoTraefikV1alpha1IngressRouteTCPSpecTls

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_resolver** | **str** | CertResolver defines the name of the certificate resolver to use. Cert resolvers have to be configured in the static configuration. More info: https://doc.traefik.io/traefik/v2.10/https/acme/#certificate-resolvers | [optional] 
**domains** | [**list[IoTraefikV1alpha1IngressRouteSpecTlsDomains]**](IoTraefikV1alpha1IngressRouteSpecTlsDomains.md) | Domains defines the list of domains that will be used to issue certificates. More info: https://doc.traefik.io/traefik/v2.10/routing/routers/#domains | [optional] 
**options** | [**IoTraefikV1alpha1IngressRouteTCPSpecTlsOptions**](IoTraefikV1alpha1IngressRouteTCPSpecTlsOptions.md) |  | [optional] 
**passthrough** | **bool** | Passthrough defines whether a TLS router will terminate the TLS connection. | [optional] 
**secret_name** | **str** | SecretName is the name of the referenced Kubernetes Secret to specify the certificate details. | [optional] 
**store** | [**IoTraefikV1alpha1IngressRouteTCPSpecTlsStore**](IoTraefikV1alpha1IngressRouteTCPSpecTlsStore.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


