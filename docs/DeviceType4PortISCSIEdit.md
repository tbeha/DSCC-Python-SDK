# DeviceType4PortISCSIEdit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | label of the port to edit to | [optional] 
**mtu** | **str** | Maximum transmission unit (MTU) size | [optional] 
**vlans** | [**List[DeviceType4PortISCSIEditVlansInner]**](DeviceType4PortISCSIEditVlansInner.md) | Port VLANs information. Specifying VLAN id is mandatory to configure VLAN. | [optional] 

## Example

```python
from dscc.models.device_type4_port_iscsi_edit import DeviceType4PortISCSIEdit

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4PortISCSIEdit from a JSON string
device_type4_port_iscsi_edit_instance = DeviceType4PortISCSIEdit.from_json(json)
# print the JSON string representation of the object
print(DeviceType4PortISCSIEdit.to_json())

# convert the object into a dict
device_type4_port_iscsi_edit_dict = device_type4_port_iscsi_edit_instance.to_dict()
# create an instance of DeviceType4PortISCSIEdit from a dict
device_type4_port_iscsi_edit_from_dict = DeviceType4PortISCSIEdit.from_dict(device_type4_port_iscsi_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


