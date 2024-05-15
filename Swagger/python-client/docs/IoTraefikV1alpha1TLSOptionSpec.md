# IoTraefikV1alpha1TLSOptionSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alpn_protocols** | **list[str]** | ALPNProtocols defines the list of supported application level protocols for the TLS handshake, in order of preference. More info: https://doc.traefik.io/traefik/v2.10/https/tls/#alpn-protocols | [optional] 
**cipher_suites** | **list[str]** | CipherSuites defines the list of supported cipher suites for TLS versions up to TLS 1.2. More info: https://doc.traefik.io/traefik/v2.10/https/tls/#cipher-suites | [optional] 
**client_auth** | [**IoTraefikV1alpha1TLSOptionSpecClientAuth**](IoTraefikV1alpha1TLSOptionSpecClientAuth.md) |  | [optional] 
**curve_preferences** | **list[str]** | CurvePreferences defines the preferred elliptic curves in a specific order. More info: https://doc.traefik.io/traefik/v2.10/https/tls/#curve-preferences | [optional] 
**max_version** | **str** | MaxVersion defines the maximum TLS version that Traefik will accept. Possible values: VersionTLS10, VersionTLS11, VersionTLS12, VersionTLS13. Default: None. | [optional] 
**min_version** | **str** | MinVersion defines the minimum TLS version that Traefik will accept. Possible values: VersionTLS10, VersionTLS11, VersionTLS12, VersionTLS13. Default: VersionTLS10. | [optional] 
**prefer_server_cipher_suites** | **bool** | PreferServerCipherSuites defines whether the server chooses a cipher suite among his own instead of among the client&#39;s. It is enabled automatically when minVersion or maxVersion is set. Deprecated: https://github.com/golang/go/issues/45430 | [optional] 
**sni_strict** | **bool** | SniStrict defines whether Traefik allows connections from clients connections that do not specify a server_name extension. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


