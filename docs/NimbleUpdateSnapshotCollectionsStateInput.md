# NimbleUpdateSnapshotCollectionsStateInput

Set snapshot collections online or offline by setting the corresponding snapshots online or offline.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**online** | **bool** | Online state for the corresponding snapshots. For a snapshot, &#39;online&#39; means it could be mounted for data restore. | 
**snapshot_collection_ids** | **List[str]** | List of IDs of snapshot collections to be set online/offline. | 

## Example

```python
from dscc.models.nimble_update_snapshot_collections_state_input import NimbleUpdateSnapshotCollectionsStateInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleUpdateSnapshotCollectionsStateInput from a JSON string
nimble_update_snapshot_collections_state_input_instance = NimbleUpdateSnapshotCollectionsStateInput.from_json(json)
# print the JSON string representation of the object
print(NimbleUpdateSnapshotCollectionsStateInput.to_json())

# convert the object into a dict
nimble_update_snapshot_collections_state_input_dict = nimble_update_snapshot_collections_state_input_instance.to_dict()
# create an instance of NimbleUpdateSnapshotCollectionsStateInput from a dict
nimble_update_snapshot_collections_state_input_from_dict = NimbleUpdateSnapshotCollectionsStateInput.from_dict(nimble_update_snapshot_collections_state_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


