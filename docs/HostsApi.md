# dscc.HostsApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type1_get_all_hosts**](HostsApi.md#device_type1_get_all_hosts) | **GET** /api/v1/storage-systems/device-type1/{systemId}/hosts | Get details of Primera / Alletra 9K Hosts
[**device_type1_get_host_by_id**](HostsApi.md#device_type1_get_host_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/hosts/{hostId} | Get details of Primera / Alletra 9K Host identified by {HostId}
[**device_type4_get_all_hosts**](HostsApi.md#device_type4_get_all_hosts) | **GET** /api/v1/storage-systems/device-type4/{systemId}/hosts | Get details of HPE Alletra Storage MP Hosts
[**device_type4_get_host_by_id**](HostsApi.md#device_type4_get_host_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/hosts/{hostId} | Get details of HPE Alletra Storage MP Host identified by {HostId}


# **device_type1_get_all_hosts**
> PrimeraHostList device_type1_get_all_hosts(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of Primera / Alletra 9K Hosts

Get details of Primera / Alletra 9K Hosts

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.primera_host_list import PrimeraHostList
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
    api_instance = dscc.HostsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter host by Key. (optional)
    sort = 'HostSpeed desc' # str | oData query to sort host resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K Hosts
        api_response = api_instance.device_type1_get_all_hosts(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of HostsApi->device_type1_get_all_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsApi->device_type1_get_all_hosts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter host by Key. | [optional] 
 **sort** | **str**| oData query to sort host resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraHostList**](PrimeraHostList.md)

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

# **device_type1_get_host_by_id**
> PrimeraHosts device_type1_get_host_by_id(system_id, host_id, select=select)

Get details of Primera / Alletra 9K Host identified by {HostId}

Get details of Primera / Alletra 9K Host identified by {HostId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.primera_hosts import PrimeraHosts
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
    api_instance = dscc.HostsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    host_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the primera Host Set. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K Host identified by {HostId}
        api_response = api_instance.device_type1_get_host_by_id(system_id, host_id, select=select)
        print("The response of HostsApi->device_type1_get_host_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsApi->device_type1_get_host_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **host_id** | **str**| ID of the primera Host Set. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraHosts**](PrimeraHosts.md)

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

# **device_type4_get_all_hosts**
> DeviceType4HostList device_type4_get_all_hosts(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of HPE Alletra Storage MP Hosts

Get details of HPE Alletra Storage MP Hosts

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_host_list import DeviceType4HostList
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
    api_instance = dscc.HostsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter host by Key. (optional)
    sort = 'HostSpeed desc' # str | oData query to sort host resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Hosts
        api_response = api_instance.device_type4_get_all_hosts(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of HostsApi->device_type4_get_all_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsApi->device_type4_get_all_hosts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter host by Key. | [optional] 
 **sort** | **str**| oData query to sort host resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4HostList**](DeviceType4HostList.md)

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

# **device_type4_get_host_by_id**
> DeviceType4Hosts device_type4_get_host_by_id(system_id, host_id, select=select)

Get details of HPE Alletra Storage MP Host identified by {HostId}

Get details of HPE Alletra Storage MP Host identified by {HostId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_hosts import DeviceType4Hosts
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
    api_instance = dscc.HostsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    host_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the HPE Alletra Storage MP Host Set. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Host identified by {HostId}
        api_response = api_instance.device_type4_get_host_by_id(system_id, host_id, select=select)
        print("The response of HostsApi->device_type4_get_host_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsApi->device_type4_get_host_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **host_id** | **str**| ID of the HPE Alletra Storage MP Host Set. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4Hosts**](DeviceType4Hosts.md)

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

