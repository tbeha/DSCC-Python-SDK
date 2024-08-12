# NimbleArraySummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | Array model. | [optional] 
**name** | **str** | The user provided name of the array. | [optional] 

## Example

```python
from dscc.models.nimble_array_summary import NimbleArraySummary

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleArraySummary from a JSON string
nimble_array_summary_instance = NimbleArraySummary.from_json(json)
# print the JSON string representation of the object
print(NimbleArraySummary.to_json())

# convert the object into a dict
nimble_array_summary_dict = nimble_array_summary_instance.to_dict()
# create an instance of NimbleArraySummary from a dict
nimble_array_summary_from_dict = NimbleArraySummary.from_dict(nimble_array_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


