# IoK8sApiCoreV1VolumeProjection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_trust_bundle** | [**IoK8sApiCoreV1ClusterTrustBundleProjection**](IoK8sApiCoreV1ClusterTrustBundleProjection.md) | ClusterTrustBundle allows a pod to access the &#x60;.spec.trustBundle&#x60; field of ClusterTrustBundle objects in an auto-updating file.  Alpha, gated by the ClusterTrustBundleProjection feature gate.  ClusterTrustBundle objects can either be selected by name, or by the combination of signer name and a label selector.  Kubelet performs aggressive normalization of the PEM contents written into the pod filesystem.  Esoteric PEM features such as inter-block comments and block headers are stripped.  Certificates are deduplicated. The ordering of certificates within the file is arbitrary, and Kubelet may change the order over time. | [optional] 
**config_map** | [**IoK8sApiCoreV1ConfigMapProjection**](IoK8sApiCoreV1ConfigMapProjection.md) | configMap information about the configMap data to project | [optional] 
**downward_api** | [**IoK8sApiCoreV1DownwardAPIProjection**](IoK8sApiCoreV1DownwardAPIProjection.md) | downwardAPI information about the downwardAPI data to project | [optional] 
**secret** | [**IoK8sApiCoreV1SecretProjection**](IoK8sApiCoreV1SecretProjection.md) | secret information about the secret data to project | [optional] 
**service_account_token** | [**IoK8sApiCoreV1ServiceAccountTokenProjection**](IoK8sApiCoreV1ServiceAccountTokenProjection.md) | serviceAccountToken is information about the serviceAccountToken data to project | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


