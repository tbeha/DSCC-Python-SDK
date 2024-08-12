# NimbleEditFCInterfaceInput

Edit Nimble FC interface input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**online** | **bool** | Identify whether the Fibre Channel interface is online. | [optional] 

## Example

```python
from dscc.models.nimble_edit_fc_interface_input import NimbleEditFCInterfaceInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleEditFCInterfaceInput from a JSON string
nimble_edit_fc_interface_input_instance = NimbleEditFCInterfaceInput.from_json(json)
# print the JSON string representation of the object
print(NimbleEditFCInterfaceInput.to_json())

# convert the object into a dict
nimble_edit_fc_interface_input_dict = nimble_edit_fc_interface_input_instance.to_dict()
# create an instance of NimbleEditFCInterfaceInput from a dict
nimble_edit_fc_interface_input_from_dict = NimbleEditFCInterfaceInput.from_dict(nimble_edit_fc_interface_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


