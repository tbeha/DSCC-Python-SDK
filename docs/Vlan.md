# Vlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_address** | **str** | VLAN Gateway address for the iSCSI port | [optional] 
**i_sns_primary_address** | **str** | The iSNS server IP address | [optional] 
**i_sns_tcp_port** | **str** | TCP port number for the iSNS server | [optional] 
**ip_address** | **str** | VLAN IP address for the iSCSI port | [optional] 
**mtu** | **str** | Maximum transmission unit (MTU) size | [optional] 
**send_target_group_tag** | **str** | The SendTargets Group Tag (STGT) for the iSCSI port | [optional] 
**subnet_mask** | **str** | VLAN Subnet mask for the iSCSI port | [optional] 
**target_portal_group_tag** | **str** | The Target portal Group Tag (TPGT) for the iSCSI port | [optional] 
**vlan_id** | **str** | VLAN id for the iSCSI port | [optional] 

## Example

```python
from dscc.models.vlan import Vlan

# TODO update the JSON string below
json = "{}"
# create an instance of Vlan from a JSON string
vlan_instance = Vlan.from_json(json)
# print the JSON string representation of the object
print(Vlan.to_json())

# convert the object into a dict
vlan_dict = vlan_instance.to_dict()
# create an instance of Vlan from a dict
vlan_from_dict = Vlan.from_dict(vlan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


