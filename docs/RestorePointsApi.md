# dscc.RestorePointsApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type2_clone_action_on_snapshot_collections**](RestorePointsApi.md#device_type2_clone_action_on_snapshot_collections) | **POST** /api/v1/storage-systems/device-type2/{systemId}/snapshot-collections/{snapshotCollectionId}/actions/clone | Perform action clone Nimble / Alletra 6K on a snapshot collection identified by {snapshotCollectionId} in system identified by {systemId}


# **device_type2_clone_action_on_snapshot_collections**
> TaskResponse device_type2_clone_action_on_snapshot_collections(system_id, snapshot_collection_id, nimble_clone_snapshot_collections_input)

Perform action clone Nimble / Alletra 6K on a snapshot collection identified by {snapshotCollectionId} in system identified by {systemId}

Perform action clone Nimble / Alletra 6K on a snapshot collection identified by {snapshotCollectionId} in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_clone_snapshot_collections_input import NimbleCloneSnapshotCollectionsInput
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
    api_instance = dscc.RestorePointsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    snapshot_collection_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of snapshot Collection. A 42 digit hexadecimal number.
    nimble_clone_snapshot_collections_input = dscc.NimbleCloneSnapshotCollectionsInput() # NimbleCloneSnapshotCollectionsInput | 

    try:
        # Perform action clone Nimble / Alletra 6K on a snapshot collection identified by {snapshotCollectionId} in system identified by {systemId}
        api_response = api_instance.device_type2_clone_action_on_snapshot_collections(system_id, snapshot_collection_id, nimble_clone_snapshot_collections_input)
        print("The response of RestorePointsApi->device_type2_clone_action_on_snapshot_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestorePointsApi->device_type2_clone_action_on_snapshot_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **snapshot_collection_id** | **str**| Identifier of snapshot Collection. A 42 digit hexadecimal number. | 
 **nimble_clone_snapshot_collections_input** | [**NimbleCloneSnapshotCollectionsInput**](NimbleCloneSnapshotCollectionsInput.md)|  | 

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

