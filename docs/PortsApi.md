# dscc.PortsApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type1_fc_port_edit**](PortsApi.md#device_type1_fc_port_edit) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/ports/{id}/fc | Edit ports identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type1_iscsi_port_edit**](PortsApi.md#device_type1_iscsi_port_edit) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/ports/{id}/edit-iscsi | Edit iscsi ports identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type1_iscsi_port_ping**](PortsApi.md#device_type1_iscsi_port_ping) | **POST** /api/v1/storage-systems/device-type1/{systemId}/ports/{id}/ping-iscsi | Ping iscsi ports identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type1_ports_clear**](PortsApi.md#device_type1_ports_clear) | **POST** /api/v1/storage-systems/device-type1/{systemId}/ports/{id}/clear | Clear the details of the ports identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type1_ports_get_by_id**](PortsApi.md#device_type1_ports_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/ports/{id} | Get details of Primera / Alletra 9K Port identified by {id}
[**device_type1_ports_list**](PortsApi.md#device_type1_ports_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/ports | Get details of Primera / Alletra 9K Ports
[**device_type1_ports_performance_history_get**](PortsApi.md#device_type1_ports_performance_history_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/ports-performance | Get details of performance metrics of Primera/ Alletra 9K host ports on storage system identified by {systemid}
[**device_type1_rcip_port_edit**](PortsApi.md#device_type1_rcip_port_edit) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/ports/{id}/edit-rcip | Edit rcip ports identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type1_rcip_port_ping**](PortsApi.md#device_type1_rcip_port_ping) | **POST** /api/v1/storage-systems/device-type1/{systemId}/ports/{id}/ping-rcip | Ping rcip ports identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type2_edit_fc_port**](PortsApi.md#device_type2_edit_fc_port) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/ports/{portId} | Edit Nimble FC Port of Nimble / Alletra 6K
[**device_type2_get_all_fibre_channel_configs**](PortsApi.md#device_type2_get_all_fibre_channel_configs) | **GET** /api/v1/storage-systems/device-type2/{systemId}/fibre-channel-configs | Get all fibre channel configs details of Nimble / Alletra 6K
[**device_type2_get_all_fibre_channel_sessions**](PortsApi.md#device_type2_get_all_fibre_channel_sessions) | **GET** /api/v1/storage-systems/device-type2/{systemId}/fibre-channel-sessions | Get all fibre channel sessions details of Nimble / Alletra 6K
[**device_type2_get_all_ports**](PortsApi.md#device_type2_get_all_ports) | **GET** /api/v1/storage-systems/device-type2/{systemId}/ports | Get all ports details of Nimble / Alletra 6K
[**device_type2_get_fibre_channel_config_by_id**](PortsApi.md#device_type2_get_fibre_channel_config_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/fibre-channel-configs/{fcConfigId} | Get fibre channel configs details of Nimble / Alletra 6K identified by {fcConfigId}.
[**device_type2_get_fibre_channel_session_by_id**](PortsApi.md#device_type2_get_fibre_channel_session_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/fibre-channel-sessions/{fcSessionId} | Get fibre channel session details of Nimble / Alletra 6K identified by {fcSessionId}.
[**device_type2_get_port_by_id**](PortsApi.md#device_type2_get_port_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/ports/{portId} | Get details of Nimble / Alletra 6K Port identified by {portId}. Fibre_channel_interfaces attributes will be shown for Fibre_channel_interface ports. Network_interfaces attributes will be shown for Network_interface ports.
[**device_type4_fc_port_edit**](PortsApi.md#device_type4_fc_port_edit) | **PUT** /api/v1/storage-systems/device-type4/{systemId}/ports/{id}/fc | Edit ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
[**device_type4_iscsi_port_edit**](PortsApi.md#device_type4_iscsi_port_edit) | **PUT** /api/v1/storage-systems/device-type4/{systemId}/ports/{id}/edit-iscsi | Edit iscsi ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
[**device_type4_iscsi_port_ping**](PortsApi.md#device_type4_iscsi_port_ping) | **POST** /api/v1/storage-systems/device-type4/{systemId}/ports/{id}/ping-iscsi | Ping iscsi ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
[**device_type4_nvme_port_edit**](PortsApi.md#device_type4_nvme_port_edit) | **PUT** /api/v1/storage-systems/device-type4/{systemId}/ports/{id}/edit-nvme | Edit nvme ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
[**device_type4_nvme_port_ping**](PortsApi.md#device_type4_nvme_port_ping) | **POST** /api/v1/storage-systems/device-type4/{systemId}/ports/{id}/ping-nvme | Ping nvme ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
[**device_type4_port_enable**](PortsApi.md#device_type4_port_enable) | **POST** /api/v1/storage-systems/device-type4/{systemId}/ports/{id} | Port enable disable identified by {id} from HPE Alletra Storage MP identified by {systemId}
[**device_type4_ports_clear**](PortsApi.md#device_type4_ports_clear) | **POST** /api/v1/storage-systems/device-type4/{systemId}/ports/{id}/clear | Clear the details of the ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
[**device_type4_ports_get_by_id**](PortsApi.md#device_type4_ports_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/ports/{id} | Get details of HPE Alletra Storage MP Port identified by {id}
[**device_type4_ports_list**](PortsApi.md#device_type4_ports_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/ports | Get details of HPE Alletra Storage MP Ports
[**device_type4_ports_performance_history_get**](PortsApi.md#device_type4_ports_performance_history_get) | **GET** /api/v1/storage-systems/device-type4/{systemId}/ports-performance | Get details of performance metrics of host ports on storage system identified by {systemid}
[**device_type4_rcip_port_edit**](PortsApi.md#device_type4_rcip_port_edit) | **PUT** /api/v1/storage-systems/device-type4/{systemId}/ports/{id}/edit-rcip | Edit rcip ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
[**device_type4_rcip_port_ping**](PortsApi.md#device_type4_rcip_port_ping) | **POST** /api/v1/storage-systems/device-type4/{systemId}/ports/{id}/ping-rcip | Ping rcip ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
[**device_type4initialise_ports**](PortsApi.md#device_type4initialise_ports) | **POST** /api/v1/storage-systems/device-type4/{systemId}/ports/{id}/initialize | Initialize the details of the ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
[**get_device_type2_network_interface_by_id**](PortsApi.md#get_device_type2_network_interface_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/network-interfaces/{networkInterfaceId} | Get all network interfaces details by Nimble / Alletra 6K identified  by {networkInterfaceId}
[**get_device_type2_network_interfaces**](PortsApi.md#get_device_type2_network_interfaces) | **GET** /api/v1/storage-systems/device-type2/{systemId}/network-interfaces | Get all network interfaces details by Nimble / Alletra 6K
[**initialise_ports**](PortsApi.md#initialise_ports) | **POST** /api/v1/storage-systems/device-type1/{systemId}/ports/{id}/initialize | Initialize the details of the ports identified by {id} from Primera / Alletra 9K identified by {systemId}
[**port_enable**](PortsApi.md#port_enable) | **POST** /api/v1/storage-systems/device-type1/{systemId}/ports/{id} | Port enable disable identified by {id} from Primera / Alletra 9K identified by {systemId}


# **device_type1_fc_port_edit**
> TaskResponse device_type1_fc_port_edit(system_id, id, port_fc_edit)

Edit ports identified by {id} from Primera / Alletra 9K identified by {systemId}

Edit ports identified by {id} from Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.port_fc_edit import PortFCEdit
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'd0fcfe2ff572f44e5beb0a9712c76d5d' # str | UID of the port
    port_fc_edit = dscc.PortFCEdit() # PortFCEdit | 

    try:
        # Edit ports identified by {id} from Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_fc_port_edit(system_id, id, port_fc_edit)
        print("The response of PortsApi->device_type1_fc_port_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type1_fc_port_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the port | 
 **port_fc_edit** | [**PortFCEdit**](PortFCEdit.md)|  | 

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

# **device_type1_iscsi_port_edit**
> TaskResponse device_type1_iscsi_port_edit(system_id, id, port_iscsi_edit)

Edit iscsi ports identified by {id} from Primera / Alletra 9K identified by {systemId}

Edit iscsi ports identified by {id} from Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.port_iscsi_edit import PortISCSIEdit
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'd0fcfe2ff572f44e5beb0a9712c76d5d' # str | UID of the port
    port_iscsi_edit = dscc.PortISCSIEdit() # PortISCSIEdit | 

    try:
        # Edit iscsi ports identified by {id} from Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_iscsi_port_edit(system_id, id, port_iscsi_edit)
        print("The response of PortsApi->device_type1_iscsi_port_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type1_iscsi_port_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the port | 
 **port_iscsi_edit** | [**PortISCSIEdit**](PortISCSIEdit.md)|  | 

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

# **device_type1_iscsi_port_ping**
> TaskResponse device_type1_iscsi_port_ping(system_id, id, port_iscsi_ping)

Ping iscsi ports identified by {id} from Primera / Alletra 9K identified by {systemId}

Ping iscsi ports identified by {id} from Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.port_iscsi_ping import PortISCSIPing
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'd0fcfe2ff572f44e5beb0a9712c76d5d' # str | UID of the port
    port_iscsi_ping = dscc.PortISCSIPing() # PortISCSIPing | 

    try:
        # Ping iscsi ports identified by {id} from Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_iscsi_port_ping(system_id, id, port_iscsi_ping)
        print("The response of PortsApi->device_type1_iscsi_port_ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type1_iscsi_port_ping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the port | 
 **port_iscsi_ping** | [**PortISCSIPing**](PortISCSIPing.md)|  | 

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

# **device_type1_ports_clear**
> TaskResponse device_type1_ports_clear(system_id, id, port_clear_input=port_clear_input)

Clear the details of the ports identified by {id} from Primera / Alletra 9K identified by {systemId}

Clear the details of the ports identified by {id} from Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.port_clear_input import PortClearInput
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'd0fcfe2ff572f44e5beb0a9712c76d5d' # str | UID of the port
    port_clear_input = dscc.PortClearInput() # PortClearInput |  (optional)

    try:
        # Clear the details of the ports identified by {id} from Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_ports_clear(system_id, id, port_clear_input=port_clear_input)
        print("The response of PortsApi->device_type1_ports_clear:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type1_ports_clear: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the port | 
 **port_clear_input** | [**PortClearInput**](PortClearInput.md)|  | [optional] 

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

# **device_type1_ports_get_by_id**
> PortDetails device_type1_ports_get_by_id(system_id, id, select=select)

Get details of Primera / Alletra 9K Port identified by {id}

Get details of Primera / Alletra 9K Port identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.port_details import PortDetails
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'd0fcfe2ff572f44e5beb0a9712c76d5d' # str | UID of the port
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K Port identified by {id}
        api_response = api_instance.device_type1_ports_get_by_id(system_id, id, select=select)
        print("The response of PortsApi->device_type1_ports_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type1_ports_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the port | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PortDetails**](PortDetails.md)

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

# **device_type1_ports_list**
> PortsSummaryList device_type1_ports_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of Primera / Alletra 9K Ports

Get details of Primera / Alletra 9K Ports

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.ports_summary_list import PortsSummaryList
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq 1:0:1 and systemWWN eq 2FF70002AC018D94' # str | oData query to filter ports by Key. (optional)
    sort = 'name desc' # str | oData query to sort ports by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K Ports
        api_response = api_instance.device_type1_ports_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of PortsApi->device_type1_ports_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type1_ports_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter ports by Key. | [optional] 
 **sort** | **str**| oData query to sort ports by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PortsSummaryList**](PortsSummaryList.md)

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

# **device_type1_ports_performance_history_get**
> PerformanceHistoryData device_type1_ports_performance_history_get(system_id, report_type=report_type, range=range, time_interval_min=time_interval_min, compare_by=compare_by, group_by=group_by, metric_type=metric_type, filter=filter)

Get details of performance metrics of Primera/ Alletra 9K host ports on storage system identified by {systemid}

Get details of performance metrics of Primera/ Alletra 9K host ports on storage system identified by {systemid}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.performance_history_data import PerformanceHistoryData
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    report_type = 'Canned,Custom,Def,ApiUser' # str | parameter will be set to report type requested. For api users, set parameter as ApiUser (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)
    compare_by = 'top eq 5 and metrics eq READ_IOPS' # str | compareBy will define top and compare metrics for which query has to be made (optional)
    group_by = 'VV_NAME,HOST_NAME,LUN,deviceName' # str | groupBy will define comma separated groupby parameters (optional)
    metric_type = 'IOPS,LATENCY,THROUGHPUT,IOSIZE,QLEN,AVG_BUSY,powerConsumption' # str | metricType will define comma separated metrics (optional)
    filter = 'vvname in (vvname1,vvname2,vvname3) ,deviceName in (cage1)' # str | filter will define objects to be filtered (optional)

    try:
        # Get details of performance metrics of Primera/ Alletra 9K host ports on storage system identified by {systemid}
        api_response = api_instance.device_type1_ports_performance_history_get(system_id, report_type=report_type, range=range, time_interval_min=time_interval_min, compare_by=compare_by, group_by=group_by, metric_type=metric_type, filter=filter)
        print("The response of PortsApi->device_type1_ports_performance_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type1_ports_performance_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **report_type** | **str**| parameter will be set to report type requested. For api users, set parameter as ApiUser | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 
 **compare_by** | **str**| compareBy will define top and compare metrics for which query has to be made | [optional] 
 **group_by** | **str**| groupBy will define comma separated groupby parameters | [optional] 
 **metric_type** | **str**| metricType will define comma separated metrics | [optional] 
 **filter** | **str**| filter will define objects to be filtered | [optional] 

### Return type

[**PerformanceHistoryData**](PerformanceHistoryData.md)

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

# **device_type1_rcip_port_edit**
> TaskResponse device_type1_rcip_port_edit(system_id, id, port_rcip_edit)

Edit rcip ports identified by {id} from Primera / Alletra 9K identified by {systemId}

Edit rcip ports identified by {id} from Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.port_rcip_edit import PortRCIPEdit
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'd0fcfe2ff572f44e5beb0a9712c76d5d' # str | UID of the port
    port_rcip_edit = dscc.PortRCIPEdit() # PortRCIPEdit | 

    try:
        # Edit rcip ports identified by {id} from Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_rcip_port_edit(system_id, id, port_rcip_edit)
        print("The response of PortsApi->device_type1_rcip_port_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type1_rcip_port_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the port | 
 **port_rcip_edit** | [**PortRCIPEdit**](PortRCIPEdit.md)|  | 

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

# **device_type1_rcip_port_ping**
> TaskResponse device_type1_rcip_port_ping(system_id, id, port_rcip_ping)

Ping rcip ports identified by {id} from Primera / Alletra 9K identified by {systemId}

Ping rcip ports identified by {id} from Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.port_rcip_ping import PortRCIPPing
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'd0fcfe2ff572f44e5beb0a9712c76d5d' # str | UID of the port
    port_rcip_ping = dscc.PortRCIPPing() # PortRCIPPing | 

    try:
        # Ping rcip ports identified by {id} from Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_rcip_port_ping(system_id, id, port_rcip_ping)
        print("The response of PortsApi->device_type1_rcip_port_ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type1_rcip_port_ping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the port | 
 **port_rcip_ping** | [**PortRCIPPing**](PortRCIPPing.md)|  | 

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

# **device_type2_edit_fc_port**
> TaskResponse device_type2_edit_fc_port(system_id, port_id, nimble_edit_fc_interface_input)

Edit Nimble FC Port of Nimble / Alletra 6K

Edit Nimble FC Port of Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_edit_fc_interface_input import NimbleEditFCInterfaceInput
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    port_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of port. A 42 digit hexadecimal number.
    nimble_edit_fc_interface_input = dscc.NimbleEditFCInterfaceInput() # NimbleEditFCInterfaceInput | 

    try:
        # Edit Nimble FC Port of Nimble / Alletra 6K
        api_response = api_instance.device_type2_edit_fc_port(system_id, port_id, nimble_edit_fc_interface_input)
        print("The response of PortsApi->device_type2_edit_fc_port:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type2_edit_fc_port: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **port_id** | **str**| Identifier of port. A 42 digit hexadecimal number. | 
 **nimble_edit_fc_interface_input** | [**NimbleEditFCInterfaceInput**](NimbleEditFCInterfaceInput.md)|  | 

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

# **device_type2_get_all_fibre_channel_configs**
> NimbleFCConfigsList device_type2_get_all_fibre_channel_configs(system_id, limit=limit, offset=offset, filter=filter, select=select)

Get all fibre channel configs details of Nimble / Alletra 6K

Get all fibre channel configs details of Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_fc_configs_list import NimbleFCConfigsList
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter Fibre Channel Configs by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all fibre channel configs details of Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_fibre_channel_configs(system_id, limit=limit, offset=offset, filter=filter, select=select)
        print("The response of PortsApi->device_type2_get_all_fibre_channel_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type2_get_all_fibre_channel_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter Fibre Channel Configs by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleFCConfigsList**](NimbleFCConfigsList.md)

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

# **device_type2_get_all_fibre_channel_sessions**
> NimbleFCSessionList device_type2_get_all_fibre_channel_sessions(system_id, limit=limit, offset=offset, filter=filter, select=select)

Get all fibre channel sessions details of Nimble / Alletra 6K

Get all fibre channel sessions details of Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_fc_session_list import NimbleFCSessionList
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter Fibre Channel Sessions by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all fibre channel sessions details of Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_fibre_channel_sessions(system_id, limit=limit, offset=offset, filter=filter, select=select)
        print("The response of PortsApi->device_type2_get_all_fibre_channel_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type2_get_all_fibre_channel_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter Fibre Channel Sessions by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleFCSessionList**](NimbleFCSessionList.md)

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

# **device_type2_get_all_ports**
> NimblePortsList device_type2_get_all_ports(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all ports details of Nimble / Alletra 6K

Get all ports details of Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_ports_list import NimblePortsList
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter fibre channel interface ports by Key. (optional)
    sort = 'name desc' # str | oData query to sort fibre channel interface ports resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all ports details of Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_ports(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of PortsApi->device_type2_get_all_ports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type2_get_all_ports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter fibre channel interface ports by Key. | [optional] 
 **sort** | **str**| oData query to sort fibre channel interface ports resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimblePortsList**](NimblePortsList.md)

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

# **device_type2_get_fibre_channel_config_by_id**
> NimblefibreChannelConfigsWithRequestUri device_type2_get_fibre_channel_config_by_id(system_id, fc_config_id, select=select)

Get fibre channel configs details of Nimble / Alletra 6K identified by {fcConfigId}.

Get fibre channel configs details of Nimble / Alletra 6K identified by {fcConfigId}.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimblefibre_channel_configs_with_request_uri import NimblefibreChannelConfigsWithRequestUri
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    fc_config_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | Identifier of fibre channel config. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get fibre channel configs details of Nimble / Alletra 6K identified by {fcConfigId}.
        api_response = api_instance.device_type2_get_fibre_channel_config_by_id(system_id, fc_config_id, select=select)
        print("The response of PortsApi->device_type2_get_fibre_channel_config_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type2_get_fibre_channel_config_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **fc_config_id** | **str**| Identifier of fibre channel config. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimblefibreChannelConfigsWithRequestUri**](NimblefibreChannelConfigsWithRequestUri.md)

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

# **device_type2_get_fibre_channel_session_by_id**
> NimbleFCSessionDetailsWithRequestUri device_type2_get_fibre_channel_session_by_id(system_id, fc_session_id, select=select)

Get fibre channel session details of Nimble / Alletra 6K identified by {fcSessionId}.

Get fibre channel session details of Nimble / Alletra 6K identified by {fcSessionId}.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_fc_session_details_with_request_uri import NimbleFCSessionDetailsWithRequestUri
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    fc_session_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the Fibre Channel Session. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get fibre channel session details of Nimble / Alletra 6K identified by {fcSessionId}.
        api_response = api_instance.device_type2_get_fibre_channel_session_by_id(system_id, fc_session_id, select=select)
        print("The response of PortsApi->device_type2_get_fibre_channel_session_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type2_get_fibre_channel_session_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **fc_session_id** | **str**| ID of the Fibre Channel Session. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleFCSessionDetailsWithRequestUri**](NimbleFCSessionDetailsWithRequestUri.md)

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

# **device_type2_get_port_by_id**
> NimblePortDetails device_type2_get_port_by_id(system_id, port_id, select=select)

Get details of Nimble / Alletra 6K Port identified by {portId}. Fibre_channel_interfaces attributes will be shown for Fibre_channel_interface ports. Network_interfaces attributes will be shown for Network_interface ports.

Get details of Nimble / Alletra 6K Port identified by {portId}.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_port_details import NimblePortDetails
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    port_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of port. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Nimble / Alletra 6K Port identified by {portId}. Fibre_channel_interfaces attributes will be shown for Fibre_channel_interface ports. Network_interfaces attributes will be shown for Network_interface ports.
        api_response = api_instance.device_type2_get_port_by_id(system_id, port_id, select=select)
        print("The response of PortsApi->device_type2_get_port_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type2_get_port_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **port_id** | **str**| Identifier of port. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimblePortDetails**](NimblePortDetails.md)

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

# **device_type4_fc_port_edit**
> TaskResponse device_type4_fc_port_edit(system_id, id, device_type4_port_fc_edit)

Edit ports identified by {id} from HPE Alletra Storage MP identified by {systemId}

Edit ports identified by {id} from HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_port_fc_edit import DeviceType4PortFCEdit
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'd0fcfe2ff572f44e5beb0a9712c76d5d' # str | UID of the port
    device_type4_port_fc_edit = dscc.DeviceType4PortFCEdit() # DeviceType4PortFCEdit | 

    try:
        # Edit ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_fc_port_edit(system_id, id, device_type4_port_fc_edit)
        print("The response of PortsApi->device_type4_fc_port_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type4_fc_port_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the port | 
 **device_type4_port_fc_edit** | [**DeviceType4PortFCEdit**](DeviceType4PortFCEdit.md)|  | 

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

# **device_type4_iscsi_port_edit**
> TaskResponse device_type4_iscsi_port_edit(system_id, id, device_type4_port_iscsi_edit)

Edit iscsi ports identified by {id} from HPE Alletra Storage MP identified by {systemId}

Edit iscsi ports identified by {id} from HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_port_iscsi_edit import DeviceType4PortISCSIEdit
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'd0fcfe2ff572f44e5beb0a9712c76d5d' # str | UID of the port
    device_type4_port_iscsi_edit = dscc.DeviceType4PortISCSIEdit() # DeviceType4PortISCSIEdit | 

    try:
        # Edit iscsi ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_iscsi_port_edit(system_id, id, device_type4_port_iscsi_edit)
        print("The response of PortsApi->device_type4_iscsi_port_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type4_iscsi_port_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the port | 
 **device_type4_port_iscsi_edit** | [**DeviceType4PortISCSIEdit**](DeviceType4PortISCSIEdit.md)|  | 

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

# **device_type4_iscsi_port_ping**
> TaskResponse device_type4_iscsi_port_ping(system_id, id, device_type4_port_iscsi_ping)

Ping iscsi ports identified by {id} from HPE Alletra Storage MP identified by {systemId}

Ping iscsi ports identified by {id} from HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_port_iscsi_ping import DeviceType4PortISCSIPing
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'd0fcfe2ff572f44e5beb0a9712c76d5d' # str | UID of the port
    device_type4_port_iscsi_ping = dscc.DeviceType4PortISCSIPing() # DeviceType4PortISCSIPing | 

    try:
        # Ping iscsi ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_iscsi_port_ping(system_id, id, device_type4_port_iscsi_ping)
        print("The response of PortsApi->device_type4_iscsi_port_ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type4_iscsi_port_ping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the port | 
 **device_type4_port_iscsi_ping** | [**DeviceType4PortISCSIPing**](DeviceType4PortISCSIPing.md)|  | 

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

# **device_type4_nvme_port_edit**
> TaskResponse device_type4_nvme_port_edit(system_id, id, device_type4_port_nvme_edit)

Edit nvme ports identified by {id} from HPE Alletra Storage MP identified by {systemId}

Edit nvme ports identified by {id} from HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_port_nvme_edit import DeviceType4PortNVMeEdit
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'd0fcfe2ff572f44e5beb0a9712c76d5d' # str | UID of the port
    device_type4_port_nvme_edit = dscc.DeviceType4PortNVMeEdit() # DeviceType4PortNVMeEdit | 

    try:
        # Edit nvme ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_nvme_port_edit(system_id, id, device_type4_port_nvme_edit)
        print("The response of PortsApi->device_type4_nvme_port_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type4_nvme_port_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the port | 
 **device_type4_port_nvme_edit** | [**DeviceType4PortNVMeEdit**](DeviceType4PortNVMeEdit.md)|  | 

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

# **device_type4_nvme_port_ping**
> TaskResponse device_type4_nvme_port_ping(system_id, id, device_type4_port_nvme_ping)

Ping nvme ports identified by {id} from HPE Alletra Storage MP identified by {systemId}

Ping nvme ports identified by {id} from HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_port_nvme_ping import DeviceType4PortNVMePing
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'd0fcfe2ff572f44e5beb0a9712c76d5d' # str | UID of the port
    device_type4_port_nvme_ping = dscc.DeviceType4PortNVMePing() # DeviceType4PortNVMePing | 

    try:
        # Ping nvme ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_nvme_port_ping(system_id, id, device_type4_port_nvme_ping)
        print("The response of PortsApi->device_type4_nvme_port_ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type4_nvme_port_ping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the port | 
 **device_type4_port_nvme_ping** | [**DeviceType4PortNVMePing**](DeviceType4PortNVMePing.md)|  | 

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

# **device_type4_port_enable**
> TaskResponse device_type4_port_enable(system_id, id, device_type4_port_enable_input)

Port enable disable identified by {id} from HPE Alletra Storage MP identified by {systemId}

Port enable disable identified by {id} from HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_port_enable_input import DeviceType4PortEnableInput
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'd0fcfe2ff572f44e5beb0a9712c76d5d' # str | UID of the port
    device_type4_port_enable_input = dscc.DeviceType4PortEnableInput() # DeviceType4PortEnableInput | 

    try:
        # Port enable disable identified by {id} from HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_port_enable(system_id, id, device_type4_port_enable_input)
        print("The response of PortsApi->device_type4_port_enable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type4_port_enable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the port | 
 **device_type4_port_enable_input** | [**DeviceType4PortEnableInput**](DeviceType4PortEnableInput.md)|  | 

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

# **device_type4_ports_clear**
> TaskResponse device_type4_ports_clear(system_id, id, device_type4_port_clear_input=device_type4_port_clear_input)

Clear the details of the ports identified by {id} from HPE Alletra Storage MP identified by {systemId}

Clear the details of the ports identified by {id} from HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_port_clear_input import DeviceType4PortClearInput
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'd0fcfe2ff572f44e5beb0a9712c76d5d' # str | UID of the port
    device_type4_port_clear_input = dscc.DeviceType4PortClearInput() # DeviceType4PortClearInput |  (optional)

    try:
        # Clear the details of the ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_ports_clear(system_id, id, device_type4_port_clear_input=device_type4_port_clear_input)
        print("The response of PortsApi->device_type4_ports_clear:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type4_ports_clear: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the port | 
 **device_type4_port_clear_input** | [**DeviceType4PortClearInput**](DeviceType4PortClearInput.md)|  | [optional] 

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

# **device_type4_ports_get_by_id**
> DeviceType4PortDetails device_type4_ports_get_by_id(system_id, id, select=select)

Get details of HPE Alletra Storage MP Port identified by {id}

Get details of HPE Alletra Storage MP Port identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_port_details import DeviceType4PortDetails
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'd0fcfe2ff572f44e5beb0a9712c76d5d' # str | UID of the port
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Port identified by {id}
        api_response = api_instance.device_type4_ports_get_by_id(system_id, id, select=select)
        print("The response of PortsApi->device_type4_ports_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type4_ports_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the port | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4PortDetails**](DeviceType4PortDetails.md)

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

# **device_type4_ports_list**
> DeviceType4PortsSummaryList device_type4_ports_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of HPE Alletra Storage MP Ports

Get details of HPE Alletra Storage MP Ports

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_ports_summary_list import DeviceType4PortsSummaryList
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq 1:0:1 and systemWWN eq 2FF70002AC018D94' # str | oData query to filter ports by Key. (optional)
    sort = 'name desc' # str | oData query to sort ports by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Ports
        api_response = api_instance.device_type4_ports_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of PortsApi->device_type4_ports_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type4_ports_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter ports by Key. | [optional] 
 **sort** | **str**| oData query to sort ports by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4PortsSummaryList**](DeviceType4PortsSummaryList.md)

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

# **device_type4_ports_performance_history_get**
> DeviceType4PerformanceHistoryData device_type4_ports_performance_history_get(system_id, report_type=report_type, range=range, time_interval_min=time_interval_min, compare_by=compare_by, group_by=group_by, metric_type=metric_type, filter=filter)

Get details of performance metrics of host ports on storage system identified by {systemid}

Get details of performance metrics of host ports on storage system identified by {systemid}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_performance_history_data import DeviceType4PerformanceHistoryData
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    report_type = 'Canned,Custom,Def,ApiUser' # str | parameter will be set to report type requested. For api users, set parameter as ApiUser (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)
    compare_by = 'top eq 5 and metrics eq READ_IOPS' # str | compareBy will define top and compare metrics for which query has to be made (optional)
    group_by = 'VV_NAME,HOST_NAME,LUN,deviceName' # str | groupBy will define comma separated groupby parameters (optional)
    metric_type = 'IOPS,LATENCY,THROUGHPUT,IOSIZE,QLEN,AVG_BUSY,powerConsumption' # str | metricType will define comma separated metrics (optional)
    filter = 'vvname in (vvname1,vvname2,vvname3) ,deviceName in (cage1)' # str | filter will define objects to be filtered (optional)

    try:
        # Get details of performance metrics of host ports on storage system identified by {systemid}
        api_response = api_instance.device_type4_ports_performance_history_get(system_id, report_type=report_type, range=range, time_interval_min=time_interval_min, compare_by=compare_by, group_by=group_by, metric_type=metric_type, filter=filter)
        print("The response of PortsApi->device_type4_ports_performance_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type4_ports_performance_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **report_type** | **str**| parameter will be set to report type requested. For api users, set parameter as ApiUser | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 
 **compare_by** | **str**| compareBy will define top and compare metrics for which query has to be made | [optional] 
 **group_by** | **str**| groupBy will define comma separated groupby parameters | [optional] 
 **metric_type** | **str**| metricType will define comma separated metrics | [optional] 
 **filter** | **str**| filter will define objects to be filtered | [optional] 

### Return type

[**DeviceType4PerformanceHistoryData**](DeviceType4PerformanceHistoryData.md)

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

# **device_type4_rcip_port_edit**
> TaskResponse device_type4_rcip_port_edit(system_id, id, device_type4_port_rcip_edit)

Edit rcip ports identified by {id} from HPE Alletra Storage MP identified by {systemId}

Edit rcip ports identified by {id} from HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_port_rcip_edit import DeviceType4PortRCIPEdit
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'd0fcfe2ff572f44e5beb0a9712c76d5d' # str | UID of the port
    device_type4_port_rcip_edit = dscc.DeviceType4PortRCIPEdit() # DeviceType4PortRCIPEdit | 

    try:
        # Edit rcip ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_rcip_port_edit(system_id, id, device_type4_port_rcip_edit)
        print("The response of PortsApi->device_type4_rcip_port_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type4_rcip_port_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the port | 
 **device_type4_port_rcip_edit** | [**DeviceType4PortRCIPEdit**](DeviceType4PortRCIPEdit.md)|  | 

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

# **device_type4_rcip_port_ping**
> TaskResponse device_type4_rcip_port_ping(system_id, id, device_type4_port_rcip_ping)

Ping rcip ports identified by {id} from HPE Alletra Storage MP identified by {systemId}

Ping rcip ports identified by {id} from HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_port_rcip_ping import DeviceType4PortRCIPPing
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'd0fcfe2ff572f44e5beb0a9712c76d5d' # str | UID of the port
    device_type4_port_rcip_ping = dscc.DeviceType4PortRCIPPing() # DeviceType4PortRCIPPing | 

    try:
        # Ping rcip ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_rcip_port_ping(system_id, id, device_type4_port_rcip_ping)
        print("The response of PortsApi->device_type4_rcip_port_ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type4_rcip_port_ping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the port | 
 **device_type4_port_rcip_ping** | [**DeviceType4PortRCIPPing**](DeviceType4PortRCIPPing.md)|  | 

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

# **device_type4initialise_ports**
> TaskResponse device_type4initialise_ports(system_id, id)

Initialize the details of the ports identified by {id} from HPE Alletra Storage MP identified by {systemId}

Initialize the details of the ports identified by {id} from HPE Alletra Storage MP identified by {systemId}

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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'd0fcfe2ff572f44e5beb0a9712c76d5d' # str | UID of the port

    try:
        # Initialize the details of the ports identified by {id} from HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4initialise_ports(system_id, id)
        print("The response of PortsApi->device_type4initialise_ports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->device_type4initialise_ports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the port | 

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

# **get_device_type2_network_interface_by_id**
> NimbleNetworkInterfaceWithRequestUri get_device_type2_network_interface_by_id(system_id, network_interface_id, select=select)

Get all network interfaces details by Nimble / Alletra 6K identified  by {networkInterfaceId}

Get all network interfaces details by Nimble / Alletra 6K identified by {networkInterfaceId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_network_interface_with_request_uri import NimbleNetworkInterfaceWithRequestUri
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    network_interface_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the Network Interface. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all network interfaces details by Nimble / Alletra 6K identified  by {networkInterfaceId}
        api_response = api_instance.get_device_type2_network_interface_by_id(system_id, network_interface_id, select=select)
        print("The response of PortsApi->get_device_type2_network_interface_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->get_device_type2_network_interface_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **network_interface_id** | **str**| ID of the Network Interface. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleNetworkInterfaceWithRequestUri**](NimbleNetworkInterfaceWithRequestUri.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_type2_network_interfaces**
> NimbleNetworkInterfaceList get_device_type2_network_interfaces(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all network interfaces details by Nimble / Alletra 6K

Get all network interfaces details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_network_interface_list import NimbleNetworkInterfaceList
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter Network Interface by Key. (optional)
    sort = 'name desc' # str | oData query to sort Network Interface resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all network interfaces details by Nimble / Alletra 6K
        api_response = api_instance.get_device_type2_network_interfaces(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of PortsApi->get_device_type2_network_interfaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->get_device_type2_network_interfaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter Network Interface by Key. | [optional] 
 **sort** | **str**| oData query to sort Network Interface resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleNetworkInterfaceList**](NimbleNetworkInterfaceList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialise_ports**
> TaskResponse initialise_ports(system_id, id)

Initialize the details of the ports identified by {id} from Primera / Alletra 9K identified by {systemId}

Initialize the details of the ports identified by {id} from Primera / Alletra 9K identified by {systemId}

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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'd0fcfe2ff572f44e5beb0a9712c76d5d' # str | UID of the port

    try:
        # Initialize the details of the ports identified by {id} from Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.initialise_ports(system_id, id)
        print("The response of PortsApi->initialise_ports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->initialise_ports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the port | 

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

# **port_enable**
> TaskResponse port_enable(system_id, id, port_enable_input)

Port enable disable identified by {id} from Primera / Alletra 9K identified by {systemId}

Port enable disable identified by {id} from Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.port_enable_input import PortEnableInput
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
    api_instance = dscc.PortsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'd0fcfe2ff572f44e5beb0a9712c76d5d' # str | UID of the port
    port_enable_input = dscc.PortEnableInput() # PortEnableInput | 

    try:
        # Port enable disable identified by {id} from Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.port_enable(system_id, id, port_enable_input)
        print("The response of PortsApi->port_enable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->port_enable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the port | 
 **port_enable_input** | [**PortEnableInput**](PortEnableInput.md)|  | 

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

