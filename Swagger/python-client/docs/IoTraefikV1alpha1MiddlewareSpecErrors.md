# IoTraefikV1alpha1MiddlewareSpecErrors

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | Query defines the URL for the error page (hosted by service). The {status} variable can be used in order to insert the status code in the URL. | [optional] 
**service** | [**IoTraefikV1alpha1MiddlewareSpecErrorsService**](IoTraefikV1alpha1MiddlewareSpecErrorsService.md) |  | [optional] 
**status** | **list[str]** | Status defines which status or range of statuses should result in an error page. It can be either a status code as a number (500), as multiple comma-separated numbers (500,502), as ranges by separating two codes with a dash (500-599), or a combination of the two (404,418,500-599). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


