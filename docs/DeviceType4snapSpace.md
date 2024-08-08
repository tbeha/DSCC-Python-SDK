# DeviceType4snapSpace

snapSpace information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ld_count** | **float** | Number of Logical Disks | [optional] 
**total_mi_b** | **float** | Total logical capacity (MiB) | [optional] 
**total_raw_mi_b** | **float** | Total physical (raw) capacity (MiB) | [optional] 
**used_mi_b** | **float** | Used logical capacity (MiB) | [optional] 
**used_raw_mi_b** | **float** | Used physical (raw) capacity (MiB) | [optional] 

## Example

```python
from dscc.models.device_type4snap_space import DeviceType4snapSpace

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4snapSpace from a JSON string
device_type4snap_space_instance = DeviceType4snapSpace.from_json(json)
# print the JSON string representation of the object
print(DeviceType4snapSpace.to_json())

# convert the object into a dict
device_type4snap_space_dict = device_type4snap_space_instance.to_dict()
# create an instance of DeviceType4snapSpace from a dict
device_type4snap_space_from_dict = DeviceType4snapSpace.from_dict(device_type4snap_space_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


