# dscc.SwitchesApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type4_switch_fan_get_by_id**](SwitchesApi.md#device_type4_switch_fan_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/switches/{switchId}/switch-fans/{id} | Get details of HPE Alletra Storage MP Switch Fan identified by switchId} and Fan id
[**device_type4_switch_fan_list**](SwitchesApi.md#device_type4_switch_fan_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/switches/{switchId}/switch-fans | Get details of HPE Alletra Storage MP Switch Fans identified by switch id
[**device_type4_switch_locate_by_id**](SwitchesApi.md#device_type4_switch_locate_by_id) | **POST** /api/v1/storage-systems/device-type4/{systemId}/switches/{id} | Locate switch of HPE Alletra Storage MP identified by {id}
[**device_type4_switch_port_get_by_id**](SwitchesApi.md#device_type4_switch_port_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/switches/{switchId}/switch-ports/{id} | Get details of HPE Alletra Storage MP Switch Port identified by {switchId} and {id}
[**device_type4_switch_port_list**](SwitchesApi.md#device_type4_switch_port_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/switches/{switchId}/switch-ports | Get details of HPE Alletra Storage MP Switch ports identified by {switchId}
[**device_type4_switch_ports_list**](SwitchesApi.md#device_type4_switch_ports_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/switch-ports | Get details of HPE Alletra Storage MP Switch ports
[**device_type4_switch_ps_get_by_id**](SwitchesApi.md#device_type4_switch_ps_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/switches/{switchId}/switch-ps/{id} | Get details of HPE Alletra Storage MP Switch Power Supplies identified by {switchId} and {id}
[**device_type4_switch_ps_list**](SwitchesApi.md#device_type4_switch_ps_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/switches/{switchId}/switch-ps | Get details of HPE Alletra Storage MP Switch power supplies identified by {switchId}
[**device_type4_switches_get_by_id**](SwitchesApi.md#device_type4_switches_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/switches/{id} | Get details of HPE Alletra Storage MP Switch identified by {id}
[**device_type4_switches_list**](SwitchesApi.md#device_type4_switches_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/switches | Get details of HPE Alletra Storage MP Switches


# **device_type4_switch_fan_get_by_id**
> DeviceType4SwitchFanDetails device_type4_switch_fan_get_by_id(system_id, switch_id, id, select=select)

Get details of HPE Alletra Storage MP Switch Fan identified by switchId} and Fan id

Get details of HPE Alletra Storage MP Switch Fan identified by switchId and Fan id

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_switch_fan_details import DeviceType4SwitchFanDetails
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
    api_instance = dscc.SwitchesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    switch_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the switch
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the switch fan
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Switch Fan identified by switchId} and Fan id
        api_response = api_instance.device_type4_switch_fan_get_by_id(system_id, switch_id, id, select=select)
        print("The response of SwitchesApi->device_type4_switch_fan_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwitchesApi->device_type4_switch_fan_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **switch_id** | **str**| UID of the switch | 
 **id** | **str**| UID of the switch fan | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4SwitchFanDetails**](DeviceType4SwitchFanDetails.md)

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
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_switch_fan_list**
> DeviceType4SwitchFansSummaryList device_type4_switch_fan_list(system_id, switch_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of HPE Alletra Storage MP Switch Fans identified by switch id

Get details of HPE Alletra Storage MP Switch Fans identified by switch id

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_switch_fans_summary_list import DeviceType4SwitchFansSummaryList
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
    api_instance = dscc.SwitchesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    switch_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the switch
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemWWN eq 2FF70002AC018D94' # str | oData query to filter switch resource by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort switch resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Switch Fans identified by switch id
        api_response = api_instance.device_type4_switch_fan_list(system_id, switch_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of SwitchesApi->device_type4_switch_fan_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwitchesApi->device_type4_switch_fan_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **switch_id** | **str**| UID of the switch | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter switch resource by Key. | [optional] 
 **sort** | **str**| oData query to sort switch resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4SwitchFansSummaryList**](DeviceType4SwitchFansSummaryList.md)

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
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_switch_locate_by_id**
> TaskResponse device_type4_switch_locate_by_id(system_id, id, device_type4_locate_input)

Locate switch of HPE Alletra Storage MP identified by {id}

Locate switch  of HPE Alletra Storage MP identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_locate_input import DeviceType4LocateInput
from dscc.models.task_response import TaskResponse
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
    api_instance = dscc.SwitchesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the switch
    device_type4_locate_input = dscc.DeviceType4LocateInput() # DeviceType4LocateInput | 

    try:
        # Locate switch of HPE Alletra Storage MP identified by {id}
        api_response = api_instance.device_type4_switch_locate_by_id(system_id, id, device_type4_locate_input)
        print("The response of SwitchesApi->device_type4_switch_locate_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwitchesApi->device_type4_switch_locate_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the switch | 
 **device_type4_locate_input** | [**DeviceType4LocateInput**](DeviceType4LocateInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_switch_port_get_by_id**
> DeviceType4SwitchPortDetails device_type4_switch_port_get_by_id(system_id, switch_id, id, select=select)

Get details of HPE Alletra Storage MP Switch Port identified by {switchId} and {id}

Get details of HPE Alletra Storage MP Switch identified by {switchId} and {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_switch_port_details import DeviceType4SwitchPortDetails
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
    api_instance = dscc.SwitchesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    switch_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the switch
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the switch fan
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Switch Port identified by {switchId} and {id}
        api_response = api_instance.device_type4_switch_port_get_by_id(system_id, switch_id, id, select=select)
        print("The response of SwitchesApi->device_type4_switch_port_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwitchesApi->device_type4_switch_port_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **switch_id** | **str**| UID of the switch | 
 **id** | **str**| UID of the switch fan | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4SwitchPortDetails**](DeviceType4SwitchPortDetails.md)

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
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_switch_port_list**
> DeviceType4SwitchPortSummaryList device_type4_switch_port_list(system_id, switch_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of HPE Alletra Storage MP Switch ports identified by {switchId}

Get details of HPE Alletra Storage MP Switch ports identified by {switchId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_switch_port_summary_list import DeviceType4SwitchPortSummaryList
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
    api_instance = dscc.SwitchesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    switch_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the switch
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemWWN eq 2FF70002AC018D94' # str | oData query to filter switch resource by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort switch resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Switch ports identified by {switchId}
        api_response = api_instance.device_type4_switch_port_list(system_id, switch_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of SwitchesApi->device_type4_switch_port_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwitchesApi->device_type4_switch_port_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **switch_id** | **str**| UID of the switch | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter switch resource by Key. | [optional] 
 **sort** | **str**| oData query to sort switch resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4SwitchPortSummaryList**](DeviceType4SwitchPortSummaryList.md)

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
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_switch_ports_list**
> DeviceType4SwitchPortSummaryList device_type4_switch_ports_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of HPE Alletra Storage MP Switch ports

Get details of HPE Alletra Storage MP Switch ports

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_switch_port_summary_list import DeviceType4SwitchPortSummaryList
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
    api_instance = dscc.SwitchesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemWWN eq 2FF70002AC018D94' # str | oData query to filter switch resource by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort switch resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Switch ports
        api_response = api_instance.device_type4_switch_ports_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of SwitchesApi->device_type4_switch_ports_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwitchesApi->device_type4_switch_ports_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter switch resource by Key. | [optional] 
 **sort** | **str**| oData query to sort switch resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4SwitchPortSummaryList**](DeviceType4SwitchPortSummaryList.md)

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
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_switch_ps_get_by_id**
> DeviceType4SwitchPSDetails device_type4_switch_ps_get_by_id(system_id, switch_id, id, select=select)

Get details of HPE Alletra Storage MP Switch Power Supplies identified by {switchId} and {id}

Get details of HPE Alletra Storage MP Switch Power Supplies identified by {switchId} and {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_switch_ps_details import DeviceType4SwitchPSDetails
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
    api_instance = dscc.SwitchesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    switch_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the switch
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the switch fan
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Switch Power Supplies identified by {switchId} and {id}
        api_response = api_instance.device_type4_switch_ps_get_by_id(system_id, switch_id, id, select=select)
        print("The response of SwitchesApi->device_type4_switch_ps_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwitchesApi->device_type4_switch_ps_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **switch_id** | **str**| UID of the switch | 
 **id** | **str**| UID of the switch fan | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4SwitchPSDetails**](DeviceType4SwitchPSDetails.md)

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
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_switch_ps_list**
> DeviceType4SwitchPSSummaryList device_type4_switch_ps_list(system_id, switch_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of HPE Alletra Storage MP Switch power supplies identified by {switchId}

Get details of HPE Alletra Storage MP Switch power supplies identified by {switchId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_switch_ps_summary_list import DeviceType4SwitchPSSummaryList
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
    api_instance = dscc.SwitchesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    switch_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the switch
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemWWN eq 2FF70002AC018D94' # str | oData query to filter switch resource by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort switch resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Switch power supplies identified by {switchId}
        api_response = api_instance.device_type4_switch_ps_list(system_id, switch_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of SwitchesApi->device_type4_switch_ps_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwitchesApi->device_type4_switch_ps_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **switch_id** | **str**| UID of the switch | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter switch resource by Key. | [optional] 
 **sort** | **str**| oData query to sort switch resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4SwitchPSSummaryList**](DeviceType4SwitchPSSummaryList.md)

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
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_switches_get_by_id**
> DeviceType4SwitchDetailedFields device_type4_switches_get_by_id(system_id, id, select=select)

Get details of HPE Alletra Storage MP Switch identified by {id}

Get details of HPE Alletra Storage MP Switch identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_switch_detailed_fields import DeviceType4SwitchDetailedFields
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
    api_instance = dscc.SwitchesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the switch
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Switch identified by {id}
        api_response = api_instance.device_type4_switches_get_by_id(system_id, id, select=select)
        print("The response of SwitchesApi->device_type4_switches_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwitchesApi->device_type4_switches_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the switch | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4SwitchDetailedFields**](DeviceType4SwitchDetailedFields.md)

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
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_switches_list**
> DeviceType4SwitchesSummaryList device_type4_switches_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of HPE Alletra Storage MP Switches

Get details of HPE Alletra Storage MP Switches

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_switches_summary_list import DeviceType4SwitchesSummaryList
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
    api_instance = dscc.SwitchesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemWWN eq 2FF70002AC018D94' # str | oData query to filter switch resource by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort switch resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Switches
        api_response = api_instance.device_type4_switches_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of SwitchesApi->device_type4_switches_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwitchesApi->device_type4_switches_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter switch resource by Key. | [optional] 
 **sort** | **str**| oData query to sort switch resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4SwitchesSummaryList**](DeviceType4SwitchesSummaryList.md)

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
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

