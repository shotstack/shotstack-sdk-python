# ShotstackDestination

Send rendered assets to the Shotstack hosting and CDN service. This destination is enabled by default.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The destination to send rendered assets to - set to &#x60;shotstack&#x60; for Shotstack hosting and CDN. | defaults to "shotstack"
**exclude** | **bool** | Set to &#x60;true&#x60; to opt-out from the Shotstack hosting and CDN service. All files must be downloaded within 24 hours of rendering. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


