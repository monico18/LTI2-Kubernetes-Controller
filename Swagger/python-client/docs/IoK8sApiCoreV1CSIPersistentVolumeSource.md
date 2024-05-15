# IoK8sApiCoreV1CSIPersistentVolumeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller_expand_secret_ref** | [**IoK8sApiCoreV1SecretReference**](IoK8sApiCoreV1SecretReference.md) | controllerExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerExpandVolume call. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. | [optional] 
**controller_publish_secret_ref** | [**IoK8sApiCoreV1SecretReference**](IoK8sApiCoreV1SecretReference.md) | controllerPublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerPublishVolume and ControllerUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. | [optional] 
**driver** | **str** | driver is the name of the driver to use for this volume. Required. | 
**fs_type** | **str** | fsType to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. | [optional] 
**node_expand_secret_ref** | [**IoK8sApiCoreV1SecretReference**](IoK8sApiCoreV1SecretReference.md) | nodeExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeExpandVolume call. This field is optional, may be omitted if no secret is required. If the secret object contains more than one secret, all secrets are passed. | [optional] 
**node_publish_secret_ref** | [**IoK8sApiCoreV1SecretReference**](IoK8sApiCoreV1SecretReference.md) | nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. | [optional] 
**node_stage_secret_ref** | [**IoK8sApiCoreV1SecretReference**](IoK8sApiCoreV1SecretReference.md) | nodeStageSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeStageVolume and NodeStageVolume and NodeUnstageVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. | [optional] 
**read_only** | **bool** | readOnly value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write). | [optional] 
**volume_attributes** | **dict(str, str)** | volumeAttributes of the volume to publish. | [optional] 
**volume_handle** | **str** | volumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


