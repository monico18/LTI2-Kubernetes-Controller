# IoTraefikV1alpha1ServersTransportTCPSpecTls

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificates_secrets** | **list[str]** | CertificatesSecrets defines a list of secret storing client certificates for mTLS. | [optional] 
**insecure_skip_verify** | **bool** | InsecureSkipVerify disables TLS certificate verification. | [optional] 
**peer_cert_uri** | **str** | MaxIdleConnsPerHost controls the maximum idle (keep-alive) to keep per-host. PeerCertURI defines the peer cert URI used to match against SAN URI during the peer certificate verification. | [optional] 
**root_cas_secrets** | **list[str]** | RootCAsSecrets defines a list of CA secret used to validate self-signed certificates. | [optional] 
**server_name** | **str** | ServerName defines the server name used to contact the server. | [optional] 
**spiffe** | [**IoTraefikV1alpha1ServersTransportTCPSpecTlsSpiffe**](IoTraefikV1alpha1ServersTransportTCPSpecTlsSpiffe.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


