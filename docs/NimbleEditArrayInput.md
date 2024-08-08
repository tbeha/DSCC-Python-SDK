# NimbleEditArrayInput

Edit Nimble array input

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The user provided name of the array. It is also the array&#39;s hostname. String of up to 63 alphanumeric and can include hyphens characters but cannot start with hyphen. | 

## Example

```python
from dscc.models.nimble_edit_array_input import NimbleEditArrayInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleEditArrayInput from a JSON string
nimble_edit_array_input_instance = NimbleEditArrayInput.from_json(json)
# print the JSON string representation of the object
print(NimbleEditArrayInput.to_json())

# convert the object into a dict
nimble_edit_array_input_dict = nimble_edit_array_input_instance.to_dict()
# create an instance of NimbleEditArrayInput from a dict
nimble_edit_array_input_from_dict = NimbleEditArrayInput.from_dict(nimble_edit_array_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


