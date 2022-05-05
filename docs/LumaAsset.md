# LumaAsset

The LumaAsset is used to create luma matte masks, transitions and effects between other assets. A luma matte is a grey scale image or animated video where the black areas are transparent and the white areas solid. The luma matte animation should be provided as an mp4 video file. The src must be a publicly accessible URL to the file.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src** | **str** | The luma matte source URL. The URL must be publicly accessible or include credentials. | 
**type** | **str** | The type of asset - set to &#x60;luma&#x60; for luma mattes. | defaults to "luma"
**trim** | **float** | The start trim point of the luma matte clip, in seconds (defaults to 0). Videos will start from the in trim point. A luma matte video will play until the file ends or the Clip length is reached. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


