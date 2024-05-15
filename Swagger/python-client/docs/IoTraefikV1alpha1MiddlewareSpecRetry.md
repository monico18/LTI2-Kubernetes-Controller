# IoTraefikV1alpha1MiddlewareSpecRetry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempts** | **int** | Attempts defines how many times the request should be retried. | [optional] 
**initial_interval** | **object** | InitialInterval defines the first wait time in the exponential backoff series. The maximum interval is calculated as twice the initialInterval. If unspecified, requests will be retried immediately. The value of initialInterval should be provided in seconds or as a valid duration format, see https://pkg.go.dev/time#ParseDuration. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


