# IoK8sApiCoreV1HostPathVolumeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath | 
**type** | **str** | type for HostPath Volume Defaults to \&quot;\&quot; More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath  Possible enum values:  - &#x60;\&quot;\&quot;&#x60; For backwards compatible, leave it empty if unset  - &#x60;\&quot;BlockDevice\&quot;&#x60; A block device must exist at the given path  - &#x60;\&quot;CharDevice\&quot;&#x60; A character device must exist at the given path  - &#x60;\&quot;Directory\&quot;&#x60; A directory must exist at the given path  - &#x60;\&quot;DirectoryOrCreate\&quot;&#x60; If nothing exists at the given path, an empty directory will be created there as needed with file mode 0755, having the same group and ownership with Kubelet.  - &#x60;\&quot;File\&quot;&#x60; A file must exist at the given path  - &#x60;\&quot;FileOrCreate\&quot;&#x60; If nothing exists at the given path, an empty file will be created there as needed with file mode 0644, having the same group and ownership with Kubelet.  - &#x60;\&quot;Socket\&quot;&#x60; A UNIX socket must exist at the given path | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


