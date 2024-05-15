# IoK8sApiAutoscalingV2HorizontalPodAutoscalerBehavior

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scale_down** | [**IoK8sApiAutoscalingV2HPAScalingRules**](IoK8sApiAutoscalingV2HPAScalingRules.md) | scaleDown is scaling policy for scaling Down. If not set, the default value is to allow to scale down to minReplicas pods, with a 300 second stabilization window (i.e., the highest recommendation for the last 300sec is used). | [optional] 
**scale_up** | [**IoK8sApiAutoscalingV2HPAScalingRules**](IoK8sApiAutoscalingV2HPAScalingRules.md) | scaleUp is scaling policy for scaling Up. If not set, the default value is the higher of:   * increase no more than 4 pods per 60 seconds   * double the number of pods per 60 seconds No stabilization is used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


