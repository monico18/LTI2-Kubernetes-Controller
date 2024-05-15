# IoK8sApiCoreV1LifecycleHandler

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_exec** | [**IoK8sApiCoreV1ExecAction**](IoK8sApiCoreV1ExecAction.md) | Exec specifies the action to take. | [optional] 
**http_get** | [**IoK8sApiCoreV1HTTPGetAction**](IoK8sApiCoreV1HTTPGetAction.md) | HTTPGet specifies the http request to perform. | [optional] 
**sleep** | [**IoK8sApiCoreV1SleepAction**](IoK8sApiCoreV1SleepAction.md) | Sleep represents the duration that the container should sleep before being terminated. | [optional] 
**tcp_socket** | [**IoK8sApiCoreV1TCPSocketAction**](IoK8sApiCoreV1TCPSocketAction.md) | Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for the backward compatibility. There are no validation of this field and lifecycle hooks will fail in runtime when tcp handler is specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


