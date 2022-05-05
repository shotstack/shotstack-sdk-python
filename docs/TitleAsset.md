# TitleAsset

The TitleAsset clip type lets you create video titles from a text string and apply styling and positioning.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The title text string - i.e. \&quot;My Title\&quot;. | 
**type** | **str** | The type of asset - set to &#x60;title&#x60; for titles. | defaults to "title"
**style** | **str** | Uses a preset to apply font properties and styling to the title. &lt;ul&gt;   &lt;li&gt;&#x60;minimal&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;blockbuster&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;vogue&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;sketchy&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;skinny&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;chunk&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;chunkLight&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;marker&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;future&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;subtitle&#x60;&lt;/li&gt; &lt;/ul&gt; | [optional] 
**color** | **str** | Set the text color using hexadecimal color notation. Transparency is supported by setting the first two characters of the hex string (opposite to HTML),  i.e. #80ffffff will be white with  50% transparency. | [optional]  if omitted the server will use the default value of "#ffffff"
**size** | **str** | Set the relative size of the text using predefined sizes from xx-small to xx-large. &lt;ul&gt;   &lt;li&gt;&#x60;xx-small&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;x-small&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;small&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;medium&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;large&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;x-large&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;xx-large&#x60;&lt;/li&gt; &lt;/ul&gt; | [optional]  if omitted the server will use the default value of "medium"
**background** | **str** | Apply a background color behind the text. Set the text color using hexadecimal color notation. Transparency is supported by setting the first two characters of the hex string (opposite to HTML),  i.e. #80ffffff will be white with 50% transparency. Omit to use transparent background. | [optional] 
**position** | **str** | Place the title in one of nine predefined positions of the viewport. &lt;ul&gt;   &lt;li&gt;&#x60;top&#x60; - top (center)&lt;/li&gt;   &lt;li&gt;&#x60;topRight&#x60; - top right&lt;/li&gt;   &lt;li&gt;&#x60;right&#x60; - right (center)&lt;/li&gt;   &lt;li&gt;&#x60;bottomRight&#x60; - bottom right&lt;/li&gt;   &lt;li&gt;&#x60;bottom&#x60; - bottom (center)&lt;/li&gt;   &lt;li&gt;&#x60;bottomLeft&#x60; - bottom left&lt;/li&gt;   &lt;li&gt;&#x60;left&#x60; - left (center)&lt;/li&gt;   &lt;li&gt;&#x60;topLeft&#x60; - top left&lt;/li&gt;   &lt;li&gt;&#x60;center&#x60; - center&lt;/li&gt; &lt;/ul&gt; | [optional]  if omitted the server will use the default value of "center"
**offset** | [**Offset**](Offset.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


