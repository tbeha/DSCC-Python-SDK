# DeviceType4DiskCapacity

Capacity of the Disk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated_mi_b** | **int** | allocated Size in MiB | [optional] 
**failed_mi_b** | **int** | failed Size in MiB | [optional] 
**free_mi_b** | **int** | free Size in MiB | [optional] 
**total_mi_b** | **int** | total Size in MiB. | [optional] 
**unavailable_mi_b** | **int** | unavailable Size in MiB | [optional] 

## Example

```python
from dscc.models.device_type4_disk_capacity import DeviceType4DiskCapacity

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4DiskCapacity from a JSON string
device_type4_disk_capacity_instance = DeviceType4DiskCapacity.from_json(json)
# print the JSON string representation of the object
print(DeviceType4DiskCapacity.to_json())

# convert the object into a dict
device_type4_disk_capacity_dict = device_type4_disk_capacity_instance.to_dict()
# create an instance of DeviceType4DiskCapacity from a dict
device_type4_disk_capacity_from_dict = DeviceType4DiskCapacity.from_dict(device_type4_disk_capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


