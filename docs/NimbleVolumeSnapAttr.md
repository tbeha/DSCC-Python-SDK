# NimbleVolumeSnapAttr

Snapshot attributes for snapshots being created as part of snapshot collection creation. List of volumes with per snapshot attributes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_uuid** | **str** | Application identifier of snapshots. String of up to 255 alphanumeric characters, hyphen, colon, dot and underscore are allowed. Defaults to empty string. | [optional] 
**metadata** | [**List[KeyValue]**](KeyValue.md) | Key-value pairs that augment a volume&#39;s attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed. Defaults to an empty array. | [optional] 
**vol_id** | **str** | Identifier of volume. A 42 digit hexadecimal number. | [optional] 

## Example

```python
from dscc.models.nimble_volume_snap_attr import NimbleVolumeSnapAttr

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleVolumeSnapAttr from a JSON string
nimble_volume_snap_attr_instance = NimbleVolumeSnapAttr.from_json(json)
# print the JSON string representation of the object
print(NimbleVolumeSnapAttr.to_json())

# convert the object into a dict
nimble_volume_snap_attr_dict = nimble_volume_snap_attr_instance.to_dict()
# create an instance of NimbleVolumeSnapAttr from a dict
nimble_volume_snap_attr_from_dict = NimbleVolumeSnapAttr.from_dict(nimble_volume_snap_attr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


