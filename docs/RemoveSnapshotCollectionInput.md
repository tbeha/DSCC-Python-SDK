# RemoveSnapshotCollectionInput

Request body for removing snapshot collections.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force** | **bool** | Force remove. | [optional] 
**snapshot_collections** | [**List[SnapshotCollectionAction]**](SnapshotCollectionAction.md) | List of snapshot collections to be deleted. | 

## Example

```python
from dscc.models.remove_snapshot_collection_input import RemoveSnapshotCollectionInput

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveSnapshotCollectionInput from a JSON string
remove_snapshot_collection_input_instance = RemoveSnapshotCollectionInput.from_json(json)
# print the JSON string representation of the object
print(RemoveSnapshotCollectionInput.to_json())

# convert the object into a dict
remove_snapshot_collection_input_dict = remove_snapshot_collection_input_instance.to_dict()
# create an instance of RemoveSnapshotCollectionInput from a dict
remove_snapshot_collection_input_from_dict = RemoveSnapshotCollectionInput.from_dict(remove_snapshot_collection_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


