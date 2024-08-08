# DeviceType4CreateCloneSnapshotInput

Request body for creating physical copy of a snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_lun** | **bool** | Secify to use auto lun number. | [optional] 
**destination_cpg** | **str** | Name of the User CPG | [optional] 
**destination_volume** | **str** | Name of the destination volume. | 
**host_group_id** | **str** | Unique identifier of host group. | [optional] 
**lun** | **int** | LUN of volume. | [optional] 
**priority** | **str** | Priority of the task for clone of a snashot. Defualts to MEDIUM. | [optional] 

## Example

```python
from dscc.models.device_type4_create_clone_snapshot_input import DeviceType4CreateCloneSnapshotInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4CreateCloneSnapshotInput from a JSON string
device_type4_create_clone_snapshot_input_instance = DeviceType4CreateCloneSnapshotInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4CreateCloneSnapshotInput.to_json())

# convert the object into a dict
device_type4_create_clone_snapshot_input_dict = device_type4_create_clone_snapshot_input_instance.to_dict()
# create an instance of DeviceType4CreateCloneSnapshotInput from a dict
device_type4_create_clone_snapshot_input_from_dict = DeviceType4CreateCloneSnapshotInput.from_dict(device_type4_create_clone_snapshot_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


