# dscc.LocalKeyManagerApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type2_create_local_key_manager**](LocalKeyManagerApi.md#device_type2_create_local_key_manager) | **POST** /api/v1/storage-systems/device-type2/{systemId}/local-key-manager | Create local key manager for a Nimble / Alletra 6K storage system
[**device_type2_delete_local_key_manager_by_id**](LocalKeyManagerApi.md#device_type2_delete_local_key_manager_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/local-key-manager/{localKeyManagerId} | Delete Nimble / Alletra 6K local key manager identified by {localKeyManagerId}
[**device_type2_edit_local_key_manager_by_id**](LocalKeyManagerApi.md#device_type2_edit_local_key_manager_by_id) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/local-key-manager/{localKeyManagerId} | Edit local key manager for a Nimble / Alletra 6K identified by {localKeyManagerId}
[**device_type2_get_local_key_manager**](LocalKeyManagerApi.md#device_type2_get_local_key_manager) | **GET** /api/v1/storage-systems/device-type2/{systemId}/local-key-manager | Get details of Nimble / Alletra 6K local-key-manager
[**device_type2_get_local_key_manager_by_id**](LocalKeyManagerApi.md#device_type2_get_local_key_manager_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/local-key-manager/{localKeyManagerId} | Get details of Nimble / Alletra 6K local-key-manager identified by {localKeyManagerId}


# **device_type2_create_local_key_manager**
> TaskResponse device_type2_create_local_key_manager(system_id, create_local_key_manager)

Create local key manager for a Nimble / Alletra 6K storage system

Create local key manager for a Nimble / Alletra 6K storage system

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.create_local_key_manager import CreateLocalKeyManager
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
    api_instance = dscc.LocalKeyManagerApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    create_local_key_manager = dscc.CreateLocalKeyManager() # CreateLocalKeyManager | 

    try:
        # Create local key manager for a Nimble / Alletra 6K storage system
        api_response = api_instance.device_type2_create_local_key_manager(system_id, create_local_key_manager)
        print("The response of LocalKeyManagerApi->device_type2_create_local_key_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalKeyManagerApi->device_type2_create_local_key_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **create_local_key_manager** | [**CreateLocalKeyManager**](CreateLocalKeyManager.md)|  | 

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

# **device_type2_delete_local_key_manager_by_id**
> TaskResponse device_type2_delete_local_key_manager_by_id(system_id, local_key_manager_id)

Delete Nimble / Alletra 6K local key manager identified by {localKeyManagerId}

Delete Nimble / Alletra 6K local key manager identified by {localKeyManagerId}

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
    api_instance = dscc.LocalKeyManagerApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    local_key_manager_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of local key manager. A 42 digit hexadecimal number.

    try:
        # Delete Nimble / Alletra 6K local key manager identified by {localKeyManagerId}
        api_response = api_instance.device_type2_delete_local_key_manager_by_id(system_id, local_key_manager_id)
        print("The response of LocalKeyManagerApi->device_type2_delete_local_key_manager_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalKeyManagerApi->device_type2_delete_local_key_manager_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **local_key_manager_id** | **str**| Identifier of local key manager. A 42 digit hexadecimal number. | 

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

# **device_type2_edit_local_key_manager_by_id**
> TaskResponse device_type2_edit_local_key_manager_by_id(system_id, local_key_manager_id, edit_local_key_manager)

Edit local key manager for a Nimble / Alletra 6K identified by {localKeyManagerId}

Edit local key manager for a Nimble / Alletra 6K identified by {localKeyManagerId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.edit_local_key_manager import EditLocalKeyManager
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
    api_instance = dscc.LocalKeyManagerApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    local_key_manager_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of local key manager. A 42 digit hexadecimal number.
    edit_local_key_manager = dscc.EditLocalKeyManager() # EditLocalKeyManager | 

    try:
        # Edit local key manager for a Nimble / Alletra 6K identified by {localKeyManagerId}
        api_response = api_instance.device_type2_edit_local_key_manager_by_id(system_id, local_key_manager_id, edit_local_key_manager)
        print("The response of LocalKeyManagerApi->device_type2_edit_local_key_manager_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalKeyManagerApi->device_type2_edit_local_key_manager_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **local_key_manager_id** | **str**| Identifier of local key manager. A 42 digit hexadecimal number. | 
 **edit_local_key_manager** | [**EditLocalKeyManager**](EditLocalKeyManager.md)|  | 

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

# **device_type2_get_local_key_manager**
> LocalKeyManagerList device_type2_get_local_key_manager(system_id, select=select)

Get details of Nimble / Alletra 6K local-key-manager

Get details of Nimble / Alletra 6K local-key-manager

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.local_key_manager_list import LocalKeyManagerList
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
    api_instance = dscc.LocalKeyManagerApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Nimble / Alletra 6K local-key-manager
        api_response = api_instance.device_type2_get_local_key_manager(system_id, select=select)
        print("The response of LocalKeyManagerApi->device_type2_get_local_key_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalKeyManagerApi->device_type2_get_local_key_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**LocalKeyManagerList**](LocalKeyManagerList.md)

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

# **device_type2_get_local_key_manager_by_id**
> LocalKeyManagerDetails device_type2_get_local_key_manager_by_id(system_id, local_key_manager_id, select=select)

Get details of Nimble / Alletra 6K local-key-manager identified by {localKeyManagerId}

Get details of Nimble / Alletra 6K local-key-manager identified by {localKeyManagerId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.local_key_manager_details import LocalKeyManagerDetails
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
    api_instance = dscc.LocalKeyManagerApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    local_key_manager_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of local key manager. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Nimble / Alletra 6K local-key-manager identified by {localKeyManagerId}
        api_response = api_instance.device_type2_get_local_key_manager_by_id(system_id, local_key_manager_id, select=select)
        print("The response of LocalKeyManagerApi->device_type2_get_local_key_manager_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalKeyManagerApi->device_type2_get_local_key_manager_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **local_key_manager_id** | **str**| Identifier of local key manager. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**LocalKeyManagerDetails**](LocalKeyManagerDetails.md)

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

