# dscc.EncryptionApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type1backup_action_on_encryption**](EncryptionApi.md#device_type1backup_action_on_encryption) | **POST** /api/v1/storage-systems/device-type1/{systemId}/encryption/backup | Encryption Backup Action on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1check_ekm_configuration**](EncryptionApi.md#device_type1check_ekm_configuration) | **POST** /api/v1/storage-systems/device-type1/{systemId}/encryption/checkekm | Check EKM configuration on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1enable_action_on_encryption**](EncryptionApi.md#device_type1enable_action_on_encryption) | **POST** /api/v1/storage-systems/device-type1/{systemId}/encryption/enable | Encryption Enable Action on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1rekey_action_on_encryption**](EncryptionApi.md#device_type1rekey_action_on_encryption) | **POST** /api/v1/storage-systems/device-type1/{systemId}/encryption/rekey | Encryption Rekey Action on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1restore_action_on_encryption**](EncryptionApi.md#device_type1restore_action_on_encryption) | **POST** /api/v1/storage-systems/device-type1/{systemId}/encryption/restore | Encryption Restore Action on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1set_ekm_configuration**](EncryptionApi.md#device_type1set_ekm_configuration) | **POST** /api/v1/storage-systems/device-type1/{systemId}/encryption/setekm | Set EKM configuration on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1setekmbackup_action_on_encryption**](EncryptionApi.md#device_type1setekmbackup_action_on_encryption) | **POST** /api/v1/storage-systems/device-type1/{systemId}/encryption/setekm/backup | Set EKM configuration and Encryption Backup Action on storage system Primera / Alletra 9K identified by {systemId}
[**device_type4backup_action_on_encryption**](EncryptionApi.md#device_type4backup_action_on_encryption) | **POST** /api/v1/storage-systems/device-type4/{systemId}/encryption/backup | Encryption Backup Action on HPE Alletra Storage MP identified by {systemId}
[**device_type4check_ekm_configuration**](EncryptionApi.md#device_type4check_ekm_configuration) | **POST** /api/v1/storage-systems/device-type4/{systemId}/encryption/checkekm | Check EKM configuration on HPE Alletra Storage MP identified by {systemId}
[**device_type4enable_action_on_encryption**](EncryptionApi.md#device_type4enable_action_on_encryption) | **POST** /api/v1/storage-systems/device-type4/{systemId}/encryption/enable | Encryption Enable Action on HPE Alletra Storage MP identified by {systemId}
[**device_type4rekey_action_on_encryption**](EncryptionApi.md#device_type4rekey_action_on_encryption) | **POST** /api/v1/storage-systems/device-type4/{systemId}/encryption/rekey | Encryption Rekey Action on HPE Alletra Storage MP identified by {systemId}
[**device_type4restore_action_on_encryption**](EncryptionApi.md#device_type4restore_action_on_encryption) | **POST** /api/v1/storage-systems/device-type4/{systemId}/encryption/restore | Encryption Restore Action on HPE Alletra Storage MP identified by {systemId}
[**device_type4set_ekm_configuration**](EncryptionApi.md#device_type4set_ekm_configuration) | **POST** /api/v1/storage-systems/device-type4/{systemId}/encryption/setekm | Set EKM configuration on HPE Alletra Storage MP identified by {systemId}
[**device_type4setekmbackup_action_on_encryption**](EncryptionApi.md#device_type4setekmbackup_action_on_encryption) | **POST** /api/v1/storage-systems/device-type4/{systemId}/encryption/setekm/backup | Set EKM configuration and Encryption Backup Action on HPE Alletra Storage MP identified by {systemId}


# **device_type1backup_action_on_encryption**
> EncryptionResponse device_type1backup_action_on_encryption(system_id, encryption_actions_input)

Encryption Backup Action on storage system Primera / Alletra 9K identified by {systemId}

Encryption Backup Action on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.encryption_actions_input import EncryptionActionsInput
from dscc.models.encryption_response import EncryptionResponse
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
    api_instance = dscc.EncryptionApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    encryption_actions_input = dscc.EncryptionActionsInput() # EncryptionActionsInput | 

    try:
        # Encryption Backup Action on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1backup_action_on_encryption(system_id, encryption_actions_input)
        print("The response of EncryptionApi->device_type1backup_action_on_encryption:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EncryptionApi->device_type1backup_action_on_encryption: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **encryption_actions_input** | [**EncryptionActionsInput**](EncryptionActionsInput.md)|  | 

### Return type

[**EncryptionResponse**](EncryptionResponse.md)

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

# **device_type1check_ekm_configuration**
> CheckekmResponse device_type1check_ekm_configuration(system_id)

Check EKM configuration on storage system Primera / Alletra 9K identified by {systemId}

Check EKM configuration on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.checkekm_response import CheckekmResponse
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
    api_instance = dscc.EncryptionApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system

    try:
        # Check EKM configuration on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1check_ekm_configuration(system_id)
        print("The response of EncryptionApi->device_type1check_ekm_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EncryptionApi->device_type1check_ekm_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 

### Return type

[**CheckekmResponse**](CheckekmResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1enable_action_on_encryption**
> EncryptionResponse device_type1enable_action_on_encryption(system_id, encryption_actions_input)

Encryption Enable Action on storage system Primera / Alletra 9K identified by {systemId}

Encryption Enable Action on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.encryption_actions_input import EncryptionActionsInput
from dscc.models.encryption_response import EncryptionResponse
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
    api_instance = dscc.EncryptionApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    encryption_actions_input = dscc.EncryptionActionsInput() # EncryptionActionsInput | 

    try:
        # Encryption Enable Action on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1enable_action_on_encryption(system_id, encryption_actions_input)
        print("The response of EncryptionApi->device_type1enable_action_on_encryption:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EncryptionApi->device_type1enable_action_on_encryption: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **encryption_actions_input** | [**EncryptionActionsInput**](EncryptionActionsInput.md)|  | 

### Return type

[**EncryptionResponse**](EncryptionResponse.md)

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

# **device_type1rekey_action_on_encryption**
> EncryptionResponse device_type1rekey_action_on_encryption(system_id, encryption_actions_input)

Encryption Rekey Action on storage system Primera / Alletra 9K identified by {systemId}

Encryption Rekey Action on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.encryption_actions_input import EncryptionActionsInput
from dscc.models.encryption_response import EncryptionResponse
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
    api_instance = dscc.EncryptionApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    encryption_actions_input = dscc.EncryptionActionsInput() # EncryptionActionsInput | 

    try:
        # Encryption Rekey Action on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1rekey_action_on_encryption(system_id, encryption_actions_input)
        print("The response of EncryptionApi->device_type1rekey_action_on_encryption:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EncryptionApi->device_type1rekey_action_on_encryption: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **encryption_actions_input** | [**EncryptionActionsInput**](EncryptionActionsInput.md)|  | 

### Return type

[**EncryptionResponse**](EncryptionResponse.md)

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

# **device_type1restore_action_on_encryption**
> TaskResponse device_type1restore_action_on_encryption(system_id, encryption_restore_action_input)

Encryption Restore Action on storage system Primera / Alletra 9K identified by {systemId}

Encryption Restore Action on  storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.encryption_restore_action_input import EncryptionRestoreActionInput
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
    api_instance = dscc.EncryptionApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    encryption_restore_action_input = dscc.EncryptionRestoreActionInput() # EncryptionRestoreActionInput | 

    try:
        # Encryption Restore Action on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1restore_action_on_encryption(system_id, encryption_restore_action_input)
        print("The response of EncryptionApi->device_type1restore_action_on_encryption:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EncryptionApi->device_type1restore_action_on_encryption: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **encryption_restore_action_input** | [**EncryptionRestoreActionInput**](EncryptionRestoreActionInput.md)|  | 

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

# **device_type1set_ekm_configuration**
> TaskResponse device_type1set_ekm_configuration(system_id, set_ekm_config_input)

Set EKM configuration on storage system Primera / Alletra 9K identified by {systemId}

Set EKM configuration on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.set_ekm_config_input import SetEKMConfigInput
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
    api_instance = dscc.EncryptionApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    set_ekm_config_input = dscc.SetEKMConfigInput() # SetEKMConfigInput | 

    try:
        # Set EKM configuration on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1set_ekm_configuration(system_id, set_ekm_config_input)
        print("The response of EncryptionApi->device_type1set_ekm_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EncryptionApi->device_type1set_ekm_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **set_ekm_config_input** | [**SetEKMConfigInput**](SetEKMConfigInput.md)|  | 

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

# **device_type1setekmbackup_action_on_encryption**
> EncryptionResponse device_type1setekmbackup_action_on_encryption(system_id, encryption_actions_input)

Set EKM configuration and Encryption Backup Action on storage system Primera / Alletra 9K identified by {systemId}

Set EKM configuration and Encryption Backup Action on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.encryption_actions_input import EncryptionActionsInput
from dscc.models.encryption_response import EncryptionResponse
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
    api_instance = dscc.EncryptionApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    encryption_actions_input = dscc.EncryptionActionsInput() # EncryptionActionsInput | 

    try:
        # Set EKM configuration and Encryption Backup Action on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1setekmbackup_action_on_encryption(system_id, encryption_actions_input)
        print("The response of EncryptionApi->device_type1setekmbackup_action_on_encryption:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EncryptionApi->device_type1setekmbackup_action_on_encryption: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **encryption_actions_input** | [**EncryptionActionsInput**](EncryptionActionsInput.md)|  | 

### Return type

[**EncryptionResponse**](EncryptionResponse.md)

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

# **device_type4backup_action_on_encryption**
> EncryptionResponse device_type4backup_action_on_encryption(system_id, device_type4_encryption_backup_rekey_input)

Encryption Backup Action on HPE Alletra Storage MP identified by {systemId}

Encryption Backup Action on HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_encryption_backup_rekey_input import DeviceType4EncryptionBackupRekeyInput
from dscc.models.encryption_response import EncryptionResponse
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
    api_instance = dscc.EncryptionApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_encryption_backup_rekey_input = dscc.DeviceType4EncryptionBackupRekeyInput() # DeviceType4EncryptionBackupRekeyInput | 

    try:
        # Encryption Backup Action on HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4backup_action_on_encryption(system_id, device_type4_encryption_backup_rekey_input)
        print("The response of EncryptionApi->device_type4backup_action_on_encryption:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EncryptionApi->device_type4backup_action_on_encryption: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_encryption_backup_rekey_input** | [**DeviceType4EncryptionBackupRekeyInput**](DeviceType4EncryptionBackupRekeyInput.md)|  | 

### Return type

[**EncryptionResponse**](EncryptionResponse.md)

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

# **device_type4check_ekm_configuration**
> CheckekmResponse device_type4check_ekm_configuration(system_id)

Check EKM configuration on HPE Alletra Storage MP identified by {systemId}

Check EKM configuration on HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.checkekm_response import CheckekmResponse
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
    api_instance = dscc.EncryptionApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system

    try:
        # Check EKM configuration on HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4check_ekm_configuration(system_id)
        print("The response of EncryptionApi->device_type4check_ekm_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EncryptionApi->device_type4check_ekm_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 

### Return type

[**CheckekmResponse**](CheckekmResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4enable_action_on_encryption**
> EncryptionResponse device_type4enable_action_on_encryption(system_id, device_type4_encryption_actions_input)

Encryption Enable Action on HPE Alletra Storage MP identified by {systemId}

Encryption Enable Action on HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_encryption_actions_input import DeviceType4EncryptionActionsInput
from dscc.models.encryption_response import EncryptionResponse
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
    api_instance = dscc.EncryptionApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_encryption_actions_input = dscc.DeviceType4EncryptionActionsInput() # DeviceType4EncryptionActionsInput | 

    try:
        # Encryption Enable Action on HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4enable_action_on_encryption(system_id, device_type4_encryption_actions_input)
        print("The response of EncryptionApi->device_type4enable_action_on_encryption:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EncryptionApi->device_type4enable_action_on_encryption: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_encryption_actions_input** | [**DeviceType4EncryptionActionsInput**](DeviceType4EncryptionActionsInput.md)|  | 

### Return type

[**EncryptionResponse**](EncryptionResponse.md)

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

# **device_type4rekey_action_on_encryption**
> EncryptionResponse device_type4rekey_action_on_encryption(system_id, device_type4_encryption_backup_rekey_input)

Encryption Rekey Action on HPE Alletra Storage MP identified by {systemId}

Encryption Rekey Action on HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_encryption_backup_rekey_input import DeviceType4EncryptionBackupRekeyInput
from dscc.models.encryption_response import EncryptionResponse
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
    api_instance = dscc.EncryptionApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_encryption_backup_rekey_input = dscc.DeviceType4EncryptionBackupRekeyInput() # DeviceType4EncryptionBackupRekeyInput | 

    try:
        # Encryption Rekey Action on HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4rekey_action_on_encryption(system_id, device_type4_encryption_backup_rekey_input)
        print("The response of EncryptionApi->device_type4rekey_action_on_encryption:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EncryptionApi->device_type4rekey_action_on_encryption: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_encryption_backup_rekey_input** | [**DeviceType4EncryptionBackupRekeyInput**](DeviceType4EncryptionBackupRekeyInput.md)|  | 

### Return type

[**EncryptionResponse**](EncryptionResponse.md)

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

# **device_type4restore_action_on_encryption**
> TaskResponse device_type4restore_action_on_encryption(system_id, device_type4_encryption_restore_action_input)

Encryption Restore Action on HPE Alletra Storage MP identified by {systemId}

Encryption Restore Action on HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_encryption_restore_action_input import DeviceType4EncryptionRestoreActionInput
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
    api_instance = dscc.EncryptionApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_encryption_restore_action_input = dscc.DeviceType4EncryptionRestoreActionInput() # DeviceType4EncryptionRestoreActionInput | 

    try:
        # Encryption Restore Action on HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4restore_action_on_encryption(system_id, device_type4_encryption_restore_action_input)
        print("The response of EncryptionApi->device_type4restore_action_on_encryption:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EncryptionApi->device_type4restore_action_on_encryption: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_encryption_restore_action_input** | [**DeviceType4EncryptionRestoreActionInput**](DeviceType4EncryptionRestoreActionInput.md)|  | 

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

# **device_type4set_ekm_configuration**
> TaskResponse device_type4set_ekm_configuration(system_id, device_type4_set_ekm_config_input)

Set EKM configuration on HPE Alletra Storage MP identified by {systemId}

Set EKM configuration on HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_set_ekm_config_input import DeviceType4SetEKMConfigInput
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
    api_instance = dscc.EncryptionApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_set_ekm_config_input = dscc.DeviceType4SetEKMConfigInput() # DeviceType4SetEKMConfigInput | 

    try:
        # Set EKM configuration on HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4set_ekm_configuration(system_id, device_type4_set_ekm_config_input)
        print("The response of EncryptionApi->device_type4set_ekm_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EncryptionApi->device_type4set_ekm_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_set_ekm_config_input** | [**DeviceType4SetEKMConfigInput**](DeviceType4SetEKMConfigInput.md)|  | 

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

# **device_type4setekmbackup_action_on_encryption**
> EncryptionResponse device_type4setekmbackup_action_on_encryption(system_id, device_type4_set_ekm_backup_config_input)

Set EKM configuration and Encryption Backup Action on HPE Alletra Storage MP identified by {systemId}

Set EKM configuration and Encryption Backup Action on HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_set_ekm_backup_config_input import DeviceType4SetEKMBackupConfigInput
from dscc.models.encryption_response import EncryptionResponse
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
    api_instance = dscc.EncryptionApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_set_ekm_backup_config_input = dscc.DeviceType4SetEKMBackupConfigInput() # DeviceType4SetEKMBackupConfigInput | 

    try:
        # Set EKM configuration and Encryption Backup Action on HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4setekmbackup_action_on_encryption(system_id, device_type4_set_ekm_backup_config_input)
        print("The response of EncryptionApi->device_type4setekmbackup_action_on_encryption:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EncryptionApi->device_type4setekmbackup_action_on_encryption: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_set_ekm_backup_config_input** | [**DeviceType4SetEKMBackupConfigInput**](DeviceType4SetEKMBackupConfigInput.md)|  | 

### Return type

[**EncryptionResponse**](EncryptionResponse.md)

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

