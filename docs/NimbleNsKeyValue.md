# NimbleNsKeyValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Identifier of key-value pair. | [optional] 
**value** | **str** | Value of key-value pair. | [optional] 

## Example

```python
from dscc.models.nimble_ns_key_value import NimbleNsKeyValue

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleNsKeyValue from a JSON string
nimble_ns_key_value_instance = NimbleNsKeyValue.from_json(json)
# print the JSON string representation of the object
print(NimbleNsKeyValue.to_json())

# convert the object into a dict
nimble_ns_key_value_dict = nimble_ns_key_value_instance.to_dict()
# create an instance of NimbleNsKeyValue from a dict
nimble_ns_key_value_from_dict = NimbleNsKeyValue.from_dict(nimble_ns_key_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


