# IoTraefikV1alpha1MiddlewareSpecInFlightReqSourceCriterionIpStrategy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**depth** | **int** | Depth tells Traefik to use the X-Forwarded-For header and take the IP located at the depth position (starting from the right). | [optional] 
**excluded_ips** | **list[str]** | ExcludedIPs configures Traefik to scan the X-Forwarded-For header and select the first IP not in the list. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


