# dscc.VolumesApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type1_get_clones**](VolumesApi.md#device_type1_get_clones) | **GET** /api/v1/storage-systems/device-type1/{systemId}/volumes/{volumeId}/clones | Get the details of the clone volumes associated with a base volume identified by {volumeId} for Primera / Alletra 9K systems.
[**device_type1_get_snapshot_vluns_by_id**](VolumesApi.md#device_type1_get_snapshot_vluns_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/snapshots/{snapshotId}/vluns/{id} | Get details of vlun identified by {id} for Snapshot identified by {snapshotId} for Primera / Alletra 9K
[**device_type1_get_snapshot_vluns_list**](VolumesApi.md#device_type1_get_snapshot_vluns_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/snapshots/{snapshotId}/vluns | Get details of vluns for Snapshot identified by {snapshotId} for Primera / Alletra 9K
[**device_type1_get_volumes_performance_history**](VolumesApi.md#device_type1_get_volumes_performance_history) | **GET** /api/v1/storage-systems/device-type1/{systemId}/volumes-performance | Get performance history of Primera / Alletra 9K Volumes
[**device_type1_promote_clone_volume**](VolumesApi.md#device_type1_promote_clone_volume) | **POST** /api/v1/storage-systems/device-type1/{systemId}/volumes/{volumeId}/clones/{cloneId}/promote | Promote a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_promote_snapshot**](VolumesApi.md#device_type1_promote_snapshot) | **POST** /api/v1/storage-systems/device-type1/{systemId}/volumes/{volumeId}/snapshots/{snapshotId} | Promote a snapshot identified by {snapshotId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_resync_clone_volume**](VolumesApi.md#device_type1_resync_clone_volume) | **POST** /api/v1/storage-systems/device-type1/{systemId}/volumes/{volumeId}/clones/{cloneId}/resync | Resynchronize a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_snapshots_get_by_id**](VolumesApi.md#device_type1_snapshots_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/volumes/{volumeId}/snapshots/{snapshotId} | Get details of snapshot identified by {snapshotId} for Volume identified by {volumeId} for Primera / Alletra 9K
[**device_type1_vlun_export**](VolumesApi.md#device_type1_vlun_export) | **POST** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id}/export | Export vlun for volume identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type1_vlun_export_for_snapshot**](VolumesApi.md#device_type1_vlun_export_for_snapshot) | **POST** /api/v1/storage-systems/device-type1/{systemId}/snapshots/{snapshotId}/export | Export vlun for snapshot identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type1_vlun_unexport**](VolumesApi.md#device_type1_vlun_unexport) | **POST** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id}/un-export | Unexport vlun for volume identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type1_vlun_unexport_for_snapshot**](VolumesApi.md#device_type1_vlun_unexport_for_snapshot) | **POST** /api/v1/storage-systems/device-type1/{systemId}/snapshots/{snapshotId}/un-export | Unexport vlun for snapshot identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type1_vluns_get_by_id**](VolumesApi.md#device_type1_vluns_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/volumes/{volumeId}/vluns/{id} | Get details of vlun identified by {id} for Volume identified by {volumeId} for Primera / Alletra 9K
[**device_type1_vluns_list**](VolumesApi.md#device_type1_vluns_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id}/vluns | Get details of vluns for Volume identified by {volumeId} for Primera / Alletra 9K
[**device_type1_volume_capacity_history_get_by_id**](VolumesApi.md#device_type1_volume_capacity_history_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id}/capacity-history | Get volume capacity trend data of Primera / Alletra 9K Volume identified by {id}
[**device_type1_volume_get_by_id**](VolumesApi.md#device_type1_volume_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id} | Get details of Primera / Alletra 9K Volume identified by {id}
[**device_type1_volume_performance_history_get_by_id**](VolumesApi.md#device_type1_volume_performance_history_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id}/performance-history | Get performance trend data of Primera / Alletra 9K Volume identified by {id}
[**device_type1_volume_performance_statistics_get_by_id**](VolumesApi.md#device_type1_volume_performance_statistics_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id}/performance-statistics | Get performance statistics of Primera / Alletra 9K Volume identified by {id}
[**device_type1_volume_snapshots_list**](VolumesApi.md#device_type1_volume_snapshots_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id}/snapshots | Get snapshot details of volume identified by {id} for Primera / Alletra 9K
[**device_type1_volumes_list**](VolumesApi.md#device_type1_volumes_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/volumes | Get all volumes details for Primera / Alletra 9K
[**device_type2_access_control_record_create**](VolumesApi.md#device_type2_access_control_record_create) | **POST** /api/v1/storage-systems/device-type2/{systemId}/access-control-records | Create Nimble / Alletra 6K access control record in system identified by {systemId}
[**device_type2_clone_volume_by_id**](VolumesApi.md#device_type2_clone_volume_by_id) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/clone | Create Nimble / Alletra 6K clone volume identified by {volumeId}.
[**device_type2_delete_snapshot_access_by_id**](VolumesApi.md#device_type2_delete_snapshot_access_by_id) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/snapshots/{snapshotId}/un-export | Delete access for snapshot identified by {snapshotId} from Nimble / Alletra 6K identified by {systemId}
[**device_type2_delete_volume_access_by_id**](VolumesApi.md#device_type2_delete_volume_access_by_id) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/un-export | Delete access for volume identified by {volumeId} from Nimble / Alletra 6K identified by {systemId}
[**device_type2_edit_access_control_record_by_id**](VolumesApi.md#device_type2_edit_access_control_record_by_id) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/access-control-records/{accessControlRecordId} | Edit access-control-record identified by {accessControlRecordId} for Nimble / Alletra 6K
[**device_type2_edit_snapshot_by_id**](VolumesApi.md#device_type2_edit_snapshot_by_id) | **POST** /api/v1/storage-systems/device-type2/{systemId}/snapshots/actions/update | Edit Multiple Nimble / Alletra 6K snapshots in system identified by {systemId}
[**device_type2_edit_volume_by_id**](VolumesApi.md#device_type2_edit_volume_by_id) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId} | Edit  details of Nimble / Alletra 6K Volume identified by {volumeId}
[**device_type2_get_access_control_record_by_id**](VolumesApi.md#device_type2_get_access_control_record_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/access-control-records/{accessControlRecordId} | Get details of Nimble / Alletra 6K access-control-records identified by {accessControlRecordId}
[**device_type2_get_all_access_control_records**](VolumesApi.md#device_type2_get_all_access_control_records) | **GET** /api/v1/storage-systems/device-type2/{systemId}/access-control-records | Get all access-control-records details by Nimble / Alletra 6K
[**device_type2_get_all_snapshots_by_volume_id**](VolumesApi.md#device_type2_get_all_snapshots_by_volume_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/snapshots | Get all snapshots&#39; details of Nimble / Alletra 6K Volume identified by {volumeId}
[**device_type2_get_all_volumes**](VolumesApi.md#device_type2_get_all_volumes) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volumes | Get all volumes details for Nimble / Alletra 6K
[**device_type2_get_snapshot_by_id**](VolumesApi.md#device_type2_get_snapshot_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/snapshots/{snapshotId} | Get details of snapshot of Nimble / Alletra 6K Volume identified by {volumeId} by {snapshotId}
[**device_type2_get_volume_by_id**](VolumesApi.md#device_type2_get_volume_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId} | Get details of Nimble / Alletra 6K Volume identified by {volumeId}
[**device_type2_get_volume_capacity_history**](VolumesApi.md#device_type2_get_volume_capacity_history) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/capacity-history | Get volume capacity trend data of Nimble / Alletra 6K Volume identified by {volumeId}
[**device_type2_get_volume_performance_history**](VolumesApi.md#device_type2_get_volume_performance_history) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/performance-history | Get performance trend data of Nimble / Alletra 6K Volume identified by {id}
[**device_type2_get_volume_performance_statistics**](VolumesApi.md#device_type2_get_volume_performance_statistics) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/performance-statistics | Get performance statistics of Nimble / Alletra 6K Volume identified by {volumeId}
[**device_type2_get_volumes_performance_history**](VolumesApi.md#device_type2_get_volumes_performance_history) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volumes-performance | Get performance history of Nimble / Alletra 6K Volumes
[**device_type2_move_volume**](VolumesApi.md#device_type2_move_volume) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/actions/move | Move Nimble / Alletra 6K volume identified by {volumeId} to another pool.
[**device_type2_provisioning_review**](VolumesApi.md#device_type2_provisioning_review) | **POST** /api/v1/storage-systems/device-type2/{systemId}/provisioning-review | Provisioning review for a storage system Nimble / Alletra 6K
[**device_type2_provisioning_worklow**](VolumesApi.md#device_type2_provisioning_worklow) | **POST** /api/v1/storage-systems/device-type2/{systemId}/provisioning | Create provisioning workflow for a Nimble / Alletra 6K storage system identified by {systemId}
[**device_type2_remove_access_control_record_by_id**](VolumesApi.md#device_type2_remove_access_control_record_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/access-control-records/{accessControlRecordId} | Remove access-control-record identified by {accessControlRecordId} from Nimble / Alletra 6K
[**device_type2_remove_snapshot_by_id**](VolumesApi.md#device_type2_remove_snapshot_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/snapshots/{snapshotId} | Remove Nimble / Alletra 6K snapshot in system identified by {snapshotId}
[**device_type2_remove_volume_by_id**](VolumesApi.md#device_type2_remove_volume_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId} | Remove volume identified by {volumeId} from Nimble / Alletra 6K
[**device_type2_restore_volume_by_id**](VolumesApi.md#device_type2_restore_volume_by_id) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/actions/restore | Restore Nimble / Alletra 6K volume identified by {volumeId} from a previous snapshot.
[**device_type2_snapshot_create**](VolumesApi.md#device_type2_snapshot_create) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/snapshots | Create Nimble / Alletra 6K snapshot in system identified by {systemId}
[**device_type2_snapshot_export**](VolumesApi.md#device_type2_snapshot_export) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/snapshots/{snapshotId}/export | Configure access for snapshot identified by {snapshotId} from Nimble / Alletra 6K identified by {systemId}
[**device_type2_volumes_create**](VolumesApi.md#device_type2_volumes_create) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volumes | Create Nimble / Alletra 6K volume in system identified by {systemId}
[**device_type2_volumes_export**](VolumesApi.md#device_type2_volumes_export) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/export | Configure access for volume identified by {volumeId} from Nimble / Alletra 6K identified by {systemId}
[**device_type4_get_clones**](VolumesApi.md#device_type4_get_clones) | **GET** /api/v1/storage-systems/device-type4/{systemId}/volumes/{volumeId}/clones | Get the details of the clone volumes associated with a base volume identified by {volumeId} for HPE Alletra Storage MP systems.
[**device_type4_get_performance_drifts**](VolumesApi.md#device_type4_get_performance_drifts) | **GET** /api/v1/storage-systems/device-type4/{systemId}/volumes/{volumeId}/insights/performance-drifts | Get latency drifts of a volume for a give duration
[**device_type4_get_performance_histogram**](VolumesApi.md#device_type4_get_performance_histogram) | **GET** /api/v1/storage-systems/device-type4/{systemId}/volumes/{id}/performance-histogram | Get histogram buckets distribution of I/Os of a volume for a given duration.
[**device_type4_get_snapshot_vluns_list**](VolumesApi.md#device_type4_get_snapshot_vluns_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/snapshots/{snapshotId}/vluns | Get details of vluns for Snapshot identified by {snapshotId} for HPE Alletra Storage MP
[**device_type4_get_volume_latency_annotations**](VolumesApi.md#device_type4_get_volume_latency_annotations) | **GET** /api/v1/storage-systems/device-type4/{systemId}/volumes/{volumeId}/insights/latency-annotations | Get volume latency annotations for device-type4
[**device_type4_get_volumes_performance_history**](VolumesApi.md#device_type4_get_volumes_performance_history) | **GET** /api/v1/storage-systems/device-type4/{systemId}/volumes-performance | Get performance history of Volumes on storage system identified by {systemid}
[**device_type4_getsnapshot_vluns_by_id**](VolumesApi.md#device_type4_getsnapshot_vluns_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/snapshots/{snapshotId}/vluns/{id} | Get details of vlun identified by {id} for Snapshot identified by {snapshotId} for HPE Alletra Storage MP
[**device_type4_promote_clone_volume**](VolumesApi.md#device_type4_promote_clone_volume) | **POST** /api/v1/storage-systems/device-type4/{systemId}/volumes/{volumeId}/clones/{cloneId}/promote | Promote a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system HPE Alletra Storage MP identified by {systemId}
[**device_type4_promote_snapshot**](VolumesApi.md#device_type4_promote_snapshot) | **POST** /api/v1/storage-systems/device-type4/{systemId}/volumes/{volumeId}/snapshots/{snapshotId} | Promote a snapshot identified by {snapshotId} of a volume identified by {volumeId} on storage system HPE Alletra Storage MP identified by {systemId}
[**device_type4_resync_clone_volume**](VolumesApi.md#device_type4_resync_clone_volume) | **POST** /api/v1/storage-systems/device-type4/{systemId}/volumes/{volumeId}/clones/{cloneId}/resync | Resynchronize a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system HPE Alletra Storage MP identified by {systemId}
[**device_type4_snapshot_clone_create**](VolumesApi.md#device_type4_snapshot_clone_create) | **POST** /api/v1/storage-systems/device-type4/{systemId}/snapshots/{snapshotId}/clone | Create a clone of a snapshot identified by {snapshotId} for HPE Alletra Storage MP systems.
[**device_type4_snapshots_get_by_id**](VolumesApi.md#device_type4_snapshots_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/volumes/{volumeId}/snapshots/{snapshotId} | Get details of snapshot identified by {snapshotId} for Volume identified by {volumeId} for HPE Alletra Storage MP
[**device_type4_vlun_export**](VolumesApi.md#device_type4_vlun_export) | **POST** /api/v1/storage-systems/device-type4/{systemId}/volumes/{id}/export | Export vlun for volume identified by {id} from HPE Alletra Storage MP identified by {systemId}
[**device_type4_vlun_export_for_snapshot**](VolumesApi.md#device_type4_vlun_export_for_snapshot) | **POST** /api/v1/storage-systems/device-type4/{systemId}/snapshots/{snapshotId}/export | Export vlun for snapshot identified by {id} from HPE Alletra Storage MP identified by {systemId}
[**device_type4_vlun_unexport**](VolumesApi.md#device_type4_vlun_unexport) | **POST** /api/v1/storage-systems/device-type4/{systemId}/volumes/{id}/un-export | Unexport vlun for volume identified by {id} from HPE Alletra Storage MP identified by {systemId}
[**device_type4_vlun_unexport_for_snapshot**](VolumesApi.md#device_type4_vlun_unexport_for_snapshot) | **POST** /api/v1/storage-systems/device-type4/{systemId}/snapshots/{snapshotId}/un-export | Unexport vlun for snapshot identified by {id} from HPE Alletra Storage MP identified by {systemId}
[**device_type4_vluns_delete**](VolumesApi.md#device_type4_vluns_delete) | **DELETE** /api/v1/storage-systems/device-type4/{systemId}/volumes/{volumeId}/vluns/{id} | Remove vlun idenfied by {id} form volume identified by {volumeId} from HPE Alletra Storage MP
[**device_type4_vluns_get_by_id**](VolumesApi.md#device_type4_vluns_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/volumes/{volumeId}/vluns/{id} | Get details of vlun identified by {id} for Volume identified by {volumeId} for HPE Alletra Storage MP
[**device_type4_vluns_list**](VolumesApi.md#device_type4_vluns_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/volumes/{id}/vluns | Get details of vluns for Volume identified by {volumeId} for HPE Alletra Storage MP
[**device_type4_volume_capacity_history_get_by_id**](VolumesApi.md#device_type4_volume_capacity_history_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/volumes/{id}/capacity-history | Get volume capacity trend data of HPE Alletra Storage MP Volume identified by {id}
[**device_type4_volume_clone_create**](VolumesApi.md#device_type4_volume_clone_create) | **POST** /api/v1/storage-systems/device-type4/{systemId}/volumes/{id}/clone | Create a clone volume identified by {id} for HPE Alletra Storage MP systems.
[**device_type4_volume_create**](VolumesApi.md#device_type4_volume_create) | **POST** /api/v1/storage-systems/device-type4/{systemId}/volumes | Create volume for a storage system HPE Alletra Storage MP
[**device_type4_volume_delete**](VolumesApi.md#device_type4_volume_delete) | **DELETE** /api/v1/storage-systems/device-type4/{systemId}/volumes/{id} | Remove volume identified by {volumeId} from HPE Alletra Storage MP
[**device_type4_volume_edit**](VolumesApi.md#device_type4_volume_edit) | **PUT** /api/v1/storage-systems/device-type4/{systemId}/volumes/{id} | Edit volume identified by {volumeId} from HPE Alletra Storage MP
[**device_type4_volume_get_by_id**](VolumesApi.md#device_type4_volume_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/volumes/{id} | Get details of HPE Alletra Storage MP Volume identified by {id}
[**device_type4_volume_performance_history_get_by_id**](VolumesApi.md#device_type4_volume_performance_history_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/volumes/{id}/performance-history | Get performance trend data of HPE Alletra Storage MP Volume identified by {id}
[**device_type4_volume_performance_statistics_get_by_id**](VolumesApi.md#device_type4_volume_performance_statistics_get_by_id) | **GET** /api/v1/storage-systems/device-type4/{systemId}/volumes/{id}/performance-statistics | Get performance statistics of HPE Alletra Storage MP Volume identified by {id}
[**device_type4_volume_snapshot_create**](VolumesApi.md#device_type4_volume_snapshot_create) | **POST** /api/v1/storage-systems/device-type4/{systemId}/volumes/{id}/snapshots | Create snapshot for volumes identified by {id}
[**device_type4_volume_snapshot_get_by_id**](VolumesApi.md#device_type4_volume_snapshot_get_by_id) | **DELETE** /api/v1/storage-systems/device-type4/{systemId}/volumes/{volumeId}/snapshots/{snapshotId} | Remove HPE Alletra Storage MP snapshot in system identified by {snapshotId}
[**device_type4_volume_snapshots_list**](VolumesApi.md#device_type4_volume_snapshots_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/volumes/{id}/snapshots | Get snapshot details of volume identified by {id} for HPE Alletra Storage MP
[**device_type4_volumes_list**](VolumesApi.md#device_type4_volumes_list) | **GET** /api/v1/storage-systems/device-type4/{systemId}/volumes | Get all volumes details for HPE Alletra Storage MP
[**snapshot_clone_create**](VolumesApi.md#snapshot_clone_create) | **POST** /api/v1/storage-systems/device-type1/{systemId}/snapshots/{snapshotId}/clone | Create a clone of a snapshot identified by {snapshotId} for Primera / Alletra 9K systems.
[**vluns_delete**](VolumesApi.md#vluns_delete) | **DELETE** /api/v1/storage-systems/device-type1/{systemId}/volumes/{volumeId}/vluns/{id} | Remove vlun idenfied by {id} form volume identified by {volumeId} from Primera / Alletra 9K
[**volume_clone_create**](VolumesApi.md#volume_clone_create) | **POST** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id}/clone | Create a clone volume identified by {id} for Primera / Alletra 9K systems.
[**volume_create**](VolumesApi.md#volume_create) | **POST** /api/v1/storage-systems/device-type1/{systemId}/volumes | Create volume for a storage system Primera / Alletra 9K
[**volume_delete**](VolumesApi.md#volume_delete) | **DELETE** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id} | Remove volume identified by {volumeId} from Primera / Alletra 9K
[**volume_edit**](VolumesApi.md#volume_edit) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id} | Edit volume identified by {volumeId} from Primera / Alletra 9K
[**volume_get_by_id**](VolumesApi.md#volume_get_by_id) | **GET** /api/v1/volumes/{id} | Get details of Volume identified by {id}
[**volume_list_for_system_by_system_id**](VolumesApi.md#volume_list_for_system_by_system_id) | **GET** /api/v1/storage-systems/{systemId}/volumes | Get details of volumes identified with {systemId}
[**volume_snapshot_create**](VolumesApi.md#volume_snapshot_create) | **POST** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id}/snapshots | Create snapshot for volumes identified by {id}
[**volume_snapshot_get_by_id**](VolumesApi.md#volume_snapshot_get_by_id) | **DELETE** /api/v1/storage-systems/device-type1/{systemId}/volumes/{volumeId}/snapshots/{snapshotId} | Remove Primera / Alletra 9K snapshot in system identified by {snapshotId}
[**volumes_list**](VolumesApi.md#volumes_list) | **GET** /api/v1/volumes | Get all volumes


# **device_type1_get_clones**
> PrimeraVolumesList device_type1_get_clones(system_id, volume_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get the details of the clone volumes associated with a base volume identified by {volumeId} for Primera / Alletra 9K systems.

Get the details of the clone volumes associated with a base volume identified by {volumeId} for Primera / Alletra 9K systems.

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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    volume_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq array1 and wwn eq 2FF70002AC018D94' # str | oData query to filter by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get the details of the clone volumes associated with a base volume identified by {volumeId} for Primera / Alletra 9K systems.
        api_response = api_instance.device_type1_get_clones(system_id, volume_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of VolumesApi->device_type1_get_clones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type1_get_clones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
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

# **device_type1_get_snapshot_vluns_by_id**
> VlunsListSingle device_type1_get_snapshot_vluns_by_id(system_id, snapshot_id, id, select=select)

Get details of vlun identified by {id} for Snapshot identified by {snapshotId} for Primera / Alletra 9K

Get details of vlun identified by {id} for Snapshot identified by {snapshotId} for Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.vluns_list_single import VlunsListSingle
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    snapshot_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the snapshots
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the vlun
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of vlun identified by {id} for Snapshot identified by {snapshotId} for Primera / Alletra 9K
        api_response = api_instance.device_type1_get_snapshot_vluns_by_id(system_id, snapshot_id, id, select=select)
        print("The response of VolumesApi->device_type1_get_snapshot_vluns_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type1_get_snapshot_vluns_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **snapshot_id** | **str**| UID of the snapshots | 
 **id** | **str**| UID of the vlun | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**VlunsListSingle**](VlunsListSingle.md)

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

# **device_type1_get_snapshot_vluns_list**
> VlunsSummaryList device_type1_get_snapshot_vluns_list(system_id, snapshot_id, select=select, limit=limit, offset=offset, filter=filter, sort=sort)

Get details of vluns for Snapshot identified by {snapshotId} for Primera / Alletra 9K

Get details of vluns for Snapshot identified by {snapshotId} for Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.vluns_summary_list import VlunsSummaryList
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    snapshot_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the snapshots
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq array1 and wwn eq 2FF70002AC018D94' # str | oData query to filter by Key. (optional)
    sort = 'id asc,name desc' # str | Query to sort the response with specified key and order (optional)

    try:
        # Get details of vluns for Snapshot identified by {snapshotId} for Primera / Alletra 9K
        api_response = api_instance.device_type1_get_snapshot_vluns_list(system_id, snapshot_id, select=select, limit=limit, offset=offset, filter=filter, sort=sort)
        print("The response of VolumesApi->device_type1_get_snapshot_vluns_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type1_get_snapshot_vluns_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **snapshot_id** | **str**| UID of the snapshots | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| Query to sort the response with specified key and order | [optional] 

### Return type

[**VlunsSummaryList**](VlunsSummaryList.md)

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

# **device_type1_get_volumes_performance_history**
> PerformanceHistoryData device_type1_get_volumes_performance_history(system_id, report_type=report_type, range=range, time_interval_min=time_interval_min, compare_by=compare_by, group_by=group_by, filter=filter, component=component, metric_type=metric_type)

Get performance history of Primera / Alletra 9K Volumes

Get performance history of Primera / Alletra 9K Volumes

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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    report_type = 'Canned,Custom,Def,ApiUser' # str | parameter will be set to report type requested. For api users, set parameter as ApiUser (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)
    compare_by = 'top eq 5 and metrics eq READ_IOPS' # str | compareBy will define top and compare metrics for which query has to be made (optional)
    group_by = 'VV_NAME,HOST_NAME,LUN,deviceName' # str | groupBy will define comma separated groupby parameters (optional)
    filter = 'vvname in (vvname1,vvname2,vvname3) ,deviceName in (cage1)' # str | filter will define objects to be filtered (optional)
    component = 'VLUN' # str | component will give information about resource to be queried (optional)
    metric_type = 'IOPS,LATENCY,THROUGHPUT,IOSIZE,QLEN,AVG_BUSY,powerConsumption' # str | metricType will define comma separated metrics (optional)

    try:
        # Get performance history of Primera / Alletra 9K Volumes
        api_response = api_instance.device_type1_get_volumes_performance_history(system_id, report_type=report_type, range=range, time_interval_min=time_interval_min, compare_by=compare_by, group_by=group_by, filter=filter, component=component, metric_type=metric_type)
        print("The response of VolumesApi->device_type1_get_volumes_performance_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type1_get_volumes_performance_history: %s\n" % e)
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
 **filter** | **str**| filter will define objects to be filtered | [optional] 
 **component** | **str**| component will give information about resource to be queried | [optional] 
 **metric_type** | **str**| metricType will define comma separated metrics | [optional] 

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
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_promote_clone_volume**
> TaskResponse device_type1_promote_clone_volume(system_id, volume_id, clone_id, promote_clone_input=promote_clone_input)

Promote a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}

Promote a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.promote_clone_input import PromoteCloneInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    volume_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    clone_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the clone
    promote_clone_input = dscc.PromoteCloneInput() # PromoteCloneInput |  (optional)

    try:
        # Promote a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_promote_clone_volume(system_id, volume_id, clone_id, promote_clone_input=promote_clone_input)
        print("The response of VolumesApi->device_type1_promote_clone_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type1_promote_clone_volume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
 **clone_id** | **str**| UID of the clone | 
 **promote_clone_input** | [**PromoteCloneInput**](PromoteCloneInput.md)|  | [optional] 

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

# **device_type1_promote_snapshot**
> TaskResponse device_type1_promote_snapshot(system_id, volume_id, snapshot_id, promote_snapshot_input=promote_snapshot_input)

Promote a snapshot identified by {snapshotId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}

Promote a snapshot identified by {snapshotId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.promote_snapshot_input import PromoteSnapshotInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    volume_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    snapshot_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the snapshots
    promote_snapshot_input = dscc.PromoteSnapshotInput() # PromoteSnapshotInput |  (optional)

    try:
        # Promote a snapshot identified by {snapshotId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_promote_snapshot(system_id, volume_id, snapshot_id, promote_snapshot_input=promote_snapshot_input)
        print("The response of VolumesApi->device_type1_promote_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type1_promote_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
 **snapshot_id** | **str**| UID of the snapshots | 
 **promote_snapshot_input** | [**PromoteSnapshotInput**](PromoteSnapshotInput.md)|  | [optional] 

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

# **device_type1_resync_clone_volume**
> TaskResponse device_type1_resync_clone_volume(system_id, volume_id, clone_id, resync_clone_volume_input=resync_clone_volume_input)

Resynchronize a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}

Resynchronize a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.resync_clone_volume_input import ResyncCloneVolumeInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    volume_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    clone_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the clone
    resync_clone_volume_input = dscc.ResyncCloneVolumeInput() # ResyncCloneVolumeInput |  (optional)

    try:
        # Resynchronize a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_resync_clone_volume(system_id, volume_id, clone_id, resync_clone_volume_input=resync_clone_volume_input)
        print("The response of VolumesApi->device_type1_resync_clone_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type1_resync_clone_volume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
 **clone_id** | **str**| UID of the clone | 
 **resync_clone_volume_input** | [**ResyncCloneVolumeInput**](ResyncCloneVolumeInput.md)|  | [optional] 

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

# **device_type1_snapshots_get_by_id**
> SnapshotsListSingle device_type1_snapshots_get_by_id(system_id, volume_id, snapshot_id, select=select)

Get details of snapshot identified by {snapshotId} for Volume identified by {volumeId} for Primera / Alletra 9K

Get details of vlun identified by {id} for Volume identified by {volumeId} for Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.snapshots_list_single import SnapshotsListSingle
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    volume_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    snapshot_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the snapshots
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of snapshot identified by {snapshotId} for Volume identified by {volumeId} for Primera / Alletra 9K
        api_response = api_instance.device_type1_snapshots_get_by_id(system_id, volume_id, snapshot_id, select=select)
        print("The response of VolumesApi->device_type1_snapshots_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type1_snapshots_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
 **snapshot_id** | **str**| UID of the snapshots | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**SnapshotsListSingle**](SnapshotsListSingle.md)

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

# **device_type1_vlun_export**
> TaskResponse device_type1_vlun_export(system_id, id, vluns_create_input)

Export vlun for volume identified by {id} from Primera / Alletra 9K identified by {systemId}

Export vlun for volume identified by {id} from Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.models.vluns_create_input import VlunsCreateInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    vluns_create_input = dscc.VlunsCreateInput() # VlunsCreateInput | 

    try:
        # Export vlun for volume identified by {id} from Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_vlun_export(system_id, id, vluns_create_input)
        print("The response of VolumesApi->device_type1_vlun_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type1_vlun_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **vluns_create_input** | [**VlunsCreateInput**](VlunsCreateInput.md)|  | 

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

# **device_type1_vlun_export_for_snapshot**
> TaskResponse device_type1_vlun_export_for_snapshot(system_id, snapshot_id, vluns_create_input)

Export vlun for snapshot identified by {id} from Primera / Alletra 9K identified by {systemId}

Export vlun for snapshot identified by {id} from Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.models.vluns_create_input import VlunsCreateInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    snapshot_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the snapshots
    vluns_create_input = dscc.VlunsCreateInput() # VlunsCreateInput | 

    try:
        # Export vlun for snapshot identified by {id} from Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_vlun_export_for_snapshot(system_id, snapshot_id, vluns_create_input)
        print("The response of VolumesApi->device_type1_vlun_export_for_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type1_vlun_export_for_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **snapshot_id** | **str**| UID of the snapshots | 
 **vluns_create_input** | [**VlunsCreateInput**](VlunsCreateInput.md)|  | 

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

# **device_type1_vlun_unexport**
> TaskResponse device_type1_vlun_unexport(system_id, id, un_export_vlun)

Unexport vlun for volume identified by {id} from Primera / Alletra 9K identified by {systemId}

Unexport vlun for volume identified by {id} from Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.models.un_export_vlun import UnExportVlun
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    un_export_vlun = dscc.UnExportVlun() # UnExportVlun | 

    try:
        # Unexport vlun for volume identified by {id} from Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_vlun_unexport(system_id, id, un_export_vlun)
        print("The response of VolumesApi->device_type1_vlun_unexport:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type1_vlun_unexport: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **un_export_vlun** | [**UnExportVlun**](UnExportVlun.md)|  | 

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

# **device_type1_vlun_unexport_for_snapshot**
> TaskResponse device_type1_vlun_unexport_for_snapshot(system_id, snapshot_id, un_export_vlun)

Unexport vlun for snapshot identified by {id} from Primera / Alletra 9K identified by {systemId}

Unexport vlun for snapshot identified by {id} from Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.models.un_export_vlun import UnExportVlun
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    snapshot_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the snapshots
    un_export_vlun = dscc.UnExportVlun() # UnExportVlun | 

    try:
        # Unexport vlun for snapshot identified by {id} from Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_vlun_unexport_for_snapshot(system_id, snapshot_id, un_export_vlun)
        print("The response of VolumesApi->device_type1_vlun_unexport_for_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type1_vlun_unexport_for_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **snapshot_id** | **str**| UID of the snapshots | 
 **un_export_vlun** | [**UnExportVlun**](UnExportVlun.md)|  | 

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

# **device_type1_vluns_get_by_id**
> VlunsListSingle device_type1_vluns_get_by_id(system_id, volume_id, id, select=select)

Get details of vlun identified by {id} for Volume identified by {volumeId} for Primera / Alletra 9K

Get details of vlun identified by {id} for Volume identified by {volumeId} for Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.vluns_list_single import VlunsListSingle
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    volume_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the vlun
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of vlun identified by {id} for Volume identified by {volumeId} for Primera / Alletra 9K
        api_response = api_instance.device_type1_vluns_get_by_id(system_id, volume_id, id, select=select)
        print("The response of VolumesApi->device_type1_vluns_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type1_vluns_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
 **id** | **str**| UID of the vlun | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**VlunsListSingle**](VlunsListSingle.md)

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

# **device_type1_vluns_list**
> VlunsSummaryList device_type1_vluns_list(system_id, id, select=select, limit=limit, offset=offset, filter=filter, sort=sort)

Get details of vluns for Volume identified by {volumeId} for Primera / Alletra 9K

Get details of vluns for Volume identified by {volumeId} for Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.vluns_summary_list import VlunsSummaryList
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq array1 and wwn eq 2FF70002AC018D94' # str | oData query to filter by Key. (optional)
    sort = 'id asc,name desc' # str | Query to sort the response with specified key and order (optional)

    try:
        # Get details of vluns for Volume identified by {volumeId} for Primera / Alletra 9K
        api_response = api_instance.device_type1_vluns_list(system_id, id, select=select, limit=limit, offset=offset, filter=filter, sort=sort)
        print("The response of VolumesApi->device_type1_vluns_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type1_vluns_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| Query to sort the response with specified key and order | [optional] 

### Return type

[**VlunsSummaryList**](VlunsSummaryList.md)

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

# **device_type1_volume_capacity_history_get_by_id**
> VolumeCapacityHistory device_type1_volume_capacity_history_get_by_id(system_id, id, select=select, range=range, time_interval_min=time_interval_min)

Get volume capacity trend data of Primera / Alletra 9K Volume identified by {id}

Get volume capacity trend data of Primera / Alletra 9K Volume identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.volume_capacity_history import VolumeCapacityHistory
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)

    try:
        # Get volume capacity trend data of Primera / Alletra 9K Volume identified by {id}
        api_response = api_instance.device_type1_volume_capacity_history_get_by_id(system_id, id, select=select, range=range, time_interval_min=time_interval_min)
        print("The response of VolumesApi->device_type1_volume_capacity_history_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type1_volume_capacity_history_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**VolumeCapacityHistory**](VolumeCapacityHistory.md)

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

# **device_type1_volume_get_by_id**
> PrimeraVolumeDetails device_type1_volume_get_by_id(system_id, id, select=select)

Get details of Primera / Alletra 9K Volume identified by {id}

Get details of Primera / Alletra 9K Volume identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.primera_volume_details import PrimeraVolumeDetails
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Primera / Alletra 9K Volume identified by {id}
        api_response = api_instance.device_type1_volume_get_by_id(system_id, id, select=select)
        print("The response of VolumesApi->device_type1_volume_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type1_volume_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraVolumeDetails**](PrimeraVolumeDetails.md)

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

# **device_type1_volume_performance_history_get_by_id**
> VolumePerformanceHistory device_type1_volume_performance_history_get_by_id(system_id, id, select=select, range=range, time_interval_min=time_interval_min)

Get performance trend data of Primera / Alletra 9K Volume identified by {id}

Get performance trend data of Primera / Alletra 9K Volume identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.volume_performance_history import VolumePerformanceHistory
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)

    try:
        # Get performance trend data of Primera / Alletra 9K Volume identified by {id}
        api_response = api_instance.device_type1_volume_performance_history_get_by_id(system_id, id, select=select, range=range, time_interval_min=time_interval_min)
        print("The response of VolumesApi->device_type1_volume_performance_history_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type1_volume_performance_history_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**VolumePerformanceHistory**](VolumePerformanceHistory.md)

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

# **device_type1_volume_performance_statistics_get_by_id**
> VolumePerformance device_type1_volume_performance_statistics_get_by_id(system_id, id, select=select)

Get performance statistics of Primera / Alletra 9K Volume identified by {id}

Get performance statistics of Primera / Alletra 9K Volume identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.volume_performance import VolumePerformance
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get performance statistics of Primera / Alletra 9K Volume identified by {id}
        api_response = api_instance.device_type1_volume_performance_statistics_get_by_id(system_id, id, select=select)
        print("The response of VolumesApi->device_type1_volume_performance_statistics_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type1_volume_performance_statistics_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**VolumePerformance**](VolumePerformance.md)

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

# **device_type1_volume_snapshots_list**
> SnapshotsSummaryList device_type1_volume_snapshots_list(system_id, id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get snapshot details of volume identified by {id} for Primera / Alletra 9K

Get snapshot details of volume identified by {id} for Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.snapshots_summary_list import SnapshotsSummaryList
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq array1 and wwn eq 2FF70002AC018D94' # str | oData query to filter by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get snapshot details of volume identified by {id} for Primera / Alletra 9K
        api_response = api_instance.device_type1_volume_snapshots_list(system_id, id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of VolumesApi->device_type1_volume_snapshots_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type1_volume_snapshots_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| oData query to sort by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**SnapshotsSummaryList**](SnapshotsSummaryList.md)

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

# **device_type1_volumes_list**
> PrimeraVolumesList device_type1_volumes_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all volumes details for Primera / Alletra 9K

Get all volumes details for Primera / Alletra 9K

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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq array1 and wwn eq 2FF70002AC018D94' # str | oData query to filter by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all volumes details for Primera / Alletra 9K
        api_response = api_instance.device_type1_volumes_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of VolumesApi->device_type1_volumes_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type1_volumes_list: %s\n" % e)
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

# **device_type2_access_control_record_create**
> TaskResponse device_type2_access_control_record_create(system_id, nimble_create_access_control_record_input)

Create Nimble / Alletra 6K access control record in system identified by {systemId}

Create Nimble / Alletra 6K access control record in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_create_access_control_record_input import NimbleCreateAccessControlRecordInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    nimble_create_access_control_record_input = dscc.NimbleCreateAccessControlRecordInput() # NimbleCreateAccessControlRecordInput | 

    try:
        # Create Nimble / Alletra 6K access control record in system identified by {systemId}
        api_response = api_instance.device_type2_access_control_record_create(system_id, nimble_create_access_control_record_input)
        print("The response of VolumesApi->device_type2_access_control_record_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_access_control_record_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_create_access_control_record_input** | [**NimbleCreateAccessControlRecordInput**](NimbleCreateAccessControlRecordInput.md)|  | 

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

# **device_type2_clone_volume_by_id**
> TaskResponse device_type2_clone_volume_by_id(system_id, volume_id, nimble_clone_volume_input)

Create Nimble / Alletra 6K clone volume identified by {volumeId}.

Create Nimble / Alletra 6K clone volume identified by {volumeId}.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_clone_volume_input import NimbleCloneVolumeInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of volume. A 42 digit hexadecimal number.
    nimble_clone_volume_input = dscc.NimbleCloneVolumeInput() # NimbleCloneVolumeInput | 

    try:
        # Create Nimble / Alletra 6K clone volume identified by {volumeId}.
        api_response = api_instance.device_type2_clone_volume_by_id(system_id, volume_id, nimble_clone_volume_input)
        print("The response of VolumesApi->device_type2_clone_volume_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_clone_volume_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **nimble_clone_volume_input** | [**NimbleCloneVolumeInput**](NimbleCloneVolumeInput.md)|  | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_delete_snapshot_access_by_id**
> TaskResponse device_type2_delete_snapshot_access_by_id(system_id, volume_id, snapshot_id, un_export_input)

Delete access for snapshot identified by {snapshotId} from Nimble / Alletra 6K identified by {systemId}

Delete access for snapshot identified by {snapshotId} from Nimble / Alletra 6K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.models.un_export_input import UnExportInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of volume. A 42 digit hexadecimal number.
    snapshot_id = '2a0df0fe6f7dc7bb17000000000000000000000008' # str | Identifier of snapshot. A 42 digit hexadecimal number.
    un_export_input = dscc.UnExportInput() # UnExportInput | 

    try:
        # Delete access for snapshot identified by {snapshotId} from Nimble / Alletra 6K identified by {systemId}
        api_response = api_instance.device_type2_delete_snapshot_access_by_id(system_id, volume_id, snapshot_id, un_export_input)
        print("The response of VolumesApi->device_type2_delete_snapshot_access_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_delete_snapshot_access_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **snapshot_id** | **str**| Identifier of snapshot. A 42 digit hexadecimal number. | 
 **un_export_input** | [**UnExportInput**](UnExportInput.md)|  | 

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

# **device_type2_delete_volume_access_by_id**
> TaskResponse device_type2_delete_volume_access_by_id(system_id, volume_id, un_export_input)

Delete access for volume identified by {volumeId} from Nimble / Alletra 6K identified by {systemId}

Delete access for volume identified by {volumeId} from Nimble / Alletra 6K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.models.un_export_input import UnExportInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of volume. A 42 digit hexadecimal number.
    un_export_input = dscc.UnExportInput() # UnExportInput | 

    try:
        # Delete access for volume identified by {volumeId} from Nimble / Alletra 6K identified by {systemId}
        api_response = api_instance.device_type2_delete_volume_access_by_id(system_id, volume_id, un_export_input)
        print("The response of VolumesApi->device_type2_delete_volume_access_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_delete_volume_access_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **un_export_input** | [**UnExportInput**](UnExportInput.md)|  | 

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

# **device_type2_edit_access_control_record_by_id**
> TaskResponse device_type2_edit_access_control_record_by_id(system_id, access_control_record_id, nimble_edit_access_control_record_input)

Edit access-control-record identified by {accessControlRecordId} for Nimble / Alletra 6K

Edit access-control-record identified by {accessControlRecordId} for Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_edit_access_control_record_input import NimbleEditAccessControlRecordInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    access_control_record_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of Access Control Record. A 42 digit hexadecimal number.
    nimble_edit_access_control_record_input = dscc.NimbleEditAccessControlRecordInput() # NimbleEditAccessControlRecordInput | 

    try:
        # Edit access-control-record identified by {accessControlRecordId} for Nimble / Alletra 6K
        api_response = api_instance.device_type2_edit_access_control_record_by_id(system_id, access_control_record_id, nimble_edit_access_control_record_input)
        print("The response of VolumesApi->device_type2_edit_access_control_record_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_edit_access_control_record_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **access_control_record_id** | **str**| Identifier of Access Control Record. A 42 digit hexadecimal number. | 
 **nimble_edit_access_control_record_input** | [**NimbleEditAccessControlRecordInput**](NimbleEditAccessControlRecordInput.md)|  | 

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

# **device_type2_edit_snapshot_by_id**
> TaskResponse device_type2_edit_snapshot_by_id(system_id, nimble_edit_multiple_snapshot_input)

Edit Multiple Nimble / Alletra 6K snapshots in system identified by {systemId}

Edit Multiple Nimble / Alletra 6K snapshots in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_edit_multiple_snapshot_input import NimbleEditMultipleSnapshotInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    nimble_edit_multiple_snapshot_input = dscc.NimbleEditMultipleSnapshotInput() # NimbleEditMultipleSnapshotInput | 

    try:
        # Edit Multiple Nimble / Alletra 6K snapshots in system identified by {systemId}
        api_response = api_instance.device_type2_edit_snapshot_by_id(system_id, nimble_edit_multiple_snapshot_input)
        print("The response of VolumesApi->device_type2_edit_snapshot_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_edit_snapshot_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_edit_multiple_snapshot_input** | [**NimbleEditMultipleSnapshotInput**](NimbleEditMultipleSnapshotInput.md)|  | 

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

# **device_type2_edit_volume_by_id**
> TaskResponse device_type2_edit_volume_by_id(system_id, volume_id, nimble_edit_volume_input)

Edit  details of Nimble / Alletra 6K Volume identified by {volumeId}

Edit  details of Nimble / Alletra 6K Volume identified by {volumeId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_edit_volume_input import NimbleEditVolumeInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of volume. A 42 digit hexadecimal number.
    nimble_edit_volume_input = dscc.NimbleEditVolumeInput() # NimbleEditVolumeInput | 

    try:
        # Edit  details of Nimble / Alletra 6K Volume identified by {volumeId}
        api_response = api_instance.device_type2_edit_volume_by_id(system_id, volume_id, nimble_edit_volume_input)
        print("The response of VolumesApi->device_type2_edit_volume_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_edit_volume_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **nimble_edit_volume_input** | [**NimbleEditVolumeInput**](NimbleEditVolumeInput.md)|  | 

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

# **device_type2_get_access_control_record_by_id**
> NimbleAccessControlRecordDetailsWithRequestUri device_type2_get_access_control_record_by_id(system_id, access_control_record_id, select=select)

Get details of Nimble / Alletra 6K access-control-records identified by {accessControlRecordId}

Get details of Nimble / Alletra 6K access-control-records identified by {accessControlRecordId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_access_control_record_details_with_request_uri import NimbleAccessControlRecordDetailsWithRequestUri
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    access_control_record_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the Access Control Record . A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Nimble / Alletra 6K access-control-records identified by {accessControlRecordId}
        api_response = api_instance.device_type2_get_access_control_record_by_id(system_id, access_control_record_id, select=select)
        print("The response of VolumesApi->device_type2_get_access_control_record_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_get_access_control_record_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **access_control_record_id** | **str**| ID of the Access Control Record . A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleAccessControlRecordDetailsWithRequestUri**](NimbleAccessControlRecordDetailsWithRequestUri.md)

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

# **device_type2_get_all_access_control_records**
> NimbleAccessControlRecordList device_type2_get_all_access_control_records(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all access-control-records details by Nimble / Alletra 6K

Get all access-control-records details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_access_control_record_list import NimbleAccessControlRecordList
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter Access Control Record  by Key. (optional)
    sort = 'name desc' # str | oData query to sort Access Control Record  resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all access-control-records details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_access_control_records(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of VolumesApi->device_type2_get_all_access_control_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_get_all_access_control_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter Access Control Record  by Key. | [optional] 
 **sort** | **str**| oData query to sort Access Control Record  resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleAccessControlRecordList**](NimbleAccessControlRecordList.md)

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

# **device_type2_get_all_snapshots_by_volume_id**
> NimbleSnapshotList device_type2_get_all_snapshots_by_volume_id(system_id, volume_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all snapshots' details of Nimble / Alletra 6K Volume identified by {volumeId}

Get all snapshots' details of Nimble / Alletra 6K Volume identified by {volumeId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_snapshot_list import NimbleSnapshotList
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of volume. A 42 digit hexadecimal number.
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter snapshots by Key. (optional)
    sort = 'name desc' # str | oData query to sort snapshots resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all snapshots' details of Nimble / Alletra 6K Volume identified by {volumeId}
        api_response = api_instance.device_type2_get_all_snapshots_by_volume_id(system_id, volume_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of VolumesApi->device_type2_get_all_snapshots_by_volume_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_get_all_snapshots_by_volume_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter snapshots by Key. | [optional] 
 **sort** | **str**| oData query to sort snapshots resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleSnapshotList**](NimbleSnapshotList.md)

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

# **device_type2_get_all_volumes**
> NimbleVolumesList device_type2_get_all_volumes(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all volumes details for Nimble / Alletra 6K

Get all volumes details for Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_volumes_list import NimbleVolumesList
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'id eq 2a0df0fe6f7dc7bb16000000000000000000004817' # str | Lucene query to filter volumes by Key. (optional)
    sort = 'name desc' # str | oData query to sort volumes resource by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all volumes details for Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_volumes(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of VolumesApi->device_type2_get_all_volumes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_get_all_volumes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter volumes by Key. | [optional] 
 **sort** | **str**| oData query to sort volumes resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleVolumesList**](NimbleVolumesList.md)

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

# **device_type2_get_snapshot_by_id**
> NimbleSnapshotDetails device_type2_get_snapshot_by_id(system_id, volume_id, snapshot_id, select=select)

Get details of snapshot of Nimble / Alletra 6K Volume identified by {volumeId} by {snapshotId}

Get details of snapshot of Nimble / Alletra 6K Volume identified by {volumeId} by {snapshotId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_snapshot_details import NimbleSnapshotDetails
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of volume. A 42 digit hexadecimal number.
    snapshot_id = '2a0df0fe6f7dc7bb17000000000000000000000008' # str | Identifier of snapshot. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of snapshot of Nimble / Alletra 6K Volume identified by {volumeId} by {snapshotId}
        api_response = api_instance.device_type2_get_snapshot_by_id(system_id, volume_id, snapshot_id, select=select)
        print("The response of VolumesApi->device_type2_get_snapshot_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_get_snapshot_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **snapshot_id** | **str**| Identifier of snapshot. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleSnapshotDetails**](NimbleSnapshotDetails.md)

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

# **device_type2_get_volume_by_id**
> NimbleVolumeDetails device_type2_get_volume_by_id(system_id, volume_id, select=select)

Get details of Nimble / Alletra 6K Volume identified by {volumeId}

Get details of Nimble / Alletra 6K Volume identified by {volumeId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_volume_details import NimbleVolumeDetails
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of volume. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Nimble / Alletra 6K Volume identified by {volumeId}
        api_response = api_instance.device_type2_get_volume_by_id(system_id, volume_id, select=select)
        print("The response of VolumesApi->device_type2_get_volume_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_get_volume_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleVolumeDetails**](NimbleVolumeDetails.md)

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

# **device_type2_get_volume_capacity_history**
> NimblevolumeCapacityHistory device_type2_get_volume_capacity_history(system_id, volume_id, select=select, range=range, time_interval_min=time_interval_min)

Get volume capacity trend data of Nimble / Alletra 6K Volume identified by {volumeId}

Get volume capacity trend data of Nimble / Alletra 6K Volume identified by {volumeId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimblevolume_capacity_history import NimblevolumeCapacityHistory
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of volume. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)

    try:
        # Get volume capacity trend data of Nimble / Alletra 6K Volume identified by {volumeId}
        api_response = api_instance.device_type2_get_volume_capacity_history(system_id, volume_id, select=select, range=range, time_interval_min=time_interval_min)
        print("The response of VolumesApi->device_type2_get_volume_capacity_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_get_volume_capacity_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**NimblevolumeCapacityHistory**](NimblevolumeCapacityHistory.md)

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

# **device_type2_get_volume_performance_history**
> NimblevolumePerformanceHistory device_type2_get_volume_performance_history(system_id, volume_id, select=select, range=range, time_interval_min=time_interval_min)

Get performance trend data of Nimble / Alletra 6K Volume identified by {id}

Get performance trend data of Nimble / Alletra 6K Volume identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimblevolume_performance_history import NimblevolumePerformanceHistory
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of volume. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)

    try:
        # Get performance trend data of Nimble / Alletra 6K Volume identified by {id}
        api_response = api_instance.device_type2_get_volume_performance_history(system_id, volume_id, select=select, range=range, time_interval_min=time_interval_min)
        print("The response of VolumesApi->device_type2_get_volume_performance_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_get_volume_performance_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**NimblevolumePerformanceHistory**](NimblevolumePerformanceHistory.md)

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

# **device_type2_get_volume_performance_statistics**
> VolPerformance device_type2_get_volume_performance_statistics(system_id, volume_id, select=select)

Get performance statistics of Nimble / Alletra 6K Volume identified by {volumeId}

Get performance statistics of Nimble / Alletra 6K Volume identified by {volumeId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.vol_performance import VolPerformance
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of volume. A 42 digit hexadecimal number.
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get performance statistics of Nimble / Alletra 6K Volume identified by {volumeId}
        api_response = api_instance.device_type2_get_volume_performance_statistics(system_id, volume_id, select=select)
        print("The response of VolumesApi->device_type2_get_volume_performance_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_get_volume_performance_statistics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**VolPerformance**](VolPerformance.md)

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

# **device_type2_get_volumes_performance_history**
> NimblePerformanceHistoryData device_type2_get_volumes_performance_history(system_id, range=range, time_interval_min=time_interval_min, compare_by=compare_by, filter=filter, metric_type=metric_type)

Get performance history of Nimble / Alletra 6K Volumes

Get performance history of Nimble / Alletra 6K Volumes

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_performance_history_data import NimblePerformanceHistoryData
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)
    compare_by = 'top eq 5 and metrics eq READ_IOPS' # str | compareBy will define top and compare metrics for which query has to be made (optional)
    filter = 'vvname in (vvname1,vvname2,vvname3) ,deviceName in (cage1)' # str | filter will define objects to be filtered (optional)
    metric_type = 'IOPS,LATENCY,THROUGHPUT' # str | metricTypes will define comma separated metrics (optional)

    try:
        # Get performance history of Nimble / Alletra 6K Volumes
        api_response = api_instance.device_type2_get_volumes_performance_history(system_id, range=range, time_interval_min=time_interval_min, compare_by=compare_by, filter=filter, metric_type=metric_type)
        print("The response of VolumesApi->device_type2_get_volumes_performance_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_get_volumes_performance_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 
 **compare_by** | **str**| compareBy will define top and compare metrics for which query has to be made | [optional] 
 **filter** | **str**| filter will define objects to be filtered | [optional] 
 **metric_type** | **str**| metricTypes will define comma separated metrics | [optional] 

### Return type

[**NimblePerformanceHistoryData**](NimblePerformanceHistoryData.md)

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

# **device_type2_move_volume**
> TaskResponse device_type2_move_volume(system_id, volume_id, nimble_move_volume_to_another_pool_input)

Move Nimble / Alletra 6K volume identified by {volumeId} to another pool.

Move Nimble / Alletra 6K volume identified by {volumeId} to another pool.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_move_volume_to_another_pool_input import NimbleMoveVolumeToAnotherPoolInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of volume. A 42 digit hexadecimal number.
    nimble_move_volume_to_another_pool_input = dscc.NimbleMoveVolumeToAnotherPoolInput() # NimbleMoveVolumeToAnotherPoolInput | 

    try:
        # Move Nimble / Alletra 6K volume identified by {volumeId} to another pool.
        api_response = api_instance.device_type2_move_volume(system_id, volume_id, nimble_move_volume_to_another_pool_input)
        print("The response of VolumesApi->device_type2_move_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_move_volume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **nimble_move_volume_to_another_pool_input** | [**NimbleMoveVolumeToAnotherPoolInput**](NimbleMoveVolumeToAnotherPoolInput.md)|  | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_provisioning_review**
> List[NimbleHostReviewSingle] device_type2_provisioning_review(system_id, nimble_host_review_input)

Provisioning review for a storage system Nimble / Alletra 6K

Provisioning review for a storage system Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_host_review_input import NimbleHostReviewInput
from dscc.models.nimble_host_review_single import NimbleHostReviewSingle
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    nimble_host_review_input = dscc.NimbleHostReviewInput() # NimbleHostReviewInput | 

    try:
        # Provisioning review for a storage system Nimble / Alletra 6K
        api_response = api_instance.device_type2_provisioning_review(system_id, nimble_host_review_input)
        print("The response of VolumesApi->device_type2_provisioning_review:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_provisioning_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_host_review_input** | [**NimbleHostReviewInput**](NimbleHostReviewInput.md)|  | 

### Return type

[**List[NimbleHostReviewSingle]**](NimbleHostReviewSingle.md)

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

# **device_type2_provisioning_worklow**
> TaskResponse device_type2_provisioning_worklow(system_id, nimble_create_volumes_workflow_input)

Create provisioning workflow for a Nimble / Alletra 6K storage system identified by {systemId}

Create provisioning workflow for a Nimble / Alletra 6K storage system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_create_volumes_workflow_input import NimbleCreateVolumesWorkflowInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    nimble_create_volumes_workflow_input = dscc.NimbleCreateVolumesWorkflowInput() # NimbleCreateVolumesWorkflowInput | 

    try:
        # Create provisioning workflow for a Nimble / Alletra 6K storage system identified by {systemId}
        api_response = api_instance.device_type2_provisioning_worklow(system_id, nimble_create_volumes_workflow_input)
        print("The response of VolumesApi->device_type2_provisioning_worklow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_provisioning_worklow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_create_volumes_workflow_input** | [**NimbleCreateVolumesWorkflowInput**](NimbleCreateVolumesWorkflowInput.md)|  | 

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

# **device_type2_remove_access_control_record_by_id**
> TaskResponse device_type2_remove_access_control_record_by_id(system_id, access_control_record_id)

Remove access-control-record identified by {accessControlRecordId} from Nimble / Alletra 6K

Remove access-control-record identified by {accessControlRecordId} from Nimble / Alletra 6K

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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    access_control_record_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of Access Control Record. A 42 digit hexadecimal number.

    try:
        # Remove access-control-record identified by {accessControlRecordId} from Nimble / Alletra 6K
        api_response = api_instance.device_type2_remove_access_control_record_by_id(system_id, access_control_record_id)
        print("The response of VolumesApi->device_type2_remove_access_control_record_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_remove_access_control_record_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **access_control_record_id** | **str**| Identifier of Access Control Record. A 42 digit hexadecimal number. | 

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

# **device_type2_remove_snapshot_by_id**
> TaskResponse device_type2_remove_snapshot_by_id(system_id, volume_id, snapshot_id, force=force)

Remove Nimble / Alletra 6K snapshot in system identified by {snapshotId}

Remove Nimble / Alletra 6K snapshot in system identified by {snapshotId}

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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of volume. A 42 digit hexadecimal number.
    snapshot_id = '2a0df0fe6f7dc7bb17000000000000000000000008' # str | Identifier of snapshot. A 42 digit hexadecimal number.
    force = true # bool | Make snapshot offline and remove. (optional)

    try:
        # Remove Nimble / Alletra 6K snapshot in system identified by {snapshotId}
        api_response = api_instance.device_type2_remove_snapshot_by_id(system_id, volume_id, snapshot_id, force=force)
        print("The response of VolumesApi->device_type2_remove_snapshot_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_remove_snapshot_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **snapshot_id** | **str**| Identifier of snapshot. A 42 digit hexadecimal number. | 
 **force** | **bool**| Make snapshot offline and remove. | [optional] 

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

# **device_type2_remove_volume_by_id**
> TaskResponse device_type2_remove_volume_by_id(system_id, volume_id, offline=offline, force=force)

Remove volume identified by {volumeId} from Nimble / Alletra 6K

Remove volume identified by {volumeId} from Nimble / Alletra 6K

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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of volume. A 42 digit hexadecimal number.
    offline = true # bool | Make volume offline and delete. Deprecated - Use force instead of offline. (optional)
    force = true # bool | Make volume and associated snapshots offline, stop protection and delete. (optional)

    try:
        # Remove volume identified by {volumeId} from Nimble / Alletra 6K
        api_response = api_instance.device_type2_remove_volume_by_id(system_id, volume_id, offline=offline, force=force)
        print("The response of VolumesApi->device_type2_remove_volume_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_remove_volume_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **offline** | **bool**| Make volume offline and delete. Deprecated - Use force instead of offline. | [optional] 
 **force** | **bool**| Make volume and associated snapshots offline, stop protection and delete. | [optional] 

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

# **device_type2_restore_volume_by_id**
> TaskResponse device_type2_restore_volume_by_id(system_id, volume_id, nimble_restore_volume_input)

Restore Nimble / Alletra 6K volume identified by {volumeId} from a previous snapshot.

Restore Nimble / Alletra 6K volume identified by {volumeId} from a previous snapshot.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_restore_volume_input import NimbleRestoreVolumeInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of volume. A 42 digit hexadecimal number.
    nimble_restore_volume_input = dscc.NimbleRestoreVolumeInput() # NimbleRestoreVolumeInput | 

    try:
        # Restore Nimble / Alletra 6K volume identified by {volumeId} from a previous snapshot.
        api_response = api_instance.device_type2_restore_volume_by_id(system_id, volume_id, nimble_restore_volume_input)
        print("The response of VolumesApi->device_type2_restore_volume_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_restore_volume_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **nimble_restore_volume_input** | [**NimbleRestoreVolumeInput**](NimbleRestoreVolumeInput.md)|  | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_snapshot_create**
> TaskResponse device_type2_snapshot_create(system_id, volume_id, nimble_create_snapshot_input)

Create Nimble / Alletra 6K snapshot in system identified by {systemId}

Create Nimble / Alletra 6K snapshot in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_create_snapshot_input import NimbleCreateSnapshotInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of volume. A 42 digit hexadecimal number.
    nimble_create_snapshot_input = dscc.NimbleCreateSnapshotInput() # NimbleCreateSnapshotInput | 

    try:
        # Create Nimble / Alletra 6K snapshot in system identified by {systemId}
        api_response = api_instance.device_type2_snapshot_create(system_id, volume_id, nimble_create_snapshot_input)
        print("The response of VolumesApi->device_type2_snapshot_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_snapshot_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **nimble_create_snapshot_input** | [**NimbleCreateSnapshotInput**](NimbleCreateSnapshotInput.md)|  | 

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

# **device_type2_snapshot_export**
> TaskResponse device_type2_snapshot_export(system_id, volume_id, snapshot_id, snapshot_export_input)

Configure access for snapshot identified by {snapshotId} from Nimble / Alletra 6K identified by {systemId}

Configure access for snapshot identified by {snapshotId} from Nimble / Alletra 6K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.snapshot_export_input import SnapshotExportInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of volume. A 42 digit hexadecimal number.
    snapshot_id = '2a0df0fe6f7dc7bb17000000000000000000000008' # str | Identifier of snapshot. A 42 digit hexadecimal number.
    snapshot_export_input = dscc.SnapshotExportInput() # SnapshotExportInput | 

    try:
        # Configure access for snapshot identified by {snapshotId} from Nimble / Alletra 6K identified by {systemId}
        api_response = api_instance.device_type2_snapshot_export(system_id, volume_id, snapshot_id, snapshot_export_input)
        print("The response of VolumesApi->device_type2_snapshot_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_snapshot_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **snapshot_id** | **str**| Identifier of snapshot. A 42 digit hexadecimal number. | 
 **snapshot_export_input** | [**SnapshotExportInput**](SnapshotExportInput.md)|  | 

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

# **device_type2_volumes_create**
> TaskResponse device_type2_volumes_create(system_id, nimble_create_volume_input)

Create Nimble / Alletra 6K volume in system identified by {systemId}

Create Nimble / Alletra 6K volume in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.nimble_create_volume_input import NimbleCreateVolumeInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    nimble_create_volume_input = dscc.NimbleCreateVolumeInput() # NimbleCreateVolumeInput | 

    try:
        # Create Nimble / Alletra 6K volume in system identified by {systemId}
        api_response = api_instance.device_type2_volumes_create(system_id, nimble_create_volume_input)
        print("The response of VolumesApi->device_type2_volumes_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_volumes_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_create_volume_input** | [**NimbleCreateVolumeInput**](NimbleCreateVolumeInput.md)|  | 

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

# **device_type2_volumes_export**
> TaskResponse device_type2_volumes_export(system_id, volume_id, export_input)

Configure access for volume identified by {volumeId} from Nimble / Alletra 6K identified by {systemId}

Configure access for volume identified by {volumeId} from Nimble / Alletra 6K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.export_input import ExportInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '2a0df0fe6f7dc7bb16000000000000000000004817' # str | ID of the storage system
    volume_id = '2a0df0fe6f7dc7bb16000000000000000000000007' # str | Identifier of volume. A 42 digit hexadecimal number.
    export_input = dscc.ExportInput() # ExportInput | 

    try:
        # Configure access for volume identified by {volumeId} from Nimble / Alletra 6K identified by {systemId}
        api_response = api_instance.device_type2_volumes_export(system_id, volume_id, export_input)
        print("The response of VolumesApi->device_type2_volumes_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type2_volumes_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **export_input** | [**ExportInput**](ExportInput.md)|  | 

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

# **device_type4_get_clones**
> DeviceType4VolumesList device_type4_get_clones(system_id, volume_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get the details of the clone volumes associated with a base volume identified by {volumeId} for HPE Alletra Storage MP systems.

Get the details of the clone volumes associated with a base volume identified by {volumeId} for HPE Alletra Storage MP systems.

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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    volume_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq array1 and wwn eq 2FF70002AC018D94' # str | oData query to filter by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get the details of the clone volumes associated with a base volume identified by {volumeId} for HPE Alletra Storage MP systems.
        api_response = api_instance.device_type4_get_clones(system_id, volume_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of VolumesApi->device_type4_get_clones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_get_clones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
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

# **device_type4_get_performance_drifts**
> VolumePerformanceDrifts device_type4_get_performance_drifts(system_id, volume_id, time_interval_min, range, operation_type=operation_type)

Get latency drifts of a volume for a give duration

Get latency drifts of a volume for a give duration.The minimum duration supported is 8 hours and a maximum duration of 2 days. Drifts are detected in both read and write latency metrics

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.volume_performance_drifts import VolumePerformanceDrifts
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = 'ABC239XFZ9' # str | SystemId of the HPE Alletra Storage MP storage system
    volume_id = '60002AC000000000000005B200029834' # str | VolumeId of the device-type4 storage system
    time_interval_min = 56 # int | Time interval granularity in minutes
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | Specifies the time period for which hotspot metrics are to be calculated. Both startTime and endTime should be specified
    operation_type = 'READ' # str | Indicates if hotspots metrics to be calculated for read, write or both operations. If this field is not provided, hotspots are calculated for both operations (optional)

    try:
        # Get latency drifts of a volume for a give duration
        api_response = api_instance.device_type4_get_performance_drifts(system_id, volume_id, time_interval_min, range, operation_type=operation_type)
        print("The response of VolumesApi->device_type4_get_performance_drifts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_get_performance_drifts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| SystemId of the HPE Alletra Storage MP storage system | 
 **volume_id** | **str**| VolumeId of the device-type4 storage system | 
 **time_interval_min** | **int**| Time interval granularity in minutes | 
 **range** | **str**| Specifies the time period for which hotspot metrics are to be calculated. Both startTime and endTime should be specified | 
 **operation_type** | **str**| Indicates if hotspots metrics to be calculated for read, write or both operations. If this field is not provided, hotspots are calculated for both operations | [optional] 

### Return type

[**VolumePerformanceDrifts**](VolumePerformanceDrifts.md)

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

# **device_type4_get_performance_histogram**
> DeviceType4VolumePerformanceHistogram device_type4_get_performance_histogram(system_id, id, range=range, time_interval_min=time_interval_min, io_type=io_type, buckets=buckets)

Get histogram buckets distribution of I/Os of a volume for a given duration.

Get histogram buckets distribution of I/Os of a volume for a given duration. buckets query param must be one or more combination of the following values: Size512B, Size1k, Size2k, Size4k, Size8k, Size16k, Size32k, Size64k, Size128k, Size256k, Size512k, Size1m, Size2m

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_volume_performance_histogram import DeviceType4VolumePerformanceHistogram
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)
    io_type = 'io_type_example' # str | Indicates if histogram metrics to be calculated for read or write. (optional)
    buckets = 'buckets_example' # str | Comma separated buckets list. Following values are supported:  Size512B, Size1k, Size2k, Size4k, Size8k, Size16k, Size32k, Size64k, Size128k, Size256k, Size512k, Size1m, Size2m (optional)

    try:
        # Get histogram buckets distribution of I/Os of a volume for a given duration.
        api_response = api_instance.device_type4_get_performance_histogram(system_id, id, range=range, time_interval_min=time_interval_min, io_type=io_type, buckets=buckets)
        print("The response of VolumesApi->device_type4_get_performance_histogram:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_get_performance_histogram: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 
 **io_type** | **str**| Indicates if histogram metrics to be calculated for read or write. | [optional] 
 **buckets** | **str**| Comma separated buckets list. Following values are supported:  Size512B, Size1k, Size2k, Size4k, Size8k, Size16k, Size32k, Size64k, Size128k, Size256k, Size512k, Size1m, Size2m | [optional] 

### Return type

[**DeviceType4VolumePerformanceHistogram**](DeviceType4VolumePerformanceHistogram.md)

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

# **device_type4_get_snapshot_vluns_list**
> DeviceType4VlunsSummaryList device_type4_get_snapshot_vluns_list(system_id, snapshot_id, select=select, limit=limit, offset=offset, filter=filter, sort=sort)

Get details of vluns for Snapshot identified by {snapshotId} for HPE Alletra Storage MP

Get details of vluns for Snapshot identified by {snapshotId} for HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_vluns_summary_list import DeviceType4VlunsSummaryList
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    snapshot_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the snapshots
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq array1 and wwn eq 2FF70002AC018D94' # str | oData query to filter by Key. (optional)
    sort = 'id asc,name desc' # str | Query to sort the response with specified key and order (optional)

    try:
        # Get details of vluns for Snapshot identified by {snapshotId} for HPE Alletra Storage MP
        api_response = api_instance.device_type4_get_snapshot_vluns_list(system_id, snapshot_id, select=select, limit=limit, offset=offset, filter=filter, sort=sort)
        print("The response of VolumesApi->device_type4_get_snapshot_vluns_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_get_snapshot_vluns_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **snapshot_id** | **str**| UID of the snapshots | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| Query to sort the response with specified key and order | [optional] 

### Return type

[**DeviceType4VlunsSummaryList**](DeviceType4VlunsSummaryList.md)

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

# **device_type4_get_volume_latency_annotations**
> VolumeLatencyAnnotations device_type4_get_volume_latency_annotations(system_id, volume_id, time_interval_min, range, operation_type=operation_type)

Get volume latency annotations for device-type4

Get the high latency points to be annotated segregated into read and write categories

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.volume_latency_annotations import VolumeLatencyAnnotations
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = 'ABC239XFZ9' # str | SystemId of the HPE Alletra Storage MP storage system
    volume_id = '60002AC000000000000005B200029834' # str | VolumeId of the device-type4 storage system
    time_interval_min = 56 # int | Time interval granularity in minutes
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | Specifies the time period for which hotspot metrics are to be calculated. Both startTime and endTime should be specified
    operation_type = 'READ' # str | Indicates if hotspots metrics to be calculated for read, write or both operations. If this field is not provided, hotspots are calculated for both operations (optional)

    try:
        # Get volume latency annotations for device-type4
        api_response = api_instance.device_type4_get_volume_latency_annotations(system_id, volume_id, time_interval_min, range, operation_type=operation_type)
        print("The response of VolumesApi->device_type4_get_volume_latency_annotations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_get_volume_latency_annotations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| SystemId of the HPE Alletra Storage MP storage system | 
 **volume_id** | **str**| VolumeId of the device-type4 storage system | 
 **time_interval_min** | **int**| Time interval granularity in minutes | 
 **range** | **str**| Specifies the time period for which hotspot metrics are to be calculated. Both startTime and endTime should be specified | 
 **operation_type** | **str**| Indicates if hotspots metrics to be calculated for read, write or both operations. If this field is not provided, hotspots are calculated for both operations | [optional] 

### Return type

[**VolumeLatencyAnnotations**](VolumeLatencyAnnotations.md)

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

# **device_type4_get_volumes_performance_history**
> DeviceType4PerformanceHistoryData device_type4_get_volumes_performance_history(system_id, report_type=report_type, range=range, time_interval_min=time_interval_min, compare_by=compare_by, group_by=group_by, filter=filter, component=component, metric_type=metric_type)

Get performance history of Volumes on storage system identified by {systemid}

Get performance history of Volumes on storage system identified by {systemid}

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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    report_type = 'Canned,Custom,Def,ApiUser' # str | parameter will be set to report type requested. For api users, set parameter as ApiUser (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)
    compare_by = 'top eq 5 and metrics eq READ_IOPS' # str | compareBy will define top and compare metrics for which query has to be made (optional)
    group_by = 'VV_NAME,HOST_NAME,LUN,deviceName' # str | groupBy will define comma separated groupby parameters (optional)
    filter = 'vvname in (vvname1,vvname2,vvname3) ,deviceName in (cage1)' # str | filter will define objects to be filtered (optional)
    component = 'VLUN' # str | component will give information about resource to be queried (optional)
    metric_type = 'IOPS,LATENCY,THROUGHPUT,IOSIZE,QLEN,AVG_BUSY,powerConsumption' # str | metricType will define comma separated metrics (optional)

    try:
        # Get performance history of Volumes on storage system identified by {systemid}
        api_response = api_instance.device_type4_get_volumes_performance_history(system_id, report_type=report_type, range=range, time_interval_min=time_interval_min, compare_by=compare_by, group_by=group_by, filter=filter, component=component, metric_type=metric_type)
        print("The response of VolumesApi->device_type4_get_volumes_performance_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_get_volumes_performance_history: %s\n" % e)
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
 **filter** | **str**| filter will define objects to be filtered | [optional] 
 **component** | **str**| component will give information about resource to be queried | [optional] 
 **metric_type** | **str**| metricType will define comma separated metrics | [optional] 

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
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type4_getsnapshot_vluns_by_id**
> DeviceType4VlunsListSingle device_type4_getsnapshot_vluns_by_id(system_id, snapshot_id, id, select=select)

Get details of vlun identified by {id} for Snapshot identified by {snapshotId} for HPE Alletra Storage MP

Get details of vlun identified by {id} for Snapshot identified by {snapshotId} for HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_vluns_list_single import DeviceType4VlunsListSingle
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    snapshot_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the snapshots
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the vlun
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of vlun identified by {id} for Snapshot identified by {snapshotId} for HPE Alletra Storage MP
        api_response = api_instance.device_type4_getsnapshot_vluns_by_id(system_id, snapshot_id, id, select=select)
        print("The response of VolumesApi->device_type4_getsnapshot_vluns_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_getsnapshot_vluns_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **snapshot_id** | **str**| UID of the snapshots | 
 **id** | **str**| UID of the vlun | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4VlunsListSingle**](DeviceType4VlunsListSingle.md)

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

# **device_type4_promote_clone_volume**
> TaskResponse device_type4_promote_clone_volume(system_id, volume_id, clone_id, device_type4_promote_clone_input=device_type4_promote_clone_input)

Promote a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system HPE Alletra Storage MP identified by {systemId}

Promote a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_promote_clone_input import DeviceType4PromoteCloneInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    volume_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    clone_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the clone
    device_type4_promote_clone_input = dscc.DeviceType4PromoteCloneInput() # DeviceType4PromoteCloneInput |  (optional)

    try:
        # Promote a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_promote_clone_volume(system_id, volume_id, clone_id, device_type4_promote_clone_input=device_type4_promote_clone_input)
        print("The response of VolumesApi->device_type4_promote_clone_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_promote_clone_volume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
 **clone_id** | **str**| UID of the clone | 
 **device_type4_promote_clone_input** | [**DeviceType4PromoteCloneInput**](DeviceType4PromoteCloneInput.md)|  | [optional] 

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

# **device_type4_promote_snapshot**
> TaskResponse device_type4_promote_snapshot(system_id, volume_id, snapshot_id, device_type4_promote_snapshot_input=device_type4_promote_snapshot_input)

Promote a snapshot identified by {snapshotId} of a volume identified by {volumeId} on storage system HPE Alletra Storage MP identified by {systemId}

Promote a snapshot identified by {snapshotId} of a volume identified by {volumeId} on storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_promote_snapshot_input import DeviceType4PromoteSnapshotInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    volume_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    snapshot_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the snapshots
    device_type4_promote_snapshot_input = dscc.DeviceType4PromoteSnapshotInput() # DeviceType4PromoteSnapshotInput |  (optional)

    try:
        # Promote a snapshot identified by {snapshotId} of a volume identified by {volumeId} on storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_promote_snapshot(system_id, volume_id, snapshot_id, device_type4_promote_snapshot_input=device_type4_promote_snapshot_input)
        print("The response of VolumesApi->device_type4_promote_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_promote_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
 **snapshot_id** | **str**| UID of the snapshots | 
 **device_type4_promote_snapshot_input** | [**DeviceType4PromoteSnapshotInput**](DeviceType4PromoteSnapshotInput.md)|  | [optional] 

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

# **device_type4_resync_clone_volume**
> TaskResponse device_type4_resync_clone_volume(system_id, volume_id, clone_id, device_type4_resync_clone_volume_input=device_type4_resync_clone_volume_input)

Resynchronize a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system HPE Alletra Storage MP identified by {systemId}

Resynchronize a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_resync_clone_volume_input import DeviceType4ResyncCloneVolumeInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    volume_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    clone_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the clone
    device_type4_resync_clone_volume_input = dscc.DeviceType4ResyncCloneVolumeInput() # DeviceType4ResyncCloneVolumeInput |  (optional)

    try:
        # Resynchronize a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_resync_clone_volume(system_id, volume_id, clone_id, device_type4_resync_clone_volume_input=device_type4_resync_clone_volume_input)
        print("The response of VolumesApi->device_type4_resync_clone_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_resync_clone_volume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
 **clone_id** | **str**| UID of the clone | 
 **device_type4_resync_clone_volume_input** | [**DeviceType4ResyncCloneVolumeInput**](DeviceType4ResyncCloneVolumeInput.md)|  | [optional] 

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

# **device_type4_snapshot_clone_create**
> TaskResponse device_type4_snapshot_clone_create(system_id, snapshot_id, device_type4_create_clone_snapshot_input)

Create a clone of a snapshot identified by {snapshotId} for HPE Alletra Storage MP systems.

Create a clone of a snapshot identified by {snapshotId} for HPE Alletra Storage MP systems.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_create_clone_snapshot_input import DeviceType4CreateCloneSnapshotInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    snapshot_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the snapshots
    device_type4_create_clone_snapshot_input = dscc.DeviceType4CreateCloneSnapshotInput() # DeviceType4CreateCloneSnapshotInput | 

    try:
        # Create a clone of a snapshot identified by {snapshotId} for HPE Alletra Storage MP systems.
        api_response = api_instance.device_type4_snapshot_clone_create(system_id, snapshot_id, device_type4_create_clone_snapshot_input)
        print("The response of VolumesApi->device_type4_snapshot_clone_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_snapshot_clone_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **snapshot_id** | **str**| UID of the snapshots | 
 **device_type4_create_clone_snapshot_input** | [**DeviceType4CreateCloneSnapshotInput**](DeviceType4CreateCloneSnapshotInput.md)|  | 

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

# **device_type4_snapshots_get_by_id**
> DeviceType4SnapshotsListSingle device_type4_snapshots_get_by_id(system_id, volume_id, snapshot_id, select=select)

Get details of snapshot identified by {snapshotId} for Volume identified by {volumeId} for HPE Alletra Storage MP

Get details of vlun identified by {id} for Volume identified by {volumeId} for HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_snapshots_list_single import DeviceType4SnapshotsListSingle
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    volume_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    snapshot_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the snapshots
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of snapshot identified by {snapshotId} for Volume identified by {volumeId} for HPE Alletra Storage MP
        api_response = api_instance.device_type4_snapshots_get_by_id(system_id, volume_id, snapshot_id, select=select)
        print("The response of VolumesApi->device_type4_snapshots_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_snapshots_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
 **snapshot_id** | **str**| UID of the snapshots | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4SnapshotsListSingle**](DeviceType4SnapshotsListSingle.md)

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

# **device_type4_vlun_export**
> TaskResponse device_type4_vlun_export(system_id, id, device_type4_vluns_create_input)

Export vlun for volume identified by {id} from HPE Alletra Storage MP identified by {systemId}

Export vlun for volume identified by {id} from HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_vluns_create_input import DeviceType4VlunsCreateInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    device_type4_vluns_create_input = dscc.DeviceType4VlunsCreateInput() # DeviceType4VlunsCreateInput | 

    try:
        # Export vlun for volume identified by {id} from HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_vlun_export(system_id, id, device_type4_vluns_create_input)
        print("The response of VolumesApi->device_type4_vlun_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_vlun_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **device_type4_vluns_create_input** | [**DeviceType4VlunsCreateInput**](DeviceType4VlunsCreateInput.md)|  | 

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

# **device_type4_vlun_export_for_snapshot**
> TaskResponse device_type4_vlun_export_for_snapshot(system_id, snapshot_id, device_type4_vluns_create_input)

Export vlun for snapshot identified by {id} from HPE Alletra Storage MP identified by {systemId}

Export vlun for snapshot identified by {id} from HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_vluns_create_input import DeviceType4VlunsCreateInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    snapshot_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the snapshots
    device_type4_vluns_create_input = dscc.DeviceType4VlunsCreateInput() # DeviceType4VlunsCreateInput | 

    try:
        # Export vlun for snapshot identified by {id} from HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_vlun_export_for_snapshot(system_id, snapshot_id, device_type4_vluns_create_input)
        print("The response of VolumesApi->device_type4_vlun_export_for_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_vlun_export_for_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **snapshot_id** | **str**| UID of the snapshots | 
 **device_type4_vluns_create_input** | [**DeviceType4VlunsCreateInput**](DeviceType4VlunsCreateInput.md)|  | 

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

# **device_type4_vlun_unexport**
> TaskResponse device_type4_vlun_unexport(system_id, id, device_type4_un_export_vlun)

Unexport vlun for volume identified by {id} from HPE Alletra Storage MP identified by {systemId}

Unexport vlun for volume identified by {id} from HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_un_export_vlun import DeviceType4UnExportVlun
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    device_type4_un_export_vlun = dscc.DeviceType4UnExportVlun() # DeviceType4UnExportVlun | 

    try:
        # Unexport vlun for volume identified by {id} from HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_vlun_unexport(system_id, id, device_type4_un_export_vlun)
        print("The response of VolumesApi->device_type4_vlun_unexport:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_vlun_unexport: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **device_type4_un_export_vlun** | [**DeviceType4UnExportVlun**](DeviceType4UnExportVlun.md)|  | 

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

# **device_type4_vlun_unexport_for_snapshot**
> TaskResponse device_type4_vlun_unexport_for_snapshot(system_id, snapshot_id, device_type4_un_export_vlun)

Unexport vlun for snapshot identified by {id} from HPE Alletra Storage MP identified by {systemId}

Unexport vlun for snapshot identified by {id} from HPE Alletra Storage MP identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_un_export_vlun import DeviceType4UnExportVlun
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    snapshot_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the snapshots
    device_type4_un_export_vlun = dscc.DeviceType4UnExportVlun() # DeviceType4UnExportVlun | 

    try:
        # Unexport vlun for snapshot identified by {id} from HPE Alletra Storage MP identified by {systemId}
        api_response = api_instance.device_type4_vlun_unexport_for_snapshot(system_id, snapshot_id, device_type4_un_export_vlun)
        print("The response of VolumesApi->device_type4_vlun_unexport_for_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_vlun_unexport_for_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **snapshot_id** | **str**| UID of the snapshots | 
 **device_type4_un_export_vlun** | [**DeviceType4UnExportVlun**](DeviceType4UnExportVlun.md)|  | 

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

# **device_type4_vluns_delete**
> TaskResponse device_type4_vluns_delete(system_id, volume_id, id)

Remove vlun idenfied by {id} form volume identified by {volumeId} from HPE Alletra Storage MP

Remove vlun idenfied by {id} form volume identified by {volumeId} from HPE Alletra Storage MP

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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    volume_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the vlun

    try:
        # Remove vlun idenfied by {id} form volume identified by {volumeId} from HPE Alletra Storage MP
        api_response = api_instance.device_type4_vluns_delete(system_id, volume_id, id)
        print("The response of VolumesApi->device_type4_vluns_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_vluns_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
 **id** | **str**| UID of the vlun | 

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

# **device_type4_vluns_get_by_id**
> DeviceType4VlunsListSingle device_type4_vluns_get_by_id(system_id, volume_id, id, select=select)

Get details of vlun identified by {id} for Volume identified by {volumeId} for HPE Alletra Storage MP

Get details of vlun identified by {id} for Volume identified by {volumeId} for HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_vluns_list_single import DeviceType4VlunsListSingle
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    volume_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the vlun
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of vlun identified by {id} for Volume identified by {volumeId} for HPE Alletra Storage MP
        api_response = api_instance.device_type4_vluns_get_by_id(system_id, volume_id, id, select=select)
        print("The response of VolumesApi->device_type4_vluns_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_vluns_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
 **id** | **str**| UID of the vlun | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4VlunsListSingle**](DeviceType4VlunsListSingle.md)

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

# **device_type4_vluns_list**
> DeviceType4VlunsSummaryList device_type4_vluns_list(system_id, id, select=select, limit=limit, offset=offset, filter=filter, sort=sort)

Get details of vluns for Volume identified by {volumeId} for HPE Alletra Storage MP

Get details of vluns for Volume identified by {volumeId} for HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_vluns_summary_list import DeviceType4VlunsSummaryList
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq array1 and wwn eq 2FF70002AC018D94' # str | oData query to filter by Key. (optional)
    sort = 'id asc,name desc' # str | Query to sort the response with specified key and order (optional)

    try:
        # Get details of vluns for Volume identified by {volumeId} for HPE Alletra Storage MP
        api_response = api_instance.device_type4_vluns_list(system_id, id, select=select, limit=limit, offset=offset, filter=filter, sort=sort)
        print("The response of VolumesApi->device_type4_vluns_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_vluns_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| Query to sort the response with specified key and order | [optional] 

### Return type

[**DeviceType4VlunsSummaryList**](DeviceType4VlunsSummaryList.md)

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

# **device_type4_volume_capacity_history_get_by_id**
> DeviceType4VolumeCapacityHistory device_type4_volume_capacity_history_get_by_id(system_id, id, select=select, range=range, time_interval_min=time_interval_min)

Get volume capacity trend data of HPE Alletra Storage MP Volume identified by {id}

Get volume capacity trend data of HPE Alletra Storage MP Volume identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_volume_capacity_history import DeviceType4VolumeCapacityHistory
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)

    try:
        # Get volume capacity trend data of HPE Alletra Storage MP Volume identified by {id}
        api_response = api_instance.device_type4_volume_capacity_history_get_by_id(system_id, id, select=select, range=range, time_interval_min=time_interval_min)
        print("The response of VolumesApi->device_type4_volume_capacity_history_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_volume_capacity_history_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**DeviceType4VolumeCapacityHistory**](DeviceType4VolumeCapacityHistory.md)

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

# **device_type4_volume_clone_create**
> TaskResponse device_type4_volume_clone_create(system_id, id, device_type4_create_clone_volume_input)

Create a clone volume identified by {id} for HPE Alletra Storage MP systems.

Create a clone volume identified by {id} for HPE Alletra Storage MP systems.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_create_clone_volume_input import DeviceType4CreateCloneVolumeInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    device_type4_create_clone_volume_input = dscc.DeviceType4CreateCloneVolumeInput() # DeviceType4CreateCloneVolumeInput | 

    try:
        # Create a clone volume identified by {id} for HPE Alletra Storage MP systems.
        api_response = api_instance.device_type4_volume_clone_create(system_id, id, device_type4_create_clone_volume_input)
        print("The response of VolumesApi->device_type4_volume_clone_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_volume_clone_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **device_type4_create_clone_volume_input** | [**DeviceType4CreateCloneVolumeInput**](DeviceType4CreateCloneVolumeInput.md)|  | 

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

# **device_type4_volume_create**
> TaskResponse device_type4_volume_create(system_id, device_type4_create_volume_input)

Create volume for a storage system HPE Alletra Storage MP

Create volume for a storage system HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_create_volume_input import DeviceType4CreateVolumeInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    device_type4_create_volume_input = dscc.DeviceType4CreateVolumeInput() # DeviceType4CreateVolumeInput | 

    try:
        # Create volume for a storage system HPE Alletra Storage MP
        api_response = api_instance.device_type4_volume_create(system_id, device_type4_create_volume_input)
        print("The response of VolumesApi->device_type4_volume_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_volume_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **device_type4_create_volume_input** | [**DeviceType4CreateVolumeInput**](DeviceType4CreateVolumeInput.md)|  | 

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

# **device_type4_volume_delete**
> TaskResponse device_type4_volume_delete(system_id, id, un_export=un_export, cascade=cascade)

Remove volume identified by {volumeId} from HPE Alletra Storage MP

Remove volume identified by {volumeId} from HPE Alletra Storage MP

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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    un_export = true # bool | UnExport Host,HostSet and delete volume (optional)
    cascade = true # bool | Delete snapshot and volume (optional)

    try:
        # Remove volume identified by {volumeId} from HPE Alletra Storage MP
        api_response = api_instance.device_type4_volume_delete(system_id, id, un_export=un_export, cascade=cascade)
        print("The response of VolumesApi->device_type4_volume_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_volume_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **un_export** | **bool**| UnExport Host,HostSet and delete volume | [optional] 
 **cascade** | **bool**| Delete snapshot and volume | [optional] 

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

# **device_type4_volume_edit**
> TaskResponse device_type4_volume_edit(system_id, id, device_type4_volume_put)

Edit volume identified by {volumeId} from HPE Alletra Storage MP

Edit volume identified by {volumeId} from HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_volume_put import DeviceType4VolumePut
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    device_type4_volume_put = dscc.DeviceType4VolumePut() # DeviceType4VolumePut | 

    try:
        # Edit volume identified by {volumeId} from HPE Alletra Storage MP
        api_response = api_instance.device_type4_volume_edit(system_id, id, device_type4_volume_put)
        print("The response of VolumesApi->device_type4_volume_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_volume_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **device_type4_volume_put** | [**DeviceType4VolumePut**](DeviceType4VolumePut.md)|  | 

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

# **device_type4_volume_get_by_id**
> DeviceType4VolumeDetails device_type4_volume_get_by_id(system_id, id, select=select)

Get details of HPE Alletra Storage MP Volume identified by {id}

Get details of HPE Alletra Storage MP Volume identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_volume_details import DeviceType4VolumeDetails
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of HPE Alletra Storage MP Volume identified by {id}
        api_response = api_instance.device_type4_volume_get_by_id(system_id, id, select=select)
        print("The response of VolumesApi->device_type4_volume_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_volume_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4VolumeDetails**](DeviceType4VolumeDetails.md)

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

# **device_type4_volume_performance_history_get_by_id**
> DeviceType4VolumePerformanceHistory device_type4_volume_performance_history_get_by_id(system_id, id, select=select, range=range, time_interval_min=time_interval_min)

Get performance trend data of HPE Alletra Storage MP Volume identified by {id}

Get performance trend data of HPE Alletra Storage MP Volume identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_volume_performance_history import DeviceType4VolumePerformanceHistory
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)
    range = 'startTime eq 1605063600 and endTime eq 1605186000' # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)

    try:
        # Get performance trend data of HPE Alletra Storage MP Volume identified by {id}
        api_response = api_instance.device_type4_volume_performance_history_get_by_id(system_id, id, select=select, range=range, time_interval_min=time_interval_min)
        print("The response of VolumesApi->device_type4_volume_performance_history_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_volume_performance_history_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**DeviceType4VolumePerformanceHistory**](DeviceType4VolumePerformanceHistory.md)

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

# **device_type4_volume_performance_statistics_get_by_id**
> DeviceType4VolumePerformance device_type4_volume_performance_statistics_get_by_id(system_id, id, select=select)

Get performance statistics of HPE Alletra Storage MP Volume identified by {id}

Get performance statistics of HPE Alletra Storage MP Volume identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_volume_performance import DeviceType4VolumePerformance
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get performance statistics of HPE Alletra Storage MP Volume identified by {id}
        api_response = api_instance.device_type4_volume_performance_statistics_get_by_id(system_id, id, select=select)
        print("The response of VolumesApi->device_type4_volume_performance_statistics_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_volume_performance_statistics_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4VolumePerformance**](DeviceType4VolumePerformance.md)

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

# **device_type4_volume_snapshot_create**
> TaskResponse device_type4_volume_snapshot_create(system_id, id, device_type4_volume_post)

Create snapshot for volumes identified by {id}

Create snapshot for volumes identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_volume_post import DeviceType4VolumePost
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    device_type4_volume_post = dscc.DeviceType4VolumePost() # DeviceType4VolumePost | 

    try:
        # Create snapshot for volumes identified by {id}
        api_response = api_instance.device_type4_volume_snapshot_create(system_id, id, device_type4_volume_post)
        print("The response of VolumesApi->device_type4_volume_snapshot_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_volume_snapshot_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **device_type4_volume_post** | [**DeviceType4VolumePost**](DeviceType4VolumePost.md)|  | 

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

# **device_type4_volume_snapshot_get_by_id**
> TaskResponse device_type4_volume_snapshot_get_by_id(system_id, volume_id, snapshot_id, force=force)

Remove HPE Alletra Storage MP snapshot in system identified by {snapshotId}

Remove HPE Alletra Storage MP snapshot in system identified by {snapshotId}

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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    volume_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    snapshot_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | Identifier of snapshot.
    force = true # bool | Make snapshot offline and remove. (optional)

    try:
        # Remove HPE Alletra Storage MP snapshot in system identified by {snapshotId}
        api_response = api_instance.device_type4_volume_snapshot_get_by_id(system_id, volume_id, snapshot_id, force=force)
        print("The response of VolumesApi->device_type4_volume_snapshot_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_volume_snapshot_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
 **snapshot_id** | **str**| Identifier of snapshot. | 
 **force** | **bool**| Make snapshot offline and remove. | [optional] 

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

# **device_type4_volume_snapshots_list**
> DeviceType4SnapshotsSummaryList device_type4_volume_snapshots_list(system_id, id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get snapshot details of volume identified by {id} for HPE Alletra Storage MP

Get snapshot details of volume identified by {id} for HPE Alletra Storage MP

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.device_type4_snapshots_summary_list import DeviceType4SnapshotsSummaryList
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq array1 and wwn eq 2FF70002AC018D94' # str | oData query to filter by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get snapshot details of volume identified by {id} for HPE Alletra Storage MP
        api_response = api_instance.device_type4_volume_snapshots_list(system_id, id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of VolumesApi->device_type4_volume_snapshots_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_volume_snapshots_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| oData query to sort by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**DeviceType4SnapshotsSummaryList**](DeviceType4SnapshotsSummaryList.md)

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

# **device_type4_volumes_list**
> DeviceType4VolumesList device_type4_volumes_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all volumes details for HPE Alletra Storage MP

Get all volumes details for HPE Alletra Storage MP

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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq array1 and wwn eq 2FF70002AC018D94' # str | oData query to filter by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all volumes details for HPE Alletra Storage MP
        api_response = api_instance.device_type4_volumes_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of VolumesApi->device_type4_volumes_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->device_type4_volumes_list: %s\n" % e)
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

# **snapshot_clone_create**
> TaskResponse snapshot_clone_create(system_id, snapshot_id, create_clone_snapshot_input)

Create a clone of a snapshot identified by {snapshotId} for Primera / Alletra 9K systems.

Create a clone of a snapshot identified by {snapshotId} for Primera / Alletra 9K systems.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.create_clone_snapshot_input import CreateCloneSnapshotInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    snapshot_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the snapshots
    create_clone_snapshot_input = dscc.CreateCloneSnapshotInput() # CreateCloneSnapshotInput | 

    try:
        # Create a clone of a snapshot identified by {snapshotId} for Primera / Alletra 9K systems.
        api_response = api_instance.snapshot_clone_create(system_id, snapshot_id, create_clone_snapshot_input)
        print("The response of VolumesApi->snapshot_clone_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->snapshot_clone_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **snapshot_id** | **str**| UID of the snapshots | 
 **create_clone_snapshot_input** | [**CreateCloneSnapshotInput**](CreateCloneSnapshotInput.md)|  | 

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

# **vluns_delete**
> TaskResponse vluns_delete(system_id, volume_id, id)

Remove vlun idenfied by {id} form volume identified by {volumeId} from Primera / Alletra 9K

Remove vlun idenfied by {id} form volume identified by {volumeId} from Primera / Alletra 9K

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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    volume_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID of the vlun

    try:
        # Remove vlun idenfied by {id} form volume identified by {volumeId} from Primera / Alletra 9K
        api_response = api_instance.vluns_delete(system_id, volume_id, id)
        print("The response of VolumesApi->vluns_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->vluns_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
 **id** | **str**| UID of the vlun | 

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

# **volume_clone_create**
> TaskResponse volume_clone_create(system_id, id, create_clone_volume_input)

Create a clone volume identified by {id} for Primera / Alletra 9K systems.

Create a clone volume identified by {id} for Primera / Alletra 9K systems.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.create_clone_volume_input import CreateCloneVolumeInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    create_clone_volume_input = dscc.CreateCloneVolumeInput() # CreateCloneVolumeInput | 

    try:
        # Create a clone volume identified by {id} for Primera / Alletra 9K systems.
        api_response = api_instance.volume_clone_create(system_id, id, create_clone_volume_input)
        print("The response of VolumesApi->volume_clone_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->volume_clone_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **create_clone_volume_input** | [**CreateCloneVolumeInput**](CreateCloneVolumeInput.md)|  | 

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

# **volume_create**
> TaskResponse volume_create(system_id, create_volume_input)

Create volume for a storage system Primera / Alletra 9K

Create volume for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.create_volume_input import CreateVolumeInput
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    create_volume_input = dscc.CreateVolumeInput() # CreateVolumeInput | 

    try:
        # Create volume for a storage system Primera / Alletra 9K
        api_response = api_instance.volume_create(system_id, create_volume_input)
        print("The response of VolumesApi->volume_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->volume_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **create_volume_input** | [**CreateVolumeInput**](CreateVolumeInput.md)|  | 

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

# **volume_delete**
> TaskResponse volume_delete(system_id, id, un_export=un_export, cascade=cascade)

Remove volume identified by {volumeId} from Primera / Alletra 9K

Remove volume identified by {volumeId} from Primera / Alletra 9K

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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    un_export = true # bool | UnExport Host,HostSet and delete volume (optional)
    cascade = true # bool | Delete snapshot and volume (optional)

    try:
        # Remove volume identified by {volumeId} from Primera / Alletra 9K
        api_response = api_instance.volume_delete(system_id, id, un_export=un_export, cascade=cascade)
        print("The response of VolumesApi->volume_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->volume_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **un_export** | **bool**| UnExport Host,HostSet and delete volume | [optional] 
 **cascade** | **bool**| Delete snapshot and volume | [optional] 

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

# **volume_edit**
> TaskResponse volume_edit(system_id, id, volume_put)

Edit volume identified by {volumeId} from Primera / Alletra 9K

Edit volume identified by {volumeId} from Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.models.volume_put import VolumePut
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    volume_put = dscc.VolumePut() # VolumePut | 

    try:
        # Edit volume identified by {volumeId} from Primera / Alletra 9K
        api_response = api_instance.volume_edit(system_id, id, volume_put)
        print("The response of VolumesApi->volume_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->volume_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **volume_put** | [**VolumePut**](VolumePut.md)|  | 

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

# **volume_get_by_id**
> FleetVolumeDetails volume_get_by_id(id, select=select)

Get details of Volume identified by {id}

Get details of Volume identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.fleet_volume_details import FleetVolumeDetails
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
    api_instance = dscc.VolumesApi(api_client)
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of Volume identified by {id}
        api_response = api_instance.volume_get_by_id(id, select=select)
        print("The response of VolumesApi->volume_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->volume_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UID(volumeuid) of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**FleetVolumeDetails**](FleetVolumeDetails.md)

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

# **volume_list_for_system_by_system_id**
> FleetVolumesList volume_list_for_system_by_system_id(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of volumes identified with {systemId}

Get details of volumes identified with {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.fleet_volumes_list import FleetVolumesList
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq array1 and wwn eq 2FF70002AC018D94' # str | oData query to filter by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get details of volumes identified with {systemId}
        api_response = api_instance.volume_list_for_system_by_system_id(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of VolumesApi->volume_list_for_system_by_system_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->volume_list_for_system_by_system_id: %s\n" % e)
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

[**FleetVolumesList**](FleetVolumesList.md)

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

# **volume_snapshot_create**
> TaskResponse volume_snapshot_create(system_id, id, volume_post)

Create snapshot for volumes identified by {id}

Create snapshot for volumes identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.task_response import TaskResponse
from dscc.models.volume_post import VolumePost
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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    volume_post = dscc.VolumePost() # VolumePost | 

    try:
        # Create snapshot for volumes identified by {id}
        api_response = api_instance.volume_snapshot_create(system_id, id, volume_post)
        print("The response of VolumesApi->volume_snapshot_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->volume_snapshot_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **volume_post** | [**VolumePost**](VolumePost.md)|  | 

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

# **volume_snapshot_get_by_id**
> TaskResponse volume_snapshot_get_by_id(system_id, volume_id, snapshot_id, force=force)

Remove Primera / Alletra 9K snapshot in system identified by {snapshotId}

Remove Primera / Alletra 9K snapshot in system identified by {snapshotId}

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
    api_instance = dscc.VolumesApi(api_client)
    system_id = '7CE751P312' # str | systemId of the storage system
    volume_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | UID(volumeuid) of the storage system
    snapshot_id = 'a7c4e6593f51d0b98f0e40d7e6df04fd' # str | Identifier of snapshot.
    force = true # bool | Make snapshot offline and remove. (optional)

    try:
        # Remove Primera / Alletra 9K snapshot in system identified by {snapshotId}
        api_response = api_instance.volume_snapshot_get_by_id(system_id, volume_id, snapshot_id, force=force)
        print("The response of VolumesApi->volume_snapshot_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->volume_snapshot_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
 **snapshot_id** | **str**| Identifier of snapshot. | 
 **force** | **bool**| Make snapshot offline and remove. | [optional] 

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

# **volumes_list**
> FleetVolumesList volumes_list(limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all volumes

Get all volumes

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import dscc
from dscc.models.fleet_volumes_list import FleetVolumesList
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
    api_instance = dscc.VolumesApi(api_client)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = 'name eq array1 and wwn eq 2FF70002AC018D94' # str | oData query to filter by Key. (optional)
    sort = 'systemWWN desc' # str | oData query to sort by Key. (optional)
    select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all volumes
        api_response = api_instance.volumes_list(limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        print("The response of VolumesApi->volumes_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumesApi->volumes_list: %s\n" % e)
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

[**FleetVolumesList**](FleetVolumesList.md)

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

