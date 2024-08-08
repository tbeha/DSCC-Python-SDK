# DeviceType4PortPositionInput

Specifies the port information of the local system (n:s:p) for Remote Copy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **int** | Port position node number | 
**port** | **int** | Port position port number | 
**slot** | **int** | Port position slot number | 

## Example

```python
from dscc.models.device_type4_port_position_input import DeviceType4PortPositionInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4PortPositionInput from a JSON string
device_type4_port_position_input_instance = DeviceType4PortPositionInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4PortPositionInput.to_json())

# convert the object into a dict
device_type4_port_position_input_dict = device_type4_port_position_input_instance.to_dict()
# create an instance of DeviceType4PortPositionInput from a dict
device_type4_port_position_input_from_dict = DeviceType4PortPositionInput.from_dict(device_type4_port_position_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


