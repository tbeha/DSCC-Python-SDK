# ArrayUnassignMigStatus

Data migration status for array being unassigned from its pool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_migrated** | **int** | Number of bytes already migrated to the destination arrays. | [optional] 
**bytes_remaining** | **int** | Number of bytes yet to be migrated to the destination arrays. | [optional] 
**destination_arrays** | [**List[NimbleArrSummary]**](NimbleArrSummary.md) | List of arrays to which data is being migrated. | [optional] 
**estimated_completion_time** | **int** | Estimated completion time. 0 if unknown. | [optional] 
**id** | **str** | Unique identifier of the array being unassigned. | [optional] 
**name** | **str** | Name of the array being unassigned. | [optional] 
**start_time** | **int** | Time when array unassign operation started. | [optional] 

## Example

```python
from dscc.models.array_unassign_mig_status import ArrayUnassignMigStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayUnassignMigStatus from a JSON string
array_unassign_mig_status_instance = ArrayUnassignMigStatus.from_json(json)
# print the JSON string representation of the object
print(ArrayUnassignMigStatus.to_json())

# convert the object into a dict
array_unassign_mig_status_dict = array_unassign_mig_status_instance.to_dict()
# create an instance of ArrayUnassignMigStatus from a dict
array_unassign_mig_status_from_dict = ArrayUnassignMigStatus.from_dict(array_unassign_mig_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


