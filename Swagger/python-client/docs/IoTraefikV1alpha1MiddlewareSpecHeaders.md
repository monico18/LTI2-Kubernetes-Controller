# IoTraefikV1alpha1MiddlewareSpecHeaders

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_control_allow_credentials** | **bool** | AccessControlAllowCredentials defines whether the request can include user credentials. | [optional] 
**access_control_allow_headers** | **list[str]** | AccessControlAllowHeaders defines the Access-Control-Request-Headers values sent in preflight response. | [optional] 
**access_control_allow_methods** | **list[str]** | AccessControlAllowMethods defines the Access-Control-Request-Method values sent in preflight response. | [optional] 
**access_control_allow_origin_list** | **list[str]** | AccessControlAllowOriginList is a list of allowable origins. Can also be a wildcard origin \&quot;*\&quot;. | [optional] 
**access_control_allow_origin_list_regex** | **list[str]** | AccessControlAllowOriginListRegex is a list of allowable origins written following the Regular Expression syntax (https://golang.org/pkg/regexp/). | [optional] 
**access_control_expose_headers** | **list[str]** | AccessControlExposeHeaders defines the Access-Control-Expose-Headers values sent in preflight response. | [optional] 
**access_control_max_age** | **int** | AccessControlMaxAge defines the time that a preflight request may be cached. | [optional] 
**add_vary_header** | **bool** | AddVaryHeader defines whether the Vary header is automatically added/updated when the AccessControlAllowOriginList is set. | [optional] 
**allowed_hosts** | **list[str]** | AllowedHosts defines the fully qualified list of allowed domain names. | [optional] 
**browser_xss_filter** | **bool** | BrowserXSSFilter defines whether to add the X-XSS-Protection header with the value 1; mode&#x3D;block. | [optional] 
**content_security_policy** | **str** | ContentSecurityPolicy defines the Content-Security-Policy header value. | [optional] 
**content_type_nosniff** | **bool** | ContentTypeNosniff defines whether to add the X-Content-Type-Options header with the nosniff value. | [optional] 
**custom_browser_xss_value** | **str** | CustomBrowserXSSValue defines the X-XSS-Protection header value. This overrides the BrowserXssFilter option. | [optional] 
**custom_frame_options_value** | **str** | CustomFrameOptionsValue defines the X-Frame-Options header value. This overrides the FrameDeny option. | [optional] 
**custom_request_headers** | **dict(str, str)** | CustomRequestHeaders defines the header names and values to apply to the request. | [optional] 
**custom_response_headers** | **dict(str, str)** | CustomResponseHeaders defines the header names and values to apply to the response. | [optional] 
**feature_policy** | **str** | Deprecated: use PermissionsPolicy instead. | [optional] 
**force_sts_header** | **bool** | ForceSTSHeader defines whether to add the STS header even when the connection is HTTP. | [optional] 
**frame_deny** | **bool** | FrameDeny defines whether to add the X-Frame-Options header with the DENY value. | [optional] 
**hosts_proxy_headers** | **list[str]** | HostsProxyHeaders defines the header keys that may hold a proxied hostname value for the request. | [optional] 
**is_development** | **bool** | IsDevelopment defines whether to mitigate the unwanted effects of the AllowedHosts, SSL, and STS options when developing. Usually testing takes place using HTTP, not HTTPS, and on localhost, not your production domain. If you would like your development environment to mimic production with complete Host blocking, SSL redirects, and STS headers, leave this as false. | [optional] 
**permissions_policy** | **str** | PermissionsPolicy defines the Permissions-Policy header value. This allows sites to control browser features. | [optional] 
**public_key** | **str** | PublicKey is the public key that implements HPKP to prevent MITM attacks with forged certificates. | [optional] 
**referrer_policy** | **str** | ReferrerPolicy defines the Referrer-Policy header value. This allows sites to control whether browsers forward the Referer header to other sites. | [optional] 
**ssl_force_host** | **bool** | Deprecated: use RedirectRegex instead. | [optional] 
**ssl_host** | **str** | Deprecated: use RedirectRegex instead. | [optional] 
**ssl_proxy_headers** | **dict(str, str)** | SSLProxyHeaders defines the header keys with associated values that would indicate a valid HTTPS request. It can be useful when using other proxies (example: \&quot;X-Forwarded-Proto\&quot;: \&quot;https\&quot;). | [optional] 
**ssl_redirect** | **bool** | Deprecated: use EntryPoint redirection or RedirectScheme instead. | [optional] 
**ssl_temporary_redirect** | **bool** | Deprecated: use EntryPoint redirection or RedirectScheme instead. | [optional] 
**sts_include_subdomains** | **bool** | STSIncludeSubdomains defines whether the includeSubDomains directive is appended to the Strict-Transport-Security header. | [optional] 
**sts_preload** | **bool** | STSPreload defines whether the preload flag is appended to the Strict-Transport-Security header. | [optional] 
**sts_seconds** | **int** | STSSeconds defines the max-age of the Strict-Transport-Security header. If set to 0, the header is not set. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


