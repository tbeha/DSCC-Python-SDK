# dscc.VvolscsApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type1_attach_detach_vol_sc**](VvolscsApi.md#device_type1_attach_detach_vol_sc) | **POST** /api/v1/storage-systems/device-type1/{systemId}/system-settings/management-services/vvolscs/{vvolscId}/attach | Attach host to Storage container identified by {vvolscId} from Primera / Alletra 9K
[**device_type1_createv_vol_sc**](VvolscsApi.md#device_type1_createv_vol_sc) | **POST** /api/v1/storage-systems/device-type1/{systemId}/system-settings/management-services/vvolscs | Creates VMware storage container on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_edit_vol_sc**](VvolscsApi.md#device_type1_edit_vol_sc) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/system-settings/management-services/vvolscs/{vvolscId} | Edit Storage container identified by {vvolscId} from Primera / Alletra 9K
[**device_type4_attach_vol_sc**](VvolscsApi.md#device_type4_attach_vol_sc) | **POST** /api/v1/storage-systems/device-type4/{systemId}/system-settings/management-services/vvolscs/{vvolscId}/attach | Attach host to Storage container identified by {vvolscId} from HPE Alletra Storage MP
[**device_type4_createv_vol_sc**](VvolscsApi.md#device_type4_createv_vol_sc) | **POST** /api/v1/storage-systems/device-type4/{systemId}/system-settings/management-services/vvolscs | Creates VMware storage container on storage system HPE Alletra Storage MP identified by {systemId}
[**device_type4_detach_vol_sc**](VvolscsApi.md#device_type4_detach_vol_sc) | **POST** /api/v1/storage-systems/device-type4/{systemId}/system-settings/management-services/vvolscs/{vvolscId}/detach | Detach host to Storage container identified by {vvolscId} from HPE Alletra Storage MP


# **device_type1_attach_detach_vol_sc**
> TaskResponse device_type1_attach_detach_vol_sc(system_id, vvolsc_id, attach_detachv_vol_sc_input)

Attach host to Storage container identified by {vvolscId} from Primera / Alletra 9K

Attach host to Storage container identified by {vvolscId} from Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.attach_detachv_vol_sc_input import AttachDetachvVolSCInput
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
    api_instance = dscc.VvolscsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    vvolsc_id = 'd09b59cd7bd07a4e9559e78dcea07498' # str | Storage container UID
    attach_detachv_vol_sc_input = dscc.AttachDetachvVolSCInput() # AttachDetachvVolSCInput | 

    try:
        # Attach host to Storage container identified by {vvolscId} from Primera / Alletra 9K
        api_response = api_instance.device_type1_attach_detach_vol_sc(system_id, vvolsc_id, attach_detachv_vol_sc_input)
        print("The response of VvolscsApi->device_type1_attach_detach_vol_sc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VvolscsApi->device_type1_attach_detach_vol_sc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **vvolsc_id** | **str**| Storage container UID | 
 **attach_detachv_vol_sc_input** | [**AttachDetachvVolSCInput**](AttachDetachvVolSCInput.md)|  | 

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

# **device_type1_createv_vol_sc**
> TaskResponse device_type1_createv_vol_sc(system_id, createv_vol_sc_input)

Creates VMware storage container on storage system Primera / Alletra 9K identified by {systemId}

Creates VMware storage container on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.createv_vol_sc_input import CreatevVolSCInput
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
    api_instance = dscc.VvolscsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    createv_vol_sc_input = dscc.CreatevVolSCInput() # CreatevVolSCInput | 

    try:
        # Creates VMware storage container on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_createv_vol_sc(system_id, createv_vol_sc_input)
        print("The response of VvolscsApi->device_type1_createv_vol_sc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VvolscsApi->device_type1_createv_vol_sc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **createv_vol_sc_input** | [**CreatevVolSCInput**](CreatevVolSCInput.md)|  | 

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

# **device_type1_edit_vol_sc**
> TaskResponse device_type1_edit_vol_sc(system_id, vvolsc_id, editv_vol_sc_input)

Edit Storage container identified by {vvolscId} from Primera / Alletra 9K

Edit Storage container identified by {volumeId} from Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.editv_vol_sc_input import EditvVolSCInput
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
    api_instance = dscc.VvolscsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    vvolsc_id = 'd09b59cd7bd07a4e9559e78dcea07498' # str | Storage container UID
    editv_vol_sc_input = dscc.EditvVolSCInput() # EditvVolSCInput | 

    try:
        # Edit Storage container identified by {vvolscId} from Primera / Alletra 9K
        api_response = api_instance.device_type1_edit_vol_sc(system_id, vvolsc_id, editv_vol_sc_input)
        print("The response of VvolscsApi->device_type1_edit_vol_sc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VvolscsApi->device_type1_edit_vol_sc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **vvolsc_id** | **str**| Storage container UID | 
 **editv_vol_sc_input** | [**EditvVolSCInput**](EditvVolSCInput.md)|  | 

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

# **device_type4_attach_vol_sc**
> TaskResponse device_type4_attach_vol_sc(system_id, vvolsc_id, attach_detach_input)

Attach host to Storage container identified by {vvolscId} from HPE Alletra Storage MP

Attach host to Storage container identified by {volumeId} from HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.attach_detach_input import AttachDetachInput
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
    api_instance = dscc.VvolscsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    vvolsc_id = 'd09b59cd7bd07a4e9559e78dcea07498' # str | Storage container UID
    attach_detach_input = dscc.AttachDetachInput() # AttachDetachInput | 

    try:
        # Attach host to Storage container identified by {vvolscId} from HPE Alletra Storage MP
        api_response = api_instance.device_type4_attach_vol_sc(system_id, vvolsc_id, attach_detach_input)
        print("The response of VvolscsApi->device_type4_attach_vol_sc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VvolscsApi->device_type4_attach_vol_sc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **vvolsc_id** | **str**| Storage container UID | 
 **attach_detach_input** | [**AttachDetachInput**](AttachDetachInput.md)|  | 

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

# **device_type4_createv_vol_sc**
> TaskResponse device_type4_createv_vol_sc(system_id, device_type4_createv_vol_sc_input)

Creates VMware storage container on storage system HPE Alletra Storage MP identified by {systemId}

Creates VMware storage container on storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_createv_vol_sc_input import DeviceType4CreatevVolSCInput
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
    api_instance = dscc.VvolscsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_createv_vol_sc_input = dscc.DeviceType4CreatevVolSCInput() # DeviceType4CreatevVolSCInput | 

    try:
        # Creates VMware storage container on storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_createv_vol_sc(system_id, device_type4_createv_vol_sc_input)
        print("The response of VvolscsApi->device_type4_createv_vol_sc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VvolscsApi->device_type4_createv_vol_sc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_createv_vol_sc_input** | [**DeviceType4CreatevVolSCInput**](DeviceType4CreatevVolSCInput.md)|  | 

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

# **device_type4_detach_vol_sc**
> TaskResponse device_type4_detach_vol_sc(system_id, vvolsc_id, attach_detach_input)

Detach host to Storage container identified by {vvolscId} from HPE Alletra Storage MP

Detach host to Storage container identified by {volumeId} from HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.attach_detach_input import AttachDetachInput
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
    api_instance = dscc.VvolscsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    vvolsc_id = 'd09b59cd7bd07a4e9559e78dcea07498' # str | Storage container UID
    attach_detach_input = dscc.AttachDetachInput() # AttachDetachInput | 

    try:
        # Detach host to Storage container identified by {vvolscId} from HPE Alletra Storage MP
        api_response = api_instance.device_type4_detach_vol_sc(system_id, vvolsc_id, attach_detach_input)
        print("The response of VvolscsApi->device_type4_detach_vol_sc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VvolscsApi->device_type4_detach_vol_sc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **vvolsc_id** | **str**| Storage container UID | 
 **attach_detach_input** | [**AttachDetachInput**](AttachDetachInput.md)|  | 

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

