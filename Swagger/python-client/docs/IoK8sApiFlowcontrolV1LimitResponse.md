# IoK8sApiFlowcontrolV1LimitResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queuing** | [**IoK8sApiFlowcontrolV1QueuingConfiguration**](IoK8sApiFlowcontrolV1QueuingConfiguration.md) | &#x60;queuing&#x60; holds the configuration parameters for queuing. This field may be non-empty only if &#x60;type&#x60; is &#x60;\&quot;Queue\&quot;&#x60;. | [optional] 
**type** | **str** | &#x60;type&#x60; is \&quot;Queue\&quot; or \&quot;Reject\&quot;. \&quot;Queue\&quot; means that requests that can not be executed upon arrival are held in a queue until they can be executed or a queuing limit is reached. \&quot;Reject\&quot; means that requests that can not be executed upon arrival are rejected. Required. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


