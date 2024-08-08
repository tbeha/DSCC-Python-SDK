# DeviceType4PortDetailsVirtualPortsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_wwn** | **str** | Node WWN of the virtual port | [optional] 
**port_link_state** | **str** | Port link state | [optional] 
**port_wwn** | **str** | Port WWN of the virtual port | [optional] 

## Example

```python
from dscc.models.device_type4_port_details_virtual_ports_inner import DeviceType4PortDetailsVirtualPortsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4PortDetailsVirtualPortsInner from a JSON string
device_type4_port_details_virtual_ports_inner_instance = DeviceType4PortDetailsVirtualPortsInner.from_json(json)
# print the JSON string representation of the object
print(DeviceType4PortDetailsVirtualPortsInner.to_json())

# convert the object into a dict
device_type4_port_details_virtual_ports_inner_dict = device_type4_port_details_virtual_ports_inner_instance.to_dict()
# create an instance of DeviceType4PortDetailsVirtualPortsInner from a dict
device_type4_port_details_virtual_ports_inner_from_dict = DeviceType4PortDetailsVirtualPortsInner.from_dict(device_type4_port_details_virtual_ports_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


