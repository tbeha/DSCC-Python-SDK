# DeviceType4enclosureConnectorsListNodePort

 It includes node number, slot number, and port number

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **int** |  | [optional] 
**port** | **int** |  | [optional] 
**slot** | **int** |  | [optional] 

## Example

```python
from dscc.models.device_type4enclosure_connectors_list_node_port import DeviceType4enclosureConnectorsListNodePort

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4enclosureConnectorsListNodePort from a JSON string
device_type4enclosure_connectors_list_node_port_instance = DeviceType4enclosureConnectorsListNodePort.from_json(json)
# print the JSON string representation of the object
print(DeviceType4enclosureConnectorsListNodePort.to_json())

# convert the object into a dict
device_type4enclosure_connectors_list_node_port_dict = device_type4enclosure_connectors_list_node_port_instance.to_dict()
# create an instance of DeviceType4enclosureConnectorsListNodePort from a dict
device_type4enclosure_connectors_list_node_port_from_dict = DeviceType4enclosureConnectorsListNodePort.from_dict(device_type4enclosure_connectors_list_node_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


