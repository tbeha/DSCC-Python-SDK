# DeviceType4WitnessFilterableFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the replication partner on which quorum witness is configured. &#x60;Filter,Sort&#x60; | [optional] 

## Example

```python
from dscc.models.device_type4_witness_filterable_fields import DeviceType4WitnessFilterableFields

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4WitnessFilterableFields from a JSON string
device_type4_witness_filterable_fields_instance = DeviceType4WitnessFilterableFields.from_json(json)
# print the JSON string representation of the object
print(DeviceType4WitnessFilterableFields.to_json())

# convert the object into a dict
device_type4_witness_filterable_fields_dict = device_type4_witness_filterable_fields_instance.to_dict()
# create an instance of DeviceType4WitnessFilterableFields from a dict
device_type4_witness_filterable_fields_from_dict = DeviceType4WitnessFilterableFields.from_dict(device_type4_witness_filterable_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


