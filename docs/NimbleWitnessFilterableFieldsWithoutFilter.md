# NimbleWitnessFilterableFieldsWithoutFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname or ip addresses of witness. Comma separated strings of up to 63 characters of hostname and/or ip addresses. Total length cannot exceed 255 characters. | [optional] 
**id** | **str** | Identifier for the witness configuration. A 42 digit hexadecimal number. | [optional] 
**port** | **int** | Port of witness. Positive integer value up to 65535 representing TCP/IP port. | [optional] 
**username** | **str** | Username of witness. This has to be a non-root that can login to the witness host. String of up to 32 characters, beginning with a letter or number or period (.) or an underscore (_). It can include underscore (_), dash (-), period (.) and end with doller ($) sign. | [optional] 

## Example

```python
from dscc.models.nimble_witness_filterable_fields_without_filter import NimbleWitnessFilterableFieldsWithoutFilter

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleWitnessFilterableFieldsWithoutFilter from a JSON string
nimble_witness_filterable_fields_without_filter_instance = NimbleWitnessFilterableFieldsWithoutFilter.from_json(json)
# print the JSON string representation of the object
print(NimbleWitnessFilterableFieldsWithoutFilter.to_json())

# convert the object into a dict
nimble_witness_filterable_fields_without_filter_dict = nimble_witness_filterable_fields_without_filter_instance.to_dict()
# create an instance of NimbleWitnessFilterableFieldsWithoutFilter from a dict
nimble_witness_filterable_fields_without_filter_from_dict = NimbleWitnessFilterableFieldsWithoutFilter.from_dict(nimble_witness_filterable_fields_without_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


