# IoTraefikV1alpha1IngressRouteSpecRoutes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Kind defines the kind of the route. Rule is the only supported kind. | 
**match** | **str** | Match defines the router&#39;s rule. More info: https://doc.traefik.io/traefik/v2.10/routing/routers/#rule | 
**middlewares** | [**list[IoTraefikV1alpha1IngressRouteSpecMiddlewares]**](IoTraefikV1alpha1IngressRouteSpecMiddlewares.md) | Middlewares defines the list of references to Middleware resources. More info: https://doc.traefik.io/traefik/v2.10/routing/providers/kubernetes-crd/#kind-middleware | [optional] 
**priority** | **int** | Priority defines the router&#39;s priority. More info: https://doc.traefik.io/traefik/v2.10/routing/routers/#priority | [optional] 
**services** | [**list[IoTraefikV1alpha1IngressRouteSpecServices]**](IoTraefikV1alpha1IngressRouteSpecServices.md) | Services defines the list of Service. It can contain any combination of TraefikService and/or reference to a Kubernetes Service. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


