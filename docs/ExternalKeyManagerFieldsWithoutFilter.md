# ExternalKeyManagerFieldsWithoutFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier for the External key manager. A 42 digit hexadecimal number. | [optional] 
**name** | **str** | Name of External key manager. | [optional] [default to 'default']

## Example

```python
from dscc.models.external_key_manager_fields_without_filter import ExternalKeyManagerFieldsWithoutFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalKeyManagerFieldsWithoutFilter from a JSON string
external_key_manager_fields_without_filter_instance = ExternalKeyManagerFieldsWithoutFilter.from_json(json)
# print the JSON string representation of the object
print(ExternalKeyManagerFieldsWithoutFilter.to_json())

# convert the object into a dict
external_key_manager_fields_without_filter_dict = external_key_manager_fields_without_filter_instance.to_dict()
# create an instance of ExternalKeyManagerFieldsWithoutFilter from a dict
external_key_manager_fields_without_filter_from_dict = ExternalKeyManagerFieldsWithoutFilter.from_dict(external_key_manager_fields_without_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


