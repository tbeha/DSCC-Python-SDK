# ArrayMigStatus

Data migration status for an array.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the array. | [optional] 
**is_data_source** | **bool** | Indicates whether the array is data source or not. | [optional] 
**name** | **str** | Name of the array. | [optional] 
**space_utilization** | **int** | Space utilization as a percentage of array size. | [optional] 

## Example

```python
from dscc.models.array_mig_status import ArrayMigStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayMigStatus from a JSON string
array_mig_status_instance = ArrayMigStatus.from_json(json)
# print the JSON string representation of the object
print(ArrayMigStatus.to_json())

# convert the object into a dict
array_mig_status_dict = array_mig_status_instance.to_dict()
# create an instance of ArrayMigStatus from a dict
array_mig_status_from_dict = ArrayMigStatus.from_dict(array_mig_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


