# dscc.HostInitiatorsApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_merge_host**](HostInitiatorsApi.md#bulk_merge_host) | **POST** /api/v1/host-initiators/bulkmerge | Bulk merge hosts into user created host
[**device_type2_get_all_initiators**](HostInitiatorsApi.md#device_type2_get_all_initiators) | **GET** /api/v1/storage-systems/device-type2/{systemId}/host-initiators | Get all nimble initiators details by Nimble / Alletra 6K
[**device_type2_get_initiators_by_id**](HostInitiatorsApi.md#device_type2_get_initiators_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/host-initiators/{hostInitiatorId} | Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorId}
[**device_type2_initiators_create**](HostInitiatorsApi.md#device_type2_initiators_create) | **POST** /api/v1/storage-systems/device-type2/{systemId}/host-initiators | Create Nimble / Alletra 6K nimble initiator in system identified by {systemId}
[**device_type2_remove_initiators_by_id**](HostInitiatorsApi.md#device_type2_remove_initiators_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/host-initiators/{hostInitiatorId} | Remove Nimble Initiator identified by {hostInitiatorId} from Nimble / Alletra 6K
[**find_bulk_merge_candidates_for_hosts**](HostInitiatorsApi.md#find_bulk_merge_candidates_for_hosts) | **GET** /api/v1/host-initiators/bulkmerge | Get the list of hosts which have duplicates
[**get_host_chap_by_id**](HostInitiatorsApi.md#get_host_chap_by_id) | **GET** /api/v1/host-initiators/{hostId}/chap | Get Host CHAP details by {hostId}
[**host_create**](HostInitiatorsApi.md#host_create) | **POST** /api/v1/host-initiators | Create a host
[**host_delete**](HostInitiatorsApi.md#host_delete) | **DELETE** /api/v1/host-initiators/{hostId} | Delete a host by {hostId}
[**host_get_by_id**](HostInitiatorsApi.md#host_get_by_id) | **GET** /api/v1/host-initiators/{hostId} | Get the host details by {hostId}
[**host_initiator_create**](HostInitiatorsApi.md#host_initiator_create) | **POST** /api/v1/initiators | Create initiator
[**host_initiator_delete**](HostInitiatorsApi.md#host_initiator_delete) | **DELETE** /api/v1/initiators/{initiatorId} | Delete initiator by {initiatorId}
[**host_initiator_get_by_id**](HostInitiatorsApi.md#host_initiator_get_by_id) | **GET** /api/v1/initiators/{initiatorId} | Get the initiator details by {initiatorId}
[**host_initiator_list**](HostInitiatorsApi.md#host_initiator_list) | **GET** /api/v1/initiators | Get the list of initiators
[**host_list**](HostInitiatorsApi.md#host_list) | **GET** /api/v1/host-initiators | Get the list of hosts
[**host_update_by_id**](HostInitiatorsApi.md#host_update_by_id) | **PUT** /api/v1/host-initiators/{hostId} | Update Host by {hostId}
[**host_volume_performance_history_get**](HostInitiatorsApi.md#host_volume_performance_history_get) | **GET** /api/v1/host-initiators/{hostId}/storage-performance-history | Get the volume performance history data associated with a host identified by {uid}
[**host_volumes_get**](HostInitiatorsApi.md#host_volumes_get) | **GET** /api/v1/host-initiators/{hostId}/volumes | Get details of volumes associated with a host identified by {uid}
[**merge_host**](HostInitiatorsApi.md#merge_host) | **POST** /api/v1/host-initiators/merge | Merge hosts into user created host
[**update_host_chap_by_id**](HostInitiatorsApi.md#update_host_chap_by_id) | **PUT** /api/v1/host-initiators/{hostId}/chap | Update Host CHAP by {hostId}


# **bulk_merge_host**
> BulkMergeOutput bulk_merge_host(create_bulk_merge_candidates)

Bulk merge hosts into user created host

Bulk Merge hosts into user created host

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.bulk_merge_output import BulkMergeOutput
from dscc.models.create_bulk_merge_candidates import CreateBulkMergeCandidates
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
    api_instance = dscc.HostInitiatorsApi(api_client)
    create_bulk_merge_candidates = dscc.CreateBulkMergeCandidates() # CreateBulkMergeCandidates | 

    try:
        # Bulk merge hosts into user created host
        api_response = api_instance.bulk_merge_host(create_bulk_merge_candidates)
        print("The response of HostInitiatorsApi->bulk_merge_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorsApi->bulk_merge_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_bulk_merge_candidates** | [**CreateBulkMergeCandidates**](CreateBulkMergeCandidates.md)|  | 

### Return type

[**BulkMergeOutput**](BulkMergeOutput.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_all_initiators**
> NimbleInitiatorsList device_type2_get_all_initiators(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all nimble initiators details by Nimble / Alletra 6K

Get all nimble initiators details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_initiators_list import NimbleInitiatorsList
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
    api_instance = dscc.HostInitiatorsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter initiators by Key. (optional)
    sort = 'initiator_group_name desc' # str | oData query to sort initiators resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all nimble initiators details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_initiators(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of HostInitiatorsApi->device_type2_get_all_initiators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorsApi->device_type2_get_all_initiators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter initiators by Key. | [optional] 
 **sort** | **str**| oData query to sort initiators resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleInitiatorsList**](NimbleInitiatorsList.md)

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

# **device_type2_get_initiators_by_id**
> NimbleInitiatorDetails device_type2_get_initiators_by_id(system_id, host_initiator_id, select=select)

Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorId}

Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_initiator_details import NimbleInitiatorDetails
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
    api_instance = dscc.HostInitiatorsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    host_initiator_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the nimble initiator. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorId}
        api_response = api_instance.device_type2_get_initiators_by_id(system_id, host_initiator_id, select=select)
        print("The response of HostInitiatorsApi->device_type2_get_initiators_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorsApi->device_type2_get_initiators_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **host_initiator_id** | **str**| ID of the nimble initiator. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleInitiatorDetails**](NimbleInitiatorDetails.md)

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

# **device_type2_initiators_create**
> TaskResponse device_type2_initiators_create(system_id, nimble_create_initiator_input)

Create Nimble / Alletra 6K nimble initiator in system identified by {systemId}

Get all nimble initiators details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_create_initiator_input import NimbleCreateInitiatorInput
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
    api_instance = dscc.HostInitiatorsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    nimble_create_initiator_input = dscc.NimbleCreateInitiatorInput() # NimbleCreateInitiatorInput | 

    try:
        # Create Nimble / Alletra 6K nimble initiator in system identified by {systemId}
        api_response = api_instance.device_type2_initiators_create(system_id, nimble_create_initiator_input)
        print("The response of HostInitiatorsApi->device_type2_initiators_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorsApi->device_type2_initiators_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_create_initiator_input** | [**NimbleCreateInitiatorInput**](NimbleCreateInitiatorInput.md)|  | 

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

# **device_type2_remove_initiators_by_id**
> TaskResponse device_type2_remove_initiators_by_id(system_id, host_initiator_id)

Remove Nimble Initiator identified by {hostInitiatorId} from Nimble / Alletra 6K

Remove Nimble Initiator identified by {hostInitiatorId} from Nimble / Alletra 6K

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
    api_instance = dscc.HostInitiatorsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    host_initiator_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of Host Initiator. A 42 digit hexadecimal number.

    try:
        # Remove Nimble Initiator identified by {hostInitiatorId} from Nimble / Alletra 6K
        api_response = api_instance.device_type2_remove_initiators_by_id(system_id, host_initiator_id)
        print("The response of HostInitiatorsApi->device_type2_remove_initiators_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorsApi->device_type2_remove_initiators_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **host_initiator_id** | **str**| Identifier of Host Initiator. A 42 digit hexadecimal number. | 

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

# **find_bulk_merge_candidates_for_hosts**
> BulkMergeCandidatesHosts find_bulk_merge_candidates_for_hosts()

Get the list of hosts which have duplicates

Get the list of hosts which have identical duplicates or are unique across different systems.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.bulk_merge_candidates_hosts import BulkMergeCandidatesHosts
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
    api_instance = dscc.HostInitiatorsApi(api_client)

    try:
        # Get the list of hosts which have duplicates
        api_response = api_instance.find_bulk_merge_candidates_for_hosts()
        print("The response of HostInitiatorsApi->find_bulk_merge_candidates_for_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorsApi->find_bulk_merge_candidates_for_hosts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BulkMergeCandidatesHosts**](BulkMergeCandidatesHosts.md)

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

# **get_host_chap_by_id**
> HostChapDetails get_host_chap_by_id(host_id)

Get Host CHAP details by {hostId}

Get Host CHAP details by {hostId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.host_chap_details import HostChapDetails
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
    api_instance = dscc.HostInitiatorsApi(api_client)
    host_id = '2b09e744496246859fde6c132b2091d3' # str | Id of the Host.

    try:
        # Get Host CHAP details by {hostId}
        api_response = api_instance.get_host_chap_by_id(host_id)
        print("The response of HostInitiatorsApi->get_host_chap_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorsApi->get_host_chap_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| Id of the Host. | 

### Return type

[**HostChapDetails**](HostChapDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * ETag - System settings configuration information <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_create**
> HostObjectDetails host_create(create_host_input)

Create a host

Create a host with same protocol initiators

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.create_host_input import CreateHostInput
from dscc.models.host_object_details import HostObjectDetails
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
    api_instance = dscc.HostInitiatorsApi(api_client)
    create_host_input = dscc.CreateHostInput() # CreateHostInput | 

    try:
        # Create a host
        api_response = api_instance.host_create(create_host_input)
        print("The response of HostInitiatorsApi->host_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorsApi->host_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_host_input** | [**CreateHostInput**](CreateHostInput.md)|  | 

### Return type

[**HostObjectDetails**](HostObjectDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_delete**
> TaskResponse host_delete(host_id, force=force, delete_associated_empty_host_group=delete_associated_empty_host_group)

Delete a host by {hostId}

Delete a host by {hostId}

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
    api_instance = dscc.HostInitiatorsApi(api_client)
    host_id = '2b09e744496246859fde6c132b2091d3' # str | Id of the Host.
    force = true # bool | Forceful delete option (optional)
    delete_associated_empty_host_group = true # bool | Delete the resulting empty host group associated to this host option (optional)

    try:
        # Delete a host by {hostId}
        api_response = api_instance.host_delete(host_id, force=force, delete_associated_empty_host_group=delete_associated_empty_host_group)
        print("The response of HostInitiatorsApi->host_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorsApi->host_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| Id of the Host. | 
 **force** | **bool**| Forceful delete option | [optional] 
 **delete_associated_empty_host_group** | **bool**| Delete the resulting empty host group associated to this host option | [optional] 

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

# **host_get_by_id**
> HostDetails host_get_by_id(host_id)

Get the host details by {hostId}

Get the host details by {hostId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.host_details import HostDetails
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
    api_instance = dscc.HostInitiatorsApi(api_client)
    host_id = '2b09e744496246859fde6c132b2091d3' # str | Id of the Host.

    try:
        # Get the host details by {hostId}
        api_response = api_instance.host_get_by_id(host_id)
        print("The response of HostInitiatorsApi->host_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorsApi->host_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| Id of the Host. | 

### Return type

[**HostDetails**](HostDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * ETag - System settings configuration information <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_initiator_create**
> Initiator host_initiator_create(initiator_input)

Create initiator

Create initiator

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.initiator import Initiator
from dscc.models.initiator_input import InitiatorInput
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
    api_instance = dscc.HostInitiatorsApi(api_client)
    initiator_input = dscc.InitiatorInput() # InitiatorInput | 

    try:
        # Create initiator
        api_response = api_instance.host_initiator_create(initiator_input)
        print("The response of HostInitiatorsApi->host_initiator_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorsApi->host_initiator_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **initiator_input** | [**InitiatorInput**](InitiatorInput.md)|  | 

### Return type

[**Initiator**](Initiator.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_initiator_delete**
> DeleteInitiator host_initiator_delete(initiator_id)

Delete initiator by {initiatorId}

Delete initiator by {initiatorId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.delete_initiator import DeleteInitiator
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
    api_instance = dscc.HostInitiatorsApi(api_client)
    initiator_id = 'e789e756496246859fde6c132b2091d3' # str | UID of Initiator.

    try:
        # Delete initiator by {initiatorId}
        api_response = api_instance.host_initiator_delete(initiator_id)
        print("The response of HostInitiatorsApi->host_initiator_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorsApi->host_initiator_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **initiator_id** | **str**| UID of Initiator. | 

### Return type

[**DeleteInitiator**](DeleteInitiator.md)

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

# **host_initiator_get_by_id**
> InitiatorDetails host_initiator_get_by_id(initiator_id)

Get the initiator details by {initiatorId}

Get the initiator details by {initiatorId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.initiator_details import InitiatorDetails
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
    api_instance = dscc.HostInitiatorsApi(api_client)
    initiator_id = 'e789e756496246859fde6c132b2091d3' # str | UID of Initiator.

    try:
        # Get the initiator details by {initiatorId}
        api_response = api_instance.host_initiator_get_by_id(initiator_id)
        print("The response of HostInitiatorsApi->host_initiator_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorsApi->host_initiator_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **initiator_id** | **str**| UID of Initiator. | 

### Return type

[**InitiatorDetails**](InitiatorDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * ETag - System settings configuration information <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_initiator_list**
> InitiatorList host_initiator_list(filter=filter, sort=sort, limit=limit, offset=offset)

Get the list of initiators

Get the list of initiators

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.initiator_list import InitiatorList
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
    api_instance = dscc.HostInitiatorsApi(api_client)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | oData query to filter hostservice by Key. (optional)
    sort = 'name desc' # str | oData query to sort hostservice by Key. (optional)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)

    try:
        # Get the list of initiators
        api_response = api_instance.host_initiator_list(filter=filter, sort=sort, limit=limit, offset=offset)
        print("The response of HostInitiatorsApi->host_initiator_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorsApi->host_initiator_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| oData query to filter hostservice by Key. | [optional] 
 **sort** | **str**| oData query to sort hostservice by Key. | [optional] 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 

### Return type

[**InitiatorList**](InitiatorList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * ETag - System settings configuration information <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_list**
> HostsList host_list(filter=filter, sort=sort, limit=limit, offset=offset)

Get the list of hosts

Get the list of hosts

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.hosts_list import HostsList
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
    api_instance = dscc.HostInitiatorsApi(api_client)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | oData query to filter hostservice by Key. (optional)
    sort = 'name desc' # str | oData query to sort hostservice by Key. (optional)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)

    try:
        # Get the list of hosts
        api_response = api_instance.host_list(filter=filter, sort=sort, limit=limit, offset=offset)
        print("The response of HostInitiatorsApi->host_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorsApi->host_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| oData query to filter hostservice by Key. | [optional] 
 **sort** | **str**| oData query to sort hostservice by Key. | [optional] 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 

### Return type

[**HostsList**](HostsList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * ETag - System settings configuration information <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_update_by_id**
> TaskResponse host_update_by_id(host_id, update_host_input)

Update Host by {hostId}

Update host details by {hostId}. Host can only be updated with the same protocol initiators

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.models.update_host_input import UpdateHostInput
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
    api_instance = dscc.HostInitiatorsApi(api_client)
    host_id = '2b09e744496246859fde6c132b2091d3' # str | Id of the Host.
    update_host_input = dscc.UpdateHostInput() # UpdateHostInput | 

    try:
        # Update Host by {hostId}
        api_response = api_instance.host_update_by_id(host_id, update_host_input)
        print("The response of HostInitiatorsApi->host_update_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorsApi->host_update_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| Id of the Host. | 
 **update_host_input** | [**UpdateHostInput**](UpdateHostInput.md)|  | 

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

# **host_volume_performance_history_get**
> HostStoragePerformanceHistory host_volume_performance_history_get(host_id, select=select, range=range, time_interval_min=time_interval_min, top_volumes_count=top_volumes_count)

Get the volume performance history data associated with a host identified by {uid}

Get the volume performance history data associated with a host identified by {uid}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.host_storage_performance_history import HostStoragePerformanceHistory
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
    api_instance = dscc.HostInitiatorsApi(api_client)
    host_id = '2b09e744496246859fde6c132b2091d3' # str | Id of the Host.
    select = 'latencyMetricsDataMs' # str | Query to select only the required parameters, separated by . if nested (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 1440 # int | It defines granularity in minutes. (optional)
    top_volumes_count = 5 # int | The number of top volumes to be returned, by default it will be 5 (optional)

    try:
        # Get the volume performance history data associated with a host identified by {uid}
        api_response = api_instance.host_volume_performance_history_get(host_id, select=select, range=range, time_interval_min=time_interval_min, top_volumes_count=top_volumes_count)
        print("The response of HostInitiatorsApi->host_volume_performance_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorsApi->host_volume_performance_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| Id of the Host. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 
 **top_volumes_count** | **int**| The number of top volumes to be returned, by default it will be 5 | [optional] 

### Return type

[**HostStoragePerformanceHistory**](HostStoragePerformanceHistory.md)

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

# **host_volumes_get**
> HostStorageVolumes host_volumes_get(host_id, select=select)

Get details of volumes associated with a host identified by {uid}

Get details of volumes associated with a host identified by {uid}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.host_storage_volumes import HostStorageVolumes
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
    api_instance = dscc.HostInitiatorsApi(api_client)
    host_id = '2b09e744496246859fde6c132b2091d3' # str | Id of the Host.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of volumes associated with a host identified by {uid}
        api_response = api_instance.host_volumes_get(host_id, select=select)
        print("The response of HostInitiatorsApi->host_volumes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorsApi->host_volumes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| Id of the Host. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**HostStorageVolumes**](HostStorageVolumes.md)

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

# **merge_host**
> TaskResponse merge_host(validate_merge_object)

Merge hosts into user created host

Merge hosts into user created host

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.models.validate_merge_object import ValidateMergeObject
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
    api_instance = dscc.HostInitiatorsApi(api_client)
    validate_merge_object = dscc.ValidateMergeObject() # ValidateMergeObject | 

    try:
        # Merge hosts into user created host
        api_response = api_instance.merge_host(validate_merge_object)
        print("The response of HostInitiatorsApi->merge_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorsApi->merge_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_merge_object** | [**ValidateMergeObject**](ValidateMergeObject.md)|  | 

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
**202** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_host_chap_by_id**
> TaskResponse update_host_chap_by_id(host_id, update_host_chap_input)

Update Host CHAP by {hostId}

Update Host CHAP details by {hostId}. Only iSCSI Host can be updated.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.models.update_host_chap_input import UpdateHostChapInput
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
    api_instance = dscc.HostInitiatorsApi(api_client)
    host_id = '2b09e744496246859fde6c132b2091d3' # str | Id of the Host.
    update_host_chap_input = dscc.UpdateHostChapInput() # UpdateHostChapInput | 

    try:
        # Update Host CHAP by {hostId}
        api_response = api_instance.update_host_chap_by_id(host_id, update_host_chap_input)
        print("The response of HostInitiatorsApi->update_host_chap_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorsApi->update_host_chap_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| Id of the Host. | 
 **update_host_chap_input** | [**UpdateHostChapInput**](UpdateHostChapInput.md)|  | 

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

