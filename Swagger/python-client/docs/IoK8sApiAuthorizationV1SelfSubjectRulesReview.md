# IoK8sApiAuthorizationV1SelfSubjectRulesReview

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**IoK8sApimachineryPkgApisMetaV1ObjectMeta**](IoK8sApimachineryPkgApisMetaV1ObjectMeta.md) | Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata | [optional] 
**spec** | [**IoK8sApiAuthorizationV1SelfSubjectRulesReviewSpec**](IoK8sApiAuthorizationV1SelfSubjectRulesReviewSpec.md) | Spec holds information about the request being evaluated. | 
**status** | [**IoK8sApiAuthorizationV1SubjectRulesReviewStatus**](IoK8sApiAuthorizationV1SubjectRulesReviewStatus.md) | Status is filled in by the server and indicates the set of actions a user can perform. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


