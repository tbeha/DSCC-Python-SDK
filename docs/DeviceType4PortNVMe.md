# DeviceType4PortNVMe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delimited_mac_address** | **str** | MAC address of the NVMe port | [optional] 
**eth** | **str** | Ethernet name used by the NVMe port | [optional] 
**gateway_address** | **str** | Gateway of the NVMe port | [optional] 
**gateway_address_v6** | **str** | Gateway address for the NVMe port. | [optional] 
**ip_address** | **str** | IP address of the NVMe port | [optional] 
**ip_address_v6** | **str** | IPV6 address for the NVMe port. | [optional] 
**mac_address** | **str** | MAC address of the NVMe port | [optional] 
**mode** | **str** | Current mode the port is in | [optional] 
**mtu** | **str** | Maximum transmission unit (MTU) size | [optional] 
**nqn** | **str** | NVMe qualified name of the NVMe port | [optional] 
**pcidev** | **str** | PCI device used by the NVMe port | [optional] 
**prefix_length** | **int** | Prefix Length of the NVMe port | [optional] 
**prefix_length_v6** | **int** | Prefix length of the NVMe port. | [optional] 
**protocol** | **str** | Current protocol the port is in | [optional] 
**rate** | **str** | Configured speed of the NVMe port | [optional] 
**state** | **str** | State of the resource | [optional] 
**vlan_count** | **int** | Number of configured VLANs on this NVMe port | [optional] 
**vlans** | [**List[DeviceType4NVMeVLAN]**](DeviceType4NVMeVLAN.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_port_nvme import DeviceType4PortNVMe

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4PortNVMe from a JSON string
device_type4_port_nvme_instance = DeviceType4PortNVMe.from_json(json)
# print the JSON string representation of the object
print(DeviceType4PortNVMe.to_json())

# convert the object into a dict
device_type4_port_nvme_dict = device_type4_port_nvme_instance.to_dict()
# create an instance of DeviceType4PortNVMe from a dict
device_type4_port_nvme_from_dict = DeviceType4PortNVMe.from_dict(device_type4_port_nvme_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


