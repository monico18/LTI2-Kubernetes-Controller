# IoK8sApiEventsV1Event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | action is what action was taken/failed regarding to the regarding object. It is machine-readable. This field cannot be empty for new Events and it can have at most 128 characters. | [optional] 
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**deprecated_count** | **int** | deprecatedCount is the deprecated field assuring backward compatibility with core.v1 Event type. | [optional] 
**deprecated_first_timestamp** | [**IoK8sApimachineryPkgApisMetaV1Time**](IoK8sApimachineryPkgApisMetaV1Time.md) | deprecatedFirstTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type. | [optional] 
**deprecated_last_timestamp** | [**IoK8sApimachineryPkgApisMetaV1Time**](IoK8sApimachineryPkgApisMetaV1Time.md) | deprecatedLastTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type. | [optional] 
**deprecated_source** | [**IoK8sApiCoreV1EventSource**](IoK8sApiCoreV1EventSource.md) | deprecatedSource is the deprecated field assuring backward compatibility with core.v1 Event type. | [optional] 
**event_time** | [**IoK8sApimachineryPkgApisMetaV1MicroTime**](IoK8sApimachineryPkgApisMetaV1MicroTime.md) | eventTime is the time when this Event was first observed. It is required. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**IoK8sApimachineryPkgApisMetaV1ObjectMeta**](IoK8sApimachineryPkgApisMetaV1ObjectMeta.md) | Standard object&#39;s metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata | [optional] 
**note** | **str** | note is a human-readable description of the status of this operation. Maximal length of the note is 1kB, but libraries should be prepared to handle values up to 64kB. | [optional] 
**reason** | **str** | reason is why the action was taken. It is human-readable. This field cannot be empty for new Events and it can have at most 128 characters. | [optional] 
**regarding** | [**IoK8sApiCoreV1ObjectReference**](IoK8sApiCoreV1ObjectReference.md) | regarding contains the object this Event is about. In most cases it&#39;s an Object reporting controller implements, e.g. ReplicaSetController implements ReplicaSets and this event is emitted because it acts on some changes in a ReplicaSet object. | [optional] 
**related** | [**IoK8sApiCoreV1ObjectReference**](IoK8sApiCoreV1ObjectReference.md) | related is the optional secondary object for more complex actions. E.g. when regarding object triggers a creation or deletion of related object. | [optional] 
**reporting_controller** | **str** | reportingController is the name of the controller that emitted this Event, e.g. &#x60;kubernetes.io/kubelet&#x60;. This field cannot be empty for new Events. | [optional] 
**reporting_instance** | **str** | reportingInstance is the ID of the controller instance, e.g. &#x60;kubelet-xyzf&#x60;. This field cannot be empty for new Events and it can have at most 128 characters. | [optional] 
**series** | [**IoK8sApiEventsV1EventSeries**](IoK8sApiEventsV1EventSeries.md) | series is data about the Event series this event represents or nil if it&#39;s a singleton Event. | [optional] 
**type** | **str** | type is the type of this event (Normal, Warning), new types could be added in the future. It is machine-readable. This field cannot be empty for new Events. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


