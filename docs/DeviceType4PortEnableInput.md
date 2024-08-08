# DeviceType4PortEnableInput

Request body for port enable/disable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_enable** | **bool** | Port enable true or false | [optional] 

## Example

```python
from dscc.models.device_type4_port_enable_input import DeviceType4PortEnableInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4PortEnableInput from a JSON string
device_type4_port_enable_input_instance = DeviceType4PortEnableInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4PortEnableInput.to_json())

# convert the object into a dict
device_type4_port_enable_input_dict = device_type4_port_enable_input_instance.to_dict()
# create an instance of DeviceType4PortEnableInput from a dict
device_type4_port_enable_input_from_dict = DeviceType4PortEnableInput.from_dict(device_type4_port_enable_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


