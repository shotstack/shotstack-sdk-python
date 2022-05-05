# ImageAsset

The ImageAsset is used to create video from images to compose an image. The src must be a publicly accessible URL to an image resource such as a jpg or png file.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src** | **str** | The image source URL. The URL must be publicly accessible or include credentials. | 
**type** | **str** | The type of asset - set to &#x60;image&#x60; for images. | defaults to "image"
**crop** | [**Crop**](Crop.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


