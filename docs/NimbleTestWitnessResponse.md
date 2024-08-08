# NimbleTestWitnessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[WitnessTestResponse]**](WitnessTestResponse.md) | Test Witness Response. | 

## Example

```python
from dscc.models.nimble_test_witness_response import NimbleTestWitnessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleTestWitnessResponse from a JSON string
nimble_test_witness_response_instance = NimbleTestWitnessResponse.from_json(json)
# print the JSON string representation of the object
print(NimbleTestWitnessResponse.to_json())

# convert the object into a dict
nimble_test_witness_response_dict = nimble_test_witness_response_instance.to_dict()
# create an instance of NimbleTestWitnessResponse from a dict
nimble_test_witness_response_from_dict = NimbleTestWitnessResponse.from_dict(nimble_test_witness_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


