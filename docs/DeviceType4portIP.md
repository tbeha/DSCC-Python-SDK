# DeviceType4portIP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoneg** | **bool** | Auto negotiation state of IP port | [optional] 
**delimited_mac_address** | **str** | MAC address of the IP port | [optional] 
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
from dscc.models.device_type4port_ip import DeviceType4portIP

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4portIP from a JSON string
device_type4port_ip_instance = DeviceType4portIP.from_json(json)
# print the JSON string representation of the object
print(DeviceType4portIP.to_json())

# convert the object into a dict
device_type4port_ip_dict = device_type4port_ip_instance.to_dict()
# create an instance of DeviceType4portIP from a dict
device_type4port_ip_from_dict = DeviceType4portIP.from_dict(device_type4port_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


