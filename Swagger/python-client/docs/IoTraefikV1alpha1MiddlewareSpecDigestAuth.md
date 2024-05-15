# IoTraefikV1alpha1MiddlewareSpecDigestAuth

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header_field** | **str** | HeaderField defines a header field to store the authenticated user. More info: https://doc.traefik.io/traefik/v2.10/middlewares/http/basicauth/#headerfield | [optional] 
**realm** | **str** | Realm allows the protected resources on a server to be partitioned into a set of protection spaces, each with its own authentication scheme. Default: traefik. | [optional] 
**remove_header** | **bool** | RemoveHeader defines whether to remove the authorization header before forwarding the request to the backend. | [optional] 
**secret** | **str** | Secret is the name of the referenced Kubernetes Secret containing user credentials. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


