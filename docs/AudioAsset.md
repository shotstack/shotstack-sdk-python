# AudioAsset

The AudioAsset is used to add sound effects and audio at specific intervals on the timeline. The src must be a publicly accessible URL to an audio resource such  as an mp3 file.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src** | **str** | The audio source URL. The URL must be publicly accessible or include credentials. | 
**type** | **str** | The type of asset - set to &#x60;audio&#x60; for audio assets. | defaults to "audio"
**trim** | **float** | The start trim point of the audio clip, in seconds (defaults to 0). Audio will start from the in trim point. The audio will play until the file ends or the Clip length is reached. | [optional] 
**volume** | **float** | Set the volume for the audio clip between 0 and 1 where 0 is muted and 1 is full volume (defaults to 1). | [optional]  if omitted the server will use the default value of 1
**effect** | **str** | The effect to apply to the audio asset &lt;ul&gt;   &lt;li&gt;&#x60;fadeIn&#x60; - fade volume in only&lt;/li&gt;   &lt;li&gt;&#x60;fadeOut&#x60; - fade volume out only&lt;/li&gt;   &lt;li&gt;&#x60;fadeInFadeOut&#x60; - fade volume in and out&lt;/li&gt; &lt;/ul&gt; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


