# IoK8sApiCoreV1AzureDiskVolumeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caching_mode** | **str** | cachingMode is the Host Caching mode: None, Read Only, Read Write.  Possible enum values:  - &#x60;\&quot;None\&quot;&#x60;  - &#x60;\&quot;ReadOnly\&quot;&#x60;  - &#x60;\&quot;ReadWrite\&quot;&#x60; | [optional] 
**disk_name** | **str** | diskName is the Name of the data disk in the blob storage | 
**disk_uri** | **str** | diskURI is the URI of data disk in the blob storage | 
**fs_type** | **str** | fsType is Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. | [optional] 
**kind** | **str** | kind expected values are Shared: multiple blob disks per storage account  Dedicated: single blob disk per storage account  Managed: azure managed data disk (only in managed availability set). defaults to shared  Possible enum values:  - &#x60;\&quot;Dedicated\&quot;&#x60;  - &#x60;\&quot;Managed\&quot;&#x60;  - &#x60;\&quot;Shared\&quot;&#x60; | [optional] 
**read_only** | **bool** | readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


