# Timeline

A timeline represents the contents of a video edit over time, an audio edit over time, in seconds, or an image layout. A timeline consists of layers called tracks. Tracks are composed of titles, images, audio, html or video segments referred to as clips which are placed along the track at specific starting point and lasting for a specific amount of time.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracks** | [**[Track]**](Track.md) | A timeline consists of an array of tracks, each track containing clips. Tracks are layered on top of each other in the same order they are added to the array with the top most track layered over the top of those below it. Ensure that a track containing titles is the top most track so that it is displayed above videos and images. | 
**soundtrack** | [**Soundtrack**](Soundtrack.md) |  | [optional] 
**background** | **str** | A hexadecimal value for the timeline background colour. Defaults to #000000 (black). | [optional]  if omitted the server will use the default value of "#000000"
**fonts** | [**[Font]**](Font.md) | An array of custom fonts to be downloaded for use by the HTML assets. | [optional] 
**cache** | **bool** | Disable the caching of ingested source footage and assets. See  [caching](https://shotstack.gitbook.io/docs/guides/architecting-an-application/caching) for more details. | [optional]  if omitted the server will use the default value of True
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


