# IoTraefikV1alpha1MiddlewareSpecCircuitBreaker

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_period** | **object** | CheckPeriod is the interval between successive checks of the circuit breaker condition (when in standby state). | [optional] 
**expression** | **str** | Expression is the condition that triggers the tripped state. | [optional] 
**fallback_duration** | **object** | FallbackDuration is the duration for which the circuit breaker will wait before trying to recover (from a tripped state). | [optional] 
**recovery_duration** | **object** | RecoveryDuration is the duration for which the circuit breaker will try to recover (as soon as it is in recovering state). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


