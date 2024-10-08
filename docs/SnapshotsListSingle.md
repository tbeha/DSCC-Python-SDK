# SnapshotsListSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_allocation_settings** | [**UserAllocationSettingsSingle**](UserAllocationSettingsSingle.md) |  | [optional] 
**admin_space** | [**Space**](Space.md) |  | [optional] 
**base_id** | **int** | snapshot Tdvv Size | [optional] 
**comment** | **str** | Comments | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**compact_efficiency** | **float** | Compact Efficiency | [optional] 
**compression_efficiency** | **float** | Compression Efficiency | [optional] 
**compression_policy** | **str** | compression policy | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**conversion_type** | **str** | Conversion Type of Volume | [optional] 
**copied_mb** | **float** | Copied MB | [optional] 
**copied_perc** | **int** | Copied Perecentage | [optional] 
**copy_of_id** | **int** | Copy of ID | [optional] 
**creation_time** | [**DeviceType4SnapshotsListSingleCreationTime**](DeviceType4SnapshotsListSingleCreationTime.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**data_reduction** | **str** | Data Reduction type | [optional] 
**ddc_size** | **float** | Note, will be updated at most once in an hour | [optional] 
**dds_size** | **float** |  | [optional] 
**dedup** | **str** |  | [optional] 
**dedup_savings_size** | **float** | Note, will be updated at most once in an hour | [optional] 
**dedup_written_size** | **float** | Note, will be updated at most once in an hour | [optional] 
**dev_type** | **str** | Device Type | [optional] 
**displayname** | **str** | Display name of the volume | [optional] 
**domain** | **str** | Domain of the volume | [optional] 
**efficiency_update_time** | [**Calendar**](Calendar.md) |  | [optional] 
**expiration_time** | [**Calendar**](Calendar.md) |  | [optional] 
**fully_provisioned** | **bool** |  | [optional] 
**generation** | **int** | generation | [optional] 
**heads_per_cylinder** | **int** | Heads per Cylinder | [optional] 
**health_state** | **int** | Health status of the Volume. | [optional] 
**hidden** | **bool** | Flag to know if the Volume is hidden or not | [optional] 
**host_written_mi_b** | **float** | Host written data size in MiB. | [optional] 
**host_written_to_virtual_percent** | **float** | Host written to virtual percent | [optional] 
**id** | **str** | UID of the snapshot. &#x60;Filter&#x60; | [optional] 
**initiators** | [**List[DeviceType4ApplicationSetDetailsInitiatorsInner]**](DeviceType4ApplicationSetDetailsInitiatorsInner.md) | Initiator details | [optional] 
**name** | **str** | A user friendly name to identify the storage system volume (resourceName). | [optional] 
**parent_id** | **int** | Parent Id | [optional] 
**phys_parent_id** | **int** | physical Parent Id | [optional] 
**physical_copy** | **bool** |  | [optional] 
**policy** | [**Policy**](Policy.md) |  | [optional] 
**prov_type** | **str** | Provisioning type | [optional] 
**raid** | **str** | Raid | [optional] 
**rcopy_status** | **str** | RemoteCopy Status | [optional] 
**read_only** | **bool** |  | [optional] 
**retention_time** | [**Calendar**](Calendar.md) |  | [optional] 
**ro_child_id** | **int** | RO child id | [optional] 
**rw_child_id** | **int** |  | [optional] 
**sectors_per_track** | **int** | Sector per Track | [optional] 
**shared_parent_id** | **int** | Shared Parent Id | [optional] 
**size_mi_b** | **float** | Size in MiB | [optional] 
**snapshot_alloc_limit** | **int** | Snapshot alloc limit | [optional] 
**snapshot_alloc_warning** | **int** | Snapshot alloc Warning | [optional] 
**snapshot_allocation_settings** | [**UserAllocationSettingsSingle**](UserAllocationSettingsSingle.md) |  | [optional] 
**snapshot_cpg_id** | **int** | Snapshot CPG Id | [optional] 
**snapshot_cpg_name** | **str** | Snapshot CPG name | [optional] 
**snapshot_id** | **int** | Numeric ID of the resource | [optional] 
**snapshot_space** | [**Space**](Space.md) |  | [optional] 
**snapshot_tdvv_size** | [**SnapshotTdvvsize**](SnapshotTdvvsize.md) |  | [optional] 
**snapshot_type** | **str** |  | [optional] 
**snapshot_used_to_virtual_percent** | **float** | Snapshot used to virtual percent | [optional] 
**space_calculation_time** | [**Calendar**](Calendar.md) |  | [optional] 
**started** | **bool** |  | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**system_id** | **str** | SystemUid/serialNumber of the array. | [optional] 
**thin_provisioned** | **bool** | Thin provisioning details | [optional] 
**total_raw_reserved_mi_b** | **float** | Total Raw Reserved Space in MiB | [optional] 
**total_reserved_mi_b** | **float** | Description | [optional] 
**total_space_mi_b** | **float** | Total Space in MiB | [optional] 
**type** | **str** | type | [optional] 
**unref_space_freed_time** | [**Calendar**](Calendar.md) |  | [optional] 
**used_capacity** | **float** | Used volume capacity. | [optional] 
**used_size_mi_b** | **float** | Used Size in MiB | [optional] 
**user_alloc_limit** | **int** | User alloc limit | [optional] 
**user_alloc_warning** | **int** | User alloc space limit warning | [optional] 
**user_allocation_settings** | [**UserAllocationSettingsSingle**](UserAllocationSettingsSingle.md) |  | [optional] 
**user_cpg_id** | **int** | User CPG Id | [optional] 
**user_cpg_name** | **str** | User CPG Name | [optional] 
**user_reserved_to_virtual_percent** | **float** | User reseved to virtual percent | [optional] 
**user_space** | [**Space**](Space.md) |  | [optional] 
**user_used_to_virtual_percent** | **float** | User used to virtual percent | [optional] 
**vlun_sector_size** | **int** | VLUN sector size | [optional] 
**wwn** | **str** | Volume wwn. | [optional] 

## Example

```python
from dscc.models.snapshots_list_single import SnapshotsListSingle

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotsListSingle from a JSON string
snapshots_list_single_instance = SnapshotsListSingle.from_json(json)
# print the JSON string representation of the object
print(SnapshotsListSingle.to_json())

# convert the object into a dict
snapshots_list_single_dict = snapshots_list_single_instance.to_dict()
# create an instance of SnapshotsListSingle from a dict
snapshots_list_single_from_dict = SnapshotsListSingle.from_dict(snapshots_list_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


