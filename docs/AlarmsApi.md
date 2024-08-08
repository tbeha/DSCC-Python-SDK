# dscc.AlarmsApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type2_get_alarms**](AlarmsApi.md#device_type2_get_alarms) | **GET** /api/v1/storage-systems/device-type2/{systemId}/alarms | Get all alarms of Nimble / Alletra 6K
[**device_type2_get_alarms_using_alarm_id**](AlarmsApi.md#device_type2_get_alarms_using_alarm_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/alarms/{alarmId} | Get all alarms of Nimble / Alletra 6K identified by {alarmId}


# **device_type2_get_alarms**
> NimbleAlarmsList device_type2_get_alarms(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all alarms of Nimble / Alletra 6K

Get all alarms of Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_alarms_list import NimbleAlarmsList
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
    api_instance = dscc.AlarmsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter Alarms by Key. (optional)
    sort = 'name desc' # str | Data query to sort Alarm resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all alarms of Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_alarms(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of AlarmsApi->device_type2_get_alarms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlarmsApi->device_type2_get_alarms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter Alarms by Key. | [optional] 
 **sort** | **str**| Data query to sort Alarm resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleAlarmsList**](NimbleAlarmsList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_alarms_using_alarm_id**
> NimbleAlarmsWithRequestUri device_type2_get_alarms_using_alarm_id(system_id, alarm_id, select=select)

Get all alarms of Nimble / Alletra 6K identified by {alarmId}

Get all alarms of Nimble / Alletra 6K identified by {alarmId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_alarms_with_request_uri import NimbleAlarmsWithRequestUri
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
    api_instance = dscc.AlarmsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    alarm_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the Alarm. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all alarms of Nimble / Alletra 6K identified by {alarmId}
        api_response = api_instance.device_type2_get_alarms_using_alarm_id(system_id, alarm_id, select=select)
        print("The response of AlarmsApi->device_type2_get_alarms_using_alarm_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlarmsApi->device_type2_get_alarms_using_alarm_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **alarm_id** | **str**| ID of the Alarm. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleAlarmsWithRequestUri**](NimbleAlarmsWithRequestUri.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

