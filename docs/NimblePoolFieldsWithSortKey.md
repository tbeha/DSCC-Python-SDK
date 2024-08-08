# NimblePoolFieldsWithSortKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of pool. A 42 digit hexadecimal number. &#x60;Filter&#x60; | [optional] 
**name** | **str** | Name of pool. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. &#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.nimble_pool_fields_with_sort_key import NimblePoolFieldsWithSortKey

# TODO update the JSON string below
json = "{}"
# create an instance of NimblePoolFieldsWithSortKey from a JSON string
nimble_pool_fields_with_sort_key_instance = NimblePoolFieldsWithSortKey.from_json(json)
# print the JSON string representation of the object
print(NimblePoolFieldsWithSortKey.to_json())

# convert the object into a dict
nimble_pool_fields_with_sort_key_dict = nimble_pool_fields_with_sort_key_instance.to_dict()
# create an instance of NimblePoolFieldsWithSortKey from a dict
nimble_pool_fields_with_sort_key_from_dict = NimblePoolFieldsWithSortKey.from_dict(nimble_pool_fields_with_sort_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


