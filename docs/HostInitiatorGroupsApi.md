# dscc.HostInitiatorGroupsApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_merge_host_group**](HostInitiatorGroupsApi.md#bulk_merge_host_group) | **POST** /api/v1/host-initiator-groups/bulkmerge | Bulk merge hosts into user created host
[**device_type2_get_all_host_initiator_groups**](HostInitiatorGroupsApi.md#device_type2_get_all_host_initiator_groups) | **GET** /api/v1/storage-systems/device-type2/{systemId}/host-groups | Get all nimble host initiator groups details by Nimble / Alletra 6K
[**device_type2_get_host_initiator_group_by_id**](HostInitiatorGroupsApi.md#device_type2_get_host_initiator_group_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/host-groups/{hostInitiatorGroupId} | Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorGroupId}
[**device_type2_host_initiator_group_create**](HostInitiatorGroupsApi.md#device_type2_host_initiator_group_create) | **POST** /api/v1/storage-systems/device-type2/{systemId}/host-groups | Create Nimble / Alletra 6K initiator group in system identified by {systemId}
[**device_type2_remove_host_initiator_group_by_id**](HostInitiatorGroupsApi.md#device_type2_remove_host_initiator_group_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/host-groups/{hostInitiatorGroupId} | Remove initiator-groups identified by {hostInitiatorGroupId} from Nimble / Alletra 6K
[**device_type2_update_host_initiator_group_by_id**](HostInitiatorGroupsApi.md#device_type2_update_host_initiator_group_by_id) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/host-groups/{hostInitiatorGroupId} | Update initiator-groups identified by {hostInitiatorGroupId}
[**find_bulk_merge_candidates_for_host_groups**](HostInitiatorGroupsApi.md#find_bulk_merge_candidates_for_host_groups) | **GET** /api/v1/host-initiator-groups/bulkmerge | Get the list of host groups which have duplicates
[**host_group_create**](HostInitiatorGroupsApi.md#host_group_create) | **POST** /api/v1/host-initiator-groups | Create a host group
[**host_group_delete**](HostInitiatorGroupsApi.md#host_group_delete) | **DELETE** /api/v1/host-initiator-groups/{hostGroupId} | Delete a host group by {hostGroupId}
[**host_group_get_by_id**](HostInitiatorGroupsApi.md#host_group_get_by_id) | **GET** /api/v1/host-initiator-groups/{hostGroupId} | Get the host group details by {hostGroupId}
[**host_group_list**](HostInitiatorGroupsApi.md#host_group_list) | **GET** /api/v1/host-initiator-groups | Get the list of host groups
[**host_group_merge**](HostInitiatorGroupsApi.md#host_group_merge) | **POST** /api/v1/host-initiator-groups/merge | Merge a host group
[**host_group_update_by_id**](HostInitiatorGroupsApi.md#host_group_update_by_id) | **PUT** /api/v1/host-initiator-groups/{hostGroupId} | Update host group by {hostGroupId}


# **bulk_merge_host_group**
> BulkMergeOutput bulk_merge_host_group(create_bulk_merge_candidates)

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
    api_instance = dscc.HostInitiatorGroupsApi(api_client)
    create_bulk_merge_candidates = dscc.CreateBulkMergeCandidates() # CreateBulkMergeCandidates | 

    try:
        # Bulk merge hosts into user created host
        api_response = api_instance.bulk_merge_host_group(create_bulk_merge_candidates)
        print("The response of HostInitiatorGroupsApi->bulk_merge_host_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorGroupsApi->bulk_merge_host_group: %s\n" % e)
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

# **device_type2_get_all_host_initiator_groups**
> NimbleInitiatorGroupList device_type2_get_all_host_initiator_groups(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all nimble host initiator groups details by Nimble / Alletra 6K

Get all nimble host initiator groups details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_initiator_group_list import NimbleInitiatorGroupList
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
    api_instance = dscc.HostInitiatorGroupsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter initiator groups by Key. (optional)
    sort = 'name desc' # str | oData query to sort initiator groups resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all nimble host initiator groups details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_host_initiator_groups(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of HostInitiatorGroupsApi->device_type2_get_all_host_initiator_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorGroupsApi->device_type2_get_all_host_initiator_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter initiator groups by Key. | [optional] 
 **sort** | **str**| oData query to sort initiator groups resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleInitiatorGroupList**](NimbleInitiatorGroupList.md)

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

# **device_type2_get_host_initiator_group_by_id**
> NimbleInitiatorGroupDetails device_type2_get_host_initiator_group_by_id(system_id, host_initiator_group_id, select=select)

Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorGroupId}

Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorGroupId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_initiator_group_details import NimbleInitiatorGroupDetails
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
    api_instance = dscc.HostInitiatorGroupsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    host_initiator_group_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | Identifier of initiator group. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorGroupId}
        api_response = api_instance.device_type2_get_host_initiator_group_by_id(system_id, host_initiator_group_id, select=select)
        print("The response of HostInitiatorGroupsApi->device_type2_get_host_initiator_group_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorGroupsApi->device_type2_get_host_initiator_group_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **host_initiator_group_id** | **str**| Identifier of initiator group. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleInitiatorGroupDetails**](NimbleInitiatorGroupDetails.md)

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

# **device_type2_host_initiator_group_create**
> TaskResponse device_type2_host_initiator_group_create(system_id, nimble_create_initiator_group_input)

Create Nimble / Alletra 6K initiator group in system identified by {systemId}

Create Nimble / Alletra 6K initiator group in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_create_initiator_group_input import NimbleCreateInitiatorGroupInput
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
    api_instance = dscc.HostInitiatorGroupsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    nimble_create_initiator_group_input = dscc.NimbleCreateInitiatorGroupInput() # NimbleCreateInitiatorGroupInput | 

    try:
        # Create Nimble / Alletra 6K initiator group in system identified by {systemId}
        api_response = api_instance.device_type2_host_initiator_group_create(system_id, nimble_create_initiator_group_input)
        print("The response of HostInitiatorGroupsApi->device_type2_host_initiator_group_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorGroupsApi->device_type2_host_initiator_group_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_create_initiator_group_input** | [**NimbleCreateInitiatorGroupInput**](NimbleCreateInitiatorGroupInput.md)|  | 

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

# **device_type2_remove_host_initiator_group_by_id**
> TaskResponse device_type2_remove_host_initiator_group_by_id(system_id, host_initiator_group_id)

Remove initiator-groups identified by {hostInitiatorGroupId} from Nimble / Alletra 6K

Remove initiator-groups identified by {hostInitiatorGroupId} from Nimble / Alletra 6K

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
    api_instance = dscc.HostInitiatorGroupsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    host_initiator_group_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | Identifier of initiator group. A 42 digit hexadecimal number.

    try:
        # Remove initiator-groups identified by {hostInitiatorGroupId} from Nimble / Alletra 6K
        api_response = api_instance.device_type2_remove_host_initiator_group_by_id(system_id, host_initiator_group_id)
        print("The response of HostInitiatorGroupsApi->device_type2_remove_host_initiator_group_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorGroupsApi->device_type2_remove_host_initiator_group_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **host_initiator_group_id** | **str**| Identifier of initiator group. A 42 digit hexadecimal number. | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_update_host_initiator_group_by_id**
> TaskResponse device_type2_update_host_initiator_group_by_id(system_id, host_initiator_group_id, nimble_edit_initiator_group_input)

Update initiator-groups identified by {hostInitiatorGroupId}

Update initiator-groups identified by {hostInitiatorGroupId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_edit_initiator_group_input import NimbleEditInitiatorGroupInput
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
    api_instance = dscc.HostInitiatorGroupsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    host_initiator_group_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | Identifier of initiator group. A 42 digit hexadecimal number.
    nimble_edit_initiator_group_input = dscc.NimbleEditInitiatorGroupInput() # NimbleEditInitiatorGroupInput | 

    try:
        # Update initiator-groups identified by {hostInitiatorGroupId}
        api_response = api_instance.device_type2_update_host_initiator_group_by_id(system_id, host_initiator_group_id, nimble_edit_initiator_group_input)
        print("The response of HostInitiatorGroupsApi->device_type2_update_host_initiator_group_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorGroupsApi->device_type2_update_host_initiator_group_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **host_initiator_group_id** | **str**| Identifier of initiator group. A 42 digit hexadecimal number. | 
 **nimble_edit_initiator_group_input** | [**NimbleEditInitiatorGroupInput**](NimbleEditInitiatorGroupInput.md)|  | 

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

# **find_bulk_merge_candidates_for_host_groups**
> BulkMergeCandidates find_bulk_merge_candidates_for_host_groups()

Get the list of host groups which have duplicates

Get the list of host groups which have identical duplicates or are unique across different systems.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.bulk_merge_candidates import BulkMergeCandidates
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
    api_instance = dscc.HostInitiatorGroupsApi(api_client)

    try:
        # Get the list of host groups which have duplicates
        api_response = api_instance.find_bulk_merge_candidates_for_host_groups()
        print("The response of HostInitiatorGroupsApi->find_bulk_merge_candidates_for_host_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorGroupsApi->find_bulk_merge_candidates_for_host_groups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BulkMergeCandidates**](BulkMergeCandidates.md)

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

# **host_group_create**
> HostGroupObjectDetails host_group_create(create_host_group_input)

Create a host group

Create a host group with hosts having same protocol initiators

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.create_host_group_input import CreateHostGroupInput
from dscc.models.host_group_object_details import HostGroupObjectDetails
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
    api_instance = dscc.HostInitiatorGroupsApi(api_client)
    create_host_group_input = dscc.CreateHostGroupInput() # CreateHostGroupInput | 

    try:
        # Create a host group
        api_response = api_instance.host_group_create(create_host_group_input)
        print("The response of HostInitiatorGroupsApi->host_group_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorGroupsApi->host_group_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_host_group_input** | [**CreateHostGroupInput**](CreateHostGroupInput.md)|  | 

### Return type

[**HostGroupObjectDetails**](HostGroupObjectDetails.md)

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

# **host_group_delete**
> TaskResponse host_group_delete(host_group_id, force=force)

Delete a host group by {hostGroupId}

Delete a host group by {hostGroupId}

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
    api_instance = dscc.HostInitiatorGroupsApi(api_client)
    host_group_id = 'e789e756496246859fde6c132b2091d3' # str | Id of the host Group.
    force = true # bool | Forceful delete option (optional)

    try:
        # Delete a host group by {hostGroupId}
        api_response = api_instance.host_group_delete(host_group_id, force=force)
        print("The response of HostInitiatorGroupsApi->host_group_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorGroupsApi->host_group_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_group_id** | **str**| Id of the host Group. | 
 **force** | **bool**| Forceful delete option | [optional] 

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

# **host_group_get_by_id**
> HostGroupDetails host_group_get_by_id(host_group_id)

Get the host group details by {hostGroupId}

Get the host group details by {hostGroupId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.host_group_details import HostGroupDetails
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
    api_instance = dscc.HostInitiatorGroupsApi(api_client)
    host_group_id = 'e789e756496246859fde6c132b2091d3' # str | Id of the host Group.

    try:
        # Get the host group details by {hostGroupId}
        api_response = api_instance.host_group_get_by_id(host_group_id)
        print("The response of HostInitiatorGroupsApi->host_group_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorGroupsApi->host_group_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_group_id** | **str**| Id of the host Group. | 

### Return type

[**HostGroupDetails**](HostGroupDetails.md)

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

# **host_group_list**
> HostGroupsList host_group_list(filter=filter, sort=sort, limit=limit, offset=offset)

Get the list of host groups

Get the list of host groups

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.host_groups_list import HostGroupsList
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
    api_instance = dscc.HostInitiatorGroupsApi(api_client)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | oData query to filter hostservice by Key. (optional)
    sort = 'name desc' # str | oData query to sort hostservice by Key. (optional)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)

    try:
        # Get the list of host groups
        api_response = api_instance.host_group_list(filter=filter, sort=sort, limit=limit, offset=offset)
        print("The response of HostInitiatorGroupsApi->host_group_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorGroupsApi->host_group_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| oData query to filter hostservice by Key. | [optional] 
 **sort** | **str**| oData query to sort hostservice by Key. | [optional] 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 

### Return type

[**HostGroupsList**](HostGroupsList.md)

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

# **host_group_merge**
> TaskResponse host_group_merge(merge_host_groups_input)

Merge a host group

Merge a host group

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.merge_host_groups_input import MergeHostGroupsInput
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
    api_instance = dscc.HostInitiatorGroupsApi(api_client)
    merge_host_groups_input = dscc.MergeHostGroupsInput() # MergeHostGroupsInput | 

    try:
        # Merge a host group
        api_response = api_instance.host_group_merge(merge_host_groups_input)
        print("The response of HostInitiatorGroupsApi->host_group_merge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorGroupsApi->host_group_merge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merge_host_groups_input** | [**MergeHostGroupsInput**](MergeHostGroupsInput.md)|  | 

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

# **host_group_update_by_id**
> TaskResponse host_group_update_by_id(host_group_id, update_host_group_input)

Update host group by {hostGroupId}

Update host group details by {hostGroupId}. Hostgroup can be updated with hosts containing same protocol initiators

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.models.update_host_group_input import UpdateHostGroupInput
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
    api_instance = dscc.HostInitiatorGroupsApi(api_client)
    host_group_id = 'e789e756496246859fde6c132b2091d3' # str | Id of the host Group.
    update_host_group_input = dscc.UpdateHostGroupInput() # UpdateHostGroupInput | 

    try:
        # Update host group by {hostGroupId}
        api_response = api_instance.host_group_update_by_id(host_group_id, update_host_group_input)
        print("The response of HostInitiatorGroupsApi->host_group_update_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostInitiatorGroupsApi->host_group_update_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_group_id** | **str**| Id of the host Group. | 
 **update_host_group_input** | [**UpdateHostGroupInput**](UpdateHostGroupInput.md)|  | 

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

