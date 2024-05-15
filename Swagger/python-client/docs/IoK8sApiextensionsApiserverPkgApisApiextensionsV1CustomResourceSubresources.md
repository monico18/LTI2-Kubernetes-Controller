# IoK8sApiextensionsApiserverPkgApisApiextensionsV1CustomResourceSubresources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scale** | [**IoK8sApiextensionsApiserverPkgApisApiextensionsV1CustomResourceSubresourceScale**](IoK8sApiextensionsApiserverPkgApisApiextensionsV1CustomResourceSubresourceScale.md) | scale indicates the custom resource should serve a &#x60;/scale&#x60; subresource that returns an &#x60;autoscaling/v1&#x60; Scale object. | [optional] 
**status** | [**IoK8sApiextensionsApiserverPkgApisApiextensionsV1CustomResourceSubresourceStatus**](IoK8sApiextensionsApiserverPkgApisApiextensionsV1CustomResourceSubresourceStatus.md) | status indicates the custom resource should serve a &#x60;/status&#x60; subresource. When enabled: 1. requests to the custom resource primary endpoint ignore changes to the &#x60;status&#x60; stanza of the object. 2. requests to the custom resource &#x60;/status&#x60; subresource ignore changes to anything other than the &#x60;status&#x60; stanza of the object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


