# dscc.HealthStatusApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type2_get_health_status**](HealthStatusApi.md#device_type2_get_health_status) | **GET** /api/v1/storage-systems/device-type2/{systemId}/health-status | Get details of  Nimble / Alletra 6K health status
[**device_type2_get_health_status_using_health_id**](HealthStatusApi.md#device_type2_get_health_status_using_health_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/health-status/{healthStatusId} | Get details of  Nimble / Alletra 6K health status identified by {healthStatusId}


# **device_type2_get_health_status**
> NimbleHealthStatusList device_type2_get_health_status(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of  Nimble / Alletra 6K health status

Get details of  Nimble / Alletra 6K health status

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_health_status_list import NimbleHealthStatusList
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.HealthStatusApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter health status by Key. (optional)
    sort = 'scope desc' # str | oData query to sort health status resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of  Nimble / Alletra 6K health status
        api_response = api_instance.device_type2_get_health_status(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of HealthStatusApi->device_type2_get_health_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthStatusApi->device_type2_get_health_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter health status by Key. | [optional] 
 **sort** | **str**| oData query to sort health status resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleHealthStatusList**](NimbleHealthStatusList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage group object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_health_status_using_health_id**
> NimbleHealthStatusDetailsWithRequestUri device_type2_get_health_status_using_health_id(system_id, health_status_id, select=select)

Get details of  Nimble / Alletra 6K health status identified by {healthStatusId}

Get details of Nimble / Alletra 6K health status identified by {healthStatusId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_health_status_details_with_request_uri import NimbleHealthStatusDetailsWithRequestUri
from dscc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dscc.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = dscc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.HealthStatusApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    health_status_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | Identifier of health status. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of  Nimble / Alletra 6K health status identified by {healthStatusId}
        api_response = api_instance.device_type2_get_health_status_using_health_id(system_id, health_status_id, select=select)
        print("The response of HealthStatusApi->device_type2_get_health_status_using_health_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthStatusApi->device_type2_get_health_status_using_health_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **health_status_id** | **str**| Identifier of health status. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleHealthStatusDetailsWithRequestUri**](NimbleHealthStatusDetailsWithRequestUri.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | network settings object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

