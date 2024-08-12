# DeviceType4SnapshotsListSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_allocation_settings** | [**DeviceType4userAllocationSettingsSingle**](DeviceType4userAllocationSettingsSingle.md) |  | [optional] 
**base_id** | **int** | snapshot Tdvv Size | [optional] 
**comment** | **str** | Comments | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**compression_policy** | **str** | compression policy | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**conversion_type** | **str** | Conversion Type of Volume | [optional] 
**copy_of_id** | **int** | Copy of ID | [optional] 
**creation_time** | [**DeviceType4SnapshotsListSingleCreationTime**](DeviceType4SnapshotsListSingleCreationTime.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**data_reduction** | **str** | Data Reduction type | [optional] 
**dedup** | **str** |  | [optional] 
**dev_type** | **str** | Device Type | [optional] 
**displayname** | **str** | Display name of the volume | [optional] 
**domain** | **str** | Domain of the volume | [optional] 
**efficiency_update_time** | [**DeprecatedDeviceType4calendar**](DeprecatedDeviceType4calendar.md) |  | [optional] 
**expiration_time** | [**DeprecatedDeviceType4calendar**](DeprecatedDeviceType4calendar.md) |  | [optional] 
**fully_provisioned** | **bool** |  | [optional] 
**generation** | **int** | generation | [optional] 
**heads_per_cylinder** | **int** | Heads per Cylinder | [optional] 
**health_state** | **int** | Health status of the Volume. | [optional] 
**hidden** | **bool** | Flag to know if the Volume is hidden or not | [optional] 
**id** | **str** | UID of the snapshot. &#x60;Filter&#x60; | [optional] 
**initiators** | [**List[DeviceType4ApplicationSetDetailsInitiatorsInner]**](DeviceType4ApplicationSetDetailsInitiatorsInner.md) | Initiator details | [optional] 
**name** | **str** | A user friendly name to identify the storage system volume (resourceName). | [optional] 
**parent_id** | **int** | Parent Id | [optional] 
**phys_parent_id** | **int** | physical Parent Id | [optional] 
**physical_copy** | **bool** |  | [optional] 
**policy** | [**DeviceType4policy**](DeviceType4policy.md) |  | [optional] 
**prov_type** | **str** | Provisioning type | [optional] 
**raid** | **str** | Raid | [optional] 
**rcopy_status** | **str** | RemoteCopy Status | [optional] 
**read_only** | **bool** |  | [optional] 
**retention_time** | [**DeprecatedDeviceType4calendar**](DeprecatedDeviceType4calendar.md) |  | [optional] 
**ro_child_id** | **int** | RO child id | [optional] 
**rw_child_id** | **int** |  | [optional] 
**sectors_per_track** | **int** | Sector per Track | [optional] 
**shared_parent_id** | **int** | Shared Parent Id | [optional] 
**snapshot_alloc_limit** | **int** | Snapshot alloc limit. This field is deprecated. | [optional] 
**snapshot_alloc_warning** | **int** | Snapshot alloc Warning. This field is deprecated. | [optional] 
**snapshot_allocation_settings** | [**DeprecatedDeviceType4userAllocationSettingsSingle**](DeprecatedDeviceType4userAllocationSettingsSingle.md) |  | [optional] 
**snapshot_capacity** | [**DeviceType4SnapshotCapacity**](DeviceType4SnapshotCapacity.md) |  | [optional] 
**snapshot_id** | **int** | Numeric ID of the resource | [optional] 
**snapshot_type** | **str** |  | [optional] 
**space_calculation_time** | [**DeprecatedDeviceType4calendar**](DeprecatedDeviceType4calendar.md) |  | [optional] 
**started** | **bool** |  | [optional] 
**state** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**system_id** | **str** | SystemUid/serialNumber of the array. | [optional] 
**thin_provisioned** | **bool** | Thin provisioning details | [optional] 
**type** | **str** | type | [optional] 
**unref_space_freed_time** | [**DeprecatedDeviceType4calendar**](DeprecatedDeviceType4calendar.md) |  | [optional] 
**user_alloc_limit** | **int** | User alloc limit | [optional] 
**user_alloc_warning** | **int** | User alloc space limit warning | [optional] 
**user_allocation_settings** | [**DeviceType4userAllocationSettingsSingle**](DeviceType4userAllocationSettingsSingle.md) |  | [optional] 
**user_cpg_id** | **int** | User CPG Id | [optional] 
**user_cpg_name** | **str** | User CPG Name | [optional] 
**vlun_sector_size** | **int** | VLUN sector size | [optional] 
**wwn** | **str** | Volume wwn. | [optional] 

## Example

```python
from dscc.models.device_type4_snapshots_list_single import DeviceType4SnapshotsListSingle

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SnapshotsListSingle from a JSON string
device_type4_snapshots_list_single_instance = DeviceType4SnapshotsListSingle.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SnapshotsListSingle.to_json())

# convert the object into a dict
device_type4_snapshots_list_single_dict = device_type4_snapshots_list_single_instance.to_dict()
# create an instance of DeviceType4SnapshotsListSingle from a dict
device_type4_snapshots_list_single_from_dict = DeviceType4SnapshotsListSingle.from_dict(device_type4_snapshots_list_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


