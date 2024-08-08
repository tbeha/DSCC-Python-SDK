# SnapshotLunInfo

Information about the snapshot LUNs. This information is available only for Fibre Channel.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of snapshot. | [optional] 
**lun** | **int** | Snapshot LUN. | [optional] 
**name** | **str** | Snapshot name. | [optional] 

## Example

```python
from dscc.models.snapshot_lun_info import SnapshotLunInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotLunInfo from a JSON string
snapshot_lun_info_instance = SnapshotLunInfo.from_json(json)
# print the JSON string representation of the object
print(SnapshotLunInfo.to_json())

# convert the object into a dict
snapshot_lun_info_dict = snapshot_lun_info_instance.to_dict()
# create an instance of SnapshotLunInfo from a dict
snapshot_lun_info_from_dict = SnapshotLunInfo.from_dict(snapshot_lun_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


