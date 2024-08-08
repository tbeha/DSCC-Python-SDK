# DeviceType4VolumeCapacity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_space** | [**DeviceType4space**](DeviceType4space.md) |  | [optional] 
**branch_used_blocks_mi_b** | **float** | Branch used blocks size in MiB. This attribute contains the used space of the base volume and its Read-Only snapshots. This field is relevant for the system OS version 10.3.0 and above. | [optional] 
**branch_v_size_mi_b** | **float** | Branch virtual size in MiB. This attribute contains the provisioned or virtual size of the base volume and its Read-Only snapshots. | [optional] 
**compact_efficiency** | **float** | Compact Efficiency | [optional] 
**compression_efficiency** | **float** | Compression Efficiency | [optional] 
**copied_mb** | **float** | Copied MB | [optional] 
**copied_perc** | **int** | Copied Perecentage | [optional] 
**ddc_size** | **float** |  | [optional] 
**dds_size** | **float** |  | [optional] 
**dedup_savings_size** | **float** |  | [optional] 
**dedup_written_size** | **float** |  | [optional] 
**host_written_mi_b** | **float** | Host written data size in MiB. | [optional] 
**host_written_to_virtual_percent** | **float** | Host written to virtual percent | [optional] 
**size_mi_b** | **float** | Size in MiB &#x60;Filter, Sort&#x60; | [optional] 
**snapshot_tdvv_size** | [**DeviceType4snapshotTdvvsize**](DeviceType4snapshotTdvvsize.md) |  | [optional] 
**snapshot_used_to_virtual_percent** | **float** | Snapshot used to virtual percent | [optional] 
**thin_savings** | **str** | Thin savings for the detailed volume object | [optional] 
**total_raw_reserved_mi_b** | **float** | Total Raw Reserved Space in MiB | [optional] 
**total_reserved_mi_b** | **float** | Description | [optional] 
**total_space_mi_b** | **float** | Total Space in MiB | [optional] 
**used_blocks_mi_b** | **float** | Used Blocks Size in MiB. This attribute contains the used space of the base volume and its Read-Only snapshots. This field is relevant for the system OS versions equal and below 10.2.x. For the system OS version 10.3.0 and above, please refer the field branchUsedBlocksMiB. | [optional] 
**used_capacity** | **float** | Used volume capacity. &#x60;Filter, Sort&#x60; | [optional] 
**used_size_mi_b** | **float** | Used Size in MiB | [optional] 
**user_reserved_to_virtual_percent** | **float** | User reseved to virtual percent | [optional] 
**user_space** | [**DeviceType4space**](DeviceType4space.md) |  | [optional] 
**user_used_to_virtual_percent** | **float** | User used to virtual percent | [optional] 

## Example

```python
from dscc.models.device_type4_volume_capacity import DeviceType4VolumeCapacity

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VolumeCapacity from a JSON string
device_type4_volume_capacity_instance = DeviceType4VolumeCapacity.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VolumeCapacity.to_json())

# convert the object into a dict
device_type4_volume_capacity_dict = device_type4_volume_capacity_instance.to_dict()
# create an instance of DeviceType4VolumeCapacity from a dict
device_type4_volume_capacity_from_dict = DeviceType4VolumeCapacity.from_dict(device_type4_volume_capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


