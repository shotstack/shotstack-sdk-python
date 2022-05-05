# QueuedResponse

The response received after a [render request](#render-asset) is submitted. The render task is queued for rendering and a unique render id is returned.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | &#x60;true&#x60; if successfully queued, else &#x60;false&#x60;. | 
**message** | **str** | &#x60;Created&#x60;, &#x60;Bad Request&#x60; or an error message. | 
**response** | [**QueuedResponseData**](QueuedResponseData.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


