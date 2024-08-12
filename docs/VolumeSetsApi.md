# dscc.VolumeSetsApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type1_create_protection_policy**](VolumeSetsApi.md#device_type1_create_protection_policy) | **POST** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id}/protection-policies | Add protection policy on application set identified by {id} for a storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_edit_protection_policies**](VolumeSetsApi.md#device_type1_edit_protection_policies) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id}/protection-policies | Edit protection policy on application set identified by {id} for a storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_edit_proximity_settings**](VolumeSetsApi.md#device_type1_edit_proximity_settings) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id}/proximity-settings | Change proximity settings of hosts where volume sets are exported identified by {id} and {systemId} from Primera / Alletra 9K
[**device_type1_fix_protection_policy**](VolumeSetsApi.md#device_type1_fix_protection_policy) | **POST** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id}/protection-policies/fix | Fix protection policy configuration on application set identified by {id} for a storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_get_protection_policies**](VolumeSetsApi.md#device_type1_get_protection_policies) | **GET** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id}/protection-policies | Get details of protection policies configured on application set identified by {id} created on Primera / Alletra 9K identified by {systemId}
[**device_type1_get_proximity_settings**](VolumeSetsApi.md#device_type1_get_proximity_settings) | **GET** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id}/proximity-settings | Get hosts and proximity details identified by application set {id} for Primera / Alletra 9K identified by {systemId}
[**device_type1_get_replication_partner_volumes_by_app_set_id**](VolumeSetsApi.md#device_type1_get_replication_partner_volumes_by_app_set_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{appsetId}/replication-partners/{replicationPartnerId}/volumes | Get volume details of replication partners identified by {appsetId} and {replicationPartnerId} for Primera / Alletra 9K
[**device_type1_get_replication_partners_by_app_set_id**](VolumeSetsApi.md#device_type1_get_replication_partners_by_app_set_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{appsetId}/replication-partners | Get details of Primera / Alletra 9K replication partners identified by {systemId} and {appsetId}
[**device_type1_snapsets_get_by_id**](VolumeSetsApi.md#device_type1_snapsets_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{appsetId}/snapsets/{snapsetId} | Get details of snapsets identified by {snapsetId} for Applicationset identified by {appsetId} for Primera / Alletra 9K
[**device_type1_volume_set_capacity_statistics_get_by_id**](VolumeSetsApi.md#device_type1_volume_set_capacity_statistics_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id}/capacity-statistics | Get capacity details for an applicationset identified by appsetUid
[**device_type1_volume_set_export**](VolumeSetsApi.md#device_type1_volume_set_export) | **POST** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{appsetId}/export | Export applicationset identified by {appsetId} from Primera / Alletra 9K identified by {systemId}
[**device_type1_volume_set_snapshot_delete_by_id**](VolumeSetsApi.md#device_type1_volume_set_snapshot_delete_by_id) | **DELETE** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{appsetId}/snapsets/{snapsetId} | Remove Primera / Alletra 9K snapset in system identified by {snapsetId}
[**device_type1_volume_set_snapshots_list**](VolumeSetsApi.md#device_type1_volume_set_snapshots_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id}/snapsets | Get snapshot details of volume sets identified by {id} for Primera / Alletra 9K
[**device_type1_volume_set_unexport**](VolumeSetsApi.md#device_type1_volume_set_unexport) | **POST** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{appsetId}/un-export | Unexport applicationset identified by {appsetId} from Primera / Alletra 9K identified by {systemId}
[**device_type1_volume_set_volumes_list**](VolumeSetsApi.md#device_type1_volume_set_volumes_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{appsetId}/volumes | Get volumes for an applicationset identified by appsetUid
[**device_type1_volume_sets_create**](VolumeSetsApi.md#device_type1_volume_sets_create) | **POST** /api/v1/storage-systems/device-type1/{systemId}/applicationsets | Create Application Set for a storage system Primera / Alletra 9K
[**device_type1_volume_sets_delete_by_id**](VolumeSetsApi.md#device_type1_volume_sets_delete_by_id) | **DELETE** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id} | Delete applicationset identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type1_volume_sets_edit_by_id**](VolumeSetsApi.md#device_type1_volume_sets_edit_by_id) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id} | Edit applicationset identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type1_volume_sets_get_by_id**](VolumeSetsApi.md#device_type1_volume_sets_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id} | Get applicationset details for an applicationset identified by appsetUid
[**device_type1_volume_sets_list**](VolumeSetsApi.md#device_type1_volume_sets_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/applicationsets | Get all applicationset details for Primera / Alletra 9K
[**device_type1_volume_sets_snapshot_create**](VolumeSetsApi.md#device_type1_volume_sets_snapshot_create) | **POST** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id}/snapsets | Create snapshot for application set identified by {id}
[**device_type1action_on_volume_sets**](VolumeSetsApi.md#device_type1action_on_volume_sets) | **POST** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id}/remote-protection/actions | Actions on volume set identified by {id} and {systemId} from Primera / Alletra 9K
[**device_type1get_supported_protection_types**](VolumeSetsApi.md#device_type1get_supported_protection_types) | **GET** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id}/supported-protection | Get supported protection types for application set identified by {id} on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1remove_protection_policies**](VolumeSetsApi.md#device_type1remove_protection_policies) | **POST** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id}/protection-policies/remove | Remove protection policy on application set identified by {id} for a storage system Primera / Alletra 9K identified by {systemId}
[**device_type2_action_on_snapshot_collection**](VolumeSetsApi.md#device_type2_action_on_snapshot_collection) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId}/snapshot-collections/update | Perform offline/online action on  snapshot collections of Nimble / Alletra 6K and associated with volume collection {volumeCollectionId}  in the system identified by {systemId}
[**device_type2_action_on_volume_collection**](VolumeSetsApi.md#device_type2_action_on_volume_collection) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId}/actions/handover | Perform handover action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}
[**device_type2_action_on_volume_collection_id**](VolumeSetsApi.md#device_type2_action_on_volume_collection_id) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId}/actions/demote | Perform demote action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}
[**device_type2_actionon_volume_collection**](VolumeSetsApi.md#device_type2_actionon_volume_collection) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId}/actions/abort-handover | Perform abort handover action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}
[**device_type2_add_volumes_to_volume_collections**](VolumeSetsApi.md#device_type2_add_volumes_to_volume_collections) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId}/actions/add-volumes | Add volumes to Nimble / Alletra 6K volumes collection in system identified by {systemId}
[**device_type2_create_snapshot_collections**](VolumeSetsApi.md#device_type2_create_snapshot_collections) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId}/snapshot-collections | Create Nimble / Alletra 6K snapshot collection in system identified by {systemId}
[**device_type2_edit_volume_collection_by_id**](VolumeSetsApi.md#device_type2_edit_volume_collection_by_id) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId} | Edit  details of Nimble / Alletra 6K Volume-collections identified by {volumeCollectionId}
[**device_type2_get_all_folders**](VolumeSetsApi.md#device_type2_get_all_folders) | **GET** /api/v1/storage-systems/device-type2/{systemId}/folders | Get all folders details by Nimble / Alletra 6K
[**device_type2_get_all_volume_collections**](VolumeSetsApi.md#device_type2_get_all_volume_collections) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volume-collections | Get all volume-collections details by Nimble / Alletra 6K
[**device_type2_get_snapshot_collections_by_id**](VolumeSetsApi.md#device_type2_get_snapshot_collections_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId}/snapshot-collections/{snapshotCollectionId} | Get details of snapshot collection of Nimble / Alletra 6K Volume collection identified by {volumeCollectionId} by {snapshotId}
[**device_type2_get_snapshots_by_volume_collection_id**](VolumeSetsApi.md#device_type2_get_snapshots_by_volume_collection_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId}/snapshot-collections | Get all snapshot collections&#39; details of Nimble / Alletra 6K Volume collection identified by {volumeCollectionId}
[**device_type2_get_volume_collection_by_id**](VolumeSetsApi.md#device_type2_get_volume_collection_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId} | Get details of Nimble / Alletra 6K volume-collections identified by {volumeCollectionId}
[**device_type2_promote_action_on_volume_collection**](VolumeSetsApi.md#device_type2_promote_action_on_volume_collection) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId}/actions/promote | Perform promote action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}
[**device_type2_remove_snap_shot_collection**](VolumeSetsApi.md#device_type2_remove_snap_shot_collection) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId}/snapshot-collections/remove | Remove multiple snapshot collections identified by {volumeCollectionId} from Nimble / Alletra 6K
[**device_type2_remove_volume_collection_by_id**](VolumeSetsApi.md#device_type2_remove_volume_collection_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId} | Remove Volume-collection identified by {volumeCollectionId} from Nimble / Alletra 6K
[**device_type2_remove_volumes_from_volume_collection**](VolumeSetsApi.md#device_type2_remove_volumes_from_volume_collection) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId}/actions/remove-volumes | Remove volumes from Nimble / Alletra 6K volumes collection in system identified by {systemId}
[**device_type2_volume_collection_create**](VolumeSetsApi.md#device_type2_volume_collection_create) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volume-collections | Create Nimble / Alletra 6K volume collection in system identified by {systemId}
[**device_type4_create_protection_policy**](VolumeSetsApi.md#device_type4_create_protection_policy) | **POST** /api/v1/storage-systems/device-type4/{systemId}/applicationsets/{id}/protection-policies | Add protection policy on application set identified by {id} for a storage system HPE Alletra Storage MP identified by {systemId}
[**device_type4_edit_protection_policies**](VolumeSetsApi.md#device_type4_edit_protection_policies) | **PUT** /api/v1/storage-systems/device-type4/{systemId}/applicationsets/{id}/protection-policies | Edit protection policy on application set identified by {id} for a storage system HPE Alletra Storage MP identified by {systemId}
[**device_type4_edit_proximity_settings**](VolumeSetsApi.md#device_type4_edit_proximity_settings) | **PUT** /api/v1/storage-systems/device-type4/{systemId}/applicationsets/{id}/proximity-settings | Change proximity settings of hosts where volume sets are exported identified by {id} and {systemId} from HPE Alletra Storage MP
[**device_type4_fix_protection_policy**](VolumeSetsApi.md#device_type4_fix_protection_policy) | **POST** /api/v1/storage-systems/device-type4/{systemId}/applicationsets/{id}/protection-policies/fix | Fix protection policy configuration on application set identified by {id} for a storage system HPE Alletra Storage MP identified by {systemId}
[**device_type4_get_protection_policies**](VolumeSetsApi.md#device_type4_get_protection_policies) | **GET** /api/v1/storage-systems/device-type4/{systemId}/applicationsets/{id}/protection-policies | Get details of protection policies configured on application set identified by {id} created on HPE Alletra Storage MP identified by {systemId}
[**device_type4_get_proximity_settings**](VolumeSetsApi.md#device_type4_get_proximity_settings) | **GET** /api/v1/storage-systems/device-type4/{systemId}/applicationsets/{id}/proximity-settings | Get hosts and proximity details identified by application set {id} for HPE Alletra Storage MP identified by {systemId}
[**device_type4_get_replication_partner_volumes_by_app_set_id**](VolumeSetsApi.md#device_type4_get_replication_partner_volumes_by_app_set_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/applicationsets/{appsetId}/replication-partners/{replicationPartnerId}/volumes | Get volume details of replication partners identified by {appsetId} and {replicationPartnerId} for HPE Alletra Storage MP
[**device_type4_get_replication_partners_by_app_set_id**](VolumeSetsApi.md#device_type4_get_replication_partners_by_app_set_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/applicationsets/{appsetId}/replication-partners | Get details of HPE Alletra Storage MP replication partners identified by {systemId} and {appsetId}
[**device_type4_snapsets_get_by_id**](VolumeSetsApi.md#device_type4_snapsets_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/applicationsets/{appsetId}/snapsets/{snapsetId} | Get details of snapsets identified by {snapsetId} for Applicationset identified by {appsetId} for HPE Alletra Storage MP
[**device_type4_volume_set_capacity_statistics_get_by_id**](VolumeSetsApi.md#device_type4_volume_set_capacity_statistics_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/applicationsets/{id}/capacity-statistics | Get capacity details for an applicationset identified by appsetUid
[**device_type4_volume_set_export**](VolumeSetsApi.md#device_type4_volume_set_export) | **POST** /api/v1/storage-systems/device-type4/{systemId}/applicationsets/{appsetId}/export | Export applicationset identified by {appsetId} from HPE Alletra Storage MP identified by {systemId}
[**device_type4_volume_set_snapshot_get_by_id**](VolumeSetsApi.md#device_type4_volume_set_snapshot_get_by_id) | **DELETE** /api/v1/storage-systems/device-type4/{systemId}/applicationsets/{appsetId}/snapsets/{snapsetId} | Remove HPE Alletra Storage MP snapset in system identified by {snapsetId}
[**device_type4_volume_set_snapshots_list**](VolumeSetsApi.md#device_type4_volume_set_snapshots_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/applicationsets/{id}/snapsets | Get snapshot details of volume sets identified by {id} for HPE Alletra Storage MP
[**device_type4_volume_set_unexport**](VolumeSetsApi.md#device_type4_volume_set_unexport) | **POST** /api/v1/storage-systems/device-type4/{systemId}/applicationsets/{appsetId}/un-export | Unexport applicationset identified by {appsetId} from HPE Alletra Storage MP identified by {systemId}
[**device_type4_volume_set_volumes_list**](VolumeSetsApi.md#device_type4_volume_set_volumes_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/applicationsets/{appsetId}/volumes | Get volumes for an applicationset identified by appsetUid
[**device_type4_volume_sets_create**](VolumeSetsApi.md#device_type4_volume_sets_create) | **POST** /api/v1/storage-systems/device-type4/{systemId}/applicationsets | Create Application Set for a storage system HPE Alletra Storage MP
[**device_type4_volume_sets_delete_by_id**](VolumeSetsApi.md#device_type4_volume_sets_delete_by_id) | **DELETE** /api/v1/storage-systems/device-type4/{systemId}/applicationsets/{id} | Remove applicationset identified by {id} from HPE Alletra Storage MP identified by {systemId}
[**device_type4_volume_sets_edit_by_id**](VolumeSetsApi.md#device_type4_volume_sets_edit_by_id) | **PUT** /api/v1/storage-systems/device-type4/{systemId}/applicationsets/{id} | Edit applicationset identified by {id} from HPE Alletra Storage MP identified by {systemId}
[**device_type4_volume_sets_get_by_id**](VolumeSetsApi.md#device_type4_volume_sets_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/applicationsets/{id} | Get applicationset details for an applicationset identified by appsetUid
[**device_type4_volume_sets_list**](VolumeSetsApi.md#device_type4_volume_sets_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/applicationsets | Get all applicationset details for HPE Alletra Storage MP
[**device_type4_volume_sets_snapshot_create**](VolumeSetsApi.md#device_type4_volume_sets_snapshot_create) | **POST** /api/v1/storage-systems/device-type4/{systemId}/applicationsets/{id}/snapsets | Create snapshot for application set identified by {id}
[**device_type4action_on_volume_sets**](VolumeSetsApi.md#device_type4action_on_volume_sets) | **POST** /api/v1/storage-systems/device-type4/{systemId}/applicationsets/{id}/remote-protection/actions | Actions on volume set identified by {id} and {systemId} from HPE Alletra Storage MP
[**device_type4get_supported_protection_types**](VolumeSetsApi.md#device_type4get_supported_protection_types) | **GET** /api/v1/storage-systems/device-type4/{systemId}/applicationsets/{id}/supported-protection | Get supported protection types for application set identified by {id} on storage system HPE Alletra Storage MP identified by {systemId}
[**device_type4remove_protection_policies**](VolumeSetsApi.md#device_type4remove_protection_policies) | **POST** /api/v1/storage-systems/device-type4/{systemId}/applicationsets/{id}/protection-policies/remove | Remove protection policy on application set identified by {id} for a storage system HPE Alletra Storage MP identified by {systemId}
[**volumeset_get_by_id**](VolumeSetsApi.md#volumeset_get_by_id) | **GET** /api/v1/volume-sets/{id} | Get volume-set identified by id
[**volumeset_get_byvolumeset_id**](VolumeSetsApi.md#volumeset_get_byvolumeset_id) | **GET** /api/v1/volume-sets/{id}/volumes | Get volumes identified by volume set id
[**volumeset_list**](VolumeSetsApi.md#volumeset_list) | **GET** /api/v1/volume-sets | Get all volume-sets
[**volumeset_list_for_system_by_system_id**](VolumeSetsApi.md#volumeset_list_for_system_by_system_id) | **GET** /api/v1/storage-systems/{systemId}/volume-sets | Get all volume-sets for a systemId
[**volumeset_system_get_by_id**](VolumeSetsApi.md#volumeset_system_get_by_id) | **GET** /api/v1/storage-systems/{systemId}/volume-sets/{id} | Get volume-set identified by id


# **device_type1_create_protection_policy**
> TaskResponse device_type1_create_protection_policy(id, system_id, create_protection_policy_input_schema)

Add protection policy on application set identified by {id} for a storage system Primera / Alletra 9K identified by {systemId}

Add protection policy on application set identified by {id} for a storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.create_protection_policy_input_schema import CreateProtectionPolicyInputSchema
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
    api_instance = dscc.VolumeSetsApi(api_client)
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the applicationset
    system_id = '7CE751P312' # str | systemId of the storage system
    create_protection_policy_input_schema = dscc.CreateProtectionPolicyInputSchema() # CreateProtectionPolicyInputSchema | 

    try:
        # Add protection policy on application set identified by {id} for a storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_create_protection_policy(id, system_id, create_protection_policy_input_schema)
        print("The response of VolumeSetsApi->device_type1_create_protection_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1_create_protection_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the applicationset | 
 **system_id** | **str**| systemId of the storage system | 
 **create_protection_policy_input_schema** | [**CreateProtectionPolicyInputSchema**](CreateProtectionPolicyInputSchema.md)|  | 

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

# **device_type1_edit_protection_policies**
> TaskResponse device_type1_edit_protection_policies(id, system_id, edit_protection_policy_input_schema)

Edit protection policy on application set identified by {id} for a storage system Primera / Alletra 9K identified by {systemId}

Edit protection policy on application set identified by {id} for a storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.edit_protection_policy_input_schema import EditProtectionPolicyInputSchema
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
    api_instance = dscc.VolumeSetsApi(api_client)
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the applicationset
    system_id = '7CE751P312' # str | systemId of the storage system
    edit_protection_policy_input_schema = dscc.EditProtectionPolicyInputSchema() # EditProtectionPolicyInputSchema | 

    try:
        # Edit protection policy on application set identified by {id} for a storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_edit_protection_policies(id, system_id, edit_protection_policy_input_schema)
        print("The response of VolumeSetsApi->device_type1_edit_protection_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1_edit_protection_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the applicationset | 
 **system_id** | **str**| systemId of the storage system | 
 **edit_protection_policy_input_schema** | [**EditProtectionPolicyInputSchema**](EditProtectionPolicyInputSchema.md)|  | 

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

# **device_type1_edit_proximity_settings**
> TaskResponse device_type1_edit_proximity_settings(system_id, id, change_proximity_settings_input)

Change proximity settings of hosts where volume sets are exported identified by {id} and {systemId} from Primera / Alletra 9K

Change proximity settings of hosts where volume sets are exported identified by {id} and {systemId} from Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.change_proximity_settings_input import ChangeProximitySettingsInput
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    change_proximity_settings_input = dscc.ChangeProximitySettingsInput() # ChangeProximitySettingsInput | 

    try:
        # Change proximity settings of hosts where volume sets are exported identified by {id} and {systemId} from Primera / Alletra 9K
        api_response = api_instance.device_type1_edit_proximity_settings(system_id, id, change_proximity_settings_input)
        print("The response of VolumeSetsApi->device_type1_edit_proximity_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1_edit_proximity_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the applicationset | 
 **change_proximity_settings_input** | [**ChangeProximitySettingsInput**](ChangeProximitySettingsInput.md)|  | 

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

# **device_type1_fix_protection_policy**
> TaskResponse device_type1_fix_protection_policy(id, system_id, create_protection_policy_input_schema)

Fix protection policy configuration on application set identified by {id} for a storage system Primera / Alletra 9K identified by {systemId}

Remedies issues caused in protection policy configuration on application set identified by {id} for a storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.create_protection_policy_input_schema import CreateProtectionPolicyInputSchema
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
    api_instance = dscc.VolumeSetsApi(api_client)
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the applicationset
    system_id = '7CE751P312' # str | systemId of the storage system
    create_protection_policy_input_schema = dscc.CreateProtectionPolicyInputSchema() # CreateProtectionPolicyInputSchema | 

    try:
        # Fix protection policy configuration on application set identified by {id} for a storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_fix_protection_policy(id, system_id, create_protection_policy_input_schema)
        print("The response of VolumeSetsApi->device_type1_fix_protection_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1_fix_protection_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the applicationset | 
 **system_id** | **str**| systemId of the storage system | 
 **create_protection_policy_input_schema** | [**CreateProtectionPolicyInputSchema**](CreateProtectionPolicyInputSchema.md)|  | 

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

# **device_type1_get_protection_policies**
> PrimeraProtectionPoliciesList device_type1_get_protection_policies(id, system_id, select=select, filter=filter)

Get details of protection policies configured on application set identified by {id} created on Primera / Alletra 9K identified by {systemId}

Get details of protection policies configured on application set identified by {id} created on Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.primera_protection_policies_list import PrimeraProtectionPoliciesList
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
    api_instance = dscc.VolumeSetsApi(api_client)
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the applicationset
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    filter = 'uid eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter application-sets by Key. (optional)

    try:
        # Get details of protection policies configured on application set identified by {id} created on Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_get_protection_policies(id, system_id, select=select, filter=filter)
        print("The response of VolumeSetsApi->device_type1_get_protection_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1_get_protection_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the applicationset | 
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **filter** | **str**| Lucene query to filter application-sets by Key. | [optional] 

### Return type

[**PrimeraProtectionPoliciesList**](PrimeraProtectionPoliciesList.md)

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

# **device_type1_get_proximity_settings**
> VolumeSetProximitySettings device_type1_get_proximity_settings(id, system_id)

Get hosts and proximity details identified by application set {id} for Primera / Alletra 9K identified by {systemId}

Get hosts and proximity details identified by application set {id} for Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.volume_set_proximity_settings import VolumeSetProximitySettings
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
    api_instance = dscc.VolumeSetsApi(api_client)
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the applicationset
    system_id = '7CE751P312' # str | systemId of the storage system

    try:
        # Get hosts and proximity details identified by application set {id} for Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_get_proximity_settings(id, system_id)
        print("The response of VolumeSetsApi->device_type1_get_proximity_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1_get_proximity_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the applicationset | 
 **system_id** | **str**| systemId of the storage system | 

### Return type

[**VolumeSetProximitySettings**](VolumeSetProximitySettings.md)

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

# **device_type1_get_replication_partner_volumes_by_app_set_id**
> ReplicationPartnerVolumesSummaryList device_type1_get_replication_partner_volumes_by_app_set_id(system_id, appset_id, replication_partner_id, limit=limit, offset=offset)

Get volume details of replication partners identified by {appsetId} and {replicationPartnerId} for Primera / Alletra 9K

Get volume details of replication partners identified by {appsetId} and {replicationPartnerId} for Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.replication_partner_volumes_summary_list import ReplicationPartnerVolumesSummaryList
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    appset_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    replication_partner_id = 'aedec7d11d02f73611a6ff992c256bdb' # str | id of device-type1 replication partner
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)

    try:
        # Get volume details of replication partners identified by {appsetId} and {replicationPartnerId} for Primera / Alletra 9K
        api_response = api_instance.device_type1_get_replication_partner_volumes_by_app_set_id(system_id, appset_id, replication_partner_id, limit=limit, offset=offset)
        print("The response of VolumeSetsApi->device_type1_get_replication_partner_volumes_by_app_set_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1_get_replication_partner_volumes_by_app_set_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **appset_id** | **str**| UID of the applicationset | 
 **replication_partner_id** | **str**| id of device-type1 replication partner | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 

### Return type

[**ReplicationPartnerVolumesSummaryList**](ReplicationPartnerVolumesSummaryList.md)

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

# **device_type1_get_replication_partners_by_app_set_id**
> ReplicationPartnersSummaryList device_type1_get_replication_partners_by_app_set_id(system_id, appset_id)

Get details of Primera / Alletra 9K replication partners identified by {systemId} and {appsetId}

Get details of Primera / Alletra 9K replication partners identified by {systemId} and {appsetId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.replication_partners_summary_list import ReplicationPartnersSummaryList
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    appset_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset

    try:
        # Get details of Primera / Alletra 9K replication partners identified by {systemId} and {appsetId}
        api_response = api_instance.device_type1_get_replication_partners_by_app_set_id(system_id, appset_id)
        print("The response of VolumeSetsApi->device_type1_get_replication_partners_by_app_set_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1_get_replication_partners_by_app_set_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **appset_id** | **str**| UID of the applicationset | 

### Return type

[**ReplicationPartnersSummaryList**](ReplicationPartnersSummaryList.md)

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

# **device_type1_snapsets_get_by_id**
> SnapshotsetListSingle device_type1_snapsets_get_by_id(system_id, appset_id, snapset_id, select=select)

Get details of snapsets identified by {snapsetId} for Applicationset identified by {appsetId} for Primera / Alletra 9K

Get details of snapset identified by {snapsetId} for Applicationset identified by {appsetId} for Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.snapshotset_list_single import SnapshotsetListSingle
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    appset_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    snapset_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | Identifier of snapset.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of snapsets identified by {snapsetId} for Applicationset identified by {appsetId} for Primera / Alletra 9K
        api_response = api_instance.device_type1_snapsets_get_by_id(system_id, appset_id, snapset_id, select=select)
        print("The response of VolumeSetsApi->device_type1_snapsets_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1_snapsets_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **appset_id** | **str**| UID of the applicationset | 
 **snapset_id** | **str**| Identifier of snapset. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**SnapshotsetListSingle**](SnapshotsetListSingle.md)

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

# **device_type1_volume_set_capacity_statistics_get_by_id**
> PrimeraApplicationSetCapacityStats device_type1_volume_set_capacity_statistics_get_by_id(id, system_id, select=select)

Get capacity details for an applicationset identified by appsetUid

Get capacity details for an applicationset identified by appsetUid

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.primera_application_set_capacity_stats import PrimeraApplicationSetCapacityStats
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
    api_instance = dscc.VolumeSetsApi(api_client)
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get capacity details for an applicationset identified by appsetUid
        api_response = api_instance.device_type1_volume_set_capacity_statistics_get_by_id(id, system_id, select=select)
        print("The response of VolumeSetsApi->device_type1_volume_set_capacity_statistics_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1_volume_set_capacity_statistics_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UID of the applicationset | 
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraApplicationSetCapacityStats**](PrimeraApplicationSetCapacityStats.md)

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

# **device_type1_volume_set_export**
> TaskResponse device_type1_volume_set_export(system_id, appset_id, export_app_set_post)

Export applicationset identified by {appsetId} from Primera / Alletra 9K identified by {systemId}

Export applicationset identified by {appsetId} from Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.export_app_set_post import ExportAppSetPost
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    appset_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    export_app_set_post = dscc.ExportAppSetPost() # ExportAppSetPost | 

    try:
        # Export applicationset identified by {appsetId} from Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_volume_set_export(system_id, appset_id, export_app_set_post)
        print("The response of VolumeSetsApi->device_type1_volume_set_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1_volume_set_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **appset_id** | **str**| UID of the applicationset | 
 **export_app_set_post** | [**ExportAppSetPost**](ExportAppSetPost.md)|  | 

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

# **device_type1_volume_set_snapshot_delete_by_id**
> TaskResponse device_type1_volume_set_snapshot_delete_by_id(system_id, appset_id, snapset_id, force=force)

Remove Primera / Alletra 9K snapset in system identified by {snapsetId}

Remove Primera / Alletra 9K snapset in system identified by {snapsetId}

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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    appset_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    snapset_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | Identifier of snapset.
    force = true # bool | Make snapset offline and remove. (optional)

    try:
        # Remove Primera / Alletra 9K snapset in system identified by {snapsetId}
        api_response = api_instance.device_type1_volume_set_snapshot_delete_by_id(system_id, appset_id, snapset_id, force=force)
        print("The response of VolumeSetsApi->device_type1_volume_set_snapshot_delete_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1_volume_set_snapshot_delete_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **appset_id** | **str**| UID of the applicationset | 
 **snapset_id** | **str**| Identifier of snapset. | 
 **force** | **bool**| Make snapset offline and remove. | [optional] 

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

# **device_type1_volume_set_snapshots_list**
> SnapshotSetsSummaryList device_type1_volume_set_snapshots_list(system_id, id, limit=limit, offset=offset, select=select, filter=filter, sort=sort)

Get snapshot details of volume sets identified by {id} for Primera / Alletra 9K

Get snapshot details of volume sets identified by {id} for Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.snapshot_sets_summary_list import SnapshotSetsSummaryList
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    filter = 'name eq array1 and wwn eq 2FF70002AC018D94' # str | oData query to filter by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort by Key. (optional)

    try:
        # Get snapshot details of volume sets identified by {id} for Primera / Alletra 9K
        api_response = api_instance.device_type1_volume_set_snapshots_list(system_id, id, limit=limit, offset=offset, select=select, filter=filter, sort=sort)
        print("The response of VolumeSetsApi->device_type1_volume_set_snapshots_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1_volume_set_snapshots_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the applicationset | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| oData query to sort by Key. | [optional] 

### Return type

[**SnapshotSetsSummaryList**](SnapshotSetsSummaryList.md)

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

# **device_type1_volume_set_unexport**
> TaskResponse device_type1_volume_set_unexport(system_id, appset_id, un_export_app_set_post)

Unexport applicationset identified by {appsetId} from Primera / Alletra 9K identified by {systemId}

Unexport applicationset identified by {appsetId} from Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.models.un_export_app_set_post import UnExportAppSetPost
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    appset_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    un_export_app_set_post = dscc.UnExportAppSetPost() # UnExportAppSetPost | 

    try:
        # Unexport applicationset identified by {appsetId} from Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_volume_set_unexport(system_id, appset_id, un_export_app_set_post)
        print("The response of VolumeSetsApi->device_type1_volume_set_unexport:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1_volume_set_unexport: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **appset_id** | **str**| UID of the applicationset | 
 **un_export_app_set_post** | [**UnExportAppSetPost**](UnExportAppSetPost.md)|  | 

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

# **device_type1_volume_set_volumes_list**
> PrimeraVolumesList device_type1_volume_set_volumes_list(appset_id, system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get volumes for an applicationset identified by appsetUid

Get volumes for an applicationset identified by appsetUid

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.primera_volumes_list import PrimeraVolumesList
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
    api_instance = dscc.VolumeSetsApi(api_client)
    appset_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq array1 and wwn eq 2FF70002AC018D94' # str | oData query to filter by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get volumes for an applicationset identified by appsetUid
        api_response = api_instance.device_type1_volume_set_volumes_list(appset_id, system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of VolumeSetsApi->device_type1_volume_set_volumes_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1_volume_set_volumes_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appset_id** | **str**| UID of the applicationset | 
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| oData query to sort by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraVolumesList**](PrimeraVolumesList.md)

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

# **device_type1_volume_sets_create**
> TaskResponse device_type1_volume_sets_create(system_id, create_app_set_input)

Create Application Set for a storage system Primera / Alletra 9K

Create Application Set for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.create_app_set_input import CreateAppSetInput
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    create_app_set_input = dscc.CreateAppSetInput() # CreateAppSetInput | 

    try:
        # Create Application Set for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_volume_sets_create(system_id, create_app_set_input)
        print("The response of VolumeSetsApi->device_type1_volume_sets_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1_volume_sets_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **create_app_set_input** | [**CreateAppSetInput**](CreateAppSetInput.md)|  | 

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

# **device_type1_volume_sets_delete_by_id**
> TaskResponse device_type1_volume_sets_delete_by_id(system_id, id)

Delete applicationset identified by {id} from Primera / Alletra 9K identified by {systemId}

Delete applicationset identified by {id} from Primera / Alletra 9K identified by {systemId}

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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset

    try:
        # Delete applicationset identified by {id} from Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_volume_sets_delete_by_id(system_id, id)
        print("The response of VolumeSetsApi->device_type1_volume_sets_delete_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1_volume_sets_delete_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the applicationset | 

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

# **device_type1_volume_sets_edit_by_id**
> TaskResponse device_type1_volume_sets_edit_by_id(system_id, id, volume_set_put)

Edit applicationset identified by {id} from Primera / Alletra 9K identified by {systemId}

Edit applicationset identified by {id} from Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.models.volume_set_put import VolumeSetPut
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    volume_set_put = dscc.VolumeSetPut() # VolumeSetPut | 

    try:
        # Edit applicationset identified by {id} from Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_volume_sets_edit_by_id(system_id, id, volume_set_put)
        print("The response of VolumeSetsApi->device_type1_volume_sets_edit_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1_volume_sets_edit_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the applicationset | 
 **volume_set_put** | [**VolumeSetPut**](VolumeSetPut.md)|  | 

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

# **device_type1_volume_sets_get_by_id**
> PrimeraApplicationSetDetails device_type1_volume_sets_get_by_id(id, system_id, select=select)

Get applicationset details for an applicationset identified by appsetUid

Get applicationset details for an applicationset identified by appsetUid

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.primera_application_set_details import PrimeraApplicationSetDetails
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
    api_instance = dscc.VolumeSetsApi(api_client)
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get applicationset details for an applicationset identified by appsetUid
        api_response = api_instance.device_type1_volume_sets_get_by_id(id, system_id, select=select)
        print("The response of VolumeSetsApi->device_type1_volume_sets_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1_volume_sets_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UID of the applicationset | 
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraApplicationSetDetails**](PrimeraApplicationSetDetails.md)

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

# **device_type1_volume_sets_list**
> PrimeraApplicationSetsList device_type1_volume_sets_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all applicationset details for Primera / Alletra 9K

Get all applicationset details for Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.primera_application_sets_list import PrimeraApplicationSetsList
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'uid eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter application-sets by Key. (optional)
    sort = 'name desc' # str | Lucene query to sort application-sets by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all applicationset details for Primera / Alletra 9K
        api_response = api_instance.device_type1_volume_sets_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of VolumeSetsApi->device_type1_volume_sets_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1_volume_sets_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter application-sets by Key. | [optional] 
 **sort** | **str**| Lucene query to sort application-sets by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraApplicationSetsList**](PrimeraApplicationSetsList.md)

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

# **device_type1_volume_sets_snapshot_create**
> TaskResponse device_type1_volume_sets_snapshot_create(system_id, id, appset_post)

Create snapshot for application set identified by {id}

Create snapshot for application set identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.appset_post import AppsetPost
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    appset_post = dscc.AppsetPost() # AppsetPost | 

    try:
        # Create snapshot for application set identified by {id}
        api_response = api_instance.device_type1_volume_sets_snapshot_create(system_id, id, appset_post)
        print("The response of VolumeSetsApi->device_type1_volume_sets_snapshot_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1_volume_sets_snapshot_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the applicationset | 
 **appset_post** | [**AppsetPost**](AppsetPost.md)|  | 

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

# **device_type1action_on_volume_sets**
> TaskResponse device_type1action_on_volume_sets(system_id, id, remote_protection_actions_input)

Actions on volume set identified by {id} and {systemId} from Primera / Alletra 9K

Actions on volume set identified by {id} and {systemId} from Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.remote_protection_actions_input import RemoteProtectionActionsInput
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the applicationset
    remote_protection_actions_input = dscc.RemoteProtectionActionsInput() # RemoteProtectionActionsInput | 

    try:
        # Actions on volume set identified by {id} and {systemId} from Primera / Alletra 9K
        api_response = api_instance.device_type1action_on_volume_sets(system_id, id, remote_protection_actions_input)
        print("The response of VolumeSetsApi->device_type1action_on_volume_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1action_on_volume_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| ID of the applicationset | 
 **remote_protection_actions_input** | [**RemoteProtectionActionsInput**](RemoteProtectionActionsInput.md)|  | 

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

# **device_type1get_supported_protection_types**
> PrimeraSupportedProtectionTypes device_type1get_supported_protection_types(id, system_id)

Get supported protection types for application set identified by {id} on storage system Primera / Alletra 9K identified by {systemId}

Get supported protection types for application set identified by {id} on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.primera_supported_protection_types import PrimeraSupportedProtectionTypes
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
    api_instance = dscc.VolumeSetsApi(api_client)
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the applicationset
    system_id = '7CE751P312' # str | systemId of the storage system

    try:
        # Get supported protection types for application set identified by {id} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1get_supported_protection_types(id, system_id)
        print("The response of VolumeSetsApi->device_type1get_supported_protection_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1get_supported_protection_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the applicationset | 
 **system_id** | **str**| systemId of the storage system | 

### Return type

[**PrimeraSupportedProtectionTypes**](PrimeraSupportedProtectionTypes.md)

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

# **device_type1remove_protection_policies**
> TaskResponse device_type1remove_protection_policies(id, system_id, remove_protection_policies_input_schema)

Remove protection policy on application set identified by {id} for a storage system Primera / Alletra 9K identified by {systemId}

Remove protection policy on application set identified by {id} for a storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.remove_protection_policies_input_schema import RemoveProtectionPoliciesInputSchema
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
    api_instance = dscc.VolumeSetsApi(api_client)
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the applicationset
    system_id = '7CE751P312' # str | systemId of the storage system
    remove_protection_policies_input_schema = dscc.RemoveProtectionPoliciesInputSchema() # RemoveProtectionPoliciesInputSchema | 

    try:
        # Remove protection policy on application set identified by {id} for a storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1remove_protection_policies(id, system_id, remove_protection_policies_input_schema)
        print("The response of VolumeSetsApi->device_type1remove_protection_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type1remove_protection_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the applicationset | 
 **system_id** | **str**| systemId of the storage system | 
 **remove_protection_policies_input_schema** | [**RemoveProtectionPoliciesInputSchema**](RemoveProtectionPoliciesInputSchema.md)|  | 

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

# **device_type2_action_on_snapshot_collection**
> TaskResponse device_type2_action_on_snapshot_collection(system_id, volume_collection_id, nimble_update_snapshot_collections_state_input)

Perform offline/online action on  snapshot collections of Nimble / Alletra 6K and associated with volume collection {volumeCollectionId}  in the system identified by {systemId}

Perform offline/online action on  snapshot collections of Nimble / Alletra 6K and associated with volume collection {volumeCollectionId}  in the system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_update_snapshot_collections_state_input import NimbleUpdateSnapshotCollectionsStateInput
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_collection_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of Volume Collection. A 42 digit hexadecimal number.
    nimble_update_snapshot_collections_state_input = dscc.NimbleUpdateSnapshotCollectionsStateInput() # NimbleUpdateSnapshotCollectionsStateInput | 

    try:
        # Perform offline/online action on  snapshot collections of Nimble / Alletra 6K and associated with volume collection {volumeCollectionId}  in the system identified by {systemId}
        api_response = api_instance.device_type2_action_on_snapshot_collection(system_id, volume_collection_id, nimble_update_snapshot_collections_state_input)
        print("The response of VolumeSetsApi->device_type2_action_on_snapshot_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type2_action_on_snapshot_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of Volume Collection. A 42 digit hexadecimal number. | 
 **nimble_update_snapshot_collections_state_input** | [**NimbleUpdateSnapshotCollectionsStateInput**](NimbleUpdateSnapshotCollectionsStateInput.md)|  | 

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

# **device_type2_action_on_volume_collection**
> TaskResponse device_type2_action_on_volume_collection(system_id, volume_collection_id, nimble_handover_volume_collections_input)

Perform handover action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}

Perform handover action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_handover_volume_collections_input import NimbleHandoverVolumeCollectionsInput
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_collection_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of Volume Collection. A 42 digit hexadecimal number.
    nimble_handover_volume_collections_input = dscc.NimbleHandoverVolumeCollectionsInput() # NimbleHandoverVolumeCollectionsInput | 

    try:
        # Perform handover action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}
        api_response = api_instance.device_type2_action_on_volume_collection(system_id, volume_collection_id, nimble_handover_volume_collections_input)
        print("The response of VolumeSetsApi->device_type2_action_on_volume_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type2_action_on_volume_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of Volume Collection. A 42 digit hexadecimal number. | 
 **nimble_handover_volume_collections_input** | [**NimbleHandoverVolumeCollectionsInput**](NimbleHandoverVolumeCollectionsInput.md)|  | 

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

# **device_type2_action_on_volume_collection_id**
> TaskResponse device_type2_action_on_volume_collection_id(system_id, volume_collection_id, nimble_demote_volume_collections_input)

Perform demote action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}

Perform demote action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_demote_volume_collections_input import NimbleDemoteVolumeCollectionsInput
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_collection_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of Volume Collection. A 42 digit hexadecimal number.
    nimble_demote_volume_collections_input = dscc.NimbleDemoteVolumeCollectionsInput() # NimbleDemoteVolumeCollectionsInput | 

    try:
        # Perform demote action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}
        api_response = api_instance.device_type2_action_on_volume_collection_id(system_id, volume_collection_id, nimble_demote_volume_collections_input)
        print("The response of VolumeSetsApi->device_type2_action_on_volume_collection_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type2_action_on_volume_collection_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of Volume Collection. A 42 digit hexadecimal number. | 
 **nimble_demote_volume_collections_input** | [**NimbleDemoteVolumeCollectionsInput**](NimbleDemoteVolumeCollectionsInput.md)|  | 

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

# **device_type2_actionon_volume_collection**
> TaskResponse device_type2_actionon_volume_collection(system_id, volume_collection_id)

Perform abort handover action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}

Perform abort handover action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}

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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_collection_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of Volume Collection. A 42 digit hexadecimal number.

    try:
        # Perform abort handover action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}
        api_response = api_instance.device_type2_actionon_volume_collection(system_id, volume_collection_id)
        print("The response of VolumeSetsApi->device_type2_actionon_volume_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type2_actionon_volume_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of Volume Collection. A 42 digit hexadecimal number. | 

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

# **device_type2_add_volumes_to_volume_collections**
> TaskResponse device_type2_add_volumes_to_volume_collections(system_id, volume_collection_id, nimble_add_volume_to_volume_collection_input)

Add volumes to Nimble / Alletra 6K volumes collection in system identified by {systemId}

Add volumes to Nimble / Alletra 6K volumes collection in system identified by {systemId

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_add_volume_to_volume_collection_input import NimbleAddVolumeToVolumeCollectionInput
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_collection_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | Identifier of volumeCollection. A 42 digit hexadecimal number.
    nimble_add_volume_to_volume_collection_input = dscc.NimbleAddVolumeToVolumeCollectionInput() # NimbleAddVolumeToVolumeCollectionInput | 

    try:
        # Add volumes to Nimble / Alletra 6K volumes collection in system identified by {systemId}
        api_response = api_instance.device_type2_add_volumes_to_volume_collections(system_id, volume_collection_id, nimble_add_volume_to_volume_collection_input)
        print("The response of VolumeSetsApi->device_type2_add_volumes_to_volume_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type2_add_volumes_to_volume_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of volumeCollection. A 42 digit hexadecimal number. | 
 **nimble_add_volume_to_volume_collection_input** | [**NimbleAddVolumeToVolumeCollectionInput**](NimbleAddVolumeToVolumeCollectionInput.md)|  | 

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

# **device_type2_create_snapshot_collections**
> TaskResponse device_type2_create_snapshot_collections(system_id, volume_collection_id, nimble_create_snapshot_collections_input)

Create Nimble / Alletra 6K snapshot collection in system identified by {systemId}

Create Nimble / Alletra 6K snapshot collection in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_create_snapshot_collections_input import NimbleCreateSnapshotCollectionsInput
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_collection_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of Volume Collection. A 42 digit hexadecimal number.
    nimble_create_snapshot_collections_input = dscc.NimbleCreateSnapshotCollectionsInput() # NimbleCreateSnapshotCollectionsInput | 

    try:
        # Create Nimble / Alletra 6K snapshot collection in system identified by {systemId}
        api_response = api_instance.device_type2_create_snapshot_collections(system_id, volume_collection_id, nimble_create_snapshot_collections_input)
        print("The response of VolumeSetsApi->device_type2_create_snapshot_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type2_create_snapshot_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of Volume Collection. A 42 digit hexadecimal number. | 
 **nimble_create_snapshot_collections_input** | [**NimbleCreateSnapshotCollectionsInput**](NimbleCreateSnapshotCollectionsInput.md)|  | 

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

# **device_type2_edit_volume_collection_by_id**
> TaskResponse device_type2_edit_volume_collection_by_id(system_id, volume_collection_id, nimble_edit_volume_collection_input)

Edit  details of Nimble / Alletra 6K Volume-collections identified by {volumeCollectionId}

Edit  details of Nimble / Alletra 6K Volume-collections identified by {volumeCollectionId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_edit_volume_collection_input import NimbleEditVolumeCollectionInput
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_collection_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | Identifier of volumeCollection. A 42 digit hexadecimal number.
    nimble_edit_volume_collection_input = dscc.NimbleEditVolumeCollectionInput() # NimbleEditVolumeCollectionInput | 

    try:
        # Edit  details of Nimble / Alletra 6K Volume-collections identified by {volumeCollectionId}
        api_response = api_instance.device_type2_edit_volume_collection_by_id(system_id, volume_collection_id, nimble_edit_volume_collection_input)
        print("The response of VolumeSetsApi->device_type2_edit_volume_collection_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type2_edit_volume_collection_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of volumeCollection. A 42 digit hexadecimal number. | 
 **nimble_edit_volume_collection_input** | [**NimbleEditVolumeCollectionInput**](NimbleEditVolumeCollectionInput.md)|  | 

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

# **device_type2_get_all_folders**
> NimbleFolderList device_type2_get_all_folders(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all folders details by Nimble / Alletra 6K

Get all folders details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_folder_list import NimbleFolderList
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter folders by Key. (optional)
    sort = 'name desc' # str | oData query to sort folders resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all folders details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_folders(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of VolumeSetsApi->device_type2_get_all_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type2_get_all_folders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter folders by Key. | [optional] 
 **sort** | **str**| oData query to sort folders resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleFolderList**](NimbleFolderList.md)

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

# **device_type2_get_all_volume_collections**
> NimbleVolumeCollectionList device_type2_get_all_volume_collections(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all volume-collections details by Nimble / Alletra 6K

Get all volume-collections details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_volume_collection_list import NimbleVolumeCollectionList
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter volume-collection by Key. (optional)
    sort = 'name desc' # str | oData query to sort volume-collection resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all volume-collections details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_volume_collections(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of VolumeSetsApi->device_type2_get_all_volume_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type2_get_all_volume_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter volume-collection by Key. | [optional] 
 **sort** | **str**| oData query to sort volume-collection resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleVolumeCollectionList**](NimbleVolumeCollectionList.md)

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

# **device_type2_get_snapshot_collections_by_id**
> NimbleSnapshotCollectionDetails device_type2_get_snapshot_collections_by_id(system_id, volume_collection_id, snapshot_collection_id, select=select)

Get details of snapshot collection of Nimble / Alletra 6K Volume collection identified by {volumeCollectionId} by {snapshotId}

Get details of snapshot collection of Nimble / Alletra 6K Volume collection identified by {volumeCollectionId} by {snapshotId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_snapshot_collection_details import NimbleSnapshotCollectionDetails
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_collection_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of Volume Collection. A 42 digit hexadecimal number.
    snapshot_collection_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of snapshot Collection. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of snapshot collection of Nimble / Alletra 6K Volume collection identified by {volumeCollectionId} by {snapshotId}
        api_response = api_instance.device_type2_get_snapshot_collections_by_id(system_id, volume_collection_id, snapshot_collection_id, select=select)
        print("The response of VolumeSetsApi->device_type2_get_snapshot_collections_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type2_get_snapshot_collections_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of Volume Collection. A 42 digit hexadecimal number. | 
 **snapshot_collection_id** | **str**| Identifier of snapshot Collection. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleSnapshotCollectionDetails**](NimbleSnapshotCollectionDetails.md)

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

# **device_type2_get_snapshots_by_volume_collection_id**
> NimbleSnapshotCollectionList device_type2_get_snapshots_by_volume_collection_id(system_id, volume_collection_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all snapshot collections' details of Nimble / Alletra 6K Volume collection identified by {volumeCollectionId}

Get all snapshot collections' details of Nimble / Alletra 6K Volume collection identified by {volumeCollectionId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_snapshot_collection_list import NimbleSnapshotCollectionList
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_collection_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of Volume Collection. A 42 digit hexadecimal number.
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter snapshot collections by Key. (optional)
    sort = 'name desc' # str | oData query to sort snapshot collections resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all snapshot collections' details of Nimble / Alletra 6K Volume collection identified by {volumeCollectionId}
        api_response = api_instance.device_type2_get_snapshots_by_volume_collection_id(system_id, volume_collection_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of VolumeSetsApi->device_type2_get_snapshots_by_volume_collection_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type2_get_snapshots_by_volume_collection_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of Volume Collection. A 42 digit hexadecimal number. | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter snapshot collections by Key. | [optional] 
 **sort** | **str**| oData query to sort snapshot collections resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleSnapshotCollectionList**](NimbleSnapshotCollectionList.md)

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

# **device_type2_get_volume_collection_by_id**
> NimbleVCollectionDetailsWithRequestUri device_type2_get_volume_collection_by_id(system_id, volume_collection_id, select=select)

Get details of Nimble / Alletra 6K volume-collections identified by {volumeCollectionId}

Get details of Nimble / Alletra 6K volume-collections identified by {volumeCollectionId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_v_collection_details_with_request_uri import NimbleVCollectionDetailsWithRequestUri
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_collection_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | Identifier of volumeCollection. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Nimble / Alletra 6K volume-collections identified by {volumeCollectionId}
        api_response = api_instance.device_type2_get_volume_collection_by_id(system_id, volume_collection_id, select=select)
        print("The response of VolumeSetsApi->device_type2_get_volume_collection_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type2_get_volume_collection_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of volumeCollection. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleVCollectionDetailsWithRequestUri**](NimbleVCollectionDetailsWithRequestUri.md)

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

# **device_type2_promote_action_on_volume_collection**
> TaskResponse device_type2_promote_action_on_volume_collection(system_id, volume_collection_id)

Perform promote action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}

Perform promote action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}

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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_collection_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of Volume Collection. A 42 digit hexadecimal number.

    try:
        # Perform promote action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}
        api_response = api_instance.device_type2_promote_action_on_volume_collection(system_id, volume_collection_id)
        print("The response of VolumeSetsApi->device_type2_promote_action_on_volume_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type2_promote_action_on_volume_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of Volume Collection. A 42 digit hexadecimal number. | 

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

# **device_type2_remove_snap_shot_collection**
> TaskResponse device_type2_remove_snap_shot_collection(system_id, volume_collection_id, remove_snapshot_collection_input)

Remove multiple snapshot collections identified by {volumeCollectionId} from Nimble / Alletra 6K

Remove multiple snapshot collections identified by {volumeCollectionId} from Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.remove_snapshot_collection_input import RemoveSnapshotCollectionInput
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_collection_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of Volume Collection. A 42 digit hexadecimal number.
    remove_snapshot_collection_input = dscc.RemoveSnapshotCollectionInput() # RemoveSnapshotCollectionInput | 

    try:
        # Remove multiple snapshot collections identified by {volumeCollectionId} from Nimble / Alletra 6K
        api_response = api_instance.device_type2_remove_snap_shot_collection(system_id, volume_collection_id, remove_snapshot_collection_input)
        print("The response of VolumeSetsApi->device_type2_remove_snap_shot_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type2_remove_snap_shot_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of Volume Collection. A 42 digit hexadecimal number. | 
 **remove_snapshot_collection_input** | [**RemoveSnapshotCollectionInput**](RemoveSnapshotCollectionInput.md)|  | 

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

# **device_type2_remove_volume_collection_by_id**
> TaskResponse device_type2_remove_volume_collection_by_id(system_id, volume_collection_id, force=force)

Remove Volume-collection identified by {volumeCollectionId} from Nimble / Alletra 6K

Remove Volume-collection identified by {volumeCollectionId} from Nimble / Alletra 6K

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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_collection_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of Volume Collection. A 42 digit hexadecimal number.
    force = true # bool | Forceful delete volume collection option. (optional)

    try:
        # Remove Volume-collection identified by {volumeCollectionId} from Nimble / Alletra 6K
        api_response = api_instance.device_type2_remove_volume_collection_by_id(system_id, volume_collection_id, force=force)
        print("The response of VolumeSetsApi->device_type2_remove_volume_collection_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type2_remove_volume_collection_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of Volume Collection. A 42 digit hexadecimal number. | 
 **force** | **bool**| Forceful delete volume collection option. | [optional] 

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

# **device_type2_remove_volumes_from_volume_collection**
> TaskResponse device_type2_remove_volumes_from_volume_collection(system_id, volume_collection_id, nimble_remove_volume_from_volume_collection_input)

Remove volumes from Nimble / Alletra 6K volumes collection in system identified by {systemId}

Remove volumes from Nimble / Alletra 6K volumes collection in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_remove_volume_from_volume_collection_input import NimbleRemoveVolumeFromVolumeCollectionInput
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_collection_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | Identifier of volumeCollection. A 42 digit hexadecimal number.
    nimble_remove_volume_from_volume_collection_input = dscc.NimbleRemoveVolumeFromVolumeCollectionInput() # NimbleRemoveVolumeFromVolumeCollectionInput | 

    try:
        # Remove volumes from Nimble / Alletra 6K volumes collection in system identified by {systemId}
        api_response = api_instance.device_type2_remove_volumes_from_volume_collection(system_id, volume_collection_id, nimble_remove_volume_from_volume_collection_input)
        print("The response of VolumeSetsApi->device_type2_remove_volumes_from_volume_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type2_remove_volumes_from_volume_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of volumeCollection. A 42 digit hexadecimal number. | 
 **nimble_remove_volume_from_volume_collection_input** | [**NimbleRemoveVolumeFromVolumeCollectionInput**](NimbleRemoveVolumeFromVolumeCollectionInput.md)|  | 

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

# **device_type2_volume_collection_create**
> TaskResponse device_type2_volume_collection_create(system_id, nimble_create_volume_collection_input)

Create Nimble / Alletra 6K volume collection in system identified by {systemId}

Create Nimble / Alletra 6K volume collection in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_create_volume_collection_input import NimbleCreateVolumeCollectionInput
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    nimble_create_volume_collection_input = dscc.NimbleCreateVolumeCollectionInput() # NimbleCreateVolumeCollectionInput | 

    try:
        # Create Nimble / Alletra 6K volume collection in system identified by {systemId}
        api_response = api_instance.device_type2_volume_collection_create(system_id, nimble_create_volume_collection_input)
        print("The response of VolumeSetsApi->device_type2_volume_collection_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type2_volume_collection_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_create_volume_collection_input** | [**NimbleCreateVolumeCollectionInput**](NimbleCreateVolumeCollectionInput.md)|  | 

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

# **device_type4_create_protection_policy**
> TaskResponse device_type4_create_protection_policy(id, system_id, device_type4_create_protection_policy_input_schema)

Add protection policy on application set identified by {id} for a storage system HPE Alletra Storage MP identified by {systemId}

Add protection policy on application set identified by {id} for a storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_create_protection_policy_input_schema import DeviceType4CreateProtectionPolicyInputSchema
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
    api_instance = dscc.VolumeSetsApi(api_client)
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the applicationset
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_create_protection_policy_input_schema = dscc.DeviceType4CreateProtectionPolicyInputSchema() # DeviceType4CreateProtectionPolicyInputSchema | 

    try:
        # Add protection policy on application set identified by {id} for a storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_create_protection_policy(id, system_id, device_type4_create_protection_policy_input_schema)
        print("The response of VolumeSetsApi->device_type4_create_protection_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4_create_protection_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the applicationset | 
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_create_protection_policy_input_schema** | [**DeviceType4CreateProtectionPolicyInputSchema**](DeviceType4CreateProtectionPolicyInputSchema.md)|  | 

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

# **device_type4_edit_protection_policies**
> TaskResponse device_type4_edit_protection_policies(id, system_id, device_type4_edit_protection_policy_input_schema)

Edit protection policy on application set identified by {id} for a storage system HPE Alletra Storage MP identified by {systemId}

Edit protection policy on application set identified by {id} for a storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_edit_protection_policy_input_schema import DeviceType4EditProtectionPolicyInputSchema
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
    api_instance = dscc.VolumeSetsApi(api_client)
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the applicationset
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_edit_protection_policy_input_schema = dscc.DeviceType4EditProtectionPolicyInputSchema() # DeviceType4EditProtectionPolicyInputSchema | 

    try:
        # Edit protection policy on application set identified by {id} for a storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_edit_protection_policies(id, system_id, device_type4_edit_protection_policy_input_schema)
        print("The response of VolumeSetsApi->device_type4_edit_protection_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4_edit_protection_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the applicationset | 
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_edit_protection_policy_input_schema** | [**DeviceType4EditProtectionPolicyInputSchema**](DeviceType4EditProtectionPolicyInputSchema.md)|  | 

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

# **device_type4_edit_proximity_settings**
> TaskResponse device_type4_edit_proximity_settings(system_id, id, device_type4_change_proximity_settings_input)

Change proximity settings of hosts where volume sets are exported identified by {id} and {systemId} from HPE Alletra Storage MP

Change proximity settings of hosts where volume sets are exported identified by {id} and {systemId} from HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_change_proximity_settings_input import DeviceType4ChangeProximitySettingsInput
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    device_type4_change_proximity_settings_input = dscc.DeviceType4ChangeProximitySettingsInput() # DeviceType4ChangeProximitySettingsInput | 

    try:
        # Change proximity settings of hosts where volume sets are exported identified by {id} and {systemId} from HPE Alletra Storage MP
        api_response = api_instance.device_type4_edit_proximity_settings(system_id, id, device_type4_change_proximity_settings_input)
        print("The response of VolumeSetsApi->device_type4_edit_proximity_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4_edit_proximity_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the applicationset | 
 **device_type4_change_proximity_settings_input** | [**DeviceType4ChangeProximitySettingsInput**](DeviceType4ChangeProximitySettingsInput.md)|  | 

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

# **device_type4_fix_protection_policy**
> TaskResponse device_type4_fix_protection_policy(id, system_id, device_type4_create_protection_policy_input_schema)

Fix protection policy configuration on application set identified by {id} for a storage system HPE Alletra Storage MP identified by {systemId}

Remedies issues caused in protection policy configuration on application set identified by {id} for a storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_create_protection_policy_input_schema import DeviceType4CreateProtectionPolicyInputSchema
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
    api_instance = dscc.VolumeSetsApi(api_client)
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the applicationset
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_create_protection_policy_input_schema = dscc.DeviceType4CreateProtectionPolicyInputSchema() # DeviceType4CreateProtectionPolicyInputSchema | 

    try:
        # Fix protection policy configuration on application set identified by {id} for a storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_fix_protection_policy(id, system_id, device_type4_create_protection_policy_input_schema)
        print("The response of VolumeSetsApi->device_type4_fix_protection_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4_fix_protection_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the applicationset | 
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_create_protection_policy_input_schema** | [**DeviceType4CreateProtectionPolicyInputSchema**](DeviceType4CreateProtectionPolicyInputSchema.md)|  | 

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

# **device_type4_get_protection_policies**
> DeviceType4ProtectionPoliciesList device_type4_get_protection_policies(id, system_id, select=select, filter=filter)

Get details of protection policies configured on application set identified by {id} created on HPE Alletra Storage MP identified by {systemId}

Get details of protection policies configured on application set identified by {id} created on HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_protection_policies_list import DeviceType4ProtectionPoliciesList
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
    api_instance = dscc.VolumeSetsApi(api_client)
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the applicationset
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    filter = 'uid eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter application-sets by Key. (optional)

    try:
        # Get details of protection policies configured on application set identified by {id} created on HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_get_protection_policies(id, system_id, select=select, filter=filter)
        print("The response of VolumeSetsApi->device_type4_get_protection_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4_get_protection_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the applicationset | 
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **filter** | **str**| Lucene query to filter application-sets by Key. | [optional] 

### Return type

[**DeviceType4ProtectionPoliciesList**](DeviceType4ProtectionPoliciesList.md)

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

# **device_type4_get_proximity_settings**
> DeviceType4VolumeSetProximitySettings device_type4_get_proximity_settings(id, system_id)

Get hosts and proximity details identified by application set {id} for HPE Alletra Storage MP identified by {systemId}

Get hosts and proximity details identified by application set {id} for HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_volume_set_proximity_settings import DeviceType4VolumeSetProximitySettings
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
    api_instance = dscc.VolumeSetsApi(api_client)
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the applicationset
    system_id = '7CE751P312' # str | systemId of the storage system

    try:
        # Get hosts and proximity details identified by application set {id} for HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_get_proximity_settings(id, system_id)
        print("The response of VolumeSetsApi->device_type4_get_proximity_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4_get_proximity_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the applicationset | 
 **system_id** | **str**| systemId of the storage system | 

### Return type

[**DeviceType4VolumeSetProximitySettings**](DeviceType4VolumeSetProximitySettings.md)

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

# **device_type4_get_replication_partner_volumes_by_app_set_id**
> DeviceType4ReplicationPartnerVolumesSummaryList device_type4_get_replication_partner_volumes_by_app_set_id(system_id, appset_id, replication_partner_id, limit=limit, offset=offset)

Get volume details of replication partners identified by {appsetId} and {replicationPartnerId} for HPE Alletra Storage MP

Get volume details of replication partners identified by {appsetId} and {replicationPartnerId} for HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_replication_partner_volumes_summary_list import DeviceType4ReplicationPartnerVolumesSummaryList
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    appset_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    replication_partner_id = 'aedec7d11d02f73611a6ff992c256bdb' # str | id of device-type1 replication partner
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)

    try:
        # Get volume details of replication partners identified by {appsetId} and {replicationPartnerId} for HPE Alletra Storage MP
        api_response = api_instance.device_type4_get_replication_partner_volumes_by_app_set_id(system_id, appset_id, replication_partner_id, limit=limit, offset=offset)
        print("The response of VolumeSetsApi->device_type4_get_replication_partner_volumes_by_app_set_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4_get_replication_partner_volumes_by_app_set_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **appset_id** | **str**| UID of the applicationset | 
 **replication_partner_id** | **str**| id of device-type1 replication partner | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 

### Return type

[**DeviceType4ReplicationPartnerVolumesSummaryList**](DeviceType4ReplicationPartnerVolumesSummaryList.md)

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

# **device_type4_get_replication_partners_by_app_set_id**
> DeviceType4ReplicationPartnersSummaryList device_type4_get_replication_partners_by_app_set_id(system_id, appset_id)

Get details of HPE Alletra Storage MP replication partners identified by {systemId} and {appsetId}

Get details of HPE Alletra Storage MP replication partners identified by {systemId} and {appsetId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_replication_partners_summary_list import DeviceType4ReplicationPartnersSummaryList
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    appset_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset

    try:
        # Get details of HPE Alletra Storage MP replication partners identified by {systemId} and {appsetId}
        api_response = api_instance.device_type4_get_replication_partners_by_app_set_id(system_id, appset_id)
        print("The response of VolumeSetsApi->device_type4_get_replication_partners_by_app_set_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4_get_replication_partners_by_app_set_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **appset_id** | **str**| UID of the applicationset | 

### Return type

[**DeviceType4ReplicationPartnersSummaryList**](DeviceType4ReplicationPartnersSummaryList.md)

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

# **device_type4_snapsets_get_by_id**
> DeviceType4SnapshotsetListSingle device_type4_snapsets_get_by_id(system_id, appset_id, snapset_id, select=select)

Get details of snapsets identified by {snapsetId} for Applicationset identified by {appsetId} for HPE Alletra Storage MP

Get details of snapset identified by {snapsetId} for Applicationset identified by {appsetId} for HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_snapshotset_list_single import DeviceType4SnapshotsetListSingle
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    appset_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    snapset_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | Identifier of snapset.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of snapsets identified by {snapsetId} for Applicationset identified by {appsetId} for HPE Alletra Storage MP
        api_response = api_instance.device_type4_snapsets_get_by_id(system_id, appset_id, snapset_id, select=select)
        print("The response of VolumeSetsApi->device_type4_snapsets_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4_snapsets_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **appset_id** | **str**| UID of the applicationset | 
 **snapset_id** | **str**| Identifier of snapset. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4SnapshotsetListSingle**](DeviceType4SnapshotsetListSingle.md)

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

# **device_type4_volume_set_capacity_statistics_get_by_id**
> DeviceType4ApplicationSetCapacityStats device_type4_volume_set_capacity_statistics_get_by_id(id, system_id, select=select)

Get capacity details for an applicationset identified by appsetUid

Get capacity details for an applicationset identified by appsetUid

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_application_set_capacity_stats import DeviceType4ApplicationSetCapacityStats
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
    api_instance = dscc.VolumeSetsApi(api_client)
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get capacity details for an applicationset identified by appsetUid
        api_response = api_instance.device_type4_volume_set_capacity_statistics_get_by_id(id, system_id, select=select)
        print("The response of VolumeSetsApi->device_type4_volume_set_capacity_statistics_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4_volume_set_capacity_statistics_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UID of the applicationset | 
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4ApplicationSetCapacityStats**](DeviceType4ApplicationSetCapacityStats.md)

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

# **device_type4_volume_set_export**
> TaskResponse device_type4_volume_set_export(system_id, appset_id, device_type4_export_app_set_post)

Export applicationset identified by {appsetId} from HPE Alletra Storage MP identified by {systemId}

Export applicationset identified by {appsetId} from HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_export_app_set_post import DeviceType4ExportAppSetPost
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    appset_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    device_type4_export_app_set_post = dscc.DeviceType4ExportAppSetPost() # DeviceType4ExportAppSetPost | 

    try:
        # Export applicationset identified by {appsetId} from HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_volume_set_export(system_id, appset_id, device_type4_export_app_set_post)
        print("The response of VolumeSetsApi->device_type4_volume_set_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4_volume_set_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **appset_id** | **str**| UID of the applicationset | 
 **device_type4_export_app_set_post** | [**DeviceType4ExportAppSetPost**](DeviceType4ExportAppSetPost.md)|  | 

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

# **device_type4_volume_set_snapshot_get_by_id**
> TaskResponse device_type4_volume_set_snapshot_get_by_id(system_id, appset_id, snapset_id, force=force)

Remove HPE Alletra Storage MP snapset in system identified by {snapsetId}

Remove HPE Alletra Storage MP snapset in system identified by {snapsetId}

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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    appset_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    snapset_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | Identifier of snapset.
    force = true # bool | Make snapset offline and remove. (optional)

    try:
        # Remove HPE Alletra Storage MP snapset in system identified by {snapsetId}
        api_response = api_instance.device_type4_volume_set_snapshot_get_by_id(system_id, appset_id, snapset_id, force=force)
        print("The response of VolumeSetsApi->device_type4_volume_set_snapshot_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4_volume_set_snapshot_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **appset_id** | **str**| UID of the applicationset | 
 **snapset_id** | **str**| Identifier of snapset. | 
 **force** | **bool**| Make snapset offline and remove. | [optional] 

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

# **device_type4_volume_set_snapshots_list**
> DeviceType4SnapshotSetsSummaryList device_type4_volume_set_snapshots_list(system_id, id, limit=limit, offset=offset, select=select, filter=filter, sort=sort)

Get snapshot details of volume sets identified by {id} for HPE Alletra Storage MP

Get snapshot details of volume sets identified by {id} for HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_snapshot_sets_summary_list import DeviceType4SnapshotSetsSummaryList
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    filter = 'name eq array1 and wwn eq 2FF70002AC018D94' # str | oData query to filter by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort by Key. (optional)

    try:
        # Get snapshot details of volume sets identified by {id} for HPE Alletra Storage MP
        api_response = api_instance.device_type4_volume_set_snapshots_list(system_id, id, limit=limit, offset=offset, select=select, filter=filter, sort=sort)
        print("The response of VolumeSetsApi->device_type4_volume_set_snapshots_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4_volume_set_snapshots_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the applicationset | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| oData query to sort by Key. | [optional] 

### Return type

[**DeviceType4SnapshotSetsSummaryList**](DeviceType4SnapshotSetsSummaryList.md)

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

# **device_type4_volume_set_unexport**
> TaskResponse device_type4_volume_set_unexport(system_id, appset_id, device_type4_un_export_app_set_post)

Unexport applicationset identified by {appsetId} from HPE Alletra Storage MP identified by {systemId}

Unexport applicationset identified by {appsetId} from HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_un_export_app_set_post import DeviceType4UnExportAppSetPost
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    appset_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    device_type4_un_export_app_set_post = dscc.DeviceType4UnExportAppSetPost() # DeviceType4UnExportAppSetPost | 

    try:
        # Unexport applicationset identified by {appsetId} from HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_volume_set_unexport(system_id, appset_id, device_type4_un_export_app_set_post)
        print("The response of VolumeSetsApi->device_type4_volume_set_unexport:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4_volume_set_unexport: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **appset_id** | **str**| UID of the applicationset | 
 **device_type4_un_export_app_set_post** | [**DeviceType4UnExportAppSetPost**](DeviceType4UnExportAppSetPost.md)|  | 

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

# **device_type4_volume_set_volumes_list**
> DeviceType4VolumesList device_type4_volume_set_volumes_list(appset_id, system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get volumes for an applicationset identified by appsetUid

Get volumes for an applicationset identified by appsetUid

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_volumes_list import DeviceType4VolumesList
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
    api_instance = dscc.VolumeSetsApi(api_client)
    appset_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq array1 and wwn eq 2FF70002AC018D94' # str | oData query to filter by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get volumes for an applicationset identified by appsetUid
        api_response = api_instance.device_type4_volume_set_volumes_list(appset_id, system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of VolumeSetsApi->device_type4_volume_set_volumes_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4_volume_set_volumes_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appset_id** | **str**| UID of the applicationset | 
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| oData query to sort by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4VolumesList**](DeviceType4VolumesList.md)

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

# **device_type4_volume_sets_create**
> TaskResponse device_type4_volume_sets_create(system_id, device_type4_create_app_set_input)

Create Application Set for a storage system HPE Alletra Storage MP

Create Application Set for a storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_create_app_set_input import DeviceType4CreateAppSetInput
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_create_app_set_input = dscc.DeviceType4CreateAppSetInput() # DeviceType4CreateAppSetInput | 

    try:
        # Create Application Set for a storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_volume_sets_create(system_id, device_type4_create_app_set_input)
        print("The response of VolumeSetsApi->device_type4_volume_sets_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4_volume_sets_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_create_app_set_input** | [**DeviceType4CreateAppSetInput**](DeviceType4CreateAppSetInput.md)|  | 

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

# **device_type4_volume_sets_delete_by_id**
> TaskResponse device_type4_volume_sets_delete_by_id(system_id, id)

Remove applicationset identified by {id} from HPE Alletra Storage MP identified by {systemId}

Remove applicationset identified by {id} from HPE Alletra Storage MP identified by {systemId}

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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset

    try:
        # Remove applicationset identified by {id} from HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_volume_sets_delete_by_id(system_id, id)
        print("The response of VolumeSetsApi->device_type4_volume_sets_delete_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4_volume_sets_delete_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the applicationset | 

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

# **device_type4_volume_sets_edit_by_id**
> TaskResponse device_type4_volume_sets_edit_by_id(system_id, id, device_type4_volume_set_put)

Edit applicationset identified by {id} from HPE Alletra Storage MP identified by {systemId}

Edit applicationset identified by {id} from HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_volume_set_put import DeviceType4VolumeSetPut
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    device_type4_volume_set_put = dscc.DeviceType4VolumeSetPut() # DeviceType4VolumeSetPut | 

    try:
        # Edit applicationset identified by {id} from HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_volume_sets_edit_by_id(system_id, id, device_type4_volume_set_put)
        print("The response of VolumeSetsApi->device_type4_volume_sets_edit_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4_volume_sets_edit_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the applicationset | 
 **device_type4_volume_set_put** | [**DeviceType4VolumeSetPut**](DeviceType4VolumeSetPut.md)|  | 

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

# **device_type4_volume_sets_get_by_id**
> DeviceType4ApplicationSetDetails device_type4_volume_sets_get_by_id(id, system_id, select=select)

Get applicationset details for an applicationset identified by appsetUid

Get applicationset details for an applicationset identified by appsetUid

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_application_set_details import DeviceType4ApplicationSetDetails
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
    api_instance = dscc.VolumeSetsApi(api_client)
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    system_id = '7CE751P312' # str | systemId of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get applicationset details for an applicationset identified by appsetUid
        api_response = api_instance.device_type4_volume_sets_get_by_id(id, system_id, select=select)
        print("The response of VolumeSetsApi->device_type4_volume_sets_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4_volume_sets_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UID of the applicationset | 
 **system_id** | **str**| systemId of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4ApplicationSetDetails**](DeviceType4ApplicationSetDetails.md)

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

# **device_type4_volume_sets_list**
> DeviceType4ApplicationSetsList device_type4_volume_sets_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all applicationset details for HPE Alletra Storage MP

Get all applicationset details for HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_application_sets_list import DeviceType4ApplicationSetsList
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'uid eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter application-sets by Key. (optional)
    sort = 'name desc' # str | Lucene query to sort application-sets by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all applicationset details for HPE Alletra Storage MP
        api_response = api_instance.device_type4_volume_sets_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of VolumeSetsApi->device_type4_volume_sets_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4_volume_sets_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter application-sets by Key. | [optional] 
 **sort** | **str**| Lucene query to sort application-sets by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4ApplicationSetsList**](DeviceType4ApplicationSetsList.md)

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

# **device_type4_volume_sets_snapshot_create**
> TaskResponse device_type4_volume_sets_snapshot_create(system_id, id, device_type4_appset_post)

Create snapshot for application set identified by {id}

Create snapshot for application set identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_appset_post import DeviceType4AppsetPost
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | UID of the applicationset
    device_type4_appset_post = dscc.DeviceType4AppsetPost() # DeviceType4AppsetPost | 

    try:
        # Create snapshot for application set identified by {id}
        api_response = api_instance.device_type4_volume_sets_snapshot_create(system_id, id, device_type4_appset_post)
        print("The response of VolumeSetsApi->device_type4_volume_sets_snapshot_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4_volume_sets_snapshot_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of the applicationset | 
 **device_type4_appset_post** | [**DeviceType4AppsetPost**](DeviceType4AppsetPost.md)|  | 

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

# **device_type4action_on_volume_sets**
> TaskResponse device_type4action_on_volume_sets(system_id, id, device_type4_remote_protection_actions_input)

Actions on volume set identified by {id} and {systemId} from HPE Alletra Storage MP

Actions on volume set identified by {id} and {systemId} from HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_remote_protection_actions_input import DeviceType4RemoteProtectionActionsInput
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the applicationset
    device_type4_remote_protection_actions_input = dscc.DeviceType4RemoteProtectionActionsInput() # DeviceType4RemoteProtectionActionsInput | 

    try:
        # Actions on volume set identified by {id} and {systemId} from HPE Alletra Storage MP
        api_response = api_instance.device_type4action_on_volume_sets(system_id, id, device_type4_remote_protection_actions_input)
        print("The response of VolumeSetsApi->device_type4action_on_volume_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4action_on_volume_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| ID of the applicationset | 
 **device_type4_remote_protection_actions_input** | [**DeviceType4RemoteProtectionActionsInput**](DeviceType4RemoteProtectionActionsInput.md)|  | 

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

# **device_type4get_supported_protection_types**
> DeviceType4SupportedProtectionTypes device_type4get_supported_protection_types(id, system_id)

Get supported protection types for application set identified by {id} on storage system HPE Alletra Storage MP identified by {systemId}

Get supported protection types for application set identified by {id} on storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_supported_protection_types import DeviceType4SupportedProtectionTypes
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
    api_instance = dscc.VolumeSetsApi(api_client)
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the applicationset
    system_id = '7CE751P312' # str | systemId of the storage system

    try:
        # Get supported protection types for application set identified by {id} on storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4get_supported_protection_types(id, system_id)
        print("The response of VolumeSetsApi->device_type4get_supported_protection_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4get_supported_protection_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the applicationset | 
 **system_id** | **str**| systemId of the storage system | 

### Return type

[**DeviceType4SupportedProtectionTypes**](DeviceType4SupportedProtectionTypes.md)

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

# **device_type4remove_protection_policies**
> TaskResponse device_type4remove_protection_policies(id, system_id, device_type4_remove_protection_policies_input_schema)

Remove protection policy on application set identified by {id} for a storage system HPE Alletra Storage MP identified by {systemId}

Remove protection policy on application set identified by {id} for a storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_remove_protection_policies_input_schema import DeviceType4RemoveProtectionPoliciesInputSchema
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
    api_instance = dscc.VolumeSetsApi(api_client)
    id = 'e9d353bf98fc1a6bdb90b824e3ca14b5' # str | ID of the applicationset
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_remove_protection_policies_input_schema = dscc.DeviceType4RemoveProtectionPoliciesInputSchema() # DeviceType4RemoveProtectionPoliciesInputSchema | 

    try:
        # Remove protection policy on application set identified by {id} for a storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4remove_protection_policies(id, system_id, device_type4_remove_protection_policies_input_schema)
        print("The response of VolumeSetsApi->device_type4remove_protection_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->device_type4remove_protection_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the applicationset | 
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_remove_protection_policies_input_schema** | [**DeviceType4RemoveProtectionPoliciesInputSchema**](DeviceType4RemoveProtectionPoliciesInputSchema.md)|  | 

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

# **volumeset_get_by_id**
> FleetVolumeSetDetails volumeset_get_by_id(id, select=select)

Get volume-set identified by id

Get volume-set identified by id

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.fleet_volume_set_details import FleetVolumeSetDetails
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
    api_instance = dscc.VolumeSetsApi(api_client)
    id = 'fd3244ef7f1ab8bd16500c7a41bdf8f8' # str | UID of Volume Set
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get volume-set identified by id
        api_response = api_instance.volumeset_get_by_id(id, select=select)
        print("The response of VolumeSetsApi->volumeset_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->volumeset_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UID of Volume Set | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**FleetVolumeSetDetails**](FleetVolumeSetDetails.md)

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
**404** | Pool object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volumeset_get_byvolumeset_id**
> FleetVolumeSetList volumeset_get_byvolumeset_id(id, select=select, limit=limit, offset=offset, filter=filter, sort=sort)

Get volumes identified by volume set id

Get volumes  identified by volume set id

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.fleet_volume_set_list import FleetVolumeSetList
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
    api_instance = dscc.VolumeSetsApi(api_client)
    id = 'fd3244ef7f1ab8bd16500c7a41bdf8f8' # str | UID of Volume Set
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq array1 and wwn eq 2FF70002AC018D94' # str | oData query to filter by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort by Key. (optional)

    try:
        # Get volumes identified by volume set id
        api_response = api_instance.volumeset_get_byvolumeset_id(id, select=select, limit=limit, offset=offset, filter=filter, sort=sort)
        print("The response of VolumeSetsApi->volumeset_get_byvolumeset_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->volumeset_get_byvolumeset_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UID of Volume Set | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| oData query to sort by Key. | [optional] 

### Return type

[**FleetVolumeSetList**](FleetVolumeSetList.md)

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
**404** | Pool object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volumeset_list**
> FleetVolumeSetList volumeset_list(limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all volume-sets

Get all volume sets

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.fleet_volume_set_list import FleetVolumeSetList
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
    api_instance = dscc.VolumeSetsApi(api_client)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq volset and systemId eq 7CE751P312' # str | oData query to filter by Key. (optional)
    sort = 'systemId desc' # str | oData query to sort by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all volume-sets
        api_response = api_instance.volumeset_list(limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of VolumeSetsApi->volumeset_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->volumeset_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| oData query to sort by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**FleetVolumeSetList**](FleetVolumeSetList.md)

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
**404** | Pool object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volumeset_list_for_system_by_system_id**
> FleetVolumeSetList volumeset_list_for_system_by_system_id(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all volume-sets for a systemId

Get all volume sets for a systemId

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.fleet_volume_set_list import FleetVolumeSetList
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq volset and systemId eq 7CE751P312' # str | oData query to filter by Key. (optional)
    sort = 'systemId desc' # str | oData query to sort by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all volume-sets for a systemId
        api_response = api_instance.volumeset_list_for_system_by_system_id(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of VolumeSetsApi->volumeset_list_for_system_by_system_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->volumeset_list_for_system_by_system_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| oData query to sort by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**FleetVolumeSetList**](FleetVolumeSetList.md)

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
**404** | Pool object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volumeset_system_get_by_id**
> FleetSystemVolumeset volumeset_system_get_by_id(system_id, id, select=select)

Get volume-set identified by id

Get volume-set identified by id

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.fleet_system_volumeset import FleetSystemVolumeset
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
    api_instance = dscc.VolumeSetsApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'fd3244ef7f1ab8bd16500c7a41bdf8f8' # str | UID of Volume Set
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get volume-set identified by id
        api_response = api_instance.volumeset_system_get_by_id(system_id, id, select=select)
        print("The response of VolumeSetsApi->volumeset_system_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeSetsApi->volumeset_system_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID of Volume Set | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**FleetSystemVolumeset**](FleetSystemVolumeset.md)

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
**404** | Pool object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

