# dscc.AuthzApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_controls**](AuthzApi.md#get_access_controls) | **GET** /api/v1/access-controls | Get User Accessible Resources
[**get_resource_types**](AuthzApi.md#get_resource_types) | **GET** /api/v1/resource-types | Get resource types with read permissions


# **get_access_controls**
> AccessControlsResponse get_access_controls(permission=permission)

Get User Accessible Resources

Retun a list of user permissions.  The returned list of permissions will be based upon the supplied filter.  If no filter was supplied, all user permissions will be returned. It is also possible to request all resource type with certain permission type (ex. ALL.read)

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.access_controls_response import AccessControlsResponse
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
    api_instance = dscc.AuthzApi(api_client)
    permission = ['[\"volume.create\",\"port.read\",\"audit.read\"]'] # List[str] | List of permissions, each of which, has the form \"resource type.permission\" (ex. volume.read,volume.write). The word \"ANY\" can be used as a wild card for the resource type (ex. ANY.read). Omitting the permission parameters is equivalent to asking for all user permissions. (optional)

    try:
        # Get User Accessible Resources
        api_response = api_instance.get_access_controls(permission=permission)
        print("The response of AuthzApi->get_access_controls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthzApi->get_access_controls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission** | [**List[str]**](str.md)| List of permissions, each of which, has the form \&quot;resource type.permission\&quot; (ex. volume.read,volume.write). The word \&quot;ANY\&quot; can be used as a wild card for the resource type (ex. ANY.read). Omitting the permission parameters is equivalent to asking for all user permissions. | [optional] 

### Return type

[**AccessControlsResponse**](AccessControlsResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | The operation cannot be authorized |  -  |
**403** | The operation is forbidden |  -  |
**404** | User not found |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_types**
> ResourceTypesResponse get_resource_types()

Get resource types with read permissions

Return resource types on which the user has a read permission.  The returned list will be based upon the supplied filter.  If no filter was provided, all resource types for which the user has a read permission on will be returned

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.resource_types_response import ResourceTypesResponse
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
    api_instance = dscc.AuthzApi(api_client)

    try:
        # Get resource types with read permissions
        api_response = api_instance.get_resource_types()
        print("The response of AuthzApi->get_resource_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthzApi->get_resource_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ResourceTypesResponse**](ResourceTypesResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | The operation cannot be authorized |  -  |
**403** | The operation is forbidden |  -  |
**404** | User not found |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

