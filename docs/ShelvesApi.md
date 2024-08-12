# dscc.ShelvesApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type1_disks_get_by_id**](ShelvesApi.md#device_type1_disks_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/enclosures/{cageId}/disks/{id} | Get details of Primera / Alletra 9K disk identified by {cageId} and {id}
[**device_type1_disks_list**](ShelvesApi.md#device_type1_disks_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/enclosures/{cageId}/disks | Get details of Primera / Alletra 9K disks identified by {cageId}
[**device_type1_enclosure_card_ports_get_by_id**](ShelvesApi.md#device_type1_enclosure_card_ports_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/enclosures/{enclosureId}/enclosure-card-ports/{id} | Get details of Primera / Alletra 9K Enclosure Card Port identified by {enclosureId} and {id}
[**device_type1_enclosure_card_ports_list**](ShelvesApi.md#device_type1_enclosure_card_ports_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/enclosures/{enclosureId}/enclosure-card-ports | Get details of Primera / Alletra 9K Enclosure Card Ports identified by {enclosureId}
[**device_type1_enclosure_cards_get_by_id**](ShelvesApi.md#device_type1_enclosure_cards_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/enclosures/{enclosureId}/enclosure-cards/{id} | Get details of Primera / Alletra 9K Enclosure Card identified by {enclosureId} and {id}
[**device_type1_enclosure_cards_list**](ShelvesApi.md#device_type1_enclosure_cards_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/enclosures/{enclosureId}/enclosure-cards | Get details of Primera / Alletra 9K Enclosure Cards identified by {enclosureId}
[**device_type1_enclosure_disks_get_by_id**](ShelvesApi.md#device_type1_enclosure_disks_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/enclosures/{enclosureId}/enclosure-disks/{id} | Get details of Primera / Alletra 9K Enclosure Disk identified by {enclosureId} and {id}
[**device_type1_enclosure_disks_list**](ShelvesApi.md#device_type1_enclosure_disks_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/enclosures/{enclosureId}/enclosure-disks | Get details of Primera / Alletra 9K Enclosure Disks identified by {enclosureId}
[**device_type1_enclosure_expanders_get_by_id**](ShelvesApi.md#device_type1_enclosure_expanders_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/enclosures/{enclosureId}/enclosure-expanders/{id} | Get details of Primera / Alletra 9K Enclosure Expander identified by {enclosureId} and {id}
[**device_type1_enclosure_expanders_list**](ShelvesApi.md#device_type1_enclosure_expanders_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/enclosures/{enclosureId}/enclosure-expanders | Get details of Primera / Alletra 9K Enclosure Expanders identified by {enclosureId}
[**device_type1_enclosure_fans_get_by_id**](ShelvesApi.md#device_type1_enclosure_fans_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/enclosures/{enclosureId}/enclosure-fans/{id} | Get details of Primera / Alletra 9K Enclosure Fan identified by {enclosureId} and {id}
[**device_type1_enclosure_fans_list**](ShelvesApi.md#device_type1_enclosure_fans_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/enclosures/{enclosureId}/enclosure-fans | Get details of Primera / Alletra 9K Enclosure Fans identified by {enclosureId}
[**device_type1_enclosure_powers_get_by_id**](ShelvesApi.md#device_type1_enclosure_powers_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/enclosures/{enclosureId}/enclosure-powers/{id} | Get details of Primera / Alletra 9K Enclosure Power identified by {enclosureId} and {id}
[**device_type1_enclosure_powers_list**](ShelvesApi.md#device_type1_enclosure_powers_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/enclosures/{enclosureId}/enclosure-powers | Get details of Primera / Alletra 9K Enclosure Powers identified by {enclosureId}
[**device_type1_enclosure_sleds_get_by_id**](ShelvesApi.md#device_type1_enclosure_sleds_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/enclosures/{enclosureId}/enclosure-sleds/{id} | Get details of Primera / Alletra 9K Enclosure Sled identified by {enclosureId} and {id}
[**device_type1_enclosure_sleds_list**](ShelvesApi.md#device_type1_enclosure_sleds_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/enclosures/{enclosureId}/enclosure-sleds | Get details of Primera / Alletra 9K Enclosure Sleds identified by {enclosureId}
[**device_type1_enclosures_get_by_id**](ShelvesApi.md#device_type1_enclosures_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/enclosures/{id} | Get details of Primera / Alletra 9K Enclosure identified by {id}
[**device_type1_enclosures_list**](ShelvesApi.md#device_type1_enclosures_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/enclosures | Get details of Primera / Alletra 9K Enclosures
[**device_type1_physical_drive_performance_history_get**](ShelvesApi.md#device_type1_physical_drive_performance_history_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/physicaldrives-performance | Get details of performance metrics of Primera/ Alletra 9K physicalDrives on storage system identified by {systemid}
[**device_type2_activate_shelf**](ShelvesApi.md#device_type2_activate_shelf) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/shelves/actions/activate | Activate shelves of a Nimble / Alletra 6K storage system identified by {systemId}
[**device_type2_get_all_shelves**](ShelvesApi.md#device_type2_get_all_shelves) | **GET** /api/v1/storage-systems/device-type2/{systemId}/shelves | Get all shelves details by Nimble / Alletra 6K
[**device_type2_get_shelf_by_id**](ShelvesApi.md#device_type2_get_shelf_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/shelves/{shelfId} | Get details of Nimble / Alletra 6K Shelf identified by {shelfId}
[**device_type2_locate_shelf_chassis**](ShelvesApi.md#device_type2_locate_shelf_chassis) | **POST** /api/v1/storage-systems/device-type2/{systemId}/shelves/{shelfId}/actions/locate | Locate chassis of Nimble / Alletra 6K shelf identified by {shelfId}
[**device_type4_disks_get_by_id**](ShelvesApi.md#device_type4_disks_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/enclosures/{cageId}/disks/{id} | Get details of HPE Alletra Storage MP disk identified by {cageId} and {id}
[**device_type4_disks_list**](ShelvesApi.md#device_type4_disks_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/enclosures/{cageId}/disks | Get details of HPE Alletra Storage MP disks identified by {cageId}
[**device_type4_enclosure_card_list**](ShelvesApi.md#device_type4_enclosure_card_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/enclosure-cards | Get details of HPE Alletra Storage MP Enclosure Cards identified by {systemId}
[**device_type4_enclosure_cards_get_by_id**](ShelvesApi.md#device_type4_enclosure_cards_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/enclosures/{enclosureId}/enclosure-cards/{id} | Get details of HPE Alletra Storage MP Enclosure Card identified by {enclosureId} and {id}
[**device_type4_enclosure_cards_list**](ShelvesApi.md#device_type4_enclosure_cards_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/enclosures/{enclosureId}/enclosure-cards | Get details of HPE Alletra Storage MP Enclosure Cards identified by {enclosureId}
[**device_type4_enclosure_cards_locate_ioby_id**](ShelvesApi.md#device_type4_enclosure_cards_locate_ioby_id) | **POST** /api/v1/storage-systems/device-type4/{systemId}/enclosures/{enclosureId}/enclosure-cards/{id} | Locate IO Module of HPE Alletra Storage MP identified by {id}
[**device_type4_enclosure_connector_list**](ShelvesApi.md#device_type4_enclosure_connector_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/enclosures/{enclosureId}/enclosure-connectors | Get details of HPE Alletra Storage MP Enclosure Connectors identified by {enclosureId}
[**device_type4_enclosure_connectors_get_by_id**](ShelvesApi.md#device_type4_enclosure_connectors_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/enclosures/{enclosureId}/enclosure-connectors/{enclosureConnectorId} | Get details of HPE Alletra Storage MP Enclosure Connector identified by {enclosureId} and {enclosureConnectorId}
[**device_type4_enclosure_connectors_list**](ShelvesApi.md#device_type4_enclosure_connectors_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/enclosure-connectors | Get details of HPE Alletra Storage MP Enclosure Connectors
[**device_type4_enclosure_disks_get_by_id**](ShelvesApi.md#device_type4_enclosure_disks_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/enclosures/{enclosureId}/enclosure-disks/{id} | Get details of HPE Alletra Storage MP Enclosure Disk identified by {enclosureId} and {id}
[**device_type4_enclosure_disks_list**](ShelvesApi.md#device_type4_enclosure_disks_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/enclosures/{enclosureId}/enclosure-disks | Get details of HPE Alletra Storage MP Enclosure Disks identified by {enclosureId}
[**device_type4_enclosure_powers_get_by_id**](ShelvesApi.md#device_type4_enclosure_powers_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/enclosures/{enclosureId}/enclosure-powers/{id} | Get details of HPE Alletra Storage MP Enclosure Power identified by {enclosureId} and {id}
[**device_type4_enclosure_powers_list**](ShelvesApi.md#device_type4_enclosure_powers_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/enclosures/{enclosureId}/enclosure-powers | Get details of HPE Alletra Storage MP Enclosure Powers identified by {enclosureId}
[**device_type4_enclosure_sleds_get_by_id**](ShelvesApi.md#device_type4_enclosure_sleds_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/enclosures/{enclosureId}/enclosure-sleds/{id} | Get details of HPE Alletra Storage MP Enclosure Sled identified by {enclosureId} and {id}
[**device_type4_enclosure_sleds_list**](ShelvesApi.md#device_type4_enclosure_sleds_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/enclosures/{enclosureId}/enclosure-sleds | Get details of HPE Alletra Storage MP Enclosure Sleds identified by {enclosureId}
[**device_type4_enclosure_sleds_locate_drive_by_id**](ShelvesApi.md#device_type4_enclosure_sleds_locate_drive_by_id) | **POST** /api/v1/storage-systems/device-type4/{systemId}/enclosures/{enclosureId}/enclosure-sleds/{id} | Locate drive of HPE Alletra Storage MP identified by {id}
[**device_type4_enclosures_edit_by_id**](ShelvesApi.md#device_type4_enclosures_edit_by_id) | **PUT** /api/v1/storage-systems/device-type4/{systemId}/enclosures/{id} | Edit details of HPE Alletra Storage MP Enclosure identified by {id}
[**device_type4_enclosures_get_by_id**](ShelvesApi.md#device_type4_enclosures_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/enclosures/{id} | Get details of HPE Alletra Storage MP Enclosure identified by {id}
[**device_type4_enclosures_list**](ShelvesApi.md#device_type4_enclosures_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/enclosures | Get details of HPE Alletra Storage MP Enclosures
[**device_type4_enclosures_locate_by_id**](ShelvesApi.md#device_type4_enclosures_locate_by_id) | **POST** /api/v1/storage-systems/device-type4/{systemId}/enclosures/{id} | Locate enclosure drive of HPE Alletra Storage MP identified by {id}
[**device_type4_physical_drive_performance_history_get**](ShelvesApi.md#device_type4_physical_drive_performance_history_get) | **GET** /api/v1/storage-systems/device-type4/{systemId}/physicaldrives-performance | Get details of performance metrics of physical drives on storage system identified by {systemid}
[**enclosure_cards_locate_ioby_id**](ShelvesApi.md#enclosure_cards_locate_ioby_id) | **POST** /api/v1/storage-systems/device-type1/{systemId}/enclosures/{enclosureId}/enclosure-cards/{id} | Locate IO Module of Primera / Alletra 9K identified by {id}
[**enclosure_powers_locate_pcmby_id**](ShelvesApi.md#enclosure_powers_locate_pcmby_id) | **POST** /api/v1/storage-systems/device-type1/{systemId}/enclosures/{enclosureId}/enclosure-powers/{id} | Locate PCM of Primera / Alletra 9K identified by {id}
[**enclosure_sleds_locate_drive_by_id**](ShelvesApi.md#enclosure_sleds_locate_drive_by_id) | **POST** /api/v1/storage-systems/device-type1/{systemId}/enclosures/{enclosureId}/enclosure-sleds/{id} | Locate drive of Primera / Alletra 9K identified by {id}
[**enclosures_edit_by_id**](ShelvesApi.md#enclosures_edit_by_id) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/enclosures/{id} | Edit details of Primera / Alletra 9K Enclosure identified by {id}
[**enclosures_locate_by_id**](ShelvesApi.md#enclosures_locate_by_id) | **POST** /api/v1/storage-systems/device-type1/{systemId}/enclosures/{id} | Locate enclosure drive of Primera / Alletra 9K identified by {id}


# **device_type1_disks_get_by_id**
> DiskDetails device_type1_disks_get_by_id(system_id, cage_id, id, select=select)

Get details of Primera / Alletra 9K disk identified by {cageId} and {id}

Get details of Primera / Alletra 9K disk identified by {cageId} and {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.disk_details import DiskDetails
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    cage_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | cage ID
    id = 'd4b13e70924d29afdb77d932f7563ea6' # str | UID of the disk
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K disk identified by {cageId} and {id}
        api_response = api_instance.device_type1_disks_get_by_id(system_id, cage_id, id, select=select)
        print("The response of ShelvesApi->device_type1_disks_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type1_disks_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **cage_id** | **str**| cage ID | 
 **id** | **str**| UID of the disk | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DiskDetails**](DiskDetails.md)

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

# **device_type1_disks_list**
> DisksSummaryList device_type1_disks_list(system_id, cage_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of Primera / Alletra 9K disks identified by {cageId}

Get details of Primera / Alletra 9K disks identified by {cageId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.disks_summary_list import DisksSummaryList
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    cage_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | cage ID
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemId eq 7CE751P312' # str | oData query to filter Disk by Key. (optional)
    sort = 'name asc' # str | oData query to sort Disk by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K disks identified by {cageId}
        api_response = api_instance.device_type1_disks_list(system_id, cage_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of ShelvesApi->device_type1_disks_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type1_disks_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **cage_id** | **str**| cage ID | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter Disk by Key. | [optional] 
 **sort** | **str**| oData query to sort Disk by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DisksSummaryList**](DisksSummaryList.md)

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

# **device_type1_enclosure_card_ports_get_by_id**
> EnclosureCardPortDetails device_type1_enclosure_card_ports_get_by_id(system_id, enclosure_id, id, select=select)

Get details of Primera / Alletra 9K Enclosure Card Port identified by {enclosureId} and {id}

Get details of Primera / Alletra 9K Enclosure Card Port identified by {enclosureId} and {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.enclosure_card_port_details import EnclosureCardPortDetails
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure card port
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K Enclosure Card Port identified by {enclosureId} and {id}
        api_response = api_instance.device_type1_enclosure_card_ports_get_by_id(system_id, enclosure_id, id, select=select)
        print("The response of ShelvesApi->device_type1_enclosure_card_ports_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type1_enclosure_card_ports_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **id** | **str**| UID of the enclosure card port | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**EnclosureCardPortDetails**](EnclosureCardPortDetails.md)

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

# **device_type1_enclosure_card_ports_list**
> EnclosureCardPortsSummaryList device_type1_enclosure_card_ports_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of Primera / Alletra 9K Enclosure Card Ports identified by {enclosureId}

Get details of Primera / Alletra 9K Enclosure Card Ports identified by {enclosureId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.enclosure_card_ports_summary_list import EnclosureCardPortsSummaryList
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemWWN eq 2FF70002AC018D94' # str | oData query to filter enclosure resource by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort enclosure resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K Enclosure Card Ports identified by {enclosureId}
        api_response = api_instance.device_type1_enclosure_card_ports_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of ShelvesApi->device_type1_enclosure_card_ports_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type1_enclosure_card_ports_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter enclosure resource by Key. | [optional] 
 **sort** | **str**| oData query to sort enclosure resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**EnclosureCardPortsSummaryList**](EnclosureCardPortsSummaryList.md)

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

# **device_type1_enclosure_cards_get_by_id**
> EnclosureCardDetails device_type1_enclosure_cards_get_by_id(system_id, enclosure_id, id, select=select)

Get details of Primera / Alletra 9K Enclosure Card identified by {enclosureId} and {id}

Get details of Primera / Alletra 9K Enclosure Card identified by {enclosureId} and {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.enclosure_card_details import EnclosureCardDetails
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure card
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K Enclosure Card identified by {enclosureId} and {id}
        api_response = api_instance.device_type1_enclosure_cards_get_by_id(system_id, enclosure_id, id, select=select)
        print("The response of ShelvesApi->device_type1_enclosure_cards_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type1_enclosure_cards_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **id** | **str**| UID of the enclosure card | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**EnclosureCardDetails**](EnclosureCardDetails.md)

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

# **device_type1_enclosure_cards_list**
> EnclosureCardsSummaryList device_type1_enclosure_cards_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of Primera / Alletra 9K Enclosure Cards identified by {enclosureId}

Get details of Primera / Alletra 9K Enclosure Cards identified by {enclosureId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.enclosure_cards_summary_list import EnclosureCardsSummaryList
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemWWN eq 2FF70002AC018D94' # str | oData query to filter enclosure resource by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort enclosure resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K Enclosure Cards identified by {enclosureId}
        api_response = api_instance.device_type1_enclosure_cards_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of ShelvesApi->device_type1_enclosure_cards_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type1_enclosure_cards_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter enclosure resource by Key. | [optional] 
 **sort** | **str**| oData query to sort enclosure resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**EnclosureCardsSummaryList**](EnclosureCardsSummaryList.md)

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

# **device_type1_enclosure_disks_get_by_id**
> EnclosureDiskDetails device_type1_enclosure_disks_get_by_id(system_id, enclosure_id, id, select=select)

Get details of Primera / Alletra 9K Enclosure Disk identified by {enclosureId} and {id}

Get details of Primera / Alletra 9K Enclosure Disk identified by {enclosureId} and {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.enclosure_disk_details import EnclosureDiskDetails
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure disk
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K Enclosure Disk identified by {enclosureId} and {id}
        api_response = api_instance.device_type1_enclosure_disks_get_by_id(system_id, enclosure_id, id, select=select)
        print("The response of ShelvesApi->device_type1_enclosure_disks_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type1_enclosure_disks_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **id** | **str**| UID of the enclosure disk | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**EnclosureDiskDetails**](EnclosureDiskDetails.md)

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

# **device_type1_enclosure_disks_list**
> EnclosureDisksSummaryList device_type1_enclosure_disks_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of Primera / Alletra 9K Enclosure Disks identified by {enclosureId}

Get details of Primera / Alletra 9K Enclosure Disks identified by {enclosureId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.enclosure_disks_summary_list import EnclosureDisksSummaryList
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemWWN eq 2FF70002AC018D94' # str | oData query to filter enclosure resource by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort enclosure resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K Enclosure Disks identified by {enclosureId}
        api_response = api_instance.device_type1_enclosure_disks_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of ShelvesApi->device_type1_enclosure_disks_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type1_enclosure_disks_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter enclosure resource by Key. | [optional] 
 **sort** | **str**| oData query to sort enclosure resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**EnclosureDisksSummaryList**](EnclosureDisksSummaryList.md)

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

# **device_type1_enclosure_expanders_get_by_id**
> EnclosureExpanderDetails device_type1_enclosure_expanders_get_by_id(system_id, enclosure_id, id, select=select)

Get details of Primera / Alletra 9K Enclosure Expander identified by {enclosureId} and {id}

Get details of Primera / Alletra 9K Enclosure Expander identified by {enclosureId} and {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.enclosure_expander_details import EnclosureExpanderDetails
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure expander
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K Enclosure Expander identified by {enclosureId} and {id}
        api_response = api_instance.device_type1_enclosure_expanders_get_by_id(system_id, enclosure_id, id, select=select)
        print("The response of ShelvesApi->device_type1_enclosure_expanders_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type1_enclosure_expanders_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **id** | **str**| UID of the enclosure expander | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**EnclosureExpanderDetails**](EnclosureExpanderDetails.md)

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

# **device_type1_enclosure_expanders_list**
> EnclosureExpandersSummaryList device_type1_enclosure_expanders_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of Primera / Alletra 9K Enclosure Expanders identified by {enclosureId}

Get details of Primera / Alletra 9K Enclosure Expanders identified by {enclosureId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.enclosure_expanders_summary_list import EnclosureExpandersSummaryList
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemWWN eq 2FF70002AC018D94' # str | oData query to filter enclosure resource by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort enclosure resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K Enclosure Expanders identified by {enclosureId}
        api_response = api_instance.device_type1_enclosure_expanders_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of ShelvesApi->device_type1_enclosure_expanders_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type1_enclosure_expanders_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter enclosure resource by Key. | [optional] 
 **sort** | **str**| oData query to sort enclosure resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**EnclosureExpandersSummaryList**](EnclosureExpandersSummaryList.md)

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

# **device_type1_enclosure_fans_get_by_id**
> EnclosureFanDetails device_type1_enclosure_fans_get_by_id(system_id, enclosure_id, id, select=select)

Get details of Primera / Alletra 9K Enclosure Fan identified by {enclosureId} and {id}

Get details of Primera / Alletra 9K Enclosure Fan identified by {enclosureId} and {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.enclosure_fan_details import EnclosureFanDetails
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure fan
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K Enclosure Fan identified by {enclosureId} and {id}
        api_response = api_instance.device_type1_enclosure_fans_get_by_id(system_id, enclosure_id, id, select=select)
        print("The response of ShelvesApi->device_type1_enclosure_fans_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type1_enclosure_fans_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **id** | **str**| UID of the enclosure fan | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**EnclosureFanDetails**](EnclosureFanDetails.md)

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

# **device_type1_enclosure_fans_list**
> EnclosureFanSummaryList device_type1_enclosure_fans_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of Primera / Alletra 9K Enclosure Fans identified by {enclosureId}

Get details of Primera / Alletra 9K Enclosure Fans identified by {enclosureId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.enclosure_fan_summary_list import EnclosureFanSummaryList
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemWWN eq 2FF70002AC018D94' # str | oData query to filter enclosure resource by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort enclosure resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K Enclosure Fans identified by {enclosureId}
        api_response = api_instance.device_type1_enclosure_fans_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of ShelvesApi->device_type1_enclosure_fans_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type1_enclosure_fans_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter enclosure resource by Key. | [optional] 
 **sort** | **str**| oData query to sort enclosure resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**EnclosureFanSummaryList**](EnclosureFanSummaryList.md)

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

# **device_type1_enclosure_powers_get_by_id**
> EnclosurePowerDetails device_type1_enclosure_powers_get_by_id(system_id, enclosure_id, id, select=select)

Get details of Primera / Alletra 9K Enclosure Power identified by {enclosureId} and {id}

Get details of Primera / Alletra 9K Enclosure Power identified by {enclosureId} and {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.enclosure_power_details import EnclosurePowerDetails
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure power
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K Enclosure Power identified by {enclosureId} and {id}
        api_response = api_instance.device_type1_enclosure_powers_get_by_id(system_id, enclosure_id, id, select=select)
        print("The response of ShelvesApi->device_type1_enclosure_powers_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type1_enclosure_powers_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **id** | **str**| UID of the enclosure power | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**EnclosurePowerDetails**](EnclosurePowerDetails.md)

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

# **device_type1_enclosure_powers_list**
> EnclosurePowersSummaryList device_type1_enclosure_powers_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of Primera / Alletra 9K Enclosure Powers identified by {enclosureId}

Get details of Primera / Alletra 9K Enclosure Powers identified by {enclosureId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.enclosure_powers_summary_list import EnclosurePowersSummaryList
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemWWN eq 2FF70002AC018D94' # str | oData query to filter enclosure resource by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort enclosure resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K Enclosure Powers identified by {enclosureId}
        api_response = api_instance.device_type1_enclosure_powers_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of ShelvesApi->device_type1_enclosure_powers_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type1_enclosure_powers_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter enclosure resource by Key. | [optional] 
 **sort** | **str**| oData query to sort enclosure resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**EnclosurePowersSummaryList**](EnclosurePowersSummaryList.md)

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

# **device_type1_enclosure_sleds_get_by_id**
> EnclosureSledDetails device_type1_enclosure_sleds_get_by_id(system_id, enclosure_id, id, select=select)

Get details of Primera / Alletra 9K Enclosure Sled identified by {enclosureId} and {id}

Get details of Primera / Alletra 9K Enclosure Sled identified by {enclosureId} and {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.enclosure_sled_details import EnclosureSledDetails
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure sled
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K Enclosure Sled identified by {enclosureId} and {id}
        api_response = api_instance.device_type1_enclosure_sleds_get_by_id(system_id, enclosure_id, id, select=select)
        print("The response of ShelvesApi->device_type1_enclosure_sleds_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type1_enclosure_sleds_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **id** | **str**| UID of the enclosure sled | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**EnclosureSledDetails**](EnclosureSledDetails.md)

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

# **device_type1_enclosure_sleds_list**
> EnclosureSledsSummaryList device_type1_enclosure_sleds_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of Primera / Alletra 9K Enclosure Sleds identified by {enclosureId}

Get details of Primera / Alletra 9K Enclosure Sleds identified by {enclosureId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.enclosure_sleds_summary_list import EnclosureSledsSummaryList
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemWWN eq 2FF70002AC018D94' # str | oData query to filter enclosure resource by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort enclosure resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K Enclosure Sleds identified by {enclosureId}
        api_response = api_instance.device_type1_enclosure_sleds_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of ShelvesApi->device_type1_enclosure_sleds_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type1_enclosure_sleds_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter enclosure resource by Key. | [optional] 
 **sort** | **str**| oData query to sort enclosure resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**EnclosureSledsSummaryList**](EnclosureSledsSummaryList.md)

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

# **device_type1_enclosures_get_by_id**
> EnclosuresDetails device_type1_enclosures_get_by_id(system_id, id, select=select)

Get details of Primera / Alletra 9K Enclosure identified by {id}

Get details of Primera / Alletra 9K Enclosure identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.enclosures_details import EnclosuresDetails
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K Enclosure identified by {id}
        api_response = api_instance.device_type1_enclosures_get_by_id(system_id, id, select=select)
        print("The response of ShelvesApi->device_type1_enclosures_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type1_enclosures_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the enclosure | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**EnclosuresDetails**](EnclosuresDetails.md)

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

# **device_type1_enclosures_list**
> EnclosuresSummaryList device_type1_enclosures_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of Primera / Alletra 9K Enclosures

Get details of Primera / Alletra 9K Enclosures

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.enclosures_summary_list import EnclosuresSummaryList
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemWWN eq 2FF70002AC018D94' # str | oData query to filter enclosure resource by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort enclosure resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K Enclosures
        api_response = api_instance.device_type1_enclosures_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of ShelvesApi->device_type1_enclosures_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type1_enclosures_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter enclosure resource by Key. | [optional] 
 **sort** | **str**| oData query to sort enclosure resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**EnclosuresSummaryList**](EnclosuresSummaryList.md)

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

# **device_type1_physical_drive_performance_history_get**
> PerformanceHistoryData device_type1_physical_drive_performance_history_get(system_id, report_type=report_type, range=range, time_interval_min=time_interval_min, compare_by=compare_by, group_by=group_by, metric_type=metric_type, filter=filter)

Get details of performance metrics of Primera/ Alletra 9K physicalDrives on storage system identified by {systemid}

Get details of performance metrics of Primera/ Alletra 9K physicalDrives on storage system identified by {systemid}

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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    report_type = 'Canned,Custom,Def,ApiUser' # str | parameter will be set to report type requested. For api users, set parameter as ApiUser (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)
    compare_by = 'top eq 5 and metrics eq READ_IOPS' # str | compareBy will define top and compare metrics for which query has to be made (optional)
    group_by = 'VV_NAME,HOST_NAME,LUN,deviceName' # str | groupBy will define comma separated groupby parameters (optional)
    metric_type = 'IOPS,LATENCY,THROUGHPUT,IOSIZE,QLEN,AVG_BUSY,powerConsumption' # str | metricType will define comma separated metrics (optional)
    filter = 'vvname in (vvname1,vvname2,vvname3) ,deviceName in (cage1)' # str | filter will define objects to be filtered (optional)

    try:
        # Get details of performance metrics of Primera/ Alletra 9K physicalDrives on storage system identified by {systemid}
        api_response = api_instance.device_type1_physical_drive_performance_history_get(system_id, report_type=report_type, range=range, time_interval_min=time_interval_min, compare_by=compare_by, group_by=group_by, metric_type=metric_type, filter=filter)
        print("The response of ShelvesApi->device_type1_physical_drive_performance_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type1_physical_drive_performance_history_get: %s\n" % e)
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

# **device_type2_activate_shelf**
> TaskResponse device_type2_activate_shelf(system_id, nimble_shelves_activate_input)

Activate shelves of a Nimble / Alletra 6K storage system identified by {systemId}

Activate shelves of a Nimble / Alletra 6K storage system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_shelves_activate_input import NimbleShelvesActivateInput
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    nimble_shelves_activate_input = dscc.NimbleShelvesActivateInput() # NimbleShelvesActivateInput | 

    try:
        # Activate shelves of a Nimble / Alletra 6K storage system identified by {systemId}
        api_response = api_instance.device_type2_activate_shelf(system_id, nimble_shelves_activate_input)
        print("The response of ShelvesApi->device_type2_activate_shelf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type2_activate_shelf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_shelves_activate_input** | [**NimbleShelvesActivateInput**](NimbleShelvesActivateInput.md)|  | 

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

# **device_type2_get_all_shelves**
> NimbleShelfList device_type2_get_all_shelves(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all shelves details by Nimble / Alletra 6K

Get all shelves details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_shelf_list import NimbleShelfList
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter shelves by Key. (optional)
    sort = 'name desc' # str | oData query to sort shelves resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all shelves details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_shelves(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of ShelvesApi->device_type2_get_all_shelves:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type2_get_all_shelves: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter shelves by Key. | [optional] 
 **sort** | **str**| oData query to sort shelves resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleShelfList**](NimbleShelfList.md)

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

# **device_type2_get_shelf_by_id**
> NimbleShelfDetailsWithRequestUri device_type2_get_shelf_by_id(system_id, shelf_id, select=select)

Get details of Nimble / Alletra 6K Shelf identified by {shelfId}

Get details of Nimble / Alletra 6K Shelf identified by {shelfId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_shelf_details_with_request_uri import NimbleShelfDetailsWithRequestUri
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    shelf_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | Identifier of shelf. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Nimble / Alletra 6K Shelf identified by {shelfId}
        api_response = api_instance.device_type2_get_shelf_by_id(system_id, shelf_id, select=select)
        print("The response of ShelvesApi->device_type2_get_shelf_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type2_get_shelf_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **shelf_id** | **str**| Identifier of shelf. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleShelfDetailsWithRequestUri**](NimbleShelfDetailsWithRequestUri.md)

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

# **device_type2_locate_shelf_chassis**
> TaskResponse device_type2_locate_shelf_chassis(system_id, shelf_id, nimble_shelf_locate_input)

Locate chassis of Nimble / Alletra 6K shelf identified by {shelfId}

Locate chassis of Nimble / Alletra 6K shelf identified by {shelfId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_shelf_locate_input import NimbleShelfLocateInput
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    shelf_id = '001df0fe6f7dc7bb16000000000000000000004817' # str | ID of the shelf.
    nimble_shelf_locate_input = dscc.NimbleShelfLocateInput() # NimbleShelfLocateInput | 

    try:
        # Locate chassis of Nimble / Alletra 6K shelf identified by {shelfId}
        api_response = api_instance.device_type2_locate_shelf_chassis(system_id, shelf_id, nimble_shelf_locate_input)
        print("The response of ShelvesApi->device_type2_locate_shelf_chassis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type2_locate_shelf_chassis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **shelf_id** | **str**| ID of the shelf. | 
 **nimble_shelf_locate_input** | [**NimbleShelfLocateInput**](NimbleShelfLocateInput.md)|  | 

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

# **device_type4_disks_get_by_id**
> DeviceType4DiskDetails device_type4_disks_get_by_id(system_id, cage_id, id, select=select)

Get details of HPE Alletra Storage MP disk identified by {cageId} and {id}

Get details of HPE Alletra Storage MP disk identified by {cageId} and {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_disk_details import DeviceType4DiskDetails
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    cage_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | cage ID
    id = 'd4b13e70924d29afdb77d932f7563ea6' # str | UID of the disk
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP disk identified by {cageId} and {id}
        api_response = api_instance.device_type4_disks_get_by_id(system_id, cage_id, id, select=select)
        print("The response of ShelvesApi->device_type4_disks_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type4_disks_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **cage_id** | **str**| cage ID | 
 **id** | **str**| UID of the disk | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4DiskDetails**](DeviceType4DiskDetails.md)

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

# **device_type4_disks_list**
> DeviceType4DisksSummaryList device_type4_disks_list(system_id, cage_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of HPE Alletra Storage MP disks identified by {cageId}

Get details of HPE Alletra Storage MP disks identified by {cageId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_disks_summary_list import DeviceType4DisksSummaryList
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    cage_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | cage ID
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemId eq 7CE751P312' # str | oData query to filter Disk by Key. (optional)
    sort = 'name asc' # str | oData query to sort Disk by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP disks identified by {cageId}
        api_response = api_instance.device_type4_disks_list(system_id, cage_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of ShelvesApi->device_type4_disks_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type4_disks_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **cage_id** | **str**| cage ID | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter Disk by Key. | [optional] 
 **sort** | **str**| oData query to sort Disk by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4DisksSummaryList**](DeviceType4DisksSummaryList.md)

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

# **device_type4_enclosure_card_list**
> DeviceType4EnclosureCardsSummaryList device_type4_enclosure_card_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of HPE Alletra Storage MP Enclosure Cards identified by {systemId}

Get details of HPE Alletra Storage MP Enclosure Cards identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_enclosure_cards_summary_list import DeviceType4EnclosureCardsSummaryList
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemWWN eq 2FF70002AC018D94' # str | oData query to filter enclosure resource by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort enclosure resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Enclosure Cards identified by {systemId}
        api_response = api_instance.device_type4_enclosure_card_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of ShelvesApi->device_type4_enclosure_card_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type4_enclosure_card_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter enclosure resource by Key. | [optional] 
 **sort** | **str**| oData query to sort enclosure resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4EnclosureCardsSummaryList**](DeviceType4EnclosureCardsSummaryList.md)

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

# **device_type4_enclosure_cards_get_by_id**
> DeviceType4EnclosureCardDetailedFields device_type4_enclosure_cards_get_by_id(system_id, enclosure_id, id, select=select)

Get details of HPE Alletra Storage MP Enclosure Card identified by {enclosureId} and {id}

Get details of HPE Alletra Storage MP Enclosure Card identified by {enclosureId} and {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_enclosure_card_detailed_fields import DeviceType4EnclosureCardDetailedFields
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure card
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Enclosure Card identified by {enclosureId} and {id}
        api_response = api_instance.device_type4_enclosure_cards_get_by_id(system_id, enclosure_id, id, select=select)
        print("The response of ShelvesApi->device_type4_enclosure_cards_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type4_enclosure_cards_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **id** | **str**| UID of the enclosure card | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4EnclosureCardDetailedFields**](DeviceType4EnclosureCardDetailedFields.md)

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

# **device_type4_enclosure_cards_list**
> DeviceType4EnclosureCardsSummaryList device_type4_enclosure_cards_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of HPE Alletra Storage MP Enclosure Cards identified by {enclosureId}

Get details of HPE Alletra Storage MP Enclosure Cards identified by {enclosureId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_enclosure_cards_summary_list import DeviceType4EnclosureCardsSummaryList
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemWWN eq 2FF70002AC018D94' # str | oData query to filter enclosure resource by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort enclosure resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Enclosure Cards identified by {enclosureId}
        api_response = api_instance.device_type4_enclosure_cards_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of ShelvesApi->device_type4_enclosure_cards_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type4_enclosure_cards_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter enclosure resource by Key. | [optional] 
 **sort** | **str**| oData query to sort enclosure resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4EnclosureCardsSummaryList**](DeviceType4EnclosureCardsSummaryList.md)

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

# **device_type4_enclosure_cards_locate_ioby_id**
> TaskResponse device_type4_enclosure_cards_locate_ioby_id(system_id, enclosure_id, id, device_type4_locate_input)

Locate IO Module of HPE Alletra Storage MP identified by {id}

Locate IO Module of HPE Alletra Storage MP identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_locate_input import DeviceType4LocateInput
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure card
    device_type4_locate_input = dscc.DeviceType4LocateInput() # DeviceType4LocateInput | 

    try:
        # Locate IO Module of HPE Alletra Storage MP identified by {id}
        api_response = api_instance.device_type4_enclosure_cards_locate_ioby_id(system_id, enclosure_id, id, device_type4_locate_input)
        print("The response of ShelvesApi->device_type4_enclosure_cards_locate_ioby_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type4_enclosure_cards_locate_ioby_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **id** | **str**| UID of the enclosure card | 
 **device_type4_locate_input** | [**DeviceType4LocateInput**](DeviceType4LocateInput.md)|  | 

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

# **device_type4_enclosure_connector_list**
> DeviceType4EnclosureConnectorsSummaryList device_type4_enclosure_connector_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of HPE Alletra Storage MP Enclosure Connectors identified by {enclosureId}

Get details of HPE Alletra Storage MP Enclosure Connectors identified by {enclosureId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_enclosure_connectors_summary_list import DeviceType4EnclosureConnectorsSummaryList
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemWWN eq 2FF70002AC018D94' # str | oData query to filter enclosure resource by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort enclosure resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Enclosure Connectors identified by {enclosureId}
        api_response = api_instance.device_type4_enclosure_connector_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of ShelvesApi->device_type4_enclosure_connector_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type4_enclosure_connector_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter enclosure resource by Key. | [optional] 
 **sort** | **str**| oData query to sort enclosure resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4EnclosureConnectorsSummaryList**](DeviceType4EnclosureConnectorsSummaryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected Error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_enclosure_connectors_get_by_id**
> DeviceType4EnclosureConnectorDetails device_type4_enclosure_connectors_get_by_id(system_id, enclosure_id, enclosure_connector_id, select=select)

Get details of HPE Alletra Storage MP Enclosure Connector identified by {enclosureId} and {enclosureConnectorId}

Get details of HPE Alletra Storage MP Enclosure Connector identified by {enclosureId} and {enclosureConnectorId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_enclosure_connector_details import DeviceType4EnclosureConnectorDetails
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    enclosure_connector_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure connector
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Enclosure Connector identified by {enclosureId} and {enclosureConnectorId}
        api_response = api_instance.device_type4_enclosure_connectors_get_by_id(system_id, enclosure_id, enclosure_connector_id, select=select)
        print("The response of ShelvesApi->device_type4_enclosure_connectors_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type4_enclosure_connectors_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **enclosure_connector_id** | **str**| UID of the enclosure connector | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4EnclosureConnectorDetails**](DeviceType4EnclosureConnectorDetails.md)

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

# **device_type4_enclosure_connectors_list**
> DeviceType4EnclosureConnectorsSummaryList device_type4_enclosure_connectors_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of HPE Alletra Storage MP Enclosure Connectors

Get details of HPE Alletra Storage MP Enclosure Connectors

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_enclosure_connectors_summary_list import DeviceType4EnclosureConnectorsSummaryList
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemWWN eq 2FF70002AC018D94' # str | oData query to filter enclosure resource by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort enclosure resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Enclosure Connectors
        api_response = api_instance.device_type4_enclosure_connectors_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of ShelvesApi->device_type4_enclosure_connectors_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type4_enclosure_connectors_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter enclosure resource by Key. | [optional] 
 **sort** | **str**| oData query to sort enclosure resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4EnclosureConnectorsSummaryList**](DeviceType4EnclosureConnectorsSummaryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected Error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_enclosure_disks_get_by_id**
> DeviceType4EnclosureDiskDetails device_type4_enclosure_disks_get_by_id(system_id, enclosure_id, id, select=select)

Get details of HPE Alletra Storage MP Enclosure Disk identified by {enclosureId} and {id}

Get details of HPE Alletra Storage MP Enclosure Disk identified by {enclosureId} and {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_enclosure_disk_details import DeviceType4EnclosureDiskDetails
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure disk
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Enclosure Disk identified by {enclosureId} and {id}
        api_response = api_instance.device_type4_enclosure_disks_get_by_id(system_id, enclosure_id, id, select=select)
        print("The response of ShelvesApi->device_type4_enclosure_disks_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type4_enclosure_disks_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **id** | **str**| UID of the enclosure disk | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4EnclosureDiskDetails**](DeviceType4EnclosureDiskDetails.md)

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

# **device_type4_enclosure_disks_list**
> DeviceType4EnclosureDisksSummaryList device_type4_enclosure_disks_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of HPE Alletra Storage MP Enclosure Disks identified by {enclosureId}

Get details of HPE Alletra Storage MP Enclosure Disks identified by {enclosureId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_enclosure_disks_summary_list import DeviceType4EnclosureDisksSummaryList
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemWWN eq 2FF70002AC018D94' # str | oData query to filter enclosure resource by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort enclosure resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Enclosure Disks identified by {enclosureId}
        api_response = api_instance.device_type4_enclosure_disks_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of ShelvesApi->device_type4_enclosure_disks_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type4_enclosure_disks_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter enclosure resource by Key. | [optional] 
 **sort** | **str**| oData query to sort enclosure resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4EnclosureDisksSummaryList**](DeviceType4EnclosureDisksSummaryList.md)

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

# **device_type4_enclosure_powers_get_by_id**
> DeviceType4EnclosurePowerDetails device_type4_enclosure_powers_get_by_id(system_id, enclosure_id, id, select=select)

Get details of HPE Alletra Storage MP Enclosure Power identified by {enclosureId} and {id}

Get details of HPE Alletra Storage MP Enclosure Power identified by {enclosureId} and {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_enclosure_power_details import DeviceType4EnclosurePowerDetails
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure power
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Enclosure Power identified by {enclosureId} and {id}
        api_response = api_instance.device_type4_enclosure_powers_get_by_id(system_id, enclosure_id, id, select=select)
        print("The response of ShelvesApi->device_type4_enclosure_powers_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type4_enclosure_powers_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **id** | **str**| UID of the enclosure power | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4EnclosurePowerDetails**](DeviceType4EnclosurePowerDetails.md)

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

# **device_type4_enclosure_powers_list**
> DeviceType4EnclosurePowersSummaryList device_type4_enclosure_powers_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of HPE Alletra Storage MP Enclosure Powers identified by {enclosureId}

Get details of HPE Alletra Storage MP Enclosure Powers identified by {enclosureId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_enclosure_powers_summary_list import DeviceType4EnclosurePowersSummaryList
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemWWN eq 2FF70002AC018D94' # str | oData query to filter enclosure resource by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort enclosure resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Enclosure Powers identified by {enclosureId}
        api_response = api_instance.device_type4_enclosure_powers_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of ShelvesApi->device_type4_enclosure_powers_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type4_enclosure_powers_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter enclosure resource by Key. | [optional] 
 **sort** | **str**| oData query to sort enclosure resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4EnclosurePowersSummaryList**](DeviceType4EnclosurePowersSummaryList.md)

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

# **device_type4_enclosure_sleds_get_by_id**
> DeviceType4EnclosureSledDetails device_type4_enclosure_sleds_get_by_id(system_id, enclosure_id, id, select=select)

Get details of HPE Alletra Storage MP Enclosure Sled identified by {enclosureId} and {id}

Get details of HPE Alletra Storage MP Enclosure Sled identified by {enclosureId} and {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_enclosure_sled_details import DeviceType4EnclosureSledDetails
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure sled
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Enclosure Sled identified by {enclosureId} and {id}
        api_response = api_instance.device_type4_enclosure_sleds_get_by_id(system_id, enclosure_id, id, select=select)
        print("The response of ShelvesApi->device_type4_enclosure_sleds_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type4_enclosure_sleds_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **id** | **str**| UID of the enclosure sled | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4EnclosureSledDetails**](DeviceType4EnclosureSledDetails.md)

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

# **device_type4_enclosure_sleds_list**
> DeviceType4EnclosureSledsSummaryList device_type4_enclosure_sleds_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of HPE Alletra Storage MP Enclosure Sleds identified by {enclosureId}

Get details of HPE Alletra Storage MP Enclosure Sleds identified by {enclosureId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_enclosure_sleds_summary_list import DeviceType4EnclosureSledsSummaryList
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemWWN eq 2FF70002AC018D94' # str | oData query to filter enclosure resource by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort enclosure resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Enclosure Sleds identified by {enclosureId}
        api_response = api_instance.device_type4_enclosure_sleds_list(system_id, enclosure_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of ShelvesApi->device_type4_enclosure_sleds_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type4_enclosure_sleds_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter enclosure resource by Key. | [optional] 
 **sort** | **str**| oData query to sort enclosure resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4EnclosureSledsSummaryList**](DeviceType4EnclosureSledsSummaryList.md)

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

# **device_type4_enclosure_sleds_locate_drive_by_id**
> TaskResponse device_type4_enclosure_sleds_locate_drive_by_id(system_id, enclosure_id, id, device_type4_locate_input)

Locate drive of HPE Alletra Storage MP identified by {id}

Locate drive of HPE Alletra Storage MP identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_locate_input import DeviceType4LocateInput
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure sled
    device_type4_locate_input = dscc.DeviceType4LocateInput() # DeviceType4LocateInput | 

    try:
        # Locate drive of HPE Alletra Storage MP identified by {id}
        api_response = api_instance.device_type4_enclosure_sleds_locate_drive_by_id(system_id, enclosure_id, id, device_type4_locate_input)
        print("The response of ShelvesApi->device_type4_enclosure_sleds_locate_drive_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type4_enclosure_sleds_locate_drive_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **id** | **str**| UID of the enclosure sled | 
 **device_type4_locate_input** | [**DeviceType4LocateInput**](DeviceType4LocateInput.md)|  | 

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

# **device_type4_enclosures_edit_by_id**
> TaskResponse device_type4_enclosures_edit_by_id(system_id, id, device_type4_edit_enclosure_input)

Edit details of HPE Alletra Storage MP Enclosure identified by {id}

Edit details of HPE Alletra Storage MP Enclosure identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_edit_enclosure_input import DeviceType4EditEnclosureInput
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    device_type4_edit_enclosure_input = dscc.DeviceType4EditEnclosureInput() # DeviceType4EditEnclosureInput | 

    try:
        # Edit details of HPE Alletra Storage MP Enclosure identified by {id}
        api_response = api_instance.device_type4_enclosures_edit_by_id(system_id, id, device_type4_edit_enclosure_input)
        print("The response of ShelvesApi->device_type4_enclosures_edit_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type4_enclosures_edit_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the enclosure | 
 **device_type4_edit_enclosure_input** | [**DeviceType4EditEnclosureInput**](DeviceType4EditEnclosureInput.md)|  | 

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

# **device_type4_enclosures_get_by_id**
> DeviceType4EnclosuresDetailedFields device_type4_enclosures_get_by_id(system_id, id, select=select)

Get details of HPE Alletra Storage MP Enclosure identified by {id}

Get details of HPE Alletra Storage MP Enclosure identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_enclosures_detailed_fields import DeviceType4EnclosuresDetailedFields
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Enclosure identified by {id}
        api_response = api_instance.device_type4_enclosures_get_by_id(system_id, id, select=select)
        print("The response of ShelvesApi->device_type4_enclosures_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type4_enclosures_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the enclosure | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4EnclosuresDetailedFields**](DeviceType4EnclosuresDetailedFields.md)

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

# **device_type4_enclosures_list**
> DeviceType4EnclosuresSummaryList device_type4_enclosures_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of HPE Alletra Storage MP Enclosures

Get details of HPE Alletra Storage MP Enclosures

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_enclosures_summary_list import DeviceType4EnclosuresSummaryList
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'systemWWN eq 2FF70002AC018D94' # str | oData query to filter enclosure resource by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort enclosure resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Enclosures
        api_response = api_instance.device_type4_enclosures_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of ShelvesApi->device_type4_enclosures_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type4_enclosures_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter enclosure resource by Key. | [optional] 
 **sort** | **str**| oData query to sort enclosure resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4EnclosuresSummaryList**](DeviceType4EnclosuresSummaryList.md)

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

# **device_type4_enclosures_locate_by_id**
> TaskResponse device_type4_enclosures_locate_by_id(system_id, id, device_type4_locate_input)

Locate enclosure drive of HPE Alletra Storage MP identified by {id}

Locate enclosure drive of HPE Alletra Storage MP identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_locate_input import DeviceType4LocateInput
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    device_type4_locate_input = dscc.DeviceType4LocateInput() # DeviceType4LocateInput | 

    try:
        # Locate enclosure drive of HPE Alletra Storage MP identified by {id}
        api_response = api_instance.device_type4_enclosures_locate_by_id(system_id, id, device_type4_locate_input)
        print("The response of ShelvesApi->device_type4_enclosures_locate_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type4_enclosures_locate_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the enclosure | 
 **device_type4_locate_input** | [**DeviceType4LocateInput**](DeviceType4LocateInput.md)|  | 

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

# **device_type4_physical_drive_performance_history_get**
> DeviceType4PerformanceHistoryData device_type4_physical_drive_performance_history_get(system_id, report_type=report_type, range=range, time_interval_min=time_interval_min, compare_by=compare_by, group_by=group_by, metric_type=metric_type, filter=filter)

Get details of performance metrics of physical drives on storage system identified by {systemid}

Get details of performance metrics of physical drives on storage system identified by {systemid}

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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    report_type = 'Canned,Custom,Def,ApiUser' # str | parameter will be set to report type requested. For api users, set parameter as ApiUser (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)
    compare_by = 'top eq 5 and metrics eq READ_IOPS' # str | compareBy will define top and compare metrics for which query has to be made (optional)
    group_by = 'VV_NAME,HOST_NAME,LUN,deviceName' # str | groupBy will define comma separated groupby parameters (optional)
    metric_type = 'IOPS,LATENCY,THROUGHPUT,IOSIZE,QLEN,AVG_BUSY,powerConsumption' # str | metricType will define comma separated metrics (optional)
    filter = 'vvname in (vvname1,vvname2,vvname3) ,deviceName in (cage1)' # str | filter will define objects to be filtered (optional)

    try:
        # Get details of performance metrics of physical drives on storage system identified by {systemid}
        api_response = api_instance.device_type4_physical_drive_performance_history_get(system_id, report_type=report_type, range=range, time_interval_min=time_interval_min, compare_by=compare_by, group_by=group_by, metric_type=metric_type, filter=filter)
        print("The response of ShelvesApi->device_type4_physical_drive_performance_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->device_type4_physical_drive_performance_history_get: %s\n" % e)
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

# **enclosure_cards_locate_ioby_id**
> TaskResponse enclosure_cards_locate_ioby_id(system_id, enclosure_id, id, locate_input)

Locate IO Module of Primera / Alletra 9K identified by {id}

Locate IO Module of Primera / Alletra 9K identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.locate_input import LocateInput
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure card
    locate_input = dscc.LocateInput() # LocateInput | 

    try:
        # Locate IO Module of Primera / Alletra 9K identified by {id}
        api_response = api_instance.enclosure_cards_locate_ioby_id(system_id, enclosure_id, id, locate_input)
        print("The response of ShelvesApi->enclosure_cards_locate_ioby_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->enclosure_cards_locate_ioby_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **id** | **str**| UID of the enclosure card | 
 **locate_input** | [**LocateInput**](LocateInput.md)|  | 

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

# **enclosure_powers_locate_pcmby_id**
> TaskResponse enclosure_powers_locate_pcmby_id(system_id, enclosure_id, id, locate_input)

Locate PCM of Primera / Alletra 9K identified by {id}

Locate PCM of Primera / Alletra 9K identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.locate_input import LocateInput
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure power
    locate_input = dscc.LocateInput() # LocateInput | 

    try:
        # Locate PCM of Primera / Alletra 9K identified by {id}
        api_response = api_instance.enclosure_powers_locate_pcmby_id(system_id, enclosure_id, id, locate_input)
        print("The response of ShelvesApi->enclosure_powers_locate_pcmby_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->enclosure_powers_locate_pcmby_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **id** | **str**| UID of the enclosure power | 
 **locate_input** | [**LocateInput**](LocateInput.md)|  | 

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

# **enclosure_sleds_locate_drive_by_id**
> TaskResponse enclosure_sleds_locate_drive_by_id(system_id, enclosure_id, id, locate_input)

Locate drive of Primera / Alletra 9K identified by {id}

Locate drive of Primera / Alletra 9K identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.locate_input import LocateInput
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    enclosure_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure sled
    locate_input = dscc.LocateInput() # LocateInput | 

    try:
        # Locate drive of Primera / Alletra 9K identified by {id}
        api_response = api_instance.enclosure_sleds_locate_drive_by_id(system_id, enclosure_id, id, locate_input)
        print("The response of ShelvesApi->enclosure_sleds_locate_drive_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->enclosure_sleds_locate_drive_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **enclosure_id** | **str**| UID of the enclosure | 
 **id** | **str**| UID of the enclosure sled | 
 **locate_input** | [**LocateInput**](LocateInput.md)|  | 

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

# **enclosures_edit_by_id**
> TaskResponse enclosures_edit_by_id(system_id, id, edit_enclosure_input)

Edit details of Primera / Alletra 9K Enclosure identified by {id}

Edit details of Primera / Alletra 9K Enclosure identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.edit_enclosure_input import EditEnclosureInput
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    edit_enclosure_input = dscc.EditEnclosureInput() # EditEnclosureInput | 

    try:
        # Edit details of Primera / Alletra 9K Enclosure identified by {id}
        api_response = api_instance.enclosures_edit_by_id(system_id, id, edit_enclosure_input)
        print("The response of ShelvesApi->enclosures_edit_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->enclosures_edit_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the enclosure | 
 **edit_enclosure_input** | [**EditEnclosureInput**](EditEnclosureInput.md)|  | 

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

# **enclosures_locate_by_id**
> TaskResponse enclosures_locate_by_id(system_id, id, locate_input)

Locate enclosure drive of Primera / Alletra 9K identified by {id}

Locate enclosure drive of Primera / Alletra 9K identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.locate_input import LocateInput
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
    api_instance = dscc.ShelvesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the enclosure
    locate_input = dscc.LocateInput() # LocateInput | 

    try:
        # Locate enclosure drive of Primera / Alletra 9K identified by {id}
        api_response = api_instance.enclosures_locate_by_id(system_id, id, locate_input)
        print("The response of ShelvesApi->enclosures_locate_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShelvesApi->enclosures_locate_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the enclosure | 
 **locate_input** | [**LocateInput**](LocateInput.md)|  | 

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

