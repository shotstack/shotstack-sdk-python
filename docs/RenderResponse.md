# RenderResponse

The response received after a [render status request](#get-render-status) is submitted. The response includes  details about status of a render and the output URL.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | &#x60;true&#x60; if status available, else &#x60;false&#x60;. | 
**message** | **str** | &#x60;OK&#x60; or an error message. | 
**response** | [**RenderResponseData**](RenderResponseData.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


