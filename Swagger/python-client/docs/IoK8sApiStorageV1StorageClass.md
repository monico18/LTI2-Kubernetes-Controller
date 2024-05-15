# IoK8sApiStorageV1StorageClass

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_volume_expansion** | **bool** | allowVolumeExpansion shows whether the storage class allow volume expand. | [optional] 
**allowed_topologies** | [**list[IoK8sApiCoreV1TopologySelectorTerm]**](IoK8sApiCoreV1TopologySelectorTerm.md) | allowedTopologies restrict the node topologies where volumes can be dynamically provisioned. Each volume plugin defines its own supported topology specifications. An empty TopologySelectorTerm list means there is no topology restriction. This field is only honored by servers that enable the VolumeScheduling feature. | [optional] 
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**IoK8sApimachineryPkgApisMetaV1ObjectMeta**](IoK8sApimachineryPkgApisMetaV1ObjectMeta.md) | Standard object&#39;s metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata | [optional] 
**mount_options** | **list[str]** | mountOptions controls the mountOptions for dynamically provisioned PersistentVolumes of this storage class. e.g. [\&quot;ro\&quot;, \&quot;soft\&quot;]. Not validated - mount of the PVs will simply fail if one is invalid. | [optional] 
**parameters** | **dict(str, str)** | parameters holds the parameters for the provisioner that should create volumes of this storage class. | [optional] 
**provisioner** | **str** | provisioner indicates the type of the provisioner. | 
**reclaim_policy** | **str** | reclaimPolicy controls the reclaimPolicy for dynamically provisioned PersistentVolumes of this storage class. Defaults to Delete.  Possible enum values:  - &#x60;\&quot;Delete\&quot;&#x60; means the volume will be deleted from Kubernetes on release from its claim. The volume plugin must support Deletion.  - &#x60;\&quot;Recycle\&quot;&#x60; means the volume will be recycled back into the pool of unbound persistent volumes on release from its claim. The volume plugin must support Recycling.  - &#x60;\&quot;Retain\&quot;&#x60; means the volume will be left in its current phase (Released) for manual reclamation by the administrator. The default policy is Retain. | [optional] 
**volume_binding_mode** | **str** | volumeBindingMode indicates how PersistentVolumeClaims should be provisioned and bound.  When unset, VolumeBindingImmediate is used. This field is only honored by servers that enable the VolumeScheduling feature.  Possible enum values:  - &#x60;\&quot;Immediate\&quot;&#x60; indicates that PersistentVolumeClaims should be immediately provisioned and bound. This is the default mode.  - &#x60;\&quot;WaitForFirstConsumer\&quot;&#x60; indicates that PersistentVolumeClaims should not be provisioned and bound until the first Pod is created that references the PeristentVolumeClaim. The volume provisioning and binding will occur during Pod scheduing. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


