# DeviceType4HostVirtualPort

Host virtual ports

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_wwn** | **str** | Node WWN of the virtual port | [optional] 
**port_link_state** | **str** | Port link state | [optional] 
**port_type** | **str** | Virtual port type | [optional] 
**port_wwn** | **str** | Port WWN of the virtual port | [optional] 
**protocol** | **str** | Protocol of the Virtual port | [optional] 
**vpi** | **int** | Virtual port index | [optional] 

## Example

```python
from dscc.models.device_type4_host_virtual_port import DeviceType4HostVirtualPort

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4HostVirtualPort from a JSON string
device_type4_host_virtual_port_instance = DeviceType4HostVirtualPort.from_json(json)
# print the JSON string representation of the object
print(DeviceType4HostVirtualPort.to_json())

# convert the object into a dict
device_type4_host_virtual_port_dict = device_type4_host_virtual_port_instance.to_dict()
# create an instance of DeviceType4HostVirtualPort from a dict
device_type4_host_virtual_port_from_dict = DeviceType4HostVirtualPort.from_dict(device_type4_host_virtual_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


