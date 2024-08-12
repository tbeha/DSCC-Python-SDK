# PortIP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoneg** | **bool** | Auto negotiation state of IP port | [optional] 
**duplex** | **str** | Duplex state of IP port | [optional] 
**gateway_address** | **str** | Gateway Address of IP port | [optional] 
**gateway_address_v6** | **str** | Gateway Address of IP port | [optional] 
**ip_address** | **str** | IP address of IP port | [optional] 
**ip_address_v6** | **str** | IP address of IP port | [optional] 
**mac_address** | **str** | IP address of IP port | [optional] 
**mtu** | **str** | Maximum transmission unit (MTU) size | [optional] 
**subnet_mask** | **str** | NetMask of IP port | [optional] 
**subnet_mask_v6** | **str** | NetMask of IP port | [optional] 

## Example

```python
from dscc.models.port_ip import PortIP

# TODO update the JSON string below
json = "{}"
# create an instance of PortIP from a JSON string
port_ip_instance = PortIP.from_json(json)
# print the JSON string representation of the object
print(PortIP.to_json())

# convert the object into a dict
port_ip_dict = port_ip_instance.to_dict()
# create an instance of PortIP from a dict
port_ip_from_dict = PortIP.from_dict(port_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


