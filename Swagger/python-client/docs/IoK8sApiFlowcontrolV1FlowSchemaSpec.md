# IoK8sApiFlowcontrolV1FlowSchemaSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distinguisher_method** | [**IoK8sApiFlowcontrolV1FlowDistinguisherMethod**](IoK8sApiFlowcontrolV1FlowDistinguisherMethod.md) | &#x60;distinguisherMethod&#x60; defines how to compute the flow distinguisher for requests that match this schema. &#x60;nil&#x60; specifies that the distinguisher is disabled and thus will always be the empty string. | [optional] 
**matching_precedence** | **int** | &#x60;matchingPrecedence&#x60; is used to choose among the FlowSchemas that match a given request. The chosen FlowSchema is among those with the numerically lowest (which we take to be logically highest) MatchingPrecedence.  Each MatchingPrecedence value must be ranged in [1,10000]. Note that if the precedence is not specified, it will be set to 1000 as default. | [optional] 
**priority_level_configuration** | [**IoK8sApiFlowcontrolV1PriorityLevelConfigurationReference**](IoK8sApiFlowcontrolV1PriorityLevelConfigurationReference.md) | &#x60;priorityLevelConfiguration&#x60; should reference a PriorityLevelConfiguration in the cluster. If the reference cannot be resolved, the FlowSchema will be ignored and marked as invalid in its status. Required. | 
**rules** | [**list[IoK8sApiFlowcontrolV1PolicyRulesWithSubjects]**](IoK8sApiFlowcontrolV1PolicyRulesWithSubjects.md) | &#x60;rules&#x60; describes which requests will match this flow schema. This FlowSchema matches a request if and only if at least one member of rules matches the request. if it is an empty slice, there will be no requests matching the FlowSchema. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


