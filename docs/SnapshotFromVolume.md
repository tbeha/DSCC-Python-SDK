# SnapshotFromVolume

Snapshots as presented to volumes in volume-sets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of snapshot. | [optional] 
**name** | **str** | Snapshot name. | [optional] 
**snap_id** | **str** | ID of snapshot. | [optional] 
**snap_name** | **str** | Snapshot name. | [optional] 

## Example

```python
from dscc.models.snapshot_from_volume import SnapshotFromVolume

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotFromVolume from a JSON string
snapshot_from_volume_instance = SnapshotFromVolume.from_json(json)
# print the JSON string representation of the object
print(SnapshotFromVolume.to_json())

# convert the object into a dict
snapshot_from_volume_dict = snapshot_from_volume_instance.to_dict()
# create an instance of SnapshotFromVolume from a dict
snapshot_from_volume_from_dict = SnapshotFromVolume.from_dict(snapshot_from_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


