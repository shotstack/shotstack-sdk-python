# Soundtrack

A music or audio file in mp3 format that plays for the duration of the rendered video or the length of the audio file, which ever is shortest.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src** | **str** | The URL of the mp3 audio file. The URL must be publicly accessible or include credentials. | 
**effect** | **str** | The effect to apply to the audio file &lt;ul&gt;   &lt;li&gt;&#x60;fadeIn&#x60; - fade volume in only&lt;/li&gt;   &lt;li&gt;&#x60;fadeOut&#x60; - fade volume out only&lt;/li&gt;   &lt;li&gt;&#x60;fadeInFadeOut&#x60; - fade volume in and out&lt;/li&gt; &lt;/ul&gt; | [optional] 
**volume** | **float** | Set the volume for the soundtrack between 0 and 1 where 0 is muted and 1 is full volume (defaults to 1). | [optional]  if omitted the server will use the default value of 1
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


