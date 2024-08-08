# NimbleArrayFailoverInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force** | **bool** | Initiate failover without performing any precheck. | [optional] 

## Example

```python
from dscc.models.nimble_array_failover_input import NimbleArrayFailoverInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleArrayFailoverInput from a JSON string
nimble_array_failover_input_instance = NimbleArrayFailoverInput.from_json(json)
# print the JSON string representation of the object
print(NimbleArrayFailoverInput.to_json())

# convert the object into a dict
nimble_array_failover_input_dict = nimble_array_failover_input_instance.to_dict()
# create an instance of NimbleArrayFailoverInput from a dict
nimble_array_failover_input_from_dict = NimbleArrayFailoverInput.from_dict(nimble_array_failover_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


