# DeviceType4connectedDevicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the device | [optional] 
**position** | **int** | Position of the device | [optional] 

## Example

```python
from dscc.models.device_type4connected_devices_inner import DeviceType4connectedDevicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4connectedDevicesInner from a JSON string
device_type4connected_devices_inner_instance = DeviceType4connectedDevicesInner.from_json(json)
# print the JSON string representation of the object
print(DeviceType4connectedDevicesInner.to_json())

# convert the object into a dict
device_type4connected_devices_inner_dict = device_type4connected_devices_inner_instance.to_dict()
# create an instance of DeviceType4connectedDevicesInner from a dict
device_type4connected_devices_inner_from_dict = DeviceType4connectedDevicesInner.from_dict(device_type4connected_devices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


