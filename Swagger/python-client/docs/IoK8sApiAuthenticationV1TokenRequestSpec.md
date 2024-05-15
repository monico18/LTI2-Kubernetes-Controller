# IoK8sApiAuthenticationV1TokenRequestSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audiences** | **list[str]** | Audiences are the intendend audiences of the token. A recipient of a token must identify themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences. | 
**bound_object_ref** | [**IoK8sApiAuthenticationV1BoundObjectReference**](IoK8sApiAuthenticationV1BoundObjectReference.md) | BoundObjectRef is a reference to an object that the token will be bound to. The token will only be valid for as long as the bound object exists. NOTE: The API server&#39;s TokenReview endpoint will validate the BoundObjectRef, but other audiences may not. Keep ExpirationSeconds small if you want prompt revocation. | [optional] 
**expiration_seconds** | **int** | ExpirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the &#39;expiration&#39; field in a response. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


