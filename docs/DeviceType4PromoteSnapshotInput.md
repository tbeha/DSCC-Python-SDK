# DeviceType4PromoteSnapshotInput

Promote snapshot input. Promote a snapshot to the target with given priority.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | [**DeviceType4Priority**](DeviceType4Priority.md) |  | [optional] 
**target** | **str** | Target volume name to which the snapshot need to be promoted. If not specified it will be promoted to its base volume. | [optional] 

## Example

```python
from dscc.models.device_type4_promote_snapshot_input import DeviceType4PromoteSnapshotInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4PromoteSnapshotInput from a JSON string
device_type4_promote_snapshot_input_instance = DeviceType4PromoteSnapshotInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4PromoteSnapshotInput.to_json())

# convert the object into a dict
device_type4_promote_snapshot_input_dict = device_type4_promote_snapshot_input_instance.to_dict()
# create an instance of DeviceType4PromoteSnapshotInput from a dict
device_type4_promote_snapshot_input_from_dict = DeviceType4PromoteSnapshotInput.from_dict(device_type4_promote_snapshot_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


