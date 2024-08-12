# dscc.ProtectionTemplatesApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type2_create_protection_template**](ProtectionTemplatesApi.md#device_type2_create_protection_template) | **POST** /api/v1/storage-systems/device-type2/{systemId}/protection-templates | Create protection template on Nimble / Alletra 6K in system identified by {systemId}
[**device_type2_edit_protection_template**](ProtectionTemplatesApi.md#device_type2_edit_protection_template) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/protection-templates/{protectionTemplateId} | Edit details of Nimble / Alletra 6K Protection-templates identified by {protectionTemplateId}
[**device_type2_get_all_protection_templates**](ProtectionTemplatesApi.md#device_type2_get_all_protection_templates) | **GET** /api/v1/storage-systems/device-type2/{systemId}/protection-templates | Get all protection-templates details by Nimble / Alletra 6K
[**device_type2_get_protection_template_by_id**](ProtectionTemplatesApi.md#device_type2_get_protection_template_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/protection-templates/{protectionTemplateId} | Get details of Nimble / Alletra 6K protection-templates identified by {protectionTemplateId}
[**device_type2_remove_protection_template**](ProtectionTemplatesApi.md#device_type2_remove_protection_template) | **POST** /api/v1/storage-systems/device-type2/{systemId}/protection-templates/remove | Remove protection templates for Nimble / Alletra 6K


# **device_type2_create_protection_template**
> TaskResponse device_type2_create_protection_template(system_id, nimble_create_protection_template_input)

Create protection template on Nimble / Alletra 6K in system identified by {systemId}

Create protection template on Nimble / Alletra 6K in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_create_protection_template_input import NimbleCreateProtectionTemplateInput
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
    api_instance = dscc.ProtectionTemplatesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    nimble_create_protection_template_input = dscc.NimbleCreateProtectionTemplateInput() # NimbleCreateProtectionTemplateInput | 

    try:
        # Create protection template on Nimble / Alletra 6K in system identified by {systemId}
        api_response = api_instance.device_type2_create_protection_template(system_id, nimble_create_protection_template_input)
        print("The response of ProtectionTemplatesApi->device_type2_create_protection_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectionTemplatesApi->device_type2_create_protection_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_create_protection_template_input** | [**NimbleCreateProtectionTemplateInput**](NimbleCreateProtectionTemplateInput.md)|  | 

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

# **device_type2_edit_protection_template**
> TaskResponse device_type2_edit_protection_template(system_id, protection_template_id, nimble_edit_protection_template_input)

Edit details of Nimble / Alletra 6K Protection-templates identified by {protectionTemplateId}

Edit  details of Nimble / Alletra 6K Protection-templates identified by {protectionTemplateId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_edit_protection_template_input import NimbleEditProtectionTemplateInput
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
    api_instance = dscc.ProtectionTemplatesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    protection_template_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the Protection Template. A 42 digit hexadecimal number.
    nimble_edit_protection_template_input = dscc.NimbleEditProtectionTemplateInput() # NimbleEditProtectionTemplateInput | 

    try:
        # Edit details of Nimble / Alletra 6K Protection-templates identified by {protectionTemplateId}
        api_response = api_instance.device_type2_edit_protection_template(system_id, protection_template_id, nimble_edit_protection_template_input)
        print("The response of ProtectionTemplatesApi->device_type2_edit_protection_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectionTemplatesApi->device_type2_edit_protection_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **protection_template_id** | **str**| ID of the Protection Template. A 42 digit hexadecimal number. | 
 **nimble_edit_protection_template_input** | [**NimbleEditProtectionTemplateInput**](NimbleEditProtectionTemplateInput.md)|  | 

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

# **device_type2_get_all_protection_templates**
> NimbleProtectionTemplateList device_type2_get_all_protection_templates(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all protection-templates details by Nimble / Alletra 6K

Get all protection-templates details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_protection_template_list import NimbleProtectionTemplateList
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
    api_instance = dscc.ProtectionTemplatesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter Protection Template  by Key. (optional)
    sort = 'name desc' # str | oData query to sort Protection Template  resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all protection-templates details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_protection_templates(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of ProtectionTemplatesApi->device_type2_get_all_protection_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectionTemplatesApi->device_type2_get_all_protection_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter Protection Template  by Key. | [optional] 
 **sort** | **str**| oData query to sort Protection Template  resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleProtectionTemplateList**](NimbleProtectionTemplateList.md)

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

# **device_type2_get_protection_template_by_id**
> NimbleProtectionTemplateDetailsWithRequestUri device_type2_get_protection_template_by_id(system_id, protection_template_id, select=select)

Get details of Nimble / Alletra 6K protection-templates identified by {protectionTemplateId}

Get details of Nimble / Alletra 6K protection-templates identified by {protectionTemplateId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_protection_template_details_with_request_uri import NimbleProtectionTemplateDetailsWithRequestUri
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
    api_instance = dscc.ProtectionTemplatesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    protection_template_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the Protection Template. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Nimble / Alletra 6K protection-templates identified by {protectionTemplateId}
        api_response = api_instance.device_type2_get_protection_template_by_id(system_id, protection_template_id, select=select)
        print("The response of ProtectionTemplatesApi->device_type2_get_protection_template_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectionTemplatesApi->device_type2_get_protection_template_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **protection_template_id** | **str**| ID of the Protection Template. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleProtectionTemplateDetailsWithRequestUri**](NimbleProtectionTemplateDetailsWithRequestUri.md)

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

# **device_type2_remove_protection_template**
> TaskResponse device_type2_remove_protection_template(system_id, remove_protection_templates)

Remove protection templates for Nimble / Alletra 6K

Remove protection templates for Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.remove_protection_templates import RemoveProtectionTemplates
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
    api_instance = dscc.ProtectionTemplatesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    remove_protection_templates = dscc.RemoveProtectionTemplates() # RemoveProtectionTemplates | 

    try:
        # Remove protection templates for Nimble / Alletra 6K
        api_response = api_instance.device_type2_remove_protection_template(system_id, remove_protection_templates)
        print("The response of ProtectionTemplatesApi->device_type2_remove_protection_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectionTemplatesApi->device_type2_remove_protection_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **remove_protection_templates** | [**RemoveProtectionTemplates**](RemoveProtectionTemplates.md)|  | 

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

