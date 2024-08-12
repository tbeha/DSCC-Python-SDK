# DeviceType4PortISCSIEditVlansInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_address** | **str** | Gateway address for the iSCSI port. If you are configuring VLAN then this is the VLAN Gateway for this port. If you want to clear or don&#39;t want to set the gateway address, then the gateway address should be 0.0.0.0.Configuring the gateway address supported from OS version 10.3.0. | [optional] 
**gateway_address_v6** | **str** | Gateway address for the iSCSI port. If you are configuring VLAN then this is the VLAN Gateway for this port. Configuring the IPV6 gateway address supported from OS version 10.4.0. | [optional] 
**ip_address** | **str** | IP address for the iSCSI port. If you are configuring VLAN then this is the VLAN IP address for this port. | [optional] 
**ip_address_v6** | **str** | IPv6 address for the iSCSI port. If you are configuring VLAN then this is the VLAN IPv6 address for this port. Configuring IPv6 address is supported from OS version 10.4.0. | [optional] 
**net_mask** | **str** | NetMask for the iSCSI port. If you are configuring VLAN then this is the VLAN Netmask for this port. | [optional] 
**net_mask_v6** | **str** | NetMask for the iSCSI port. If you are configuring VLAN then this is the VLAN Netmask for this port. Configuring this is supported from OS version 10.4.0. | [optional] 
**send_target_group_tag** | **int** | The SendTargets Group Tag (STGT) for the iSCSI port | [optional] 
**vlan_id** | **str** | VLAN id for the iSCSI port. Value ranges between 1 to 4096 | [optional] 

## Example

```python
from dscc.models.device_type4_port_iscsi_edit_vlans_inner import DeviceType4PortISCSIEditVlansInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4PortISCSIEditVlansInner from a JSON string
device_type4_port_iscsi_edit_vlans_inner_instance = DeviceType4PortISCSIEditVlansInner.from_json(json)
# print the JSON string representation of the object
print(DeviceType4PortISCSIEditVlansInner.to_json())

# convert the object into a dict
device_type4_port_iscsi_edit_vlans_inner_dict = device_type4_port_iscsi_edit_vlans_inner_instance.to_dict()
# create an instance of DeviceType4PortISCSIEditVlansInner from a dict
device_type4_port_iscsi_edit_vlans_inner_from_dict = DeviceType4PortISCSIEditVlansInner.from_dict(device_type4_port_iscsi_edit_vlans_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


