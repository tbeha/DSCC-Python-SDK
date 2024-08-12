# NimbleErrorWithArguments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Error code. | [optional] 
**severity** | **str** | Severity of the error. Possible values: &#39;warn&#39;, &#39;debug&#39;, &#39;error&#39;, &#39;fatal&#39;, &#39;info&#39;. | [optional] 
**text** | **str** | Full error message with argument populated. | [optional] 

## Example

```python
from dscc.models.nimble_error_with_arguments import NimbleErrorWithArguments

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleErrorWithArguments from a JSON string
nimble_error_with_arguments_instance = NimbleErrorWithArguments.from_json(json)
# print the JSON string representation of the object
print(NimbleErrorWithArguments.to_json())

# convert the object into a dict
nimble_error_with_arguments_dict = nimble_error_with_arguments_instance.to_dict()
# create an instance of NimbleErrorWithArguments from a dict
nimble_error_with_arguments_from_dict = NimbleErrorWithArguments.from_dict(nimble_error_with_arguments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


