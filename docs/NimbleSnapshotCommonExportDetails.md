# NimbleSnapshotCommonExportDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_export_details** | [**NimbleVolumeExportDetails**](NimbleVolumeExportDetails.md) |  | [optional] 

## Example

```python
from dscc.models.nimble_snapshot_common_export_details import NimbleSnapshotCommonExportDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleSnapshotCommonExportDetails from a JSON string
nimble_snapshot_common_export_details_instance = NimbleSnapshotCommonExportDetails.from_json(json)
# print the JSON string representation of the object
print(NimbleSnapshotCommonExportDetails.to_json())

# convert the object into a dict
nimble_snapshot_common_export_details_dict = nimble_snapshot_common_export_details_instance.to_dict()
# create an instance of NimbleSnapshotCommonExportDetails from a dict
nimble_snapshot_common_export_details_from_dict = NimbleSnapshotCommonExportDetails.from_dict(nimble_snapshot_common_export_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


