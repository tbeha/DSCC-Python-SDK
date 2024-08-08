# PortPositionInput

Specifies the port information of the local system (n:s:p) for Remote Copy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **int** | Port position node number | 
**port** | **int** | Port position port number | 
**slot** | **int** | Port position slot number | 

## Example

```python
from dscc.models.port_position_input import PortPositionInput

# TODO update the JSON string below
json = "{}"
# create an instance of PortPositionInput from a JSON string
port_position_input_instance = PortPositionInput.from_json(json)
# print the JSON string representation of the object
print(PortPositionInput.to_json())

# convert the object into a dict
port_position_input_dict = port_position_input_instance.to_dict()
# create an instance of PortPositionInput from a dict
port_position_input_from_dict = PortPositionInput.from_dict(port_position_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


