# ErrorCount

Number of errors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correctable** | **int** | correctable errors | [optional] 
**uncorrectable** | **int** | uncorrectable errors | [optional] 

## Example

```python
from dscc.models.error_count import ErrorCount

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorCount from a JSON string
error_count_instance = ErrorCount.from_json(json)
# print the JSON string representation of the object
print(ErrorCount.to_json())

# convert the object into a dict
error_count_dict = error_count_instance.to_dict()
# create an instance of ErrorCount from a dict
error_count_from_dict = ErrorCount.from_dict(error_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


