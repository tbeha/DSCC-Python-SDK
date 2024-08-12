# NimbleUninitializedArrayInput

get uninitialized array input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier for the uninitialized array. A 42 digit hexadecimal number | 

## Example

```python
from dscc.models.nimble_uninitialized_array_input import NimbleUninitializedArrayInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleUninitializedArrayInput from a JSON string
nimble_uninitialized_array_input_instance = NimbleUninitializedArrayInput.from_json(json)
# print the JSON string representation of the object
print(NimbleUninitializedArrayInput.to_json())

# convert the object into a dict
nimble_uninitialized_array_input_dict = nimble_uninitialized_array_input_instance.to_dict()
# create an instance of NimbleUninitializedArrayInput from a dict
nimble_uninitialized_array_input_from_dict = NimbleUninitializedArrayInput.from_dict(nimble_uninitialized_array_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


