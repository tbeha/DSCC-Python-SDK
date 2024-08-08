# PortISCSI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_address** | **str** | Gateway Address of iSCSI port | [optional] 
**i_sns_primary_address** | **str** | Primary iSNS address | [optional] 
**i_sns_tcp_port** | **int** | iSNS TCP port | [optional] 
**ip_address** | **str** | IP address of iSCSI port | [optional] 
**iscsi_name** | **str** | iSCSI name of iSCSI port | [optional] 
**mac_address** | **str** | IP address of iSCSI port | [optional] 
**mtu** | **str** | Maximum transmission unit (MTU) size | [optional] 
**send_target_group_tag** | **int** | Send target group of the iSCSI port | [optional] 
**subnet_mask** | **str** | NetMask of iSCSI port | [optional] 
**supports_vlan** | **bool** | Indicates if the port support VLAN | [optional] 
**target_portal_group_tag** | **int** | Target portal group of the iSCSI port | [optional] 

## Example

```python
from dscc.models.port_iscsi import PortISCSI

# TODO update the JSON string below
json = "{}"
# create an instance of PortISCSI from a JSON string
port_iscsi_instance = PortISCSI.from_json(json)
# print the JSON string representation of the object
print(PortISCSI.to_json())

# convert the object into a dict
port_iscsi_dict = port_iscsi_instance.to_dict()
# create an instance of PortISCSI from a dict
port_iscsi_from_dict = PortISCSI.from_dict(port_iscsi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


