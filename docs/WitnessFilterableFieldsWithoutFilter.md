# WitnessFilterableFieldsWithoutFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the replication partner on which quorum witness is configured | [optional] 

## Example

```python
from dscc.models.witness_filterable_fields_without_filter import WitnessFilterableFieldsWithoutFilter

# TODO update the JSON string below
json = "{}"
# create an instance of WitnessFilterableFieldsWithoutFilter from a JSON string
witness_filterable_fields_without_filter_instance = WitnessFilterableFieldsWithoutFilter.from_json(json)
# print the JSON string representation of the object
print(WitnessFilterableFieldsWithoutFilter.to_json())

# convert the object into a dict
witness_filterable_fields_without_filter_dict = witness_filterable_fields_without_filter_instance.to_dict()
# create an instance of WitnessFilterableFieldsWithoutFilter from a dict
witness_filterable_fields_without_filter_from_dict = WitnessFilterableFieldsWithoutFilter.from_dict(witness_filterable_fields_without_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


