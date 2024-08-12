# PortEnableInput

Request body for port enable/disable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_enable** | **bool** | Port enable true or false | [optional] 

## Example

```python
from dscc.models.port_enable_input import PortEnableInput

# TODO update the JSON string below
json = "{}"
# create an instance of PortEnableInput from a JSON string
port_enable_input_instance = PortEnableInput.from_json(json)
# print the JSON string representation of the object
print(PortEnableInput.to_json())

# convert the object into a dict
port_enable_input_dict = port_enable_input_instance.to_dict()
# create an instance of PortEnableInput from a dict
port_enable_input_from_dict = PortEnableInput.from_dict(port_enable_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


