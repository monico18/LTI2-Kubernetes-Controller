# IoK8sApiextensionsApiserverPkgApisApiextensionsV1CustomResourceDefinitionStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted_names** | [**IoK8sApiextensionsApiserverPkgApisApiextensionsV1CustomResourceDefinitionNames**](IoK8sApiextensionsApiserverPkgApisApiextensionsV1CustomResourceDefinitionNames.md) | acceptedNames are the names that are actually being used to serve discovery. They may be different than the names in spec. | [optional] 
**conditions** | [**list[IoK8sApiextensionsApiserverPkgApisApiextensionsV1CustomResourceDefinitionCondition]**](IoK8sApiextensionsApiserverPkgApisApiextensionsV1CustomResourceDefinitionCondition.md) | conditions indicate state for particular aspects of a CustomResourceDefinition | [optional] 
**stored_versions** | **list[str]** | storedVersions lists all versions of CustomResources that were ever persisted. Tracking these versions allows a migration path for stored versions in etcd. The field is mutable so a migration controller can finish a migration to another version (ensuring no old objects are left in storage), and then remove the rest of the versions from this list. Versions may not be removed from &#x60;spec.versions&#x60; while they exist in this list. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


