# CreateCloneSnapshotInput

Request body for creating physical copy of a snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_lun** | **bool** | Secify to use auto lun number. | [optional] 
**destination_cpg** | **str** | Name of the User CPG | [optional] 
**destination_snapshot_cpg** | **str** | Name of the Snapshot CPG | [optional] 
**destination_volume** | **str** | Name of the destination volume. | 
**host_group_id** | **str** | Unique identifier of host group. | [optional] 
**lun** | **int** | LUN of volume. | [optional] 
**priority** | **str** | Priority of the task for clone of a snashot. Defualts to MEDIUM. | [optional] 

## Example

```python
from dscc.models.create_clone_snapshot_input import CreateCloneSnapshotInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCloneSnapshotInput from a JSON string
create_clone_snapshot_input_instance = CreateCloneSnapshotInput.from_json(json)
# print the JSON string representation of the object
print(CreateCloneSnapshotInput.to_json())

# convert the object into a dict
create_clone_snapshot_input_dict = create_clone_snapshot_input_instance.to_dict()
# create an instance of CreateCloneSnapshotInput from a dict
create_clone_snapshot_input_from_dict = CreateCloneSnapshotInput.from_dict(create_clone_snapshot_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


