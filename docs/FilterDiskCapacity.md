# FilterDiskCapacity

Capacity of the Disk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated_mi_b** | **int** | allocated Size in MiB | [optional] 
**failed_mi_b** | **int** | failed Size in MiB | [optional] 
**free_mi_b** | **int** | free Size in MiB | [optional] 
**total_mi_b** | **int** | total Size in MiB. &#x60;Filter, Sort&#x60; | [optional] 
**unavailable_mi_b** | **int** | unavailable Size in MiB | [optional] 

## Example

```python
from dscc.models.filter_disk_capacity import FilterDiskCapacity

# TODO update the JSON string below
json = "{}"
# create an instance of FilterDiskCapacity from a JSON string
filter_disk_capacity_instance = FilterDiskCapacity.from_json(json)
# print the JSON string representation of the object
print(FilterDiskCapacity.to_json())

# convert the object into a dict
filter_disk_capacity_dict = filter_disk_capacity_instance.to_dict()
# create an instance of FilterDiskCapacity from a dict
filter_disk_capacity_from_dict = FilterDiskCapacity.from_dict(filter_disk_capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


