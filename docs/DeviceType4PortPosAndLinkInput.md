# DeviceType4PortPosAndLinkInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** | Specifies the link for the remote system. If the Link Protocol Type is IP, specify an IP address for the corresponding port on the remote system. If the Link Protocol Type is FC, specify the WWN of the peer port on the remote system | 
**port_position** | [**DeviceType4PortPositionInput**](DeviceType4PortPositionInput.md) |  | 

## Example

```python
from dscc.models.device_type4_port_pos_and_link_input import DeviceType4PortPosAndLinkInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4PortPosAndLinkInput from a JSON string
device_type4_port_pos_and_link_input_instance = DeviceType4PortPosAndLinkInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4PortPosAndLinkInput.to_json())

# convert the object into a dict
device_type4_port_pos_and_link_input_dict = device_type4_port_pos_and_link_input_instance.to_dict()
# create an instance of DeviceType4PortPosAndLinkInput from a dict
device_type4_port_pos_and_link_input_from_dict = DeviceType4PortPosAndLinkInput.from_dict(device_type4_port_pos_and_link_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


