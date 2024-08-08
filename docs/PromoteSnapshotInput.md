# PromoteSnapshotInput

Promote snapshot input. Promote a snapshot to the target with given priority.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | [**Priority**](Priority.md) |  | [optional] 
**target** | **str** | Target volume name to which the snapshot need to be promoted. If not specified it will be promoted to its base volume. | [optional] 

## Example

```python
from dscc.models.promote_snapshot_input import PromoteSnapshotInput

# TODO update the JSON string below
json = "{}"
# create an instance of PromoteSnapshotInput from a JSON string
promote_snapshot_input_instance = PromoteSnapshotInput.from_json(json)
# print the JSON string representation of the object
print(PromoteSnapshotInput.to_json())

# convert the object into a dict
promote_snapshot_input_dict = promote_snapshot_input_instance.to_dict()
# create an instance of PromoteSnapshotInput from a dict
promote_snapshot_input_from_dict = PromoteSnapshotInput.from_dict(promote_snapshot_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


