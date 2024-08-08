# SnapshotCollectionAction

Snapshot collection input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the snapshot collection. A 42 digit hexadecimal number. | [optional] 

## Example

```python
from dscc.models.snapshot_collection_action import SnapshotCollectionAction

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotCollectionAction from a JSON string
snapshot_collection_action_instance = SnapshotCollectionAction.from_json(json)
# print the JSON string representation of the object
print(SnapshotCollectionAction.to_json())

# convert the object into a dict
snapshot_collection_action_dict = snapshot_collection_action_instance.to_dict()
# create an instance of SnapshotCollectionAction from a dict
snapshot_collection_action_from_dict = SnapshotCollectionAction.from_dict(snapshot_collection_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


