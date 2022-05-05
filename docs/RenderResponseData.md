# RenderResponseData

The response data returned with the [RenderResponse](#tocs_renderresponse) including status and URL.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the render task in UUID format. | 
**owner** | **str** | The owner id of the render task. | 
**status** | **str** | The status of the render task. &lt;ul&gt;   &lt;li&gt;&#x60;queued&#x60; - render is queued waiting to be rendered&lt;/li&gt;   &lt;li&gt;&#x60;fetching&#x60; - assets are being fetched&lt;/li&gt;   &lt;li&gt;&#x60;rendering&#x60; - the asset is being rendered&lt;/li&gt;   &lt;li&gt;&#x60;saving&#x60; - the final asset is being saved to storage&lt;/li&gt;   &lt;li&gt;&#x60;done&#x60; - the asset is ready to be downloaded&lt;/li&gt;   &lt;li&gt;&#x60;failed&#x60; - there was an error rendering the asset&lt;/li&gt; &lt;/ul&gt; | 
**data** | [**Edit**](Edit.md) |  | 
**created** | **str** | The time the render task was initially queued. | 
**updated** | **str** | The time the render status was last updated. | 
**plan** | **str** | The customer subscription plan. | [optional] 
**error** | **str** | An error message, only displayed if an error occurred. | [optional] 
**duration** | **float** | The output video or audio length in seconds. | [optional] 
**render_time** | **float** | The time taken to render the asset in milliseconds. | [optional] 
**url** | **str** | The URL of the final asset. This will only be available if status is done. This is a temporary URL and will be deleted after 24 hours. By default all assets are copied to the Shotstack hosting and CDN destination. | [optional] 
**poster** | **str** | The URL of the poster image if requested. This will only be available if status is done. | [optional] 
**thumbnail** | **str** | The URL of the thumbnail image if requested. This will only be available if status is done. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


