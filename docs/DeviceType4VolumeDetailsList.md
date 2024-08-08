# DeviceType4VolumeDetailsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_allocation_settings** | [**DeviceType4userAllocationSettings**](DeviceType4userAllocationSettings.md) |  | [optional] 
**associated_links** | [**List[DeviceType4ReplicationPartnerCommonFieldsAssociatedLinksInner]**](DeviceType4ReplicationPartnerCommonFieldsAssociatedLinksInner.md) | Associated Links | [optional] 
**base_id** | **int** | snapshot Tdvv Size | [optional] 
**comment** | **str** | Comments | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**compression_policy** | **str** | Compression Policy | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**conversion_type** | **str** | Conversion Type of Volume | [optional] 
**copy_of_id** | **int** | Copy of Id | [optional] 
**creation_time** | [**DeviceType4VolumeDetailsListCreationTime**](DeviceType4VolumeDetailsListCreationTime.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**data_reduction** | **str** | Data Reduction type. Possible values:               - DATA_REDUCTION_ON               - DATA_REDUCTION_OFF               - DATA_REDUCTION_DISABLED | [optional] 
**dedup** | **str** | Field to indicate Dedup status | [optional] 
**dev_type** | **str** | Device Type &#x60;Filter&#x60; | [optional] 
**displayname** | **str** | Display name of the volume | [optional] 
**domain** | **str** | Domain of the volume | [optional] 
**efficiency_update_time** | [**DeprecatedDeviceType4calendar**](DeprecatedDeviceType4calendar.md) |  | [optional] 
**expiration_time** | [**DeprecatedDeviceType4calendar**](DeprecatedDeviceType4calendar.md) |  | [optional] 
**fully_provisioned** | **bool** |  | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**heads_per_cylinder** | **int** | Heads per Cylinder | [optional] 
**health_state** | **int** | Health status of the Volume. &#x60;Filter, Sort&#x60; | [optional] 
**hidden** | **bool** | Flag to know if the Volume is hidden or not | [optional] 
**id** | **str** | UUID string uniquely identifying the storage system object. &#x60;Filter&#x60; | [optional] 
**initiators** | [**List[DeviceType4ApplicationSetDetailsInitiatorsInner]**](DeviceType4ApplicationSetDetailsInitiatorsInner.md) | Initiator details, this field is deprecated | [optional] 
**name** | **str** | A user friendly name to identify the storage system volume (resourceName). &#x60;Filter, Sort&#x60; | [optional] 
**nguid** | **str** | Namespace Globally Unique Identifier. This data is available only for NVMe enabled storage system. &#x60;Filter&#x60; | [optional] 
**parent_id** | **int** | Parent Id &#x60;Filter&#x60; | [optional] 
**phys_parent_id** | **int** | physical Parent Id | [optional] 
**physical_copy** | **bool** |  | [optional] 
**policy** | [**DeviceType4policy**](DeviceType4policy.md) |  | [optional] 
**prov_type** | **str** | Description | [optional] 
**raid** | **str** | Raid | [optional] 
**rcopy_status** | **str** | RemoteCopy Status | [optional] 
**read_only** | **bool** |  | [optional] 
**resource_uri** | **str** | resourceUri for detailed volume object | [optional] 
**retention_time** | [**DeprecatedDeviceType4calendar**](DeprecatedDeviceType4calendar.md) |  | [optional] 
**ro_child_id** | **int** | RO child id. This field is deprecated. | [optional] 
**rw_child_id** | **int** | This field is deprecated. | [optional] 
**sectors_per_track** | **int** | Sector per Track | [optional] 
**shared_parent_id** | **int** | Shared Parent Id | [optional] 
**snap_shot_tier** | **str** | Snapshot Tier | [optional] 
**snapshot_alloc_limit** | **int** | Snapshot alloc limit. This field is deprecated. | [optional] 
**snapshot_alloc_warning** | **int** | Snapshot alloc Warning. This field is deprecated. | [optional] 
**snapshot_allocation_settings** | [**DeprecatedDeviceType4userAllocationSettingsSingle**](DeprecatedDeviceType4userAllocationSettingsSingle.md) |  | [optional] 
**space_calculation_time** | [**DeprecatedDeviceType4calendar**](DeprecatedDeviceType4calendar.md) |  | [optional] 
**started** | **bool** |  | [optional] 
**state** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**storage_tier** | **str** | Storage Tier | [optional] 
**system_id** | **str** | SystemUid/serialNumber of the array. | [optional] 
**thin_provisioned** | **bool** | Description | [optional] 
**type** | **str** | type | [optional] 
**unref_space_freed_time** | [**DeprecatedDeviceType4calendar**](DeprecatedDeviceType4calendar.md) |  | [optional] 
**user_alloc_limit** | **int** | User alloc limit | [optional] 
**user_alloc_warning** | **int** | User alloc space limit warning | [optional] 
**user_allocation_settings** | [**DeviceType4userAllocationSettings**](DeviceType4userAllocationSettings.md) |  | [optional] 
**user_cpg_id** | **int** | User CPG Id &#x60;Filter&#x60; | [optional] 
**user_cpg_name** | **str** | User CPG Name | [optional] 
**vlun_sector_size** | **int** | VLUN sector size | [optional] 
**volume_capacity** | [**DeviceType4VolumeCapacity**](DeviceType4VolumeCapacity.md) |  | [optional] 
**volume_id** | **int** | Numeric ID of the resource | [optional] 
**volume_performance** | [**DeviceType4volumePerformanceDetails**](DeviceType4volumePerformanceDetails.md) |  | [optional] 
**volume_type** | **str** | VV Type | [optional] 
**wwn** | **str** | Volume wwn. &#x60;Filter&#x60; | [optional] 

## Example

```python
from dscc.models.device_type4_volume_details_list import DeviceType4VolumeDetailsList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VolumeDetailsList from a JSON string
device_type4_volume_details_list_instance = DeviceType4VolumeDetailsList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VolumeDetailsList.to_json())

# convert the object into a dict
device_type4_volume_details_list_dict = device_type4_volume_details_list_instance.to_dict()
# create an instance of DeviceType4VolumeDetailsList from a dict
device_type4_volume_details_list_from_dict = DeviceType4VolumeDetailsList.from_dict(device_type4_volume_details_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


