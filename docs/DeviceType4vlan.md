# DeviceType4vlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_address** | **str** | VLAN Gateway address for the iSCSI port | [optional] 
**gateway_address_v6** | **str** | Gateway Address of iSCSI port. If Vlan is configured,then this is Vlan gateway address of this port. | [optional] 
**i_sns_primary_address** | **str** | The iSNS server IP address | [optional] 
**i_sns_tcp_port** | **str** | TCP port number for the iSNS server | [optional] 
**ip_address** | **str** | VLAN IP address for the iSCSI port | [optional] 
**ip_address_v6** | **str** | IPv6 address of iSCSI port. If Vlan is configured,then this is Vlan IPv6 address of this port. | [optional] 
**mtu** | **str** | Maximum transmission unit (MTU) size | [optional] 
**send_target_group_tag** | **int** | The SendTargets Group Tag (STGT) for the iSCSI port | [optional] 
**subnet_mask** | **str** | VLAN Subnet mask for the iSCSI port | [optional] 
**subnet_mask_v6** | **str** | Netmask of iSCSI port. If Vlan is configured,then this is Vlan subnet mask of this port. | [optional] 
**target_portal_group_tag** | **int** | The Target portal Group Tag (TPGT) for the iSCSI port | [optional] 
**vlan_id** | **str** | VLAN id for the iSCSI port | [optional] 

## Example

```python
from dscc.models.device_type4vlan import DeviceType4vlan

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4vlan from a JSON string
device_type4vlan_instance = DeviceType4vlan.from_json(json)
# print the JSON string representation of the object
print(DeviceType4vlan.to_json())

# convert the object into a dict
device_type4vlan_dict = device_type4vlan_instance.to_dict()
# create an instance of DeviceType4vlan from a dict
device_type4vlan_from_dict = DeviceType4vlan.from_dict(device_type4vlan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


