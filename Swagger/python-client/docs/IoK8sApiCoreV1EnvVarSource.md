# IoK8sApiCoreV1EnvVarSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_map_key_ref** | [**IoK8sApiCoreV1ConfigMapKeySelector**](IoK8sApiCoreV1ConfigMapKeySelector.md) | Selects a key of a ConfigMap. | [optional] 
**field_ref** | [**IoK8sApiCoreV1ObjectFieldSelector**](IoK8sApiCoreV1ObjectFieldSelector.md) | Selects a field of the pod: supports metadata.name, metadata.namespace, &#x60;metadata.labels[&#39;&lt;KEY&gt;&#39;]&#x60;, &#x60;metadata.annotations[&#39;&lt;KEY&gt;&#39;]&#x60;, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs. | [optional] 
**resource_field_ref** | [**IoK8sApiCoreV1ResourceFieldSelector**](IoK8sApiCoreV1ResourceFieldSelector.md) | Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported. | [optional] 
**secret_key_ref** | [**IoK8sApiCoreV1SecretKeySelector**](IoK8sApiCoreV1SecretKeySelector.md) | Selects a key of a secret in the pod&#39;s namespace | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


