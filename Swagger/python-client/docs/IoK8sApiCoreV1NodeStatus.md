# IoK8sApiCoreV1NodeStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**list[IoK8sApiCoreV1NodeAddress]**](IoK8sApiCoreV1NodeAddress.md) | List of addresses reachable to the node. Queried from cloud provider, if available. More info: https://kubernetes.io/docs/concepts/nodes/node/#addresses Note: This field is declared as mergeable, but the merge key is not sufficiently unique, which can cause data corruption when it is merged. Callers should instead use a full-replacement patch. See https://pr.k8s.io/79391 for an example. Consumers should assume that addresses can change during the lifetime of a Node. However, there are some exceptions where this may not be possible, such as Pods that inherit a Node&#39;s address in its own status or consumers of the downward API (status.hostIP). | [optional] 
**allocatable** | [**dict(str, IoK8sApimachineryPkgApiResourceQuantity)**](IoK8sApimachineryPkgApiResourceQuantity.md) | Allocatable represents the resources of a node that are available for scheduling. Defaults to Capacity. | [optional] 
**capacity** | [**dict(str, IoK8sApimachineryPkgApiResourceQuantity)**](IoK8sApimachineryPkgApiResourceQuantity.md) | Capacity represents the total resources of a node. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity | [optional] 
**conditions** | [**list[IoK8sApiCoreV1NodeCondition]**](IoK8sApiCoreV1NodeCondition.md) | Conditions is an array of current observed node conditions. More info: https://kubernetes.io/docs/concepts/nodes/node/#condition | [optional] 
**config** | [**IoK8sApiCoreV1NodeConfigStatus**](IoK8sApiCoreV1NodeConfigStatus.md) | Status of the config assigned to the node via the dynamic Kubelet config feature. | [optional] 
**daemon_endpoints** | [**IoK8sApiCoreV1NodeDaemonEndpoints**](IoK8sApiCoreV1NodeDaemonEndpoints.md) | Endpoints of daemons running on the Node. | [optional] 
**images** | [**list[IoK8sApiCoreV1ContainerImage]**](IoK8sApiCoreV1ContainerImage.md) | List of container images on this node | [optional] 
**node_info** | [**IoK8sApiCoreV1NodeSystemInfo**](IoK8sApiCoreV1NodeSystemInfo.md) | Set of ids/uuids to uniquely identify the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#info | [optional] 
**phase** | **str** | NodePhase is the recently observed lifecycle phase of the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#phase The field is never populated, and now is deprecated.  Possible enum values:  - &#x60;\&quot;Pending\&quot;&#x60; means the node has been created/added by the system, but not configured.  - &#x60;\&quot;Running\&quot;&#x60; means the node has been configured and has Kubernetes components running.  - &#x60;\&quot;Terminated\&quot;&#x60; means the node has been removed from the cluster. | [optional] 
**volumes_attached** | [**list[IoK8sApiCoreV1AttachedVolume]**](IoK8sApiCoreV1AttachedVolume.md) | List of volumes that are attached to the node. | [optional] 
**volumes_in_use** | **list[str]** | List of attachable volumes in use (mounted) by the node. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


