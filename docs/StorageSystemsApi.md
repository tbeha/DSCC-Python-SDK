# dscc.StorageSystemsApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device1_latency_factors_get**](StorageSystemsApi.md#device1_latency_factors_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/insights/latencyfactors | Get system level latency factors
[**device1headroom_utilization_get**](StorageSystemsApi.md#device1headroom_utilization_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/headroom-utilization | Get system level saturation details
[**device4_latency_factors_get**](StorageSystemsApi.md#device4_latency_factors_get) | **GET** /api/v1/storage-systems/device-type4/{systemId}/insights/latencyfactors | Get system level latency factors
[**device_type1_application_summary_get**](StorageSystemsApi.md#device_type1_application_summary_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/application-summary | Get Application Summary for a storage system Primera / Alletra 9K
[**device_type1_get_system_performance_statistics**](StorageSystemsApi.md#device_type1_get_system_performance_statistics) | **GET** /api/v1/storage-systems/device-type1/{systemId}/performance-statistics | Get performance statistics for a storage system Primera / Alletra 9K
[**device_type1_qo_s_performance_statistics_get_by_target_name**](StorageSystemsApi.md#device_type1_qo_s_performance_statistics_get_by_target_name) | **GET** /api/v1/storage-systems/device-type1/{systemId}/targets/{targetName}/performance-history | Get QoS performance trend data of Primera / Alletra 9K target identified by {targetName}
[**device_type1_qo_s_policy_get_by_system_id**](StorageSystemsApi.md#device_type1_qo_s_policy_get_by_system_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/qos-policy | Get QoS policy data for a storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_recommendations_get**](StorageSystemsApi.md#device_type1_recommendations_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/recommendations | Get recommendations for a storage system Primera / Alletra 9K
[**device_type1_system_capacity_history_get**](StorageSystemsApi.md#device_type1_system_capacity_history_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/capacity-history | Get capacity trend data for a storage system Primera / Alletra 9K
[**device_type1_system_capacity_summary_get**](StorageSystemsApi.md#device_type1_system_capacity_summary_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/capacity-summary | Get system capacity for a storage system Primera / Alletra 9K
[**device_type1_system_component_performance_statistics_get**](StorageSystemsApi.md#device_type1_system_component_performance_statistics_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/component-performance-statistics | Get component performance statistics details for a storage system Primera / Alletra 9K idenfified by {systemId}
[**device_type1_system_get_by_id**](StorageSystemsApi.md#device_type1_system_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{id} | Get Primera / Alletra 9K object identified by {id}
[**device_type1_system_performance_history_get**](StorageSystemsApi.md#device_type1_system_performance_history_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/performance-history | Get performance trend data for a storage system Primera / Alletra 9K
[**device_type1_systems_list**](StorageSystemsApi.md#device_type1_systems_list) | **GET** /api/v1/storage-systems/device-type1 | Get all Primera / Alletra 9K storage systems
[**device_type2_array_failover**](StorageSystemsApi.md#device_type2_array_failover) | **POST** /api/v1/storage-systems/device-type2/{systemId}/arrays/{arrayId}/actions/failover | Perform failover of Nimble / Alletra 6K array identified by {arrayId}
[**device_type2_create_array**](StorageSystemsApi.md#device_type2_create_array) | **POST** /api/v1/storage-systems/device-type2/{systemId}/arrays | Create Nimble / Alletra 6K array identified by {systemId}
[**device_type2_delete_array_by_id**](StorageSystemsApi.md#device_type2_delete_array_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/arrays/{arrayId} | Delete Nimble / Alletra 6K array identified by {arrayId}
[**device_type2_edit_array_by_id**](StorageSystemsApi.md#device_type2_edit_array_by_id) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/arrays/{arrayId} | Edit  details of Nimble / Alletra 6K array identified by {arrayId}
[**device_type2_edit_storage_system_settings_by_id**](StorageSystemsApi.md#device_type2_edit_storage_system_settings_by_id) | **PUT** /api/v1/storage-systems/device-type2/{systemId} | Edit settings of Nimble / Alletra 6K system identified by {systemId}
[**device_type2_get_application_capacity_statistics_by_id**](StorageSystemsApi.md#device_type2_get_application_capacity_statistics_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/applications/{id}/capacity-stats | Get capacity stats of Application identified by {id} for a storage system Nimble / Alletra 6K
[**device_type2_get_applications_capacity_statistics**](StorageSystemsApi.md#device_type2_get_applications_capacity_statistics) | **GET** /api/v1/storage-systems/device-type2/{systemId}/applications/capacity-stats | Get capacity stats of Applications for a storage system Nimble / Alletra 6K
[**device_type2_get_storage_system**](StorageSystemsApi.md#device_type2_get_storage_system) | **GET** /api/v1/storage-systems/device-type2 | Get all storage systems by Nimble / Alletra 6K
[**device_type2_get_storage_system_by_id**](StorageSystemsApi.md#device_type2_get_storage_system_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId} | Get Nimble / Alletra 6K object identified by {systemId}
[**device_type2_get_storage_system_capacity_history**](StorageSystemsApi.md#device_type2_get_storage_system_capacity_history) | **GET** /api/v1/storage-systems/device-type2/{systemId}/capacity-history | Get capacity trend data for a storage system Nimble / Alletra 6K
[**device_type2_get_storage_system_performance_history**](StorageSystemsApi.md#device_type2_get_storage_system_performance_history) | **GET** /api/v1/storage-systems/device-type2/{systemId}/performance-history | Get performance trend data for a storage system Nimble / Alletra 6K
[**device_type2_merge_groups**](StorageSystemsApi.md#device_type2_merge_groups) | **POST** /api/v1/storage-systems/device-type2/{systemId}/actions/merge | Perform group merge with the specified group.
[**device_type4_application_summary_get**](StorageSystemsApi.md#device_type4_application_summary_get) | **GET** /api/v1/storage-systems/device-type4/{systemId}/application-summary | Get Application Summary for a storage system HPE Alletra Storage MP
[**device_type4_get_headroom_contribution**](StorageSystemsApi.md#device_type4_get_headroom_contribution) | **GET** /api/v1/storage-systems/device-type4/{systemId}/insights/headroom-contribution | Get Top headroom contribution by volumes/Apps for device-type4
[**device_type4_get_hotspots**](StorageSystemsApi.md#device_type4_get_hotspots) | **GET** /api/v1/storage-systems/device-type4/{systemId}/insights/hotspots | Get hotspots for HPE Alletra Storage MP storage system based on resourceType &#x60;VOLUMES or VOLUME-SET&#x60; and metricType &#x60;LATENCY&#x60;
[**device_type4_get_resource_contention_data**](StorageSystemsApi.md#device_type4_get_resource_contention_data) | **GET** /api/v1/storage-systems/device-type4/{systemId}/insights/resource-contention | Get resource contention data for resources &#x60;DISK and CPU&#x60; for device-type4
[**device_type4_get_system_performance_statistics**](StorageSystemsApi.md#device_type4_get_system_performance_statistics) | **GET** /api/v1/storage-systems/device-type4/{systemId}/performance-statistics | Get performance statistics for a storage system HPE Alletra Storage MP
[**device_type4_insights**](StorageSystemsApi.md#device_type4_insights) | **GET** /api/v1/storage-systems/device-type4/systemInsights/insights | Get all insights.
[**device_type4_licenses_get_by_id**](StorageSystemsApi.md#device_type4_licenses_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/licenses | Get licenses of the storage system identified by {systemId}
[**device_type4_recommendations_get**](StorageSystemsApi.md#device_type4_recommendations_get) | **GET** /api/v1/storage-systems/device-type4/{systemId}/recommendations | Get recommendations for a storage system HPE Alletra Storage MP
[**device_type4_system_capacity_forecast_get**](StorageSystemsApi.md#device_type4_system_capacity_forecast_get) | **GET** /api/v1/storage-systems/device-type4/{systemId}/capacity-forecast | Get latest capacity trend data and forecasted data
[**device_type4_system_capacity_history_get**](StorageSystemsApi.md#device_type4_system_capacity_history_get) | **GET** /api/v1/storage-systems/device-type4/{systemId}/capacity-history | Get capacity trend data for a storage system HPE Alletra Storage MP
[**device_type4_system_capacity_summary_get**](StorageSystemsApi.md#device_type4_system_capacity_summary_get) | **GET** /api/v1/storage-systems/device-type4/{systemId}/capacity-summary | Get system capacity for a storage system HPE Alletra Storage MP
[**device_type4_system_capacity_time_until_full**](StorageSystemsApi.md#device_type4_system_capacity_time_until_full) | **GET** /api/v1/storage-systems/device-type4/{systemId}/capacity-timeuntilfull | Get capacity time until full data for a storage system HPE Alletra Storage MP
[**device_type4_system_component_performance_statistics_get**](StorageSystemsApi.md#device_type4_system_component_performance_statistics_get) | **GET** /api/v1/storage-systems/device-type4/{systemId}/component-performance-statistics | Get component performance statistics details for a storage system HPE Alletra Storage MP idenfified by {systemId}
[**device_type4_system_get_by_id**](StorageSystemsApi.md#device_type4_system_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{id} | Get HPE Alletra Storage MP object identified by {id}
[**device_type4_system_locate**](StorageSystemsApi.md#device_type4_system_locate) | **POST** /api/v1/storage-systems/device-type4/{id} | Locate system of HPE Alletra Storage MP
[**device_type4_system_performance_history_get**](StorageSystemsApi.md#device_type4_system_performance_history_get) | **GET** /api/v1/storage-systems/device-type4/{systemId}/performance-history | Get performance trend data for a storage system HPE Alletra Storage MP
[**device_type4_systems_list**](StorageSystemsApi.md#device_type4_systems_list) | **GET** /api/v1/storage-systems/device-type4 | Get all HPE Alletra Storage MP storage systems
[**get_device_type**](StorageSystemsApi.md#get_device_type) | **GET** /api/v1/storage-systems/storage-types | Get all device types
[**get_device_type2_array_by_id**](StorageSystemsApi.md#get_device_type2_array_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/arrays/{arrayId} | Get details of Nimble / Alletra 6K array identified by {arrayId}
[**get_device_type2_arrays**](StorageSystemsApi.md#get_device_type2_arrays) | **GET** /api/v1/storage-systems/device-type2/{systemId}/arrays | Get all arrays details by Nimble / Alletra 6K
[**get_device_type2_uninitialized_array_by_id**](StorageSystemsApi.md#get_device_type2_uninitialized_array_by_id) | **POST** /api/v1/storage-systems/device-type2/{systemId}/uninitialized-arrays/{uninitializedArrayId} | Get  uninitialized arrays details by Nimble / Alletra 6K  identified  by {uninitializedArrayId}
[**get_device_type2_uninitialized_arrays**](StorageSystemsApi.md#get_device_type2_uninitialized_arrays) | **POST** /api/v1/storage-systems/device-type2/{systemId}/uninitialized-arrays | Get all uninitialized arrays details by Nimble / Alletra 6K
[**provisioning_recommendations**](StorageSystemsApi.md#provisioning_recommendations) | **POST** /api/v1/storage-systems/provisioning-recommendations | provisioning recommendations
[**system_get_by_id**](StorageSystemsApi.md#system_get_by_id) | **GET** /api/v1/storage-systems/{id} | Get storage system object identified by {id}
[**system_locate**](StorageSystemsApi.md#system_locate) | **POST** /api/v1/storage-systems/device-type1/{id} | Locate system of Primera / Alletra 9K
[**systems_list**](StorageSystemsApi.md#systems_list) | **GET** /api/v1/storage-systems | Get all storage systems


# **device1_latency_factors_get**
> SystemLatencyFactors device1_latency_factors_get(system_id, time_interval_min, range=range)

Get system level latency factors

Get system level latency factors of system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.system_latency_factors import SystemLatencyFactors
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    time_interval_min = 60 # int | Time interval granularity in minutes
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)

    try:
        # Get system level latency factors
        api_response = api_instance.device1_latency_factors_get(system_id, time_interval_min, range=range)
        print("The response of StorageSystemsApi->device1_latency_factors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device1_latency_factors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **time_interval_min** | **int**| Time interval granularity in minutes | 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 

### Return type

[**SystemLatencyFactors**](SystemLatencyFactors.md)

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

# **device1headroom_utilization_get**
> HeadroomUtilization device1headroom_utilization_get(system_id, time_interval_min, range=range)

Get system level saturation details

Get system level saturation details of system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.headroom_utilization import HeadroomUtilization
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    time_interval_min = 60 # int | Time interval granularity in minutes
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)

    try:
        # Get system level saturation details
        api_response = api_instance.device1headroom_utilization_get(system_id, time_interval_min, range=range)
        print("The response of StorageSystemsApi->device1headroom_utilization_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device1headroom_utilization_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **time_interval_min** | **int**| Time interval granularity in minutes | 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 

### Return type

[**HeadroomUtilization**](HeadroomUtilization.md)

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

# **device4_latency_factors_get**
> DeviceType4SystemLatencyFactors device4_latency_factors_get(system_id, time_interval_min, range=range)

Get system level latency factors

Get system level latency factors of system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_system_latency_factors import DeviceType4SystemLatencyFactors
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    time_interval_min = 56 # int | Time interval granularity in minutes
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)

    try:
        # Get system level latency factors
        api_response = api_instance.device4_latency_factors_get(system_id, time_interval_min, range=range)
        print("The response of StorageSystemsApi->device4_latency_factors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device4_latency_factors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **time_interval_min** | **int**| Time interval granularity in minutes | 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 

### Return type

[**DeviceType4SystemLatencyFactors**](DeviceType4SystemLatencyFactors.md)

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

# **device_type1_application_summary_get**
> ApplicationSummary device_type1_application_summary_get(system_id)

Get Application Summary for a storage system Primera / Alletra 9K

Get Application Summary for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.application_summary import ApplicationSummary
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system

    try:
        # Get Application Summary for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_application_summary_get(system_id)
        print("The response of StorageSystemsApi->device_type1_application_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type1_application_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 

### Return type

[**ApplicationSummary**](ApplicationSummary.md)

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

# **device_type1_get_system_performance_statistics**
> SystemPerformance device_type1_get_system_performance_statistics(system_id, select=select)

Get performance statistics for a storage system Primera / Alletra 9K

Get performance statistics for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.system_performance import SystemPerformance
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get performance statistics for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_get_system_performance_statistics(system_id, select=select)
        print("The response of StorageSystemsApi->device_type1_get_system_performance_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type1_get_system_performance_statistics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**SystemPerformance**](SystemPerformance.md)

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

# **device_type1_qo_s_performance_statistics_get_by_target_name**
> QosPerformanceHistory device_type1_qo_s_performance_statistics_get_by_target_name(system_id, target_name, select=select, range=range, time_interval_min=time_interval_min)

Get QoS performance trend data of Primera / Alletra 9K target identified by {targetName}

Get QoS performance trend data of Primera / Alletra 9K target identified by {targetName}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.qos_performance_history import QosPerformanceHistory
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    target_name = 'targetName eq volume1' # str | targetName will define the QoS target name in which query has to be made.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)

    try:
        # Get QoS performance trend data of Primera / Alletra 9K target identified by {targetName}
        api_response = api_instance.device_type1_qo_s_performance_statistics_get_by_target_name(system_id, target_name, select=select, range=range, time_interval_min=time_interval_min)
        print("The response of StorageSystemsApi->device_type1_qo_s_performance_statistics_get_by_target_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type1_qo_s_performance_statistics_get_by_target_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **target_name** | **str**| targetName will define the QoS target name in which query has to be made. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**QosPerformanceHistory**](QosPerformanceHistory.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_qo_s_policy_get_by_system_id**
> QosPolicy device_type1_qo_s_policy_get_by_system_id(system_id, limit=limit, offset=offset, select=select, range=range, target_name=target_name, target_type=target_type)

Get QoS policy data for a storage system Primera / Alletra 9K identified by {systemId}

Get QoS policy data for a storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.qos_policy import QosPolicy
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    target_name = 'targetName eq volume1' # str | targetName will define the QoS target name in which query has to be made. (optional)
    target_type = 'targetType eq vv' # str | targetType will define the QoS target type in which query has to be made. (optional)

    try:
        # Get QoS policy data for a storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_qo_s_policy_get_by_system_id(system_id, limit=limit, offset=offset, select=select, range=range, target_name=target_name, target_type=target_type)
        print("The response of StorageSystemsApi->device_type1_qo_s_policy_get_by_system_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type1_qo_s_policy_get_by_system_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **target_name** | **str**| targetName will define the QoS target name in which query has to be made. | [optional] 
 **target_type** | **str**| targetType will define the QoS target type in which query has to be made. | [optional] 

### Return type

[**QosPolicy**](QosPolicy.md)

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

# **device_type1_recommendations_get**
> Recommendation device_type1_recommendations_get(system_id, select=select)

Get recommendations for a storage system Primera / Alletra 9K

Get recommendations for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.recommendation import Recommendation
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get recommendations for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_recommendations_get(system_id, select=select)
        print("The response of StorageSystemsApi->device_type1_recommendations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type1_recommendations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**Recommendation**](Recommendation.md)

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

# **device_type1_system_capacity_history_get**
> CapacityHistory device_type1_system_capacity_history_get(system_id, select=select, range=range, time_interval_min=time_interval_min)

Get capacity trend data for a storage system Primera / Alletra 9K

Get capacity trend data for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.capacity_history import CapacityHistory
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 1440 # int | It defines granularity in minutes. (optional)

    try:
        # Get capacity trend data for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_system_capacity_history_get(system_id, select=select, range=range, time_interval_min=time_interval_min)
        print("The response of StorageSystemsApi->device_type1_system_capacity_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type1_system_capacity_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**CapacityHistory**](CapacityHistory.md)

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

# **device_type1_system_capacity_summary_get**
> Syscapacity device_type1_system_capacity_summary_get(system_id, select=select)

Get system capacity for a storage system Primera / Alletra 9K

Get system capacity for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.syscapacity import Syscapacity
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get system capacity for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_system_capacity_summary_get(system_id, select=select)
        print("The response of StorageSystemsApi->device_type1_system_capacity_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type1_system_capacity_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**Syscapacity**](Syscapacity.md)

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

# **device_type1_system_component_performance_statistics_get**
> PerfStats device_type1_system_component_performance_statistics_get(system_id, select=select)

Get component performance statistics details for a storage system Primera / Alletra 9K idenfified by {systemId}

Get component performance statistics details for a storage system Primera / Alletra 9K idenfified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.perf_stats import PerfStats
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get component performance statistics details for a storage system Primera / Alletra 9K idenfified by {systemId}
        api_response = api_instance.device_type1_system_component_performance_statistics_get(system_id, select=select)
        print("The response of StorageSystemsApi->device_type1_system_component_performance_statistics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type1_system_component_performance_statistics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PerfStats**](PerfStats.md)

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

# **device_type1_system_get_by_id**
> PrimeraStorageSystemDetail device_type1_system_get_by_id(id, select=select)

Get Primera / Alletra 9K object identified by {id}

Get Primera / Alletra 9K object identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.primera_storage_system_detail import PrimeraStorageSystemDetail
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
    api_instance = dscc.StorageSystemsApi(api_client)
    id = 'SGH029VBHV' # str | Serial number of the device-type1 storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get Primera / Alletra 9K object identified by {id}
        api_response = api_instance.device_type1_system_get_by_id(id, select=select)
        print("The response of StorageSystemsApi->device_type1_system_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type1_system_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Serial number of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraStorageSystemDetail**](PrimeraStorageSystemDetail.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_system_performance_history_get**
> SystemPerformanceHistory device_type1_system_performance_history_get(system_id, select=select, range=range, time_interval_min=time_interval_min)

Get performance trend data for a storage system Primera / Alletra 9K

Get performance trend data for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.system_performance_history import SystemPerformanceHistory
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)

    try:
        # Get performance trend data for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_system_performance_history_get(system_id, select=select, range=range, time_interval_min=time_interval_min)
        print("The response of StorageSystemsApi->device_type1_system_performance_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type1_system_performance_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**SystemPerformanceHistory**](SystemPerformanceHistory.md)

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

# **device_type1_systems_list**
> PrimeraStorageSystemList device_type1_systems_list(limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all Primera / Alletra 9K storage systems

Get all Primera / Alletra 9K storage systems

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.primera_storage_system_list import PrimeraStorageSystemList
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
    api_instance = dscc.StorageSystemsApi(api_client)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq VEGA_CB1507_8400_2N_150' # str | oData query to filter systems by Key. (optional)
    sort = 'id asc,name desc' # str | Query to sort the response with specified key and order (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all Primera / Alletra 9K storage systems
        api_response = api_instance.device_type1_systems_list(limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of StorageSystemsApi->device_type1_systems_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type1_systems_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter systems by Key. | [optional] 
 **sort** | **str**| Query to sort the response with specified key and order | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraStorageSystemList**](PrimeraStorageSystemList.md)

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

# **device_type2_array_failover**
> TaskResponse device_type2_array_failover(system_id, array_id, nimble_array_failover_input)

Perform failover of Nimble / Alletra 6K array identified by {arrayId}

Perform failover of Nimble / Alletra 6K array identified by {arrayId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_array_failover_input import NimbleArrayFailoverInput
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    array_id = '001df0fe6f7dc7bb16000000000000000000004817' # str | ID of the array.
    nimble_array_failover_input = dscc.NimbleArrayFailoverInput() # NimbleArrayFailoverInput | 

    try:
        # Perform failover of Nimble / Alletra 6K array identified by {arrayId}
        api_response = api_instance.device_type2_array_failover(system_id, array_id, nimble_array_failover_input)
        print("The response of StorageSystemsApi->device_type2_array_failover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type2_array_failover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **array_id** | **str**| ID of the array. | 
 **nimble_array_failover_input** | [**NimbleArrayFailoverInput**](NimbleArrayFailoverInput.md)|  | 

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

# **device_type2_create_array**
> TaskResponse device_type2_create_array(system_id, nimble_create_array_input)

Create Nimble / Alletra 6K array identified by {systemId}

Create Nimble / Alletra 6K array identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_create_array_input import NimbleCreateArrayInput
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    nimble_create_array_input = dscc.NimbleCreateArrayInput() # NimbleCreateArrayInput | 

    try:
        # Create Nimble / Alletra 6K array identified by {systemId}
        api_response = api_instance.device_type2_create_array(system_id, nimble_create_array_input)
        print("The response of StorageSystemsApi->device_type2_create_array:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type2_create_array: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_create_array_input** | [**NimbleCreateArrayInput**](NimbleCreateArrayInput.md)|  | 

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

# **device_type2_delete_array_by_id**
> TaskResponse device_type2_delete_array_by_id(system_id, array_id)

Delete Nimble / Alletra 6K array identified by {arrayId}

Delete Nimble / Alletra 6K array identified by {arrayId}

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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    array_id = '001df0fe6f7dc7bb16000000000000000000004817' # str | ID of the array.

    try:
        # Delete Nimble / Alletra 6K array identified by {arrayId}
        api_response = api_instance.device_type2_delete_array_by_id(system_id, array_id)
        print("The response of StorageSystemsApi->device_type2_delete_array_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type2_delete_array_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **array_id** | **str**| ID of the array. | 

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

# **device_type2_edit_array_by_id**
> TaskResponse device_type2_edit_array_by_id(system_id, array_id, nimble_edit_array_input)

Edit  details of Nimble / Alletra 6K array identified by {arrayId}

Edit  details of Nimble / Alletra 6K array identified by {arrayId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_edit_array_input import NimbleEditArrayInput
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    array_id = '001df0fe6f7dc7bb16000000000000000000004817' # str | ID of the array.
    nimble_edit_array_input = dscc.NimbleEditArrayInput() # NimbleEditArrayInput | 

    try:
        # Edit  details of Nimble / Alletra 6K array identified by {arrayId}
        api_response = api_instance.device_type2_edit_array_by_id(system_id, array_id, nimble_edit_array_input)
        print("The response of StorageSystemsApi->device_type2_edit_array_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type2_edit_array_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **array_id** | **str**| ID of the array. | 
 **nimble_edit_array_input** | [**NimbleEditArrayInput**](NimbleEditArrayInput.md)|  | 

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

# **device_type2_edit_storage_system_settings_by_id**
> TaskResponse device_type2_edit_storage_system_settings_by_id(system_id, nimble_edit_group_input)

Edit settings of Nimble / Alletra 6K system identified by {systemId}

Edit settings of Nimble / Alletra 6K system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_edit_group_input import NimbleEditGroupInput
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    nimble_edit_group_input = dscc.NimbleEditGroupInput() # NimbleEditGroupInput | 

    try:
        # Edit settings of Nimble / Alletra 6K system identified by {systemId}
        api_response = api_instance.device_type2_edit_storage_system_settings_by_id(system_id, nimble_edit_group_input)
        print("The response of StorageSystemsApi->device_type2_edit_storage_system_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type2_edit_storage_system_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_edit_group_input** | [**NimbleEditGroupInput**](NimbleEditGroupInput.md)|  | 

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

# **device_type2_get_application_capacity_statistics_by_id**
> NimbleSpaceDomainDetailsWithRequestUri device_type2_get_application_capacity_statistics_by_id(system_id, id, select=select)

Get capacity stats of Application identified by {id} for a storage system Nimble / Alletra 6K

Get capacity stats of Application identified by {id} for a storage system Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_space_domain_details_with_request_uri import NimbleSpaceDomainDetailsWithRequestUri
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the application-summery. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get capacity stats of Application identified by {id} for a storage system Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_application_capacity_statistics_by_id(system_id, id, select=select)
        print("The response of StorageSystemsApi->device_type2_get_application_capacity_statistics_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type2_get_application_capacity_statistics_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **id** | **str**| ID of the application-summery. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleSpaceDomainDetailsWithRequestUri**](NimbleSpaceDomainDetailsWithRequestUri.md)

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

# **device_type2_get_applications_capacity_statistics**
> NimbleSpaceDomainList device_type2_get_applications_capacity_statistics(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get capacity stats of Applications for a storage system Nimble / Alletra 6K

Get capacity stats of Applications for a storage system Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_space_domain_list import NimbleSpaceDomainList
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter application summery by Key. (optional)
    sort = 'name desc' # str | oData query to sort application summery resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get capacity stats of Applications for a storage system Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_applications_capacity_statistics(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of StorageSystemsApi->device_type2_get_applications_capacity_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type2_get_applications_capacity_statistics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter application summery by Key. | [optional] 
 **sort** | **str**| oData query to sort application summery resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleSpaceDomainList**](NimbleSpaceDomainList.md)

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

# **device_type2_get_storage_system**
> NimbleStorageSystemSummaryList device_type2_get_storage_system(limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all storage systems by Nimble / Alletra 6K

Get all storage systems by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_storage_system_summary_list import NimbleStorageSystemSummaryList
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
    api_instance = dscc.StorageSystemsApi(api_client)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'NAME eq g1a1' # str | Lucene query to filter systems by Key. (optional)
    sort = 'name desc' # str | Lucene query to sort systems by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all storage systems by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_storage_system(limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of StorageSystemsApi->device_type2_get_storage_system:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type2_get_storage_system: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter systems by Key. | [optional] 
 **sort** | **str**| Lucene query to sort systems by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleStorageSystemSummaryList**](NimbleStorageSystemSummaryList.md)

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

# **device_type2_get_storage_system_by_id**
> NimbleStorageSystemDetailsWithRequestUri device_type2_get_storage_system_by_id(system_id, select=select)

Get Nimble / Alletra 6K object identified by {systemId}

Get Nimble / Alletra 6K object identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_storage_system_details_with_request_uri import NimbleStorageSystemDetailsWithRequestUri
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get Nimble / Alletra 6K object identified by {systemId}
        api_response = api_instance.device_type2_get_storage_system_by_id(system_id, select=select)
        print("The response of StorageSystemsApi->device_type2_get_storage_system_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type2_get_storage_system_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleStorageSystemDetailsWithRequestUri**](NimbleStorageSystemDetailsWithRequestUri.md)

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

# **device_type2_get_storage_system_capacity_history**
> NimblecapacityHistory device_type2_get_storage_system_capacity_history(system_id, select=select, range=range, time_interval_min=time_interval_min)

Get capacity trend data for a storage system Nimble / Alletra 6K

Get capacity trend data for a storage system Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimblecapacity_history import NimblecapacityHistory
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)

    try:
        # Get capacity trend data for a storage system Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_storage_system_capacity_history(system_id, select=select, range=range, time_interval_min=time_interval_min)
        print("The response of StorageSystemsApi->device_type2_get_storage_system_capacity_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type2_get_storage_system_capacity_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**NimblecapacityHistory**](NimblecapacityHistory.md)

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

# **device_type2_get_storage_system_performance_history**
> SysPerformanceHistory device_type2_get_storage_system_performance_history(system_id, select=select, range=range, time_interval_min=time_interval_min)

Get performance trend data for a storage system Nimble / Alletra 6K

Get performance trend data for a storage system Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.sys_performance_history import SysPerformanceHistory
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)

    try:
        # Get performance trend data for a storage system Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_storage_system_performance_history(system_id, select=select, range=range, time_interval_min=time_interval_min)
        print("The response of StorageSystemsApi->device_type2_get_storage_system_performance_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type2_get_storage_system_performance_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**SysPerformanceHistory**](SysPerformanceHistory.md)

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

# **device_type2_merge_groups**
> TaskResponse device_type2_merge_groups(system_id, nimble_merge_groups_input)

Perform group merge with the specified group.

Perform group merge with the specified group.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_merge_groups_input import NimbleMergeGroupsInput
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    nimble_merge_groups_input = dscc.NimbleMergeGroupsInput() # NimbleMergeGroupsInput | 

    try:
        # Perform group merge with the specified group.
        api_response = api_instance.device_type2_merge_groups(system_id, nimble_merge_groups_input)
        print("The response of StorageSystemsApi->device_type2_merge_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type2_merge_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_merge_groups_input** | [**NimbleMergeGroupsInput**](NimbleMergeGroupsInput.md)|  | 

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
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_application_summary_get**
> DeviceType4ApplicationSummary device_type4_application_summary_get(system_id)

Get Application Summary for a storage system HPE Alletra Storage MP

Get Application Summary for a storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_application_summary import DeviceType4ApplicationSummary
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system

    try:
        # Get Application Summary for a storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_application_summary_get(system_id)
        print("The response of StorageSystemsApi->device_type4_application_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type4_application_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 

### Return type

[**DeviceType4ApplicationSummary**](DeviceType4ApplicationSummary.md)

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

# **device_type4_get_headroom_contribution**
> HeadroomContribution device_type4_get_headroom_contribution(system_id, time_interval_min, range, resource_type=resource_type)

Get Top headroom contribution by volumes/Apps for device-type4

Get Top headroom contribution by volumes/Apps for device-type4

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.headroom_contribution import HeadroomContribution
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = 'ABC239XFZ9' # str | SystemId of the HPE Alletra Storage MP storage system
    time_interval_min = 56 # int | Time interval granularity in minutes
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | Specifies the time period for which hotspot metrics are to be calculated. Both startTime and endTime should be specified
    resource_type = VOLUMES # str | Query to select resource (volumes, volume-set) for getting Headroom Contributors (optional) (default to VOLUMES)

    try:
        # Get Top headroom contribution by volumes/Apps for device-type4
        api_response = api_instance.device_type4_get_headroom_contribution(system_id, time_interval_min, range, resource_type=resource_type)
        print("The response of StorageSystemsApi->device_type4_get_headroom_contribution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type4_get_headroom_contribution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| SystemId of the HPE Alletra Storage MP storage system | 
 **time_interval_min** | **int**| Time interval granularity in minutes | 
 **range** | **str**| Specifies the time period for which hotspot metrics are to be calculated. Both startTime and endTime should be specified | 
 **resource_type** | **str**| Query to select resource (volumes, volume-set) for getting Headroom Contributors | [optional] [default to VOLUMES]

### Return type

[**HeadroomContribution**](HeadroomContribution.md)

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

# **device_type4_get_hotspots**
> Hotspots device_type4_get_hotspots(system_id, time_interval_min, range, operation_type=operation_type, resource_type=resource_type, metric_type=metric_type)

Get hotspots for HPE Alletra Storage MP storage system based on resourceType `VOLUMES or VOLUME-SET` and metricType `LATENCY`

Get the top hotspots segregated into read and write categories

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.hotspots import Hotspots
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = 'ABC239XFZ9' # str | SystemId of the HPE Alletra Storage MP storage system
    time_interval_min = 56 # int | Time interval granularity in minutes
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | Specifies the time period for which hotspot metrics are to be calculated. Both startTime and endTime should be specified
    operation_type = 'READ' # str | Indicates if hotspots metrics to be calculated for read, write or both operations. If this field is not provided, hotspots are calculated for both operations (optional)
    resource_type = VOLUMES # str | Query to select resource (volumes, volume-set) for analytics (optional) (default to VOLUMES)
    metric_type = LATENCY # str | Query to select metric for which hotspot is to calculated (optional) (default to LATENCY)

    try:
        # Get hotspots for HPE Alletra Storage MP storage system based on resourceType `VOLUMES or VOLUME-SET` and metricType `LATENCY`
        api_response = api_instance.device_type4_get_hotspots(system_id, time_interval_min, range, operation_type=operation_type, resource_type=resource_type, metric_type=metric_type)
        print("The response of StorageSystemsApi->device_type4_get_hotspots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type4_get_hotspots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| SystemId of the HPE Alletra Storage MP storage system | 
 **time_interval_min** | **int**| Time interval granularity in minutes | 
 **range** | **str**| Specifies the time period for which hotspot metrics are to be calculated. Both startTime and endTime should be specified | 
 **operation_type** | **str**| Indicates if hotspots metrics to be calculated for read, write or both operations. If this field is not provided, hotspots are calculated for both operations | [optional] 
 **resource_type** | **str**| Query to select resource (volumes, volume-set) for analytics | [optional] [default to VOLUMES]
 **metric_type** | **str**| Query to select metric for which hotspot is to calculated | [optional] [default to LATENCY]

### Return type

[**Hotspots**](Hotspots.md)

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

# **device_type4_get_resource_contention_data**
> ResourceContention device_type4_get_resource_contention_data(system_id, time_interval_min, range, resource_contention_type=resource_contention_type)

Get resource contention data for resources `DISK and CPU` for device-type4

Get the top volume contributors and timeseries data for disk and cpu resource contention

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.resource_contention import ResourceContention
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = 'ABC239XFZ9' # str | SystemId of the HPE Alletra Storage MP storage system
    time_interval_min = 56 # int | Time interval granularity in minutes
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | Specifies the time period for which hotspot metrics are to be calculated. Both startTime and endTime should be specified
    resource_contention_type = 'DISK' # str | Indicates if resource contention has to be calculated for disk, cpu or both resources. If this field is not provided, resource contention is calculated for both resources (optional)

    try:
        # Get resource contention data for resources `DISK and CPU` for device-type4
        api_response = api_instance.device_type4_get_resource_contention_data(system_id, time_interval_min, range, resource_contention_type=resource_contention_type)
        print("The response of StorageSystemsApi->device_type4_get_resource_contention_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type4_get_resource_contention_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| SystemId of the HPE Alletra Storage MP storage system | 
 **time_interval_min** | **int**| Time interval granularity in minutes | 
 **range** | **str**| Specifies the time period for which hotspot metrics are to be calculated. Both startTime and endTime should be specified | 
 **resource_contention_type** | **str**| Indicates if resource contention has to be calculated for disk, cpu or both resources. If this field is not provided, resource contention is calculated for both resources | [optional] 

### Return type

[**ResourceContention**](ResourceContention.md)

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

# **device_type4_get_system_performance_statistics**
> DeviceType4SystemPerformance device_type4_get_system_performance_statistics(system_id, select=select)

Get performance statistics for a storage system HPE Alletra Storage MP

Get performance statistics for a storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_system_performance import DeviceType4SystemPerformance
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get performance statistics for a storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_get_system_performance_statistics(system_id, select=select)
        print("The response of StorageSystemsApi->device_type4_get_system_performance_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type4_get_system_performance_statistics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4SystemPerformance**](DeviceType4SystemPerformance.md)

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

# **device_type4_insights**
> InsightsResponse device_type4_insights(filter=filter)

Get all insights.

List all insights.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.insights_response import InsightsResponse
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
    api_instance = dscc.StorageSystemsApi(api_client)
    filter = 'filter_example' # str | GET /api/v1/insights?filter=type eq 'TIME_UNTIL_FULL' GET /api/v1/insights?filter=score lt 3 GET /api/v1/insights?filter=value gt 60 GET /api/v1/insights?filter=date eq '2024-05-12'  (optional)

    try:
        # Get all insights.
        api_response = api_instance.device_type4_insights(filter=filter)
        print("The response of StorageSystemsApi->device_type4_insights:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type4_insights: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| GET /api/v1/insights?filter&#x3D;type eq &#39;TIME_UNTIL_FULL&#39; GET /api/v1/insights?filter&#x3D;score lt 3 GET /api/v1/insights?filter&#x3D;value gt 60 GET /api/v1/insights?filter&#x3D;date eq &#39;2024-05-12&#39;  | [optional] 

### Return type

[**InsightsResponse**](InsightsResponse.md)

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
**401** | Unauthorized request |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_licenses_get_by_id**
> DeviceType4Licenses device_type4_licenses_get_by_id(system_id)

Get licenses of the storage system identified by {systemId}

Get licenses of the storage system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_licenses import DeviceType4Licenses
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system

    try:
        # Get licenses of the storage system identified by {systemId}
        api_response = api_instance.device_type4_licenses_get_by_id(system_id)
        print("The response of StorageSystemsApi->device_type4_licenses_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type4_licenses_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 

### Return type

[**DeviceType4Licenses**](DeviceType4Licenses.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_recommendations_get**
> DeviceType4Recommendation device_type4_recommendations_get(system_id, select=select)

Get recommendations for a storage system HPE Alletra Storage MP

Get recommendations for a storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_recommendation import DeviceType4Recommendation
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get recommendations for a storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_recommendations_get(system_id, select=select)
        print("The response of StorageSystemsApi->device_type4_recommendations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type4_recommendations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4Recommendation**](DeviceType4Recommendation.md)

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

# **device_type4_system_capacity_forecast_get**
> DeviceType4CapacityForecast device_type4_system_capacity_forecast_get(system_id, start_time=start_time)

Get latest capacity trend data and forecasted data

Get latest capacity trend data and forecasted data

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_capacity_forecast import DeviceType4CapacityForecast
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    start_time = 1591601529000 # int | Start time from which forecasted data is needed (optional)

    try:
        # Get latest capacity trend data and forecasted data
        api_response = api_instance.device_type4_system_capacity_forecast_get(system_id, start_time=start_time)
        print("The response of StorageSystemsApi->device_type4_system_capacity_forecast_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type4_system_capacity_forecast_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **start_time** | **int**| Start time from which forecasted data is needed | [optional] 

### Return type

[**DeviceType4CapacityForecast**](DeviceType4CapacityForecast.md)

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

# **device_type4_system_capacity_history_get**
> DeviceType4CapacityHistory device_type4_system_capacity_history_get(system_id, select=select, range=range, time_interval_min=time_interval_min)

Get capacity trend data for a storage system HPE Alletra Storage MP

Get capacity trend data for a storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_capacity_history import DeviceType4CapacityHistory
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 1440 # int | It defines granularity in minutes. (optional)

    try:
        # Get capacity trend data for a storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_system_capacity_history_get(system_id, select=select, range=range, time_interval_min=time_interval_min)
        print("The response of StorageSystemsApi->device_type4_system_capacity_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type4_system_capacity_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**DeviceType4CapacityHistory**](DeviceType4CapacityHistory.md)

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

# **device_type4_system_capacity_summary_get**
> DeviceType4SysCapacity device_type4_system_capacity_summary_get(system_id, select=select)

Get system capacity for a storage system HPE Alletra Storage MP

Get system capacity for a storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_sys_capacity import DeviceType4SysCapacity
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get system capacity for a storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_system_capacity_summary_get(system_id, select=select)
        print("The response of StorageSystemsApi->device_type4_system_capacity_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type4_system_capacity_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4SysCapacity**](DeviceType4SysCapacity.md)

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

# **device_type4_system_capacity_time_until_full**
> DeviceType4CapacityTimeUntilFull device_type4_system_capacity_time_until_full(system_id)

Get capacity time until full data for a storage system HPE Alletra Storage MP

Get capacity time until full data for a storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_capacity_time_until_full import DeviceType4CapacityTimeUntilFull
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system

    try:
        # Get capacity time until full data for a storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_system_capacity_time_until_full(system_id)
        print("The response of StorageSystemsApi->device_type4_system_capacity_time_until_full:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type4_system_capacity_time_until_full: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 

### Return type

[**DeviceType4CapacityTimeUntilFull**](DeviceType4CapacityTimeUntilFull.md)

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

# **device_type4_system_component_performance_statistics_get**
> DeviceType4PerfStats device_type4_system_component_performance_statistics_get(system_id, select=select)

Get component performance statistics details for a storage system HPE Alletra Storage MP idenfified by {systemId}

Get component performance statistics details for a storage system HPE Alletra Storage MP idenfified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_perf_stats import DeviceType4PerfStats
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get component performance statistics details for a storage system HPE Alletra Storage MP idenfified by {systemId}
        api_response = api_instance.device_type4_system_component_performance_statistics_get(system_id, select=select)
        print("The response of StorageSystemsApi->device_type4_system_component_performance_statistics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type4_system_component_performance_statistics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4PerfStats**](DeviceType4PerfStats.md)

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

# **device_type4_system_get_by_id**
> DeviceType4StorageSystemDetail device_type4_system_get_by_id(id, select=select)

Get HPE Alletra Storage MP object identified by {id}

Get HPE Alletra Storage MP object identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_storage_system_detail import DeviceType4StorageSystemDetail
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
    api_instance = dscc.StorageSystemsApi(api_client)
    id = 'SGH029VBHV' # str | Serial number of the device-type1 storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get HPE Alletra Storage MP object identified by {id}
        api_response = api_instance.device_type4_system_get_by_id(id, select=select)
        print("The response of StorageSystemsApi->device_type4_system_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type4_system_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Serial number of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4StorageSystemDetail**](DeviceType4StorageSystemDetail.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_system_locate**
> TaskResponse device_type4_system_locate(id, device_type4_sys_locate_input)

Locate system of HPE Alletra Storage MP

Locate system of HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_sys_locate_input import DeviceType4SysLocateInput
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
    api_instance = dscc.StorageSystemsApi(api_client)
    id = 'SGH029VBHV' # str | Serial number of the device-type1 storage system
    device_type4_sys_locate_input = dscc.DeviceType4SysLocateInput() # DeviceType4SysLocateInput | 

    try:
        # Locate system of HPE Alletra Storage MP
        api_response = api_instance.device_type4_system_locate(id, device_type4_sys_locate_input)
        print("The response of StorageSystemsApi->device_type4_system_locate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type4_system_locate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Serial number of the device-type1 storage system | 
 **device_type4_sys_locate_input** | [**DeviceType4SysLocateInput**](DeviceType4SysLocateInput.md)|  | 

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

# **device_type4_system_performance_history_get**
> DeviceType4SystemPerformanceHistory device_type4_system_performance_history_get(system_id, select=select, range=range, time_interval_min=time_interval_min)

Get performance trend data for a storage system HPE Alletra Storage MP

Get performance trend data for a storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_system_performance_history import DeviceType4SystemPerformanceHistory
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)

    try:
        # Get performance trend data for a storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_system_performance_history_get(system_id, select=select, range=range, time_interval_min=time_interval_min)
        print("The response of StorageSystemsApi->device_type4_system_performance_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type4_system_performance_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**DeviceType4SystemPerformanceHistory**](DeviceType4SystemPerformanceHistory.md)

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

# **device_type4_systems_list**
> DeviceType4StorageSystemList device_type4_systems_list(limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all HPE Alletra Storage MP storage systems

Get all HPE Alletra Storage MP storage systems

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_storage_system_list import DeviceType4StorageSystemList
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
    api_instance = dscc.StorageSystemsApi(api_client)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq VEGA_CB1507_8400_2N_150' # str | oData query to filter systems by Key. (optional)
    sort = 'id asc,name desc' # str | Query to sort the response with specified key and order (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all HPE Alletra Storage MP storage systems
        api_response = api_instance.device_type4_systems_list(limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of StorageSystemsApi->device_type4_systems_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->device_type4_systems_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter systems by Key. | [optional] 
 **sort** | **str**| Query to sort the response with specified key and order | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4StorageSystemList**](DeviceType4StorageSystemList.md)

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

# **get_device_type**
> StorageTypes get_device_type()

Get all device types

Get all device types

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.storage_types import StorageTypes
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
    api_instance = dscc.StorageSystemsApi(api_client)

    try:
        # Get all device types
        api_response = api_instance.get_device_type()
        print("The response of StorageSystemsApi->get_device_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->get_device_type: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StorageTypes**](StorageTypes.md)

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

# **get_device_type2_array_by_id**
> NimbleArrayDetailsWithRequestUri get_device_type2_array_by_id(system_id, array_id, select=select)

Get details of Nimble / Alletra 6K array identified by {arrayId}

Get details of Nimble / Alletra 6K array identified by {arrayId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_array_details_with_request_uri import NimbleArrayDetailsWithRequestUri
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    array_id = '001df0fe6f7dc7bb16000000000000000000004817' # str | ID of the array.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Nimble / Alletra 6K array identified by {arrayId}
        api_response = api_instance.get_device_type2_array_by_id(system_id, array_id, select=select)
        print("The response of StorageSystemsApi->get_device_type2_array_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->get_device_type2_array_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **array_id** | **str**| ID of the array. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleArrayDetailsWithRequestUri**](NimbleArrayDetailsWithRequestUri.md)

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

# **get_device_type2_arrays**
> NimbleNewArrayList get_device_type2_arrays(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all arrays details by Nimble / Alletra 6K

Get all arrays details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_new_array_list import NimbleNewArrayList
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter array by Key. (optional)
    sort = 'name desc' # str | oData query to sort array resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all arrays details by Nimble / Alletra 6K
        api_response = api_instance.get_device_type2_arrays(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of StorageSystemsApi->get_device_type2_arrays:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->get_device_type2_arrays: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter array by Key. | [optional] 
 **sort** | **str**| oData query to sort array resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleNewArrayList**](NimbleNewArrayList.md)

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

# **get_device_type2_uninitialized_array_by_id**
> NimbleUninitializedArrayWithRequestUri get_device_type2_uninitialized_array_by_id(system_id, uninitialized_array_id, nimble_uninitialized_array_input, select=select)

Get  uninitialized arrays details by Nimble / Alletra 6K  identified  by {uninitializedArrayId}

Get uninitialized arrays details by Nimble / Alletra 6K identified  by {uninitializedArrayId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_uninitialized_array_input import NimbleUninitializedArrayInput
from dscc.models.nimble_uninitialized_array_with_request_uri import NimbleUninitializedArrayWithRequestUri
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    uninitialized_array_id = 'c463732d6436306437370000000000000000000000' # str | ID of the uninitialized Array.A 42 digit hexadecimal number.
    nimble_uninitialized_array_input = dscc.NimbleUninitializedArrayInput() # NimbleUninitializedArrayInput | 
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get  uninitialized arrays details by Nimble / Alletra 6K  identified  by {uninitializedArrayId}
        api_response = api_instance.get_device_type2_uninitialized_array_by_id(system_id, uninitialized_array_id, nimble_uninitialized_array_input, select=select)
        print("The response of StorageSystemsApi->get_device_type2_uninitialized_array_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->get_device_type2_uninitialized_array_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **uninitialized_array_id** | **str**| ID of the uninitialized Array.A 42 digit hexadecimal number. | 
 **nimble_uninitialized_array_input** | [**NimbleUninitializedArrayInput**](NimbleUninitializedArrayInput.md)|  | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleUninitializedArrayWithRequestUri**](NimbleUninitializedArrayWithRequestUri.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

# **get_device_type2_uninitialized_arrays**
> NimbleUninitializedArrayResponse get_device_type2_uninitialized_arrays(system_id)

Get all uninitialized arrays details by Nimble / Alletra 6K

Get all uninitialized arrays details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_uninitialized_array_response import NimbleUninitializedArrayResponse
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
    api_instance = dscc.StorageSystemsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system

    try:
        # Get all uninitialized arrays details by Nimble / Alletra 6K
        api_response = api_instance.get_device_type2_uninitialized_arrays(system_id)
        print("The response of StorageSystemsApi->get_device_type2_uninitialized_arrays:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->get_device_type2_uninitialized_arrays: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 

### Return type

[**NimbleUninitializedArrayResponse**](NimbleUninitializedArrayResponse.md)

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

# **provisioning_recommendations**
> StorageSystemRecommendationList provisioning_recommendations(recommendation_input)

provisioning recommendations

provisioning recommendations

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.recommendation_input import RecommendationInput
from dscc.models.storage_system_recommendation_list import StorageSystemRecommendationList
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
    api_instance = dscc.StorageSystemsApi(api_client)
    recommendation_input = dscc.RecommendationInput() # RecommendationInput | 

    try:
        # provisioning recommendations
        api_response = api_instance.provisioning_recommendations(recommendation_input)
        print("The response of StorageSystemsApi->provisioning_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->provisioning_recommendations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recommendation_input** | [**RecommendationInput**](RecommendationInput.md)|  | 

### Return type

[**StorageSystemRecommendationList**](StorageSystemRecommendationList.md)

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

# **system_get_by_id**
> StorageSystemDetail system_get_by_id(id, select=select)

Get storage system object identified by {id}

Get storage system object identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.storage_system_detail import StorageSystemDetail
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
    api_instance = dscc.StorageSystemsApi(api_client)
    id = 'SGH029VBHV' # str | Serial number of the device-type1 storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get storage system object identified by {id}
        api_response = api_instance.system_get_by_id(id, select=select)
        print("The response of StorageSystemsApi->system_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->system_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Serial number of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**StorageSystemDetail**](StorageSystemDetail.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_locate**
> TaskResponse system_locate(id, sys_locate_input)

Locate system of Primera / Alletra 9K

Locate system of Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.sys_locate_input import SysLocateInput
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
    api_instance = dscc.StorageSystemsApi(api_client)
    id = 'SGH029VBHV' # str | Serial number of the device-type1 storage system
    sys_locate_input = dscc.SysLocateInput() # SysLocateInput | 

    try:
        # Locate system of Primera / Alletra 9K
        api_response = api_instance.system_locate(id, sys_locate_input)
        print("The response of StorageSystemsApi->system_locate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->system_locate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Serial number of the device-type1 storage system | 
 **sys_locate_input** | [**SysLocateInput**](SysLocateInput.md)|  | 

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

# **systems_list**
> StorageSystemSummaryList systems_list(limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all storage systems

Get all storage systems

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.storage_system_summary_list import StorageSystemSummaryList
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
    api_instance = dscc.StorageSystemsApi(api_client)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq VEGA_CB1507_8400_2N_150' # str | oData query to filter systems by Key. (optional)
    sort = 'id asc,name desc' # str | Query to sort the response with specified key and order (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all storage systems
        api_response = api_instance.systems_list(limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of StorageSystemsApi->systems_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->systems_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter systems by Key. | [optional] 
 **sort** | **str**| Query to sort the response with specified key and order | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**StorageSystemSummaryList**](StorageSystemSummaryList.md)

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

