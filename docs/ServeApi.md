# shotstack_sdk.ServeApi

All URIs are relative to *https://api.shotstack.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_asset**](ServeApi.md#delete_asset) | **DELETE** /assets/{id} | Delete Asset
[**get_asset**](ServeApi.md#get_asset) | **GET** /assets/{id} | Get Asset
[**get_asset_by_render_id**](ServeApi.md#get_asset_by_render_id) | **GET** /assets/render/{id} | Get Asset by Render ID


# **delete_asset**
> delete_asset(id)

Delete Asset

Delete an asset by its asset id. If a render creates multiple assets, such as thumbnail and poster images, each asset must be deleted individually by the asset id.  **Base URL:** https://api.shotstack.io/serve/{version}

### Example

* Api Key Authentication (DeveloperKey):

```python
import time
import shotstack_sdk
from shotstack_sdk.api import serve_api
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
    api_instance = serve_api.ServeApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | The id of the asset in UUID format

    # example passing only required values which don't have defaults set
    try:
        # Delete Asset
        api_instance.delete_asset(id)
    except shotstack_sdk.ApiException as e:
        print("Exception when calling ServeApi->delete_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the asset in UUID format |

### Return type

void (empty response body)

### Authorization

[DeveloperKey](../README.md#DeveloperKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | An empty response signifying the asset has been deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset**
> AssetResponse get_asset(id)

Get Asset

The Serve API is used to interact with, and delete hosted assets including videos, images, audio files,  thumbnails and poster images. Use this endpoint to fetch an asset by asset id. Note that an asset id is unique for each asset and different from the render id.  **Base URL:** https://api.shotstack.io/serve/{version}

### Example

* Api Key Authentication (DeveloperKey):

```python
import time
import shotstack_sdk
from shotstack_sdk.api import serve_api
from shotstack_sdk.model.asset_response import AssetResponse
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
    api_instance = serve_api.ServeApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | The id of the asset in UUID format

    # example passing only required values which don't have defaults set
    try:
        # Get Asset
        api_response = api_instance.get_asset(id)
        pprint(api_response)
    except shotstack_sdk.ApiException as e:
        print("Exception when calling ServeApi->get_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the asset in UUID format |

### Return type

[**AssetResponse**](AssetResponse.md)

### Authorization

[DeveloperKey](../README.md#DeveloperKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get asset by asset id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_by_render_id**
> AssetRenderResponse get_asset_by_render_id(id)

Get Asset by Render ID

A render may generate more than one file, such as a video, thumbnail and poster image. When the assets are created the only known id is the render id returned by the original [render request](#render-video), status  request or webhook. This endpoint lets you look up one or more assets by the render id.  **Base URL:** https://api.shotstack.io/serve/{version}

### Example

* Api Key Authentication (DeveloperKey):

```python
import time
import shotstack_sdk
from shotstack_sdk.api import serve_api
from shotstack_sdk.model.asset_render_response import AssetRenderResponse
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
    api_instance = serve_api.ServeApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | The render id associated with the asset in UUID format

    # example passing only required values which don't have defaults set
    try:
        # Get Asset by Render ID
        api_response = api_instance.get_asset_by_render_id(id)
        pprint(api_response)
    except shotstack_sdk.ApiException as e:
        print("Exception when calling ServeApi->get_asset_by_render_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The render id associated with the asset in UUID format |

### Return type

[**AssetRenderResponse**](AssetRenderResponse.md)

### Authorization

[DeveloperKey](../README.md#DeveloperKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get one or more assets by render id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

