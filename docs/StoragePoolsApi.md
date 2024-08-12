# dscc.StoragePoolsApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type1_storage_pool_get_by_id**](StoragePoolsApi.md#device_type1_storage_pool_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/storage-pools/{id} | Get details of Primera / Alletra 9K storage-pool identified by {id}
[**device_type1_storage_pool_list**](StoragePoolsApi.md#device_type1_storage_pool_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/storage-pools | Get all storage-pools details by Primera / Alletra 9K
[**device_type1_storage_pool_volume_get_by_id**](StoragePoolsApi.md#device_type1_storage_pool_volume_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/storage-pools/{id}/volumes | Get all volumes for storage-pool identified by {uuid} of Primera / Alletra 9K
[**device_type2_create_pool**](StoragePoolsApi.md#device_type2_create_pool) | **POST** /api/v1/storage-systems/device-type2/{systemId}/storage-pools | Create storage pool from Nimble / Alletra 6K  system identified by {systemId}
[**device_type2_edit_pool_detail_by_id**](StoragePoolsApi.md#device_type2_edit_pool_detail_by_id) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/storage-pools/{storagePoolId} | Edit details of Nimble / Alletra 6K pool identified by {storagePoolId}
[**device_type2_get_all_pool_details**](StoragePoolsApi.md#device_type2_get_all_pool_details) | **GET** /api/v1/storage-systems/device-type2/{systemId}/storage-pools | Get all pools details by Nimble / Alletra 6K
[**device_type2_get_pool_capacity_history**](StoragePoolsApi.md#device_type2_get_pool_capacity_history) | **GET** /api/v1/storage-systems/device-type2/{systemId}/storage-pools/{storagePoolId}/capacity-history | Get storage pool capacity trend data of Nimble / Alletra 6K storage pool identified by {storagePoolId}
[**device_type2_get_pool_detail_by_id**](StoragePoolsApi.md#device_type2_get_pool_detail_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/storage-pools/{storagePoolId} | Get details of Nimble / Alletra 6K pool identified by {storagePoolId}
[**device_type2_get_pool_performance_history**](StoragePoolsApi.md#device_type2_get_pool_performance_history) | **GET** /api/v1/storage-systems/device-type2/{systemId}/storage-pools/{storagePoolId}/performance-history | Get performance trend data of Nimble / Alletra 6K storage pool identified by {storagePoolId}
[**device_type2_get_pool_performance_statistics**](StoragePoolsApi.md#device_type2_get_pool_performance_statistics) | **GET** /api/v1/storage-systems/device-type2/{systemId}/storage-pools/{storagePoolId}/performance-statistics | Get performance statistics of Nimble / Alletra 6K storage pool identified by {storagePoolId}
[**device_type2_get_pools_performance_history**](StoragePoolsApi.md#device_type2_get_pools_performance_history) | **GET** /api/v1/storage-systems/device-type2/{systemId}/pools-performance | Get performance history of Nimble / Alletra 6K Pools
[**device_type2_merge_pool_by_id**](StoragePoolsApi.md#device_type2_merge_pool_by_id) | **POST** /api/v1/storage-systems/device-type2/{systemId}/storage-pools/{storagePoolId}/actions/merge | Merge pool identified by {storagePoolId} from Nimble / Alletra 6K
[**device_type2_remove_pool_by_id**](StoragePoolsApi.md#device_type2_remove_pool_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/storage-pools/{storagePoolId} | Delete pool identified by {storagePoolId} from Nimble / Alletra 6K
[**device_type4_storage_pool_get_by_id**](StoragePoolsApi.md#device_type4_storage_pool_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/storage-pools/{id} | Get details of HPE Alletra Storage MP storage-pool identified by {id}
[**device_type4_storage_pool_list**](StoragePoolsApi.md#device_type4_storage_pool_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/storage-pools | Get all storage-pools details by HPE Alletra Storage MP
[**device_type4_storage_pool_volume_get_by_id**](StoragePoolsApi.md#device_type4_storage_pool_volume_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/storage-pools/{id}/volumes | Get all volumes for storage-pool identified by {uuid} of HPE Alletra Storage MP
[**storage_pool_volumes_list**](StoragePoolsApi.md#storage_pool_volumes_list) | **GET** /api/v1/storage-systems/{systemId}/storage-pools/{id}/volumes | Get all volumes for storage-pool identified by {id}
[**storage_pools_get_by_id**](StoragePoolsApi.md#storage_pools_get_by_id) | **GET** /api/v1/storage-systems/{systemId}/storage-pools/{id} | Get details of storage pools identified by {id}
[**storage_pools_list**](StoragePoolsApi.md#storage_pools_list) | **GET** /api/v1/storage-systems/{systemId}/storage-pools | Get all storage pools for a device {systemId}


# **device_type1_storage_pool_get_by_id**
> PrimeraPoolDetails device_type1_storage_pool_get_by_id(system_id, id, select=select)

Get details of Primera / Alletra 9K storage-pool identified by {id}

Get details of Primera / Alletra 9K storage-pool identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.primera_pool_details import PrimeraPoolDetails
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
    api_instance = dscc.StoragePoolsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = '147c439db3ecb34d1ccccc932d14fd60' # str | Identifier of pool. A 32 digit number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K storage-pool identified by {id}
        api_response = api_instance.device_type1_storage_pool_get_by_id(system_id, id, select=select)
        print("The response of StoragePoolsApi->device_type1_storage_pool_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePoolsApi->device_type1_storage_pool_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| Identifier of pool. A 32 digit number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraPoolDetails**](PrimeraPoolDetails.md)

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
**404** | Pool object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_storage_pool_list**
> PrimeraPoolsSummaryList device_type1_storage_pool_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all storage-pools details by Primera / Alletra 9K

Get all storage-pools details by Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.primera_pools_summary_list import PrimeraPoolsSummaryList
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
    api_instance = dscc.StoragePoolsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq CPG_1' # str | oData query to filter pools by Key. (optional)
    sort = 'name desc' # str | oData query to sort pools by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all storage-pools details by Primera / Alletra 9K
        api_response = api_instance.device_type1_storage_pool_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of StoragePoolsApi->device_type1_storage_pool_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePoolsApi->device_type1_storage_pool_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter pools by Key. | [optional] 
 **sort** | **str**| oData query to sort pools by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraPoolsSummaryList**](PrimeraPoolsSummaryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Pool object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_storage_pool_volume_get_by_id**
> PrimeraVolumesList device_type1_storage_pool_volume_get_by_id(system_id, id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all volumes for storage-pool identified by {uuid} of Primera / Alletra 9K

Get all volumes for storage-pool identified by {uuid} of Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.primera_volumes_list import PrimeraVolumesList
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
    api_instance = dscc.StoragePoolsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = '147c439db3ecb34d1ccccc932d14fd60' # str | Identifier of pool. A 32 digit number.
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq array1 and wwn eq 2FF70002AC018D94' # str | oData query to filter by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all volumes for storage-pool identified by {uuid} of Primera / Alletra 9K
        api_response = api_instance.device_type1_storage_pool_volume_get_by_id(system_id, id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of StoragePoolsApi->device_type1_storage_pool_volume_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePoolsApi->device_type1_storage_pool_volume_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| Identifier of pool. A 32 digit number. | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| oData query to sort by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraVolumesList**](PrimeraVolumesList.md)

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
**404** | Pool object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_create_pool**
> TaskResponse device_type2_create_pool(system_id, nimble_create_pool_input)

Create storage pool from Nimble / Alletra 6K  system identified by {systemId}

Create storage pool from Nimble / Alletra 6K  system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_create_pool_input import NimbleCreatePoolInput
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
    api_instance = dscc.StoragePoolsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    nimble_create_pool_input = dscc.NimbleCreatePoolInput() # NimbleCreatePoolInput | 

    try:
        # Create storage pool from Nimble / Alletra 6K  system identified by {systemId}
        api_response = api_instance.device_type2_create_pool(system_id, nimble_create_pool_input)
        print("The response of StoragePoolsApi->device_type2_create_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePoolsApi->device_type2_create_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_create_pool_input** | [**NimbleCreatePoolInput**](NimbleCreatePoolInput.md)|  | 

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

# **device_type2_edit_pool_detail_by_id**
> TaskResponse device_type2_edit_pool_detail_by_id(system_id, storage_pool_id, nimble_edit_pool_input)

Edit details of Nimble / Alletra 6K pool identified by {storagePoolId}

Edit details of Nimble / Alletra 6K pool identified by {storagePoolId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_edit_pool_input import NimbleEditPoolInput
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
    api_instance = dscc.StoragePoolsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    storage_pool_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | Identifier of pool. A 42 digit hexadecimal number.
    nimble_edit_pool_input = dscc.NimbleEditPoolInput() # NimbleEditPoolInput | 

    try:
        # Edit details of Nimble / Alletra 6K pool identified by {storagePoolId}
        api_response = api_instance.device_type2_edit_pool_detail_by_id(system_id, storage_pool_id, nimble_edit_pool_input)
        print("The response of StoragePoolsApi->device_type2_edit_pool_detail_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePoolsApi->device_type2_edit_pool_detail_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **storage_pool_id** | **str**| Identifier of pool. A 42 digit hexadecimal number. | 
 **nimble_edit_pool_input** | [**NimbleEditPoolInput**](NimbleEditPoolInput.md)|  | 

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

# **device_type2_get_all_pool_details**
> NimblePoolsList device_type2_get_all_pool_details(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all pools details by Nimble / Alletra 6K

Get all pools details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_pools_list import NimblePoolsList
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
    api_instance = dscc.StoragePoolsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter pools by Key. (optional)
    sort = 'name desc' # str | oData query to sort pools resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all pools details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_pool_details(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of StoragePoolsApi->device_type2_get_all_pool_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePoolsApi->device_type2_get_all_pool_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter pools by Key. | [optional] 
 **sort** | **str**| oData query to sort pools resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimblePoolsList**](NimblePoolsList.md)

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

# **device_type2_get_pool_capacity_history**
> PoolCapacityHistory device_type2_get_pool_capacity_history(system_id, storage_pool_id, select=select, range=range, time_interval_min=time_interval_min)

Get storage pool capacity trend data of Nimble / Alletra 6K storage pool identified by {storagePoolId}

Get storage pool capacity trend data of Nimble / Alletra 6K storage pool identified by {storagePoolId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.pool_capacity_history import PoolCapacityHistory
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
    api_instance = dscc.StoragePoolsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    storage_pool_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of storage pool. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)

    try:
        # Get storage pool capacity trend data of Nimble / Alletra 6K storage pool identified by {storagePoolId}
        api_response = api_instance.device_type2_get_pool_capacity_history(system_id, storage_pool_id, select=select, range=range, time_interval_min=time_interval_min)
        print("The response of StoragePoolsApi->device_type2_get_pool_capacity_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePoolsApi->device_type2_get_pool_capacity_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **storage_pool_id** | **str**| Identifier of storage pool. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**PoolCapacityHistory**](PoolCapacityHistory.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_pool_detail_by_id**
> NimblePoolDetailsWithRequestUri device_type2_get_pool_detail_by_id(system_id, storage_pool_id, select=select)

Get details of Nimble / Alletra 6K pool identified by {storagePoolId}

Get details of Nimble / Alletra 6K pool identified by {storagePoolId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_pool_details_with_request_uri import NimblePoolDetailsWithRequestUri
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
    api_instance = dscc.StoragePoolsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    storage_pool_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | Identifier of pool. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Nimble / Alletra 6K pool identified by {storagePoolId}
        api_response = api_instance.device_type2_get_pool_detail_by_id(system_id, storage_pool_id, select=select)
        print("The response of StoragePoolsApi->device_type2_get_pool_detail_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePoolsApi->device_type2_get_pool_detail_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **storage_pool_id** | **str**| Identifier of pool. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimblePoolDetailsWithRequestUri**](NimblePoolDetailsWithRequestUri.md)

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
**404** | Pool object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_pool_performance_history**
> StoragePoolPerformanceHistory device_type2_get_pool_performance_history(system_id, storage_pool_id, select=select, range=range, time_interval_min=time_interval_min)

Get performance trend data of Nimble / Alletra 6K storage pool identified by {storagePoolId}

Get performance trend data of Nimble / Alletra 6K storage pool identified by {storagePoolId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.storage_pool_performance_history import StoragePoolPerformanceHistory
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
    api_instance = dscc.StoragePoolsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    storage_pool_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of storage pool. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)

    try:
        # Get performance trend data of Nimble / Alletra 6K storage pool identified by {storagePoolId}
        api_response = api_instance.device_type2_get_pool_performance_history(system_id, storage_pool_id, select=select, range=range, time_interval_min=time_interval_min)
        print("The response of StoragePoolsApi->device_type2_get_pool_performance_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePoolsApi->device_type2_get_pool_performance_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **storage_pool_id** | **str**| Identifier of storage pool. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**StoragePoolPerformanceHistory**](StoragePoolPerformanceHistory.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_pool_performance_statistics**
> StoragePoolPerformance device_type2_get_pool_performance_statistics(system_id, storage_pool_id, select=select)

Get performance statistics of Nimble / Alletra 6K storage pool identified by {storagePoolId}

Get performance statistics of Nimble / Alletra 6K storage pool identified by {storagePoolId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.storage_pool_performance import StoragePoolPerformance
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
    api_instance = dscc.StoragePoolsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    storage_pool_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of storage pool. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get performance statistics of Nimble / Alletra 6K storage pool identified by {storagePoolId}
        api_response = api_instance.device_type2_get_pool_performance_statistics(system_id, storage_pool_id, select=select)
        print("The response of StoragePoolsApi->device_type2_get_pool_performance_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePoolsApi->device_type2_get_pool_performance_statistics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **storage_pool_id** | **str**| Identifier of storage pool. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**StoragePoolPerformance**](StoragePoolPerformance.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_pools_performance_history**
> NimblePerformanceHistoryData device_type2_get_pools_performance_history(system_id, range=range, time_interval_min=time_interval_min, compare_by=compare_by, filter=filter, metric_type=metric_type)

Get performance history of Nimble / Alletra 6K Pools

Get performance history of Nimble / Alletra 6K Pools

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_performance_history_data import NimblePerformanceHistoryData
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
    api_instance = dscc.StoragePoolsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)
    compare_by = 'top eq 5 and metrics eq READ_IOPS' # str | compareBy will define top and compare metrics for which query has to be made (optional)
    filter = 'vvname in (vvname1,vvname2,vvname3) ,deviceName in (cage1)' # str | filter will define objects to be filtered (optional)
    metric_type = 'IOPS,LATENCY,THROUGHPUT' # str | metricTypes will define comma separated metrics (optional)

    try:
        # Get performance history of Nimble / Alletra 6K Pools
        api_response = api_instance.device_type2_get_pools_performance_history(system_id, range=range, time_interval_min=time_interval_min, compare_by=compare_by, filter=filter, metric_type=metric_type)
        print("The response of StoragePoolsApi->device_type2_get_pools_performance_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePoolsApi->device_type2_get_pools_performance_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 
 **compare_by** | **str**| compareBy will define top and compare metrics for which query has to be made | [optional] 
 **filter** | **str**| filter will define objects to be filtered | [optional] 
 **metric_type** | **str**| metricTypes will define comma separated metrics | [optional] 

### Return type

[**NimblePerformanceHistoryData**](NimblePerformanceHistoryData.md)

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
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_merge_pool_by_id**
> TaskResponse device_type2_merge_pool_by_id(system_id, storage_pool_id, nimble_merge_pool_input)

Merge pool identified by {storagePoolId} from Nimble / Alletra 6K

Merge pool identified by {storagePoolId} from Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_merge_pool_input import NimbleMergePoolInput
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
    api_instance = dscc.StoragePoolsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    storage_pool_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | Identifier of pool. A 42 digit hexadecimal number.
    nimble_merge_pool_input = dscc.NimbleMergePoolInput() # NimbleMergePoolInput | 

    try:
        # Merge pool identified by {storagePoolId} from Nimble / Alletra 6K
        api_response = api_instance.device_type2_merge_pool_by_id(system_id, storage_pool_id, nimble_merge_pool_input)
        print("The response of StoragePoolsApi->device_type2_merge_pool_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePoolsApi->device_type2_merge_pool_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **storage_pool_id** | **str**| Identifier of pool. A 42 digit hexadecimal number. | 
 **nimble_merge_pool_input** | [**NimbleMergePoolInput**](NimbleMergePoolInput.md)|  | 

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

# **device_type2_remove_pool_by_id**
> TaskResponse device_type2_remove_pool_by_id(system_id, storage_pool_id)

Delete pool identified by {storagePoolId} from Nimble / Alletra 6K

Delete pool identified by {storagePoolId} from Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
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
    api_instance = dscc.StoragePoolsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    storage_pool_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | Identifier of pool. A 42 digit hexadecimal number.

    try:
        # Delete pool identified by {storagePoolId} from Nimble / Alletra 6K
        api_response = api_instance.device_type2_remove_pool_by_id(system_id, storage_pool_id)
        print("The response of StoragePoolsApi->device_type2_remove_pool_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePoolsApi->device_type2_remove_pool_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **storage_pool_id** | **str**| Identifier of pool. A 42 digit hexadecimal number. | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **device_type4_storage_pool_get_by_id**
> DeviceType4PoolDetails device_type4_storage_pool_get_by_id(system_id, id, select=select)

Get details of HPE Alletra Storage MP storage-pool identified by {id}

Get details of HPE Alletra Storage MP storage-pool identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_pool_details import DeviceType4PoolDetails
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
    api_instance = dscc.StoragePoolsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = '147c439db3ecb34d1ccccc932d14fd60' # str | Identifier of pool. A 32 digit number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP storage-pool identified by {id}
        api_response = api_instance.device_type4_storage_pool_get_by_id(system_id, id, select=select)
        print("The response of StoragePoolsApi->device_type4_storage_pool_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePoolsApi->device_type4_storage_pool_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| Identifier of pool. A 32 digit number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4PoolDetails**](DeviceType4PoolDetails.md)

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
**404** | Pool object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_storage_pool_list**
> DeviceType4PoolsSummaryList device_type4_storage_pool_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all storage-pools details by HPE Alletra Storage MP

Get all storage-pools details by HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_pools_summary_list import DeviceType4PoolsSummaryList
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
    api_instance = dscc.StoragePoolsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq CPG_1' # str | oData query to filter pools by Key. (optional)
    sort = 'name desc' # str | oData query to sort pools by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all storage-pools details by HPE Alletra Storage MP
        api_response = api_instance.device_type4_storage_pool_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of StoragePoolsApi->device_type4_storage_pool_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePoolsApi->device_type4_storage_pool_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter pools by Key. | [optional] 
 **sort** | **str**| oData query to sort pools by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4PoolsSummaryList**](DeviceType4PoolsSummaryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Pool object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_storage_pool_volume_get_by_id**
> DeviceType4VolumesList device_type4_storage_pool_volume_get_by_id(system_id, id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all volumes for storage-pool identified by {uuid} of HPE Alletra Storage MP

Get all volumes for storage-pool identified by {uuid} of HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_volumes_list import DeviceType4VolumesList
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
    api_instance = dscc.StoragePoolsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = '147c439db3ecb34d1ccccc932d14fd60' # str | Identifier of pool. A 32 digit number.
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq array1 and wwn eq 2FF70002AC018D94' # str | oData query to filter by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all volumes for storage-pool identified by {uuid} of HPE Alletra Storage MP
        api_response = api_instance.device_type4_storage_pool_volume_get_by_id(system_id, id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of StoragePoolsApi->device_type4_storage_pool_volume_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePoolsApi->device_type4_storage_pool_volume_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| Identifier of pool. A 32 digit number. | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| oData query to sort by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4VolumesList**](DeviceType4VolumesList.md)

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
**404** | Pool object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pool_volumes_list**
> FleetVolumesList storage_pool_volumes_list(system_id, id, select=select)

Get all volumes for storage-pool identified by {id}

Get all volumes for storage-pool identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.fleet_volumes_list import FleetVolumesList
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
    api_instance = dscc.StoragePoolsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = '147c439db3ecb34d1ccccc932d14fd60' # str | Identifier of pool. A 32 digit number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all volumes for storage-pool identified by {id}
        api_response = api_instance.storage_pool_volumes_list(system_id, id, select=select)
        print("The response of StoragePoolsApi->storage_pool_volumes_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePoolsApi->storage_pool_volumes_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| Identifier of pool. A 32 digit number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**FleetVolumesList**](FleetVolumesList.md)

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
**404** | Pool object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pools_get_by_id**
> FleetPoolDetails storage_pools_get_by_id(system_id, id, select=select)

Get details of storage pools identified by {id}

Get details of storage pools identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.fleet_pool_details import FleetPoolDetails
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
    api_instance = dscc.StoragePoolsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = '147c439db3ecb34d1ccccc932d14fd60' # str | Identifier of pool. A 32 digit number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of storage pools identified by {id}
        api_response = api_instance.storage_pools_get_by_id(system_id, id, select=select)
        print("The response of StoragePoolsApi->storage_pools_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePoolsApi->storage_pools_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| Identifier of pool. A 32 digit number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**FleetPoolDetails**](FleetPoolDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pools_list**
> StoragePoolsFleetSummaryList storage_pools_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all storage pools for a device {systemId}

Get all storage pools for a device {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.storage_pools_fleet_summary_list import StoragePoolsFleetSummaryList
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
    api_instance = dscc.StoragePoolsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq CPG_1' # str | oData query to filter pools by Key. (optional)
    sort = 'name desc' # str | oData query to sort pools by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all storage pools for a device {systemId}
        api_response = api_instance.storage_pools_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of StoragePoolsApi->storage_pools_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePoolsApi->storage_pools_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter pools by Key. | [optional] 
 **sort** | **str**| oData query to sort pools by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**StoragePoolsFleetSummaryList**](StoragePoolsFleetSummaryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

