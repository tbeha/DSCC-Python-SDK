# DeviceType4PortClearInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_type** | **str** | For RCIP ports, the IP version of the address that needs to be cleared from the port. Either the IPv4 address or IPv6 address or both addresses can be cleared. Possible values: v4,v6,both | [optional] 

## Example

```python
from dscc.models.device_type4_port_clear_input import DeviceType4PortClearInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4PortClearInput from a JSON string
device_type4_port_clear_input_instance = DeviceType4PortClearInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4PortClearInput.to_json())

# convert the object into a dict
device_type4_port_clear_input_dict = device_type4_port_clear_input_instance.to_dict()
# create an instance of DeviceType4PortClearInput from a dict
device_type4_port_clear_input_from_dict = DeviceType4PortClearInput.from_dict(device_type4_port_clear_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


