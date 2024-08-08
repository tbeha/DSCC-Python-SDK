# LocalKeyManagerFieldsWithFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier for the local key manager. A 42 digit hexadecimal number. &#x60;Filter&#x60; | [optional] 
**name** | **str** | Name of local key manager. &#x60;Filter, Sort&#x60; | [optional] [default to 'default']

## Example

```python
from dscc.models.local_key_manager_fields_with_filter import LocalKeyManagerFieldsWithFilter

# TODO update the JSON string below
json = "{}"
# create an instance of LocalKeyManagerFieldsWithFilter from a JSON string
local_key_manager_fields_with_filter_instance = LocalKeyManagerFieldsWithFilter.from_json(json)
# print the JSON string representation of the object
print(LocalKeyManagerFieldsWithFilter.to_json())

# convert the object into a dict
local_key_manager_fields_with_filter_dict = local_key_manager_fields_with_filter_instance.to_dict()
# create an instance of LocalKeyManagerFieldsWithFilter from a dict
local_key_manager_fields_with_filter_from_dict = LocalKeyManagerFieldsWithFilter.from_dict(local_key_manager_fields_with_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


