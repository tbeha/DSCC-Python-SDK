# NimbleArraysList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_name** | **str** | Name of the  array . String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**array_id** | **str** | Identifier for the array. A 42 digit hexadecimal number. | [optional] 
**ctrlr_a_fc_config** | [**NimbleControllerConfig**](NimbleControllerConfig.md) |  | [optional] 
**ctrlr_b_fc_config** | [**NimbleControllerConfig**](NimbleControllerConfig.md) |  | [optional] 
**id** | **str** | Identifier for the array. A 42 digit hexadecimal number. | [optional] 
**name** | **str** | Name of the  array list. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 

## Example

```python
from dscc.models.nimble_arrays_list import NimbleArraysList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleArraysList from a JSON string
nimble_arrays_list_instance = NimbleArraysList.from_json(json)
# print the JSON string representation of the object
print(NimbleArraysList.to_json())

# convert the object into a dict
nimble_arrays_list_dict = nimble_arrays_list_instance.to_dict()
# create an instance of NimbleArraysList from a dict
nimble_arrays_list_from_dict = NimbleArraysList.from_dict(nimble_arrays_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


