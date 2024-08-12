# NimbleArrayFieldsWithoutSortKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier for array. A 42 digit hexadecimal number. | [optional] 
**model** | **str** | Array model. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**name** | **str** | The user provided name of the array. It is also the array&#39;s hostname. String of up to 63 alphanumeric and can include hyphens characters but cannot start with hyphen. | [optional] 
**pool_id** | **str** | ID of pool to which this is a member. A 42 digit hexadecimal number. | [optional] 
**serial** | **str** | Serial number of the array. | [optional] 

## Example

```python
from dscc.models.nimble_array_fields_without_sort_key import NimbleArrayFieldsWithoutSortKey

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleArrayFieldsWithoutSortKey from a JSON string
nimble_array_fields_without_sort_key_instance = NimbleArrayFieldsWithoutSortKey.from_json(json)
# print the JSON string representation of the object
print(NimbleArrayFieldsWithoutSortKey.to_json())

# convert the object into a dict
nimble_array_fields_without_sort_key_dict = nimble_array_fields_without_sort_key_instance.to_dict()
# create an instance of NimbleArrayFieldsWithoutSortKey from a dict
nimble_array_fields_without_sort_key_from_dict = NimbleArrayFieldsWithoutSortKey.from_dict(nimble_array_fields_without_sort_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


