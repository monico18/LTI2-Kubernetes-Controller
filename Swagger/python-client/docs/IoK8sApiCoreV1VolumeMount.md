# IoK8sApiCoreV1VolumeMount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_path** | **str** | Path within the container at which the volume should be mounted.  Must not contain &#39;:&#39;. | 
**mount_propagation** | **str** | mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10.  Possible enum values:  - &#x60;\&quot;Bidirectional\&quot;&#x60; means that the volume in a container will receive new mounts from the host or other containers, and its own mounts will be propagated from the container to the host or other containers. Note that this mode is recursively applied to all mounts in the volume (\&quot;rshared\&quot; in Linux terminology).  - &#x60;\&quot;HostToContainer\&quot;&#x60; means that the volume in a container will receive new mounts from the host or other containers, but filesystems mounted inside the container won&#39;t be propagated to the host or other containers. Note that this mode is recursively applied to all mounts in the volume (\&quot;rslave\&quot; in Linux terminology).  - &#x60;\&quot;None\&quot;&#x60; means that the volume in a container will not receive new mounts from the host or other containers, and filesystems mounted inside the container won&#39;t be propagated to the host or other containers. Note that this mode corresponds to \&quot;private\&quot; in Linux terminology. | [optional] 
**name** | **str** | This must match the Name of a Volume. | 
**read_only** | **bool** | Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false. | [optional] 
**sub_path** | **str** | Path within the volume from which the container&#39;s volume should be mounted. Defaults to \&quot;\&quot; (volume&#39;s root). | [optional] 
**sub_path_expr** | **str** | Expanded path within the volume from which the container&#39;s volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container&#39;s environment. Defaults to \&quot;\&quot; (volume&#39;s root). SubPathExpr and SubPath are mutually exclusive. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


