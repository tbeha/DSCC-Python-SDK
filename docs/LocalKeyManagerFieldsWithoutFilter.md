# LocalKeyManagerFieldsWithoutFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier for the local key manager. A 42 digit hexadecimal number. | [optional] 
**name** | **str** | Name of local key manager. | [optional] [default to 'default']

## Example

```python
from dscc.models.local_key_manager_fields_without_filter import LocalKeyManagerFieldsWithoutFilter

# TODO update the JSON string below
json = "{}"
# create an instance of LocalKeyManagerFieldsWithoutFilter from a JSON string
local_key_manager_fields_without_filter_instance = LocalKeyManagerFieldsWithoutFilter.from_json(json)
# print the JSON string representation of the object
print(LocalKeyManagerFieldsWithoutFilter.to_json())

# convert the object into a dict
local_key_manager_fields_without_filter_dict = local_key_manager_fields_without_filter_instance.to_dict()
# create an instance of LocalKeyManagerFieldsWithoutFilter from a dict
local_key_manager_fields_without_filter_from_dict = LocalKeyManagerFieldsWithoutFilter.from_dict(local_key_manager_fields_without_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


