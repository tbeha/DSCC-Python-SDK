# dscc.ExternalKeyManagerApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type2_create_external_key_manager**](ExternalKeyManagerApi.md#device_type2_create_external_key_manager) | **POST** /api/v1/storage-systems/device-type2/{systemId}/external-key-manager | Create external key manager for a Nimble / Alletra 6K storage system
[**device_type2_delete_external_key_manager_by_id**](ExternalKeyManagerApi.md#device_type2_delete_external_key_manager_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/external-key-manager/{externalKeyManagerId} | Delete Nimble / Alletra 6K external key manager identified by {externalKeyManagerId}
[**device_type2_edit_external_key_manager_by_id**](ExternalKeyManagerApi.md#device_type2_edit_external_key_manager_by_id) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/external-key-manager/{externalKeyManagerId} | Edit external key manager for a Nimble / Alletra 6K identified by {externalKeyManagerId}
[**device_type2_get_external_key_manager**](ExternalKeyManagerApi.md#device_type2_get_external_key_manager) | **GET** /api/v1/storage-systems/device-type2/{systemId}/external-key-manager | Get details of Nimble / Alletra 6K external-key-manager
[**device_type2_get_external_key_manager_by_id**](ExternalKeyManagerApi.md#device_type2_get_external_key_manager_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/external-key-manager/{externalKeyManagerId} | Get details of Nimble / Alletra 6K external-key-manager identified by {externalKeyManagerId}
[**device_type2_migrate_external_key_manager_by_id**](ExternalKeyManagerApi.md#device_type2_migrate_external_key_manager_by_id) | **POST** /api/v1/storage-systems/device-type2/{systemId}/external-key-manager/{externalKeyManagerId}/actions/migrate | Migrate external key manager for a Nimble / Alletra 6K identified by {externalKeyManagerId}
[**device_type2_remove_external_key_manager_by_id**](ExternalKeyManagerApi.md#device_type2_remove_external_key_manager_by_id) | **POST** /api/v1/storage-systems/device-type2/{systemId}/external-key-manager/{externalKeyManagerId}/actions/remove | Remove Nimble / Alletra 6K external key manager identified by {externalKeyManagerId}


# **device_type2_create_external_key_manager**
> TaskResponse device_type2_create_external_key_manager(system_id, create_external_key_manager)

Create external key manager for a Nimble / Alletra 6K storage system

Create external key manager for a Nimble / Alletra 6K storage system

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.create_external_key_manager import CreateExternalKeyManager
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
    api_instance = dscc.ExternalKeyManagerApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    create_external_key_manager = dscc.CreateExternalKeyManager() # CreateExternalKeyManager | 

    try:
        # Create external key manager for a Nimble / Alletra 6K storage system
        api_response = api_instance.device_type2_create_external_key_manager(system_id, create_external_key_manager)
        print("The response of ExternalKeyManagerApi->device_type2_create_external_key_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalKeyManagerApi->device_type2_create_external_key_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **create_external_key_manager** | [**CreateExternalKeyManager**](CreateExternalKeyManager.md)|  | 

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

# **device_type2_delete_external_key_manager_by_id**
> TaskResponse device_type2_delete_external_key_manager_by_id(system_id, external_key_manager_id)

Delete Nimble / Alletra 6K external key manager identified by {externalKeyManagerId}

Delete Nimble / Alletra 6K external key manager identified by {externalKeyManagerId}

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
    api_instance = dscc.ExternalKeyManagerApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    external_key_manager_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of external key manager. A 42 digit hexadecimal number.

    try:
        # Delete Nimble / Alletra 6K external key manager identified by {externalKeyManagerId}
        api_response = api_instance.device_type2_delete_external_key_manager_by_id(system_id, external_key_manager_id)
        print("The response of ExternalKeyManagerApi->device_type2_delete_external_key_manager_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalKeyManagerApi->device_type2_delete_external_key_manager_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **external_key_manager_id** | **str**| Identifier of external key manager. A 42 digit hexadecimal number. | 

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

# **device_type2_edit_external_key_manager_by_id**
> TaskResponse device_type2_edit_external_key_manager_by_id(system_id, external_key_manager_id, edit_external_key_manager)

Edit external key manager for a Nimble / Alletra 6K identified by {externalKeyManagerId}

Edit external key manager for a Nimble / Alletra 6K identified by {externalKeyManagerId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.edit_external_key_manager import EditExternalKeyManager
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
    api_instance = dscc.ExternalKeyManagerApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    external_key_manager_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of external key manager. A 42 digit hexadecimal number.
    edit_external_key_manager = dscc.EditExternalKeyManager() # EditExternalKeyManager | 

    try:
        # Edit external key manager for a Nimble / Alletra 6K identified by {externalKeyManagerId}
        api_response = api_instance.device_type2_edit_external_key_manager_by_id(system_id, external_key_manager_id, edit_external_key_manager)
        print("The response of ExternalKeyManagerApi->device_type2_edit_external_key_manager_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalKeyManagerApi->device_type2_edit_external_key_manager_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **external_key_manager_id** | **str**| Identifier of external key manager. A 42 digit hexadecimal number. | 
 **edit_external_key_manager** | [**EditExternalKeyManager**](EditExternalKeyManager.md)|  | 

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

# **device_type2_get_external_key_manager**
> ExternalKeyManagerList device_type2_get_external_key_manager(system_id, select=select)

Get details of Nimble / Alletra 6K external-key-manager

Get details of Nimble / Alletra 6K external-key-manager

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.external_key_manager_list import ExternalKeyManagerList
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
    api_instance = dscc.ExternalKeyManagerApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Nimble / Alletra 6K external-key-manager
        api_response = api_instance.device_type2_get_external_key_manager(system_id, select=select)
        print("The response of ExternalKeyManagerApi->device_type2_get_external_key_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalKeyManagerApi->device_type2_get_external_key_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**ExternalKeyManagerList**](ExternalKeyManagerList.md)

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

# **device_type2_get_external_key_manager_by_id**
> ExternalKeyManagerDetails device_type2_get_external_key_manager_by_id(system_id, external_key_manager_id, select=select)

Get details of Nimble / Alletra 6K external-key-manager identified by {externalKeyManagerId}

Get details of Nimble / Alletra 6K external-key-manager identified by {externalKeyManagerId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.external_key_manager_details import ExternalKeyManagerDetails
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
    api_instance = dscc.ExternalKeyManagerApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    external_key_manager_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of external key manager. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Nimble / Alletra 6K external-key-manager identified by {externalKeyManagerId}
        api_response = api_instance.device_type2_get_external_key_manager_by_id(system_id, external_key_manager_id, select=select)
        print("The response of ExternalKeyManagerApi->device_type2_get_external_key_manager_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalKeyManagerApi->device_type2_get_external_key_manager_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **external_key_manager_id** | **str**| Identifier of external key manager. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**ExternalKeyManagerDetails**](ExternalKeyManagerDetails.md)

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

# **device_type2_migrate_external_key_manager_by_id**
> TaskResponse device_type2_migrate_external_key_manager_by_id(system_id, external_key_manager_id)

Migrate external key manager for a Nimble / Alletra 6K identified by {externalKeyManagerId}

Migrate external key manager for a Nimble / Alletra 6K identified by {externalKeyManagerId}

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
    api_instance = dscc.ExternalKeyManagerApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    external_key_manager_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of external key manager. A 42 digit hexadecimal number.

    try:
        # Migrate external key manager for a Nimble / Alletra 6K identified by {externalKeyManagerId}
        api_response = api_instance.device_type2_migrate_external_key_manager_by_id(system_id, external_key_manager_id)
        print("The response of ExternalKeyManagerApi->device_type2_migrate_external_key_manager_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalKeyManagerApi->device_type2_migrate_external_key_manager_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **external_key_manager_id** | **str**| Identifier of external key manager. A 42 digit hexadecimal number. | 

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

# **device_type2_remove_external_key_manager_by_id**
> TaskResponse device_type2_remove_external_key_manager_by_id(system_id, external_key_manager_id)

Remove Nimble / Alletra 6K external key manager identified by {externalKeyManagerId}

Remove Nimble / Alletra 6K external key manager identified by {externalKeyManagerId}

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
    api_instance = dscc.ExternalKeyManagerApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    external_key_manager_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of external key manager. A 42 digit hexadecimal number.

    try:
        # Remove Nimble / Alletra 6K external key manager identified by {externalKeyManagerId}
        api_response = api_instance.device_type2_remove_external_key_manager_by_id(system_id, external_key_manager_id)
        print("The response of ExternalKeyManagerApi->device_type2_remove_external_key_manager_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalKeyManagerApi->device_type2_remove_external_key_manager_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **external_key_manager_id** | **str**| Identifier of external key manager. A 42 digit hexadecimal number. | 

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

