# DeviceType4DiskPortPosition

Port Position

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **int** | node ID | [optional] 
**port** | **int** | port ID | [optional] 
**slot** | **int** | slot ID | [optional] 

## Example

```python
from dscc.models.device_type4_disk_port_position import DeviceType4DiskPortPosition

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4DiskPortPosition from a JSON string
device_type4_disk_port_position_instance = DeviceType4DiskPortPosition.from_json(json)
# print the JSON string representation of the object
print(DeviceType4DiskPortPosition.to_json())

# convert the object into a dict
device_type4_disk_port_position_dict = device_type4_disk_port_position_instance.to_dict()
# create an instance of DeviceType4DiskPortPosition from a dict
device_type4_disk_port_position_from_dict = DeviceType4DiskPortPosition.from_dict(device_type4_disk_port_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


