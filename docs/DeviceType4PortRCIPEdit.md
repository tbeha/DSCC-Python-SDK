# DeviceType4PortRCIPEdit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_address** | **str** | Gateway address to edit to for IPv4 address | [optional] 
**gateway_address_v6** | **str** | Gateway address to edit to for IPv6 address | [optional] 
**ip_address** | **str** | IPv4 address to edit to | [optional] 
**ip_address_v6** | **str** | IPv6 address to edit to | [optional] 
**label** | **str** | label of the port to edit to | [optional] 
**mtu** | **str** | MTU to edit to. Possible Values: \&quot;1500\&quot;, \&quot;9000\&quot; | [optional] 
**net_mask** | **str** | NetMask address to edit to for IPv4 address | [optional] 
**net_mask_v6** | **str** | NetMask address to edit to for IPv6 address | [optional] 
**speed_configured** | **str** | Configured speed. Possible Values: auto, \&quot;1\&quot;, \&quot;2\&quot;, \&quot;4\&quot;, \&quot;8\&quot;, \&quot;16\&quot;, \&quot;32\&quot; | [optional] 

## Example

```python
from dscc.models.device_type4_port_rcip_edit import DeviceType4PortRCIPEdit

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4PortRCIPEdit from a JSON string
device_type4_port_rcip_edit_instance = DeviceType4PortRCIPEdit.from_json(json)
# print the JSON string representation of the object
print(DeviceType4PortRCIPEdit.to_json())

# convert the object into a dict
device_type4_port_rcip_edit_dict = device_type4_port_rcip_edit_instance.to_dict()
# create an instance of DeviceType4PortRCIPEdit from a dict
device_type4_port_rcip_edit_from_dict = DeviceType4PortRCIPEdit.from_dict(device_type4_port_rcip_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


