# IoTraefikV1alpha1ServersTransportSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificates_secrets** | **list[str]** | CertificatesSecrets defines a list of secret storing client certificates for mTLS. | [optional] 
**disable_http2** | **bool** | DisableHTTP2 disables HTTP/2 for connections with backend servers. | [optional] 
**forwarding_timeouts** | [**IoTraefikV1alpha1ServersTransportSpecForwardingTimeouts**](IoTraefikV1alpha1ServersTransportSpecForwardingTimeouts.md) |  | [optional] 
**insecure_skip_verify** | **bool** | InsecureSkipVerify disables SSL certificate verification. | [optional] 
**max_idle_conns_per_host** | **int** | MaxIdleConnsPerHost controls the maximum idle (keep-alive) to keep per-host. | [optional] 
**peer_cert_uri** | **str** | PeerCertURI defines the peer cert URI used to match against SAN URI during the peer certificate verification. | [optional] 
**root_cas_secrets** | **list[str]** | RootCAsSecrets defines a list of CA secret used to validate self-signed certificate. | [optional] 
**server_name** | **str** | ServerName defines the server name used to contact the server. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


