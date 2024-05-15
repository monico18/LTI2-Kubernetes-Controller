# IoTraefikV1alpha1MiddlewareSpecRateLimit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average** | **int** | Average is the maximum rate, by default in requests/s, allowed for the given source. It defaults to 0, which means no rate limiting. The rate is actually defined by dividing Average by Period. So for a rate below 1req/s, one needs to define a Period larger than a second. | [optional] 
**burst** | **int** | Burst is the maximum number of requests allowed to arrive in the same arbitrarily small period of time. It defaults to 1. | [optional] 
**period** | **object** | Period, in combination with Average, defines the actual maximum rate, such as: r &#x3D; Average / Period. It defaults to a second. | [optional] 
**source_criterion** | [**IoTraefikV1alpha1MiddlewareSpecRateLimitSourceCriterion**](IoTraefikV1alpha1MiddlewareSpecRateLimitSourceCriterion.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


