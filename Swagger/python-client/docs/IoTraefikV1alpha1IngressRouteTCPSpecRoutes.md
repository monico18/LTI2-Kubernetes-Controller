# IoTraefikV1alpha1IngressRouteTCPSpecRoutes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match** | **str** | Match defines the router&#39;s rule. More info: https://doc.traefik.io/traefik/v2.10/routing/routers/#rule_1 | 
**middlewares** | [**list[IoTraefikV1alpha1IngressRouteTCPSpecMiddlewares]**](IoTraefikV1alpha1IngressRouteTCPSpecMiddlewares.md) | Middlewares defines the list of references to MiddlewareTCP resources. | [optional] 
**priority** | **int** | Priority defines the router&#39;s priority. More info: https://doc.traefik.io/traefik/v2.10/routing/routers/#priority_1 | [optional] 
**services** | [**list[IoTraefikV1alpha1IngressRouteTCPSpecServices]**](IoTraefikV1alpha1IngressRouteTCPSpecServices.md) | Services defines the list of TCP services. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


