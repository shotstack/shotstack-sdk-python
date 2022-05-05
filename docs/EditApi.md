# shotstack_sdk.EditApi

All URIs are relative to *https://api.shotstack.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_render**](EditApi.md#get_render) | **GET** /render/{id} | Get Render Status
[**post_render**](EditApi.md#post_render) | **POST** /render | Render Asset
[**probe**](EditApi.md#probe) | **GET** /probe/{url} | Inspect Media


# **get_render**
> RenderResponse get_render(id)

Get Render Status

Get the rendering status, temporary asset url and details of a render by ID.  **Base URL:** https://api.shotstack.io/{version}

### Example

* Api Key Authentication (DeveloperKey):

```python
import time
import shotstack_sdk
from shotstack_sdk.api import edit_api
from shotstack_sdk.model.render_response import RenderResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.shotstack.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = shotstack_sdk.Configuration(
    host = "https://api.shotstack.io/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: DeveloperKey
configuration.api_key['DeveloperKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['DeveloperKey'] = 'Bearer'

# Enter a context with an instance of the API client
with shotstack_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edit_api.EditApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | The id of the timeline render task in UUID format
    data = False # bool | Include the data parameter in the response. The data parameter includes the original timeline, output and other settings sent to the API.<br><br><b>Note:</b> the default is currently `true`, this is deprecated and the default will soon be `false`. If you rely on the data being returned in the response you should explicitly set the parameter to `true`. (optional)
    merged = False # bool | Used when data is set to true, it will show the [merge fields](#tocs_mergefield) merged in to the data response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Render Status
        api_response = api_instance.get_render(id)
        pprint(api_response)
    except shotstack_sdk.ApiException as e:
        print("Exception when calling EditApi->get_render: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Render Status
        api_response = api_instance.get_render(id, data=data, merged=merged)
        pprint(api_response)
    except shotstack_sdk.ApiException as e:
        print("Exception when calling EditApi->get_render: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the timeline render task in UUID format |
 **data** | **bool**| Include the data parameter in the response. The data parameter includes the original timeline, output and other settings sent to the API.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; the default is currently &#x60;true&#x60;, this is deprecated and the default will soon be &#x60;false&#x60;. If you rely on the data being returned in the response you should explicitly set the parameter to &#x60;true&#x60;. | [optional]
 **merged** | **bool**| Used when data is set to true, it will show the [merge fields](#tocs_mergefield) merged in to the data response. | [optional]

### Return type

[**RenderResponse**](RenderResponse.md)

### Authorization

[DeveloperKey](../README.md#DeveloperKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The render status details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_render**
> QueuedResponse post_render(edit)

Render Asset

Queue and render the contents of a timeline as a video, image or audio file.  **Base URL:** https://api.shotstack.io/{version}

### Example

* Api Key Authentication (DeveloperKey):

```python
import time
import shotstack_sdk
from shotstack_sdk.api import edit_api
from shotstack_sdk.model.queued_response import QueuedResponse
from shotstack_sdk.model.edit import Edit
from pprint import pprint
# Defining the host is optional and defaults to https://api.shotstack.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = shotstack_sdk.Configuration(
    host = "https://api.shotstack.io/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: DeveloperKey
configuration.api_key['DeveloperKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['DeveloperKey'] = 'Bearer'

# Enter a context with an instance of the API client
with shotstack_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edit_api.EditApi(api_client)
    edit = Edit(
        timeline=Timeline(
            soundtrack=Soundtrack(
                src="https://s3-ap-northeast-1.amazonaws.com/my-bucket/music.mp3",
                effect="fadeIn",
                volume=1,
            ),
            background="#000000",
            fonts=[
                Font(
                    src="https://s3-ap-northeast-1.amazonaws.com/my-bucket/open-sans.ttf",
                ),
            ],
            tracks=[
                Track(
                    clips=[
                        Clip(
                            asset=None,
                            start=2,
                            length=5,
                            fit="crop",
                            scale=0,
                            position="center",
                            offset=Offset(
                                x=0.1,
                                y=-0.2,
                            ),
                            transition=Transition(
                                _in="fade",
                                out="fade",
                            ),
                            effect="zoomIn",
                            filter="greyscale",
                            opacity=1,
                            transform=Transformation(
                                rotate=RotateTransformation(
                                    angle=45,
                                ),
                                skew=SkewTransformation(
                                    x=0.5,
                                    y=0.5,
                                ),
                                flip=FlipTransformation(
                                    horizontal=True,
                                    vertical=True,
                                ),
                            ),
                        ),
                    ],
                ),
            ],
            cache=True,
        ),
        output=Output(
            format="mp4",
            resolution="sd",
            aspect_ratio="16:9",
            size=Size(
                width=1200,
                height=800,
            ),
            fps=25,
            scale_to="preview",
            quality="medium",
            repeat=True,
            range=Range(
                start=3,
                length=6,
            ),
            poster=Poster(
                capture=1,
            ),
            thumbnail=Thumbnail(
                capture=1,
                scale=0.3,
            ),
            destinations=[
                None,
            ],
        ),
        merge=[
            MergeField(
                find="NAME",
                replace=None,
            ),
        ],
        callback="https://my-server.com/callback.php",
        disk="local",
    ) # Edit | The video, image or audio edit specified using JSON.

    # example passing only required values which don't have defaults set
    try:
        # Render Asset
        api_response = api_instance.post_render(edit)
        pprint(api_response)
    except shotstack_sdk.ApiException as e:
        print("Exception when calling EditApi->post_render: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit** | [**Edit**](Edit.md)| The video, image or audio edit specified using JSON. |

### Return type

[**QueuedResponse**](QueuedResponse.md)

### Authorization

[DeveloperKey](../README.md#DeveloperKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The queued render details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **probe**
> ProbeResponse probe(url)

Inspect Media

Inspects any media asset (image, video, audio) on the internet using a hosted version of [FFprobe](https://ffmpeg.org/ffprobe.html). The probe endpoint returns useful information about an asset such as width, height, duration, rotation, framerate, etc...  **Base URL:** https://api.shotstack.io/{version}

### Example

* Api Key Authentication (DeveloperKey):

```python
import time
import shotstack_sdk
from shotstack_sdk.api import edit_api
from shotstack_sdk.model.probe_response import ProbeResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.shotstack.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = shotstack_sdk.Configuration(
    host = "https://api.shotstack.io/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: DeveloperKey
configuration.api_key['DeveloperKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['DeveloperKey'] = 'Bearer'

# Enter a context with an instance of the API client
with shotstack_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edit_api.EditApi(api_client)
    url = "url_example" # str | The URL of the media to inspect, must be **URL encoded**.

    # example passing only required values which don't have defaults set
    try:
        # Inspect Media
        api_response = api_instance.probe(url)
        pprint(api_response)
    except shotstack_sdk.ApiException as e:
        print("Exception when calling EditApi->probe: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| The URL of the media to inspect, must be **URL encoded**. |

### Return type

[**ProbeResponse**](ProbeResponse.md)

### Authorization

[DeveloperKey](../README.md#DeveloperKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | FFprobe response formatted as JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

