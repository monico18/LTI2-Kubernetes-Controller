# IoK8sApiCoordinationV1LeaseSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquire_time** | [**IoK8sApimachineryPkgApisMetaV1MicroTime**](IoK8sApimachineryPkgApisMetaV1MicroTime.md) | acquireTime is a time when the current lease was acquired. | [optional] 
**holder_identity** | **str** | holderIdentity contains the identity of the holder of a current lease. | [optional] 
**lease_duration_seconds** | **int** | leaseDurationSeconds is a duration that candidates for a lease need to wait to force acquire it. This is measure against time of last observed renewTime. | [optional] 
**lease_transitions** | **int** | leaseTransitions is the number of transitions of a lease between holders. | [optional] 
**renew_time** | [**IoK8sApimachineryPkgApisMetaV1MicroTime**](IoK8sApimachineryPkgApisMetaV1MicroTime.md) | renewTime is a time when the current holder of a lease has last updated the lease. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


