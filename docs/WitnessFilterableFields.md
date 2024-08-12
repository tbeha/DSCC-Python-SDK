# WitnessFilterableFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the replication partner on which quorum witness is configured. &#x60;Filter,Sort&#x60; | [optional] 

## Example

```python
from dscc.models.witness_filterable_fields import WitnessFilterableFields

# TODO update the JSON string below
json = "{}"
# create an instance of WitnessFilterableFields from a JSON string
witness_filterable_fields_instance = WitnessFilterableFields.from_json(json)
# print the JSON string representation of the object
print(WitnessFilterableFields.to_json())

# convert the object into a dict
witness_filterable_fields_dict = witness_filterable_fields_instance.to_dict()
# create an instance of WitnessFilterableFields from a dict
witness_filterable_fields_from_dict = WitnessFilterableFields.from_dict(witness_filterable_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


