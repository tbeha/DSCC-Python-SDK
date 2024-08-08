# DeviceType4PortNVMeEdit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Label of the port to edit to | [optional] 
**mtu** | **str** | Maximum transmission unit (MTU) size | [optional] 
**vlans** | [**List[DeviceType4PortNVMeEditVlansInner]**](DeviceType4PortNVMeEditVlansInner.md) | Port VLANs information. Specifying VLAN id is mandatory to configure VLAN. | [optional] 

## Example

```python
from dscc.models.device_type4_port_nvme_edit import DeviceType4PortNVMeEdit

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4PortNVMeEdit from a JSON string
device_type4_port_nvme_edit_instance = DeviceType4PortNVMeEdit.from_json(json)
# print the JSON string representation of the object
print(DeviceType4PortNVMeEdit.to_json())

# convert the object into a dict
device_type4_port_nvme_edit_dict = device_type4_port_nvme_edit_instance.to_dict()
# create an instance of DeviceType4PortNVMeEdit from a dict
device_type4_port_nvme_edit_from_dict = DeviceType4PortNVMeEdit.from_dict(device_type4_port_nvme_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


