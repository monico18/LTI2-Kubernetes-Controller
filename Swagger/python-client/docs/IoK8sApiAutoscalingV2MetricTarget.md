# IoK8sApiAutoscalingV2MetricTarget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_utilization** | **int** | averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type | [optional] 
**average_value** | [**IoK8sApimachineryPkgApiResourceQuantity**](IoK8sApimachineryPkgApiResourceQuantity.md) | averageValue is the target value of the average of the metric across all relevant pods (as a quantity) | [optional] 
**type** | **str** | type represents whether the metric type is Utilization, Value, or AverageValue | 
**value** | [**IoK8sApimachineryPkgApiResourceQuantity**](IoK8sApimachineryPkgApiResourceQuantity.md) | value is the target value of the metric (as a quantity). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


