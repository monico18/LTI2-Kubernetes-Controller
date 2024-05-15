# IoK8sApiStorageV1VolumeAttachmentSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inline_volume_spec** | [**IoK8sApiCoreV1PersistentVolumeSpec**](IoK8sApiCoreV1PersistentVolumeSpec.md) | inlineVolumeSpec contains all the information necessary to attach a persistent volume defined by a pod&#39;s inline VolumeSource. This field is populated only for the CSIMigration feature. It contains translated fields from a pod&#39;s inline VolumeSource to a PersistentVolumeSpec. This field is beta-level and is only honored by servers that enabled the CSIMigration feature. | [optional] 
**persistent_volume_name** | **str** | persistentVolumeName represents the name of the persistent volume to attach. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


