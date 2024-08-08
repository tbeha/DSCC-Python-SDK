# DeviceType4EnclosureConnectorDetailsNodePort

It includes node number, slot number, and port number

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **int** | &#x60;Filter, Sort&#x60; | [optional] 
**port** | **int** | &#x60;Filter, Sort&#x60; | [optional] 
**slot** | **int** | &#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.device_type4_enclosure_connector_details_node_port import DeviceType4EnclosureConnectorDetailsNodePort

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EnclosureConnectorDetailsNodePort from a JSON string
device_type4_enclosure_connector_details_node_port_instance = DeviceType4EnclosureConnectorDetailsNodePort.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EnclosureConnectorDetailsNodePort.to_json())

# convert the object into a dict
device_type4_enclosure_connector_details_node_port_dict = device_type4_enclosure_connector_details_node_port_instance.to_dict()
# create an instance of DeviceType4EnclosureConnectorDetailsNodePort from a dict
device_type4_enclosure_connector_details_node_port_from_dict = DeviceType4EnclosureConnectorDetailsNodePort.from_dict(device_type4_enclosure_connector_details_node_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


