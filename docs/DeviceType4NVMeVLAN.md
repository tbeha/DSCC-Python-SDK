# DeviceType4NVMeVLAN

Port VLANs information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eth** | **str** | Ethernet name used by the NVMe port | [optional] 
**gateway_address** | **str** | VLAN Gateway address for the NVMe port | [optional] 
**gateway_address_v6** | **str** | Gateway address for the NVMe port. If Vlan is configured, then this is Vlan gateway address of this port. | [optional] 
**ip_address** | **str** | VLAN IP address for the NVMe port | [optional] 
**ip_address_v6** | **str** | IPV6 address for the NVMe port. If Vlan is configured, then this is Vlan IPV6 address of this port. | [optional] 
**mtu** | **str** | Maximum transmission unit (MTU) size | [optional] 
**nqn** | **str** | NVMe qualified name of the NVMe port | [optional] 
**prefix_length** | **int** | Prefix length of the NVMe port | [optional] 
**prefix_length_v6** | **int** | Prefix length of the NVMe port. | [optional] 
**vlan_id** | **str** | VLAN id for the NVMe port | [optional] 

## Example

```python
from dscc.models.device_type4_nvme_vlan import DeviceType4NVMeVLAN

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4NVMeVLAN from a JSON string
device_type4_nvme_vlan_instance = DeviceType4NVMeVLAN.from_json(json)
# print the JSON string representation of the object
print(DeviceType4NVMeVLAN.to_json())

# convert the object into a dict
device_type4_nvme_vlan_dict = device_type4_nvme_vlan_instance.to_dict()
# create an instance of DeviceType4NVMeVLAN from a dict
device_type4_nvme_vlan_from_dict = DeviceType4NVMeVLAN.from_dict(device_type4_nvme_vlan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


