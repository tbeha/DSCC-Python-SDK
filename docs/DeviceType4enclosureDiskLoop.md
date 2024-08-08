# DeviceType4enclosureDiskLoop


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alpa** | **int** |  | [optional] 
**state** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4enclosure_disk_loop import DeviceType4enclosureDiskLoop

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4enclosureDiskLoop from a JSON string
device_type4enclosure_disk_loop_instance = DeviceType4enclosureDiskLoop.from_json(json)
# print the JSON string representation of the object
print(DeviceType4enclosureDiskLoop.to_json())

# convert the object into a dict
device_type4enclosure_disk_loop_dict = device_type4enclosure_disk_loop_instance.to_dict()
# create an instance of DeviceType4enclosureDiskLoop from a dict
device_type4enclosure_disk_loop_from_dict = DeviceType4enclosureDiskLoop.from_dict(device_type4enclosure_disk_loop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


