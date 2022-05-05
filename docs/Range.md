# Range

Specify a time range to render, i.e. to render only a portion of a video or audio file. Omit this setting to  export the entire video. Range can also be used to render a frame at a specific time point - setting a range and output format as `jpg` will output a single frame image at the range `start` point.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **float** | The point on the timeline, in seconds, to start the render from - i.e. start at second 3. | [optional] 
**length** | **float** | The length of the portion of the video or audio to render - i.e. render 6 seconds of the video. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


