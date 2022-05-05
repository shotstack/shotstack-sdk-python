# VideoAsset

The VideoAsset is used to create video sequences from video files. The src must be a publicly accessible URL to a video resource such as an mp4 file.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src** | **str** | The video source URL. The URL must be publicly accessible or include credentials. | 
**type** | **str** | The type of asset - set to &#x60;video&#x60; for videos. | defaults to "video"
**trim** | **float** | The start trim point of the video clip, in seconds (defaults to 0). Videos will start from the in trim point. The video will play until the file ends or the Clip length is reached. | [optional] 
**volume** | **float** | Set the volume for the video clip between 0 and 1 where 0 is muted and 1 is full volume (defaults to 0). | [optional] 
**crop** | [**Crop**](Crop.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


