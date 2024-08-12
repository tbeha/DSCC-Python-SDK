# DeviceType4disksList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admit_time** | [**DeviceType4AdmitTime**](DeviceType4AdmitTime.md) |  | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**capacity** | [**DeviceType4filterDiskCapacity**](DeviceType4filterDiskCapacity.md) |  | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**consumable_size_mi_b** | **int** | consumable size of disk in MiB | [optional] 
**customer_id** | **str** | customerId | [optional] 
**dev_type** | **str** | Type of the disk. | [optional] 
**disk_id** | **int** | id of the disk | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**enclosure_uid** | **str** | Unique Identifier of the enclosure | [optional] 
**fw_status** | **str** | firmware status | [optional] 
**fw_version** | **str** | firmware version | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**insert_time** | [**DeviceType4AdmitTime**](DeviceType4AdmitTime.md) |  | [optional] 
**life_left_pct** | **float** | Life Left Percentage | [optional] 
**manufacturing** | [**DeviceType4ManufacturingSingle**](DeviceType4ManufacturingSingle.md) |  | [optional] 
**media_type** | **str** | Media Type of the disk | [optional] 
**mfg_capacity_gb** | **int** | manufacturing capacity of disk in GB | [optional] 
**paths** | [**List[DeviceType4DiskLoopInner]**](DeviceType4DiskLoopInner.md) | Disk Loop | [optional] 
**position_last** | [**DeviceType4DiskPosition**](DeviceType4DiskPosition.md) |  | [optional] 
**position_now** | [**DeviceType4filterDiskPositionNow**](DeviceType4filterDiskPositionNow.md) |  | [optional] 
**protocol** | **str** | protocol over the disk | [optional] 
**raw_size_mi_b** | **int** | raw Size of disk in GB | [optional] 
**read_errors** | [**DeviceType4ErrorCount**](DeviceType4ErrorCount.md) |  | [optional] 
**resource_uri** | **str** | resourceUri for detailed disk object | [optional] 
**sed_status** | **str** | SED Status | [optional] 
**state** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**system_id** | **str** | SystemId/SerialNumber of the array. | [optional] 
**type** | **str** | type | [optional] 
**write_errors** | [**DeviceType4ErrorCount**](DeviceType4ErrorCount.md) |  | [optional] 
**wwn** | **str** | unique WWN of the disk. &#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.device_type4disks_list import DeviceType4disksList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4disksList from a JSON string
device_type4disks_list_instance = DeviceType4disksList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4disksList.to_json())

# convert the object into a dict
device_type4disks_list_dict = device_type4disks_list_instance.to_dict()
# create an instance of DeviceType4disksList from a dict
device_type4disks_list_from_dict = DeviceType4disksList.from_dict(device_type4disks_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


