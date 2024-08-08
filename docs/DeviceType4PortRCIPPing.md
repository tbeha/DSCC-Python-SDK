# DeviceType4PortRCIPPing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**packet_size** | **int** | Packet size of the ping | [optional] 
**wait_time** | **int** | Wait time | [optional] 
**ip_address** | **str** | IP Address to ping | [optional] 
**ip_addressv6** | **str** | IP Address to ping | [optional] 
**ping_count** | **int** | ping count | [optional] 

## Example

```python
from dscc.models.device_type4_port_rcip_ping import DeviceType4PortRCIPPing

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4PortRCIPPing from a JSON string
device_type4_port_rcip_ping_instance = DeviceType4PortRCIPPing.from_json(json)
# print the JSON string representation of the object
print(DeviceType4PortRCIPPing.to_json())

# convert the object into a dict
device_type4_port_rcip_ping_dict = device_type4_port_rcip_ping_instance.to_dict()
# create an instance of DeviceType4PortRCIPPing from a dict
device_type4_port_rcip_ping_from_dict = DeviceType4PortRCIPPing.from_dict(device_type4_port_rcip_ping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


