# IoTraefikV1alpha1IngressRouteSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_points** | **list[str]** | EntryPoints defines the list of entry point names to bind to. Entry points have to be configured in the static configuration. More info: https://doc.traefik.io/traefik/v2.10/routing/entrypoints/ Default: all. | [optional] 
**routes** | [**list[IoTraefikV1alpha1IngressRouteSpecRoutes]**](IoTraefikV1alpha1IngressRouteSpecRoutes.md) | Routes defines the list of routes. | 
**tls** | [**IoTraefikV1alpha1IngressRouteSpecTls**](IoTraefikV1alpha1IngressRouteSpecTls.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


