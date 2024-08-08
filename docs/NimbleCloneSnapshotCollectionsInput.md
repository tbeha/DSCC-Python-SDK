# NimbleCloneSnapshotCollectionsInput

Clone snapshot collections input {DeviceType-2}. Clone a snapshot collection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clone_volumes** | [**List[CloneVolumesInput]**](CloneVolumesInput.md) | List of clone volumes. | 

## Example

```python
from dscc.models.nimble_clone_snapshot_collections_input import NimbleCloneSnapshotCollectionsInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleCloneSnapshotCollectionsInput from a JSON string
nimble_clone_snapshot_collections_input_instance = NimbleCloneSnapshotCollectionsInput.from_json(json)
# print the JSON string representation of the object
print(NimbleCloneSnapshotCollectionsInput.to_json())

# convert the object into a dict
nimble_clone_snapshot_collections_input_dict = nimble_clone_snapshot_collections_input_instance.to_dict()
# create an instance of NimbleCloneSnapshotCollectionsInput from a dict
nimble_clone_snapshot_collections_input_from_dict = NimbleCloneSnapshotCollectionsInput.from_dict(nimble_clone_snapshot_collections_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


