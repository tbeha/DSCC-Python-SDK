# NimbleSubnet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_group** | **bool** | Indicates whether group is allowed. | [optional] 
**allow_iscsi** | **bool** | Indicates whether iSCSI is allowed. | [optional] 
**discovery_ip** | **str** | Discovery IP address. | [optional] 
**failover** | **bool** | Failover setting of the subnet. | [optional] 
**failover_enable_time** | **int** | Failover for this subnet will be enabled again at the time specified by failover_enable_time. | [optional] 
**label** | **str** | Subnet label. | [optional] 
**mtu** | **int** | MTU for specified subnet. | [optional] 
**netmask** | **str** | Subnet netmask address. | [optional] 
**network** | **str** | Network IP address. | [optional] 
**netzone_type** | **str** | Netzone type. Possible values: &#39;single&#39;, &#39;evenodd&#39;, &#39;bisect&#39;, &#39;none&#39;. | [optional] 
**type** | **str** | Subnet type. Possible values: &#39;mgmt&#39;, &#39;unconfigured&#39;, &#39;data&#39;, &#39;mgmt_data&#39;, &#39;invalid&#39;. | [optional] 
**vlan_id** | **int** | VLAN ID for specified subnet. | [optional] 

## Example

```python
from dscc.models.nimble_subnet import NimbleSubnet

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleSubnet from a JSON string
nimble_subnet_instance = NimbleSubnet.from_json(json)
# print the JSON string representation of the object
print(NimbleSubnet.to_json())

# convert the object into a dict
nimble_subnet_dict = nimble_subnet_instance.to_dict()
# create an instance of NimbleSubnet from a dict
nimble_subnet_from_dict = NimbleSubnet.from_dict(nimble_subnet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


