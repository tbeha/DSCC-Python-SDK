# ExternalKeyManagerFieldsWithFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier for the external key manager. A 42 digit hexadecimal number. &#x60;Filter&#x60; | [optional] 
**name** | **str** | Name of external key manager. &#x60;Filter, Sort&#x60; | [optional] [default to 'default']
**system_id** | **str** | Id of the storage system | [optional] 

## Example

```python
from dscc.models.external_key_manager_fields_with_filter import ExternalKeyManagerFieldsWithFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalKeyManagerFieldsWithFilter from a JSON string
external_key_manager_fields_with_filter_instance = ExternalKeyManagerFieldsWithFilter.from_json(json)
# print the JSON string representation of the object
print(ExternalKeyManagerFieldsWithFilter.to_json())

# convert the object into a dict
external_key_manager_fields_with_filter_dict = external_key_manager_fields_with_filter_instance.to_dict()
# create an instance of ExternalKeyManagerFieldsWithFilter from a dict
external_key_manager_fields_with_filter_from_dict = ExternalKeyManagerFieldsWithFilter.from_dict(external_key_manager_fields_with_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


