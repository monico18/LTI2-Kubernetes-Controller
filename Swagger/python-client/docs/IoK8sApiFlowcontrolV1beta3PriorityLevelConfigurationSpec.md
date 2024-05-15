# IoK8sApiFlowcontrolV1beta3PriorityLevelConfigurationSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exempt** | [**IoK8sApiFlowcontrolV1beta3ExemptPriorityLevelConfiguration**](IoK8sApiFlowcontrolV1beta3ExemptPriorityLevelConfiguration.md) | &#x60;exempt&#x60; specifies how requests are handled for an exempt priority level. This field MUST be empty if &#x60;type&#x60; is &#x60;\&quot;Limited\&quot;&#x60;. This field MAY be non-empty if &#x60;type&#x60; is &#x60;\&quot;Exempt\&quot;&#x60;. If empty and &#x60;type&#x60; is &#x60;\&quot;Exempt\&quot;&#x60; then the default values for &#x60;ExemptPriorityLevelConfiguration&#x60; apply. | [optional] 
**limited** | [**IoK8sApiFlowcontrolV1beta3LimitedPriorityLevelConfiguration**](IoK8sApiFlowcontrolV1beta3LimitedPriorityLevelConfiguration.md) | &#x60;limited&#x60; specifies how requests are handled for a Limited priority level. This field must be non-empty if and only if &#x60;type&#x60; is &#x60;\&quot;Limited\&quot;&#x60;. | [optional] 
**type** | **str** | &#x60;type&#x60; indicates whether this priority level is subject to limitation on request execution.  A value of &#x60;\&quot;Exempt\&quot;&#x60; means that requests of this priority level are not subject to a limit (and thus are never queued) and do not detract from the capacity made available to other priority levels.  A value of &#x60;\&quot;Limited\&quot;&#x60; means that (a) requests of this priority level _are_ subject to limits and (b) some of the server&#39;s limited capacity is made available exclusively to this priority level. Required. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


