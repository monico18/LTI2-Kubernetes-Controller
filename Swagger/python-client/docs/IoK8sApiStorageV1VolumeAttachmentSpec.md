# IoK8sApiStorageV1VolumeAttachmentSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attacher** | **str** | attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName(). | 
**node_name** | **str** | nodeName represents the node that the volume should be attached to. | 
**source** | [**IoK8sApiStorageV1VolumeAttachmentSource**](IoK8sApiStorageV1VolumeAttachmentSource.md) | source represents the volume that should be attached. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


