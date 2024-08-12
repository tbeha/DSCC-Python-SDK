# DeviceType4DiskLoopInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**degraded** | **bool** | degraded loop | [optional] 
**disabled** | **bool** | disabled loop | [optional] 
**port** | [**DeviceType4DiskPortPosition**](DeviceType4DiskPortPosition.md) |  | [optional] 
**primary** | **bool** | primary loop | [optional] 

## Example

```python
from dscc.models.device_type4_disk_loop_inner import DeviceType4DiskLoopInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4DiskLoopInner from a JSON string
device_type4_disk_loop_inner_instance = DeviceType4DiskLoopInner.from_json(json)
# print the JSON string representation of the object
print(DeviceType4DiskLoopInner.to_json())

# convert the object into a dict
device_type4_disk_loop_inner_dict = device_type4_disk_loop_inner_instance.to_dict()
# create an instance of DeviceType4DiskLoopInner from a dict
device_type4_disk_loop_inner_from_dict = DeviceType4DiskLoopInner.from_dict(device_type4_disk_loop_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


