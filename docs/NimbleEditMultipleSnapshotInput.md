# NimbleEditMultipleSnapshotInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_list** | [**List[NimbleEditSnapshotInput]**](NimbleEditSnapshotInput.md) |  | 

## Example

```python
from dscc.models.nimble_edit_multiple_snapshot_input import NimbleEditMultipleSnapshotInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleEditMultipleSnapshotInput from a JSON string
nimble_edit_multiple_snapshot_input_instance = NimbleEditMultipleSnapshotInput.from_json(json)
# print the JSON string representation of the object
print(NimbleEditMultipleSnapshotInput.to_json())

# convert the object into a dict
nimble_edit_multiple_snapshot_input_dict = nimble_edit_multiple_snapshot_input_instance.to_dict()
# create an instance of NimbleEditMultipleSnapshotInput from a dict
nimble_edit_multiple_snapshot_input_from_dict = NimbleEditMultipleSnapshotInput.from_dict(nimble_edit_multiple_snapshot_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


