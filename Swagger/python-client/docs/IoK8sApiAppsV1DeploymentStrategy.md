# IoK8sApiAppsV1DeploymentStrategy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rolling_update** | [**IoK8sApiAppsV1RollingUpdateDeployment**](IoK8sApiAppsV1RollingUpdateDeployment.md) | Rolling update config params. Present only if DeploymentStrategyType &#x3D; RollingUpdate. | [optional] 
**type** | **str** | Type of deployment. Can be \&quot;Recreate\&quot; or \&quot;RollingUpdate\&quot;. Default is RollingUpdate.  Possible enum values:  - &#x60;\&quot;Recreate\&quot;&#x60; Kill all existing pods before creating new ones.  - &#x60;\&quot;RollingUpdate\&quot;&#x60; Replace the old ReplicaSets by new one using rolling update i.e gradually scale down the old ReplicaSets and scale up the new one. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


