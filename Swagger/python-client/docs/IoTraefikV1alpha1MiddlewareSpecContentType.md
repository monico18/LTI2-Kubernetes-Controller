# IoTraefikV1alpha1MiddlewareSpecContentType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_detect** | **bool** | AutoDetect specifies whether to let the &#x60;Content-Type&#x60; header, if it has not been set by the backend, be automatically set to a value derived from the contents of the response. As a proxy, the default behavior should be to leave the header alone, regardless of what the backend did with it. However, the historic default was to always auto-detect and set the header if it was nil, and it is going to be kept that way in order to support users currently relying on it. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


