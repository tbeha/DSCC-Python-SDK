# DiskCapacity

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
from dscc.models.disk_capacity import DiskCapacity

# TODO update the JSON string below
json = "{}"
# create an instance of DiskCapacity from a JSON string
disk_capacity_instance = DiskCapacity.from_json(json)
# print the JSON string representation of the object
print(DiskCapacity.to_json())

# convert the object into a dict
disk_capacity_dict = disk_capacity_instance.to_dict()
# create an instance of DiskCapacity from a dict
disk_capacity_from_dict = DiskCapacity.from_dict(disk_capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


