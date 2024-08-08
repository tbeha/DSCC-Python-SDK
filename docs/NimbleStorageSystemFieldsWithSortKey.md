# NimbleStorageSystemFieldsWithSortKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the group. A 42 digit hexadecimal number. &#x60;Filter&#x60; | [optional] 
**name** | **str** | Name of the group. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. &#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.nimble_storage_system_fields_with_sort_key import NimbleStorageSystemFieldsWithSortKey

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleStorageSystemFieldsWithSortKey from a JSON string
nimble_storage_system_fields_with_sort_key_instance = NimbleStorageSystemFieldsWithSortKey.from_json(json)
# print the JSON string representation of the object
print(NimbleStorageSystemFieldsWithSortKey.to_json())

# convert the object into a dict
nimble_storage_system_fields_with_sort_key_dict = nimble_storage_system_fields_with_sort_key_instance.to_dict()
# create an instance of NimbleStorageSystemFieldsWithSortKey from a dict
nimble_storage_system_fields_with_sort_key_from_dict = NimbleStorageSystemFieldsWithSortKey.from_dict(nimble_storage_system_fields_with_sort_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


