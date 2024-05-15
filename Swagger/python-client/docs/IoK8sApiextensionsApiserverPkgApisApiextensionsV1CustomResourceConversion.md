# IoK8sApiextensionsApiserverPkgApisApiextensionsV1CustomResourceConversion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | **str** | strategy specifies how custom resources are converted between versions. Allowed values are: - &#x60;\&quot;None\&quot;&#x60;: The converter only change the apiVersion and would not touch any other field in the custom resource. - &#x60;\&quot;Webhook\&quot;&#x60;: API Server will call to an external webhook to do the conversion. Additional information   is needed for this option. This requires spec.preserveUnknownFields to be false, and spec.conversion.webhook to be set. | 
**webhook** | [**IoK8sApiextensionsApiserverPkgApisApiextensionsV1WebhookConversion**](IoK8sApiextensionsApiserverPkgApisApiextensionsV1WebhookConversion.md) | webhook describes how to call the conversion webhook. Required when &#x60;strategy&#x60; is set to &#x60;\&quot;Webhook\&quot;&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


