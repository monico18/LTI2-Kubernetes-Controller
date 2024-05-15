# IoTraefikV1alpha1MiddlewareSpecInFlightReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Amount defines the maximum amount of allowed simultaneous in-flight request. The middleware responds with HTTP 429 Too Many Requests if there are already amount requests in progress (based on the same sourceCriterion strategy). | [optional] 
**source_criterion** | [**IoTraefikV1alpha1MiddlewareSpecInFlightReqSourceCriterion**](IoTraefikV1alpha1MiddlewareSpecInFlightReqSourceCriterion.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


