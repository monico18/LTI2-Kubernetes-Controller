# IoTraefikV1alpha1MiddlewareSpecForwardAuthTls

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_optional** | **bool** |  | [optional] 
**ca_secret** | **str** | CASecret is the name of the referenced Kubernetes Secret containing the CA to validate the server certificate. The CA certificate is extracted from key &#x60;tls.ca&#x60; or &#x60;ca.crt&#x60;. | [optional] 
**cert_secret** | **str** | CertSecret is the name of the referenced Kubernetes Secret containing the client certificate. The client certificate is extracted from the keys &#x60;tls.crt&#x60; and &#x60;tls.key&#x60;. | [optional] 
**insecure_skip_verify** | **bool** | InsecureSkipVerify defines whether the server certificates should be validated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


