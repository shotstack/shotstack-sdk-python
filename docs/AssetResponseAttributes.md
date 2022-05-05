# AssetResponseAttributes

The list of asset attributes and their values.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the hosted asset in UUID format. | [optional] 
**owner** | **str** | The owner id of the render task. | [optional] 
**region** | **str** | The region the asset is hosted, currently only &#x60;au&#x60; (Australia). | [optional] 
**render_id** | **str** | The original render id that created the asset in UUID format. Multiple assets can share the same render id. | [optional] 
**filename** | **str** | The asset file name. | [optional] 
**url** | **str** | The asset file name. | [optional] 
**status** | **str** | The status of the asset. &lt;ul&gt;   &lt;li&gt;&#x60;importing&#x60; - the asset is being copied to the hosting service&lt;/li&gt;   &lt;li&gt;&#x60;ready&#x60; - the asset is ready to be served to users&lt;/li&gt;   &lt;li&gt;&#x60;failed&#x60; - the asset failed to copy or delete&lt;/li&gt;   &lt;li&gt;&#x60;deleted&#x60; - the asset has been deleted&lt;/li&gt; &lt;/ul&gt; | [optional] 
**created** | **str** | The time the asset was created. | [optional] 
**updated** | **str** | The time the asset status was last updated. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


