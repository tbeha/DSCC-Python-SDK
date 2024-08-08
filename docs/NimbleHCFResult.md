# NimbleHCFResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**element_name** | **str** | Name of the element | [optional] 
**error_list** | **List[str]** | List of health check errors for this element. | [optional] 
**messages** | [**List[NimbleErrorWithArguments]**](NimbleErrorWithArguments.md) | List of error or info messages. | [optional] 

## Example

```python
from dscc.models.nimble_hcf_result import NimbleHCFResult

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleHCFResult from a JSON string
nimble_hcf_result_instance = NimbleHCFResult.from_json(json)
# print the JSON string representation of the object
print(NimbleHCFResult.to_json())

# convert the object into a dict
nimble_hcf_result_dict = nimble_hcf_result_instance.to_dict()
# create an instance of NimbleHCFResult from a dict
nimble_hcf_result_from_dict = NimbleHCFResult.from_dict(nimble_hcf_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


