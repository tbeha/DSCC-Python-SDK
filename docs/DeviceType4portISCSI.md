# DeviceType4portISCSI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delimited_mac_address** | **str** | MAC address of the iSCSI port | [optional] 
**gateway_address** | **str** | Gateway Address of iSCSI port | [optional] 
**gateway_address_v6** | **str** | Gateway Address of iSCSI port. | [optional] 
**i_sns_primary_address** | **str** | Primary iSNS address | [optional] 
**i_sns_tcp_port** | **int** | iSNS TCP port | [optional] 
**ip_address** | **str** | IP address of iSCSI port | [optional] 
**ip_address_v6** | **str** | IPv6 address of iSCSI port. | [optional] 
**iscsi_name** | **str** | iSCSI name of iSCSI port | [optional] 
**mac_address** | **str** | IP address of iSCSI port | [optional] 
**mtu** | **str** | Maximum transmission unit (MTU) size | [optional] 
**send_target_group_tag** | **int** | Send target group of the iSCSI port | [optional] 
**subnet_mask** | **str** | NetMask of iSCSI port | [optional] 
**subnet_mask_v6** | **str** | Netmask of iSCSI port. | [optional] 
**supports_vlan** | **bool** | Indicates if the port support VLAN | [optional] 
**target_portal_group_tag** | **int** | Target portal group of the iSCSI port | [optional] 

## Example

```python
from dscc.models.device_type4port_iscsi import DeviceType4portISCSI

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4portISCSI from a JSON string
device_type4port_iscsi_instance = DeviceType4portISCSI.from_json(json)
# print the JSON string representation of the object
print(DeviceType4portISCSI.to_json())

# convert the object into a dict
device_type4port_iscsi_dict = device_type4port_iscsi_instance.to_dict()
# create an instance of DeviceType4portISCSI from a dict
device_type4port_iscsi_from_dict = DeviceType4portISCSI.from_dict(device_type4port_iscsi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


