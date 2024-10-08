# NimbleCreateSnapshotInput

Create Nimble snapshot input. Create a snapshot with the given attributes. VSS application-synchronized snapshot must specify the 'writable' parameter and set it to 'true'.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_uuid** | **str** | Application identifier of snapshots. String of up to 255 alphanumeric characters, hyphen, colon, dot and underscore are allowed. Defaults to empty string. | [optional] 
**description** | **str** | Text description of snapshot. String of up to 255 printable ASCII characters. Defaults to the empty string. | [optional] 
**lock_period** | **int** | Number of seconds to keep a snapshot as immutable. | [optional] 
**metadata** | [**List[KeyValue]**](KeyValue.md) | Key-value pairs that augment a volume&#39;s attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed. Defaults to an empty array. | [optional] 
**name** | **str** | Name of the snapshot. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. This type is used for object sets containing volumes, snapshots, snapshot collections and protocol endpoints. | 
**online** | **bool** | Online state for a snapshot means it could be mounted for data restore. Defaults to &#39;false&#39;. | [optional] 
**writable** | **bool** | Allow snapshot to be writable. Mandatory and must be set to &#39;true&#39; for VSS application synchronized snapshots. Defaults to &#39;false&#39;. | [optional] 

## Example

```python
from dscc.models.nimble_create_snapshot_input import NimbleCreateSnapshotInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleCreateSnapshotInput from a JSON string
nimble_create_snapshot_input_instance = NimbleCreateSnapshotInput.from_json(json)
# print the JSON string representation of the object
print(NimbleCreateSnapshotInput.to_json())

# convert the object into a dict
nimble_create_snapshot_input_dict = nimble_create_snapshot_input_instance.to_dict()
# create an instance of NimbleCreateSnapshotInput from a dict
nimble_create_snapshot_input_from_dict = NimbleCreateSnapshotInput.from_dict(nimble_create_snapshot_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


