# IoK8sApiextensionsApiserverPkgApisApiextensionsV1WebhookConversion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_config** | [**IoK8sApiextensionsApiserverPkgApisApiextensionsV1WebhookClientConfig**](IoK8sApiextensionsApiserverPkgApisApiextensionsV1WebhookClientConfig.md) | clientConfig is the instructions for how to call the webhook if strategy is &#x60;Webhook&#x60;. | [optional] 
**conversion_review_versions** | **list[str]** | conversionReviewVersions is an ordered list of preferred &#x60;ConversionReview&#x60; versions the Webhook expects. The API server will use the first version in the list which it supports. If none of the versions specified in this list are supported by API server, conversion will fail for the custom resource. If a persisted Webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


