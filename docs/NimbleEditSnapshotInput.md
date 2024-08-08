# NimbleEditSnapshotInput

Edit Nimble snapshot input. Edit a snapshot with the given attributes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_uuid** | **str** | Application identifier of snapshots. String of up to 255 alphanumeric characters, hyphen, colon, dot and underscore are allowed. Defaults to empty string. | [optional] 
**description** | **str** | Text description of snapshot. String of up to 255 printable ASCII characters. Defaults to the empty string. | [optional] 
**id** | **str** | Identifier for the snapshot. A 42 digit hexadecimal number. | 
**lock_period** | **int** | Number of seconds to keep a snapshot as immutable. | [optional] 
**metadata** | [**List[KeyValue]**](KeyValue.md) | Key-value pairs that augment a volume&#39;s attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed. Defaults to an empty array. | [optional] 
**online** | **bool** | Online state for a snapshot means it could be mounted for data restore. Defaults to &#39;false&#39;. | [optional] 

## Example

```python
from dscc.models.nimble_edit_snapshot_input import NimbleEditSnapshotInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleEditSnapshotInput from a JSON string
nimble_edit_snapshot_input_instance = NimbleEditSnapshotInput.from_json(json)
# print the JSON string representation of the object
print(NimbleEditSnapshotInput.to_json())

# convert the object into a dict
nimble_edit_snapshot_input_dict = nimble_edit_snapshot_input_instance.to_dict()
# create an instance of NimbleEditSnapshotInput from a dict
nimble_edit_snapshot_input_from_dict = NimbleEditSnapshotInput.from_dict(nimble_edit_snapshot_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


