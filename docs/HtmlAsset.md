# HtmlAsset

The HtmlAsset clip type lets you create text based layout and formatting using HTML and CSS. You can also set the height and width of a bounding box for the HTML content to sit within. Text and elements will wrap within the bounding box.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html** | **str** | The HTML text string. See list of [supported HTML tags](https://shotstack.gitbook.io/docs/guides/architecting-an-application/html-support#supported-html-tags). | 
**type** | **str** | The type of asset - set to &#x60;html&#x60; for HTML. | defaults to "html"
**css** | **str** | The CSS text string to apply styling to the HTML. See list of  [support CSS properties](https://shotstack.gitbook.io/docs/guides/architecting-an-application/html-support#supported-html-tags). | [optional] 
**width** | **int** | Set the width of the HTML asset bounding box in pixels. Text will wrap to fill the bounding box. | [optional] 
**height** | **int** | Set the width of the HTML asset bounding box in pixels. Text and elements will be masked if they exceed the  height of the bounding box. | [optional] 
**background** | **str** | Apply a background color behind the HTML bounding box using. Set the text color using hexadecimal  color notation. Transparency is supported by setting the first two characters of the hex string  (opposite to HTML), i.e. #80ffffff will be white with 50% transparency. | [optional]  if omitted the server will use the default value of "transparent"
**position** | **str** | Place the HTML in one of nine predefined positions within the HTML area. &lt;ul&gt;   &lt;li&gt;&#x60;top&#x60; - top (center)&lt;/li&gt;   &lt;li&gt;&#x60;topRight&#x60; - top right&lt;/li&gt;   &lt;li&gt;&#x60;right&#x60; - right (center)&lt;/li&gt;   &lt;li&gt;&#x60;bottomRight&#x60; - bottom right&lt;/li&gt;   &lt;li&gt;&#x60;bottom&#x60; - bottom (center)&lt;/li&gt;   &lt;li&gt;&#x60;bottomLeft&#x60; - bottom left&lt;/li&gt;   &lt;li&gt;&#x60;left&#x60; - left (center)&lt;/li&gt;   &lt;li&gt;&#x60;topLeft&#x60; - top left&lt;/li&gt;   &lt;li&gt;&#x60;center&#x60; - center&lt;/li&gt; &lt;/ul&gt; | [optional]  if omitted the server will use the default value of "center"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


