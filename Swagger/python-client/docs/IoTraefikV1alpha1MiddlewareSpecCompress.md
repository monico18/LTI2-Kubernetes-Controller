# IoTraefikV1alpha1MiddlewareSpecCompress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_content_types** | **list[str]** | ExcludedContentTypes defines the list of content types to compare the Content-Type header of the incoming requests and responses before compressing. | [optional] 
**min_response_body_bytes** | **int** | MinResponseBodyBytes defines the minimum amount of bytes a response body must have to be compressed. Default: 1024. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


