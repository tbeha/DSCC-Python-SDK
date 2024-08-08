# NimbleUninitializedArrayResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[UninitializedArrayResponse]**](UninitializedArrayResponse.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**total** | **int** | Total number of Uninitialized array. | [optional] 

## Example

```python
from dscc.models.nimble_uninitialized_array_response import NimbleUninitializedArrayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleUninitializedArrayResponse from a JSON string
nimble_uninitialized_array_response_instance = NimbleUninitializedArrayResponse.from_json(json)
# print the JSON string representation of the object
print(NimbleUninitializedArrayResponse.to_json())

# convert the object into a dict
nimble_uninitialized_array_response_dict = nimble_uninitialized_array_response_instance.to_dict()
# create an instance of NimbleUninitializedArrayResponse from a dict
nimble_uninitialized_array_response_from_dict = NimbleUninitializedArrayResponse.from_dict(nimble_uninitialized_array_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


