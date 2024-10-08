# dscc.TasksApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_task**](TasksApi.md#get_task) | **GET** /api/v1/tasks/{id} | Returns details of a specific task
[**list_tasks**](TasksApi.md#list_tasks) | **GET** /api/v1/tasks | Returns a list of tasks accessible by the user


# **get_task**
> Task get_task(id)

Returns details of a specific task

Returns the task with the given id.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task import Task
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
    api_instance = dscc.TasksApi(api_client)
    id = 'c1a0eb78-41a0-4151-93b2-f057ffeca3f3' # str | The UUID of the object

    try:
        # Returns details of a specific task
        api_response = api_instance.get_task(id)
        print("The response of TasksApi->get_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the object | 

### Return type

[**Task**](Task.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Single Task |  -  |
**400** | An invalid request was received. |  -  |
**401** | The request did not provide valid authentication. |  -  |
**403** | The requesting user was not permitted to access this resource. |  -  |
**404** | A task with the provided ID was not found. |  -  |
**500** | An internal error occurred. |  -  |
**503** | Service unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tasks**
> TaskList list_tasks(offset=offset, limit=limit, filter=filter)

Returns a list of tasks accessible by the user

Returns a list of tasks that are visible to the user. The response can be paged by using the limit and offset query parameters and filtered, sorted and ordered by using the filter, sortby and orderby query parameters. 

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_list import TaskList
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
    api_instance = dscc.TasksApi(api_client)
    offset = 30 # int | The offset query parameter should be used in conjunction with limit for paging, e.g.: offset=30&&limit=10. The offset is the number of items from the beginning of the result set to the first item included in the response.  (optional)
    limit = 10 # int | The limit query parameter should be used in conjunction with offset for paging, e.g.: offset=30&&limit=10. The limit is the maximum number of items to include in the response.  (optional)
    filter = 'owner.name eq fred@example.com' # str | The expression to filter responses. (optional)

    try:
        # Returns a list of tasks accessible by the user
        api_response = api_instance.list_tasks(offset=offset, limit=limit, filter=filter)
        print("The response of TasksApi->list_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->list_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The offset query parameter should be used in conjunction with limit for paging, e.g.: offset&#x3D;30&amp;&amp;limit&#x3D;10. The offset is the number of items from the beginning of the result set to the first item included in the response.  | [optional] 
 **limit** | **int**| The limit query parameter should be used in conjunction with offset for paging, e.g.: offset&#x3D;30&amp;&amp;limit&#x3D;10. The limit is the maximum number of items to include in the response.  | [optional] 
 **filter** | **str**| The expression to filter responses. | [optional] 

### Return type

[**TaskList**](TaskList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tasks list |  -  |
**400** | An invalid request was received. |  -  |
**401** | The request did not provide valid authentication. |  -  |
**403** | The requesting user was not permitted to access this resource. |  -  |
**500** | An internal error occurred. |  -  |
**503** | Service unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

