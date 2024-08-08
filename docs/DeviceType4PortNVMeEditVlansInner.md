# DeviceType4PortNVMeEditVlansInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_address** | **str** | Gateway address for the NVMe port. If you are configuring VLAN then this is the VLAN Gateway for this port. If you want to clear or don&#39;t want to set the gateway address, then the gateway address should be 0.0.0.0 | [optional] 
**gateway_address_v6** | **str** | Gateway address for the NVME port. If you are configuring VLAN then this is the VLAN Gateway for this port. Configuring the IPV6 gateway address supported from OS version 10.4.0. | [optional] 
**ip_address** | **str** | IP address for the NVMe port. If you are configuring VLAN then this is the VLAN IP address for this port. | [optional] 
**ip_address_v6** | **str** | IPV6 address for the NVME port. If you are configuring VLAN then this is the VLAN IP address for this port. Configuring IPV6 address is supported from OS version 10.4.0. | [optional] 
**mtu** | **str** | Maximum transmission unit (MTU) size | [optional] 
**prefix_length** | **int** | Prefix length of the NVMe port | [optional] 
**prefix_length_v6** | **int** | Prefix length of the NVMe port. | [optional] 
**vlan_id** | **str** | VLAN id for the NVMe port. Value ranges between 1 to 4096 | [optional] 

## Example

```python
from dscc.models.device_type4_port_nvme_edit_vlans_inner import DeviceType4PortNVMeEditVlansInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4PortNVMeEditVlansInner from a JSON string
device_type4_port_nvme_edit_vlans_inner_instance = DeviceType4PortNVMeEditVlansInner.from_json(json)
# print the JSON string representation of the object
print(DeviceType4PortNVMeEditVlansInner.to_json())

# convert the object into a dict
device_type4_port_nvme_edit_vlans_inner_dict = device_type4_port_nvme_edit_vlans_inner_instance.to_dict()
# create an instance of DeviceType4PortNVMeEditVlansInner from a dict
device_type4_port_nvme_edit_vlans_inner_from_dict = DeviceType4PortNVMeEditVlansInner.from_dict(device_type4_port_nvme_edit_vlans_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


