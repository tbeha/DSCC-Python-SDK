# dscc.FoldersApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type2_attach_detach_vvolby_id**](FoldersApi.md#device_type2_attach_detach_vvolby_id) | **POST** /api/v1/storage-systems/device-type2/{systemId}/folders/{folderId}/attach | Attach hosts to Storage container identified by {folderId} from Nimble / Alletra 6K
[**device_type2_folder_create**](FoldersApi.md#device_type2_folder_create) | **POST** /api/v1/storage-systems/device-type2/{systemId}/folders | Create Nimble / Alletra 6K folder in system identified by {systemId}
[**device_type2_folder_edit**](FoldersApi.md#device_type2_folder_edit) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/folders/{folderId} | Edit details of Nimble / Alletra 6K folder identified by {folderId}
[**device_type2_get_folder_by_id**](FoldersApi.md#device_type2_get_folder_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/folders/{folderId} | Get details of Nimble / Alletra 6K Folders identified by {folderId}
[**device_type2_remove_folder_by_id**](FoldersApi.md#device_type2_remove_folder_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/folders/{folderId} | Remove Nimble / Alletra 6K folder identified by {folderId}


# **device_type2_attach_detach_vvolby_id**
> TaskResponse device_type2_attach_detach_vvolby_id(system_id, folder_id, attach_detach_nimble_vvol_sc_input)

Attach hosts to Storage container identified by {folderId} from Nimble / Alletra 6K

Attach hosts to Storage container identified by {folderId} from Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.attach_detach_nimble_vvol_sc_input import AttachDetachNimbleVvolSCInput
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
    api_instance = dscc.FoldersApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    folder_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the folder. A 42 digit hexadecimal number.
    attach_detach_nimble_vvol_sc_input = dscc.AttachDetachNimbleVvolSCInput() # AttachDetachNimbleVvolSCInput | 

    try:
        # Attach hosts to Storage container identified by {folderId} from Nimble / Alletra 6K
        api_response = api_instance.device_type2_attach_detach_vvolby_id(system_id, folder_id, attach_detach_nimble_vvol_sc_input)
        print("The response of FoldersApi->device_type2_attach_detach_vvolby_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->device_type2_attach_detach_vvolby_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **folder_id** | **str**| ID of the folder. A 42 digit hexadecimal number. | 
 **attach_detach_nimble_vvol_sc_input** | [**AttachDetachNimbleVvolSCInput**](AttachDetachNimbleVvolSCInput.md)|  | 

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
**404** | Storage container object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_folder_create**
> TaskResponse device_type2_folder_create(system_id, nimble_create_folder_input)

Create Nimble / Alletra 6K folder in system identified by {systemId}

Create Nimble / Alletra 6K folder in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_create_folder_input import NimbleCreateFolderInput
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
    api_instance = dscc.FoldersApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    nimble_create_folder_input = dscc.NimbleCreateFolderInput() # NimbleCreateFolderInput | 

    try:
        # Create Nimble / Alletra 6K folder in system identified by {systemId}
        api_response = api_instance.device_type2_folder_create(system_id, nimble_create_folder_input)
        print("The response of FoldersApi->device_type2_folder_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->device_type2_folder_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_create_folder_input** | [**NimbleCreateFolderInput**](NimbleCreateFolderInput.md)|  | 

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

# **device_type2_folder_edit**
> TaskResponse device_type2_folder_edit(system_id, folder_id, nimble_edit_folder_input)

Edit details of Nimble / Alletra 6K folder identified by {folderId}

Edit details of Nimble / Alletra 6K folder identified by {folderId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_edit_folder_input import NimbleEditFolderInput
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
    api_instance = dscc.FoldersApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    folder_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the folder. A 42 digit hexadecimal number.
    nimble_edit_folder_input = dscc.NimbleEditFolderInput() # NimbleEditFolderInput | 

    try:
        # Edit details of Nimble / Alletra 6K folder identified by {folderId}
        api_response = api_instance.device_type2_folder_edit(system_id, folder_id, nimble_edit_folder_input)
        print("The response of FoldersApi->device_type2_folder_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->device_type2_folder_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **folder_id** | **str**| ID of the folder. A 42 digit hexadecimal number. | 
 **nimble_edit_folder_input** | [**NimbleEditFolderInput**](NimbleEditFolderInput.md)|  | 

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

# **device_type2_get_folder_by_id**
> NimbleFolderDetailsWithRequestUri device_type2_get_folder_by_id(system_id, folder_id, select=select)

Get details of Nimble / Alletra 6K Folders identified by {folderId}

Get details of Nimble / Alletra 6K Folders identified by {folderId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_folder_details_with_request_uri import NimbleFolderDetailsWithRequestUri
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
    api_instance = dscc.FoldersApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    folder_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the folder. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Nimble / Alletra 6K Folders identified by {folderId}
        api_response = api_instance.device_type2_get_folder_by_id(system_id, folder_id, select=select)
        print("The response of FoldersApi->device_type2_get_folder_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->device_type2_get_folder_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **folder_id** | **str**| ID of the folder. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleFolderDetailsWithRequestUri**](NimbleFolderDetailsWithRequestUri.md)

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

# **device_type2_remove_folder_by_id**
> TaskResponse device_type2_remove_folder_by_id(system_id, folder_id)

Remove Nimble / Alletra 6K folder identified by {folderId}

Remove Nimble / Alletra 6K folder identified by {folderId}

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
    api_instance = dscc.FoldersApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    folder_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the folder. A 42 digit hexadecimal number.

    try:
        # Remove Nimble / Alletra 6K folder identified by {folderId}
        api_response = api_instance.device_type2_remove_folder_by_id(system_id, folder_id)
        print("The response of FoldersApi->device_type2_remove_folder_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->device_type2_remove_folder_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **folder_id** | **str**| ID of the folder. A 42 digit hexadecimal number. | 

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

