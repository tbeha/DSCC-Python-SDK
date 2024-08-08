# NimbleArrSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_id** | **str** | Identifier for array. A 42 digit hexadecimal number. | [optional] 
**array_name** | **str** | The user provided name of the array. It is also the array&#39;s hostname. String of up to 63 alphanumeric and can include hyphens characters but cannot start with hyphen. | [optional] 
**id** | **str** | Identifier for array. A 42 digit hexadecimal number. | [optional] 
**name** | **str** | The user provided name of the array. It is also the array&#39;s hostname. String of up to 63 alphanumeric and can include hyphens characters but cannot start with hyphen. | [optional] 

## Example

```python
from dscc.models.nimble_arr_summary import NimbleArrSummary

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleArrSummary from a JSON string
nimble_arr_summary_instance = NimbleArrSummary.from_json(json)
# print the JSON string representation of the object
print(NimbleArrSummary.to_json())

# convert the object into a dict
nimble_arr_summary_dict = nimble_arr_summary_instance.to_dict()
# create an instance of NimbleArrSummary from a dict
nimble_arr_summary_from_dict = NimbleArrSummary.from_dict(nimble_arr_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


