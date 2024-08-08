# NimbleRestoreVolumeInput

Restore volume data from a previous snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_snap_id** | **str** | ID of the snapshot to which this the volume is restored. | 
**enable_vol_offline** | **bool** | Option to specify if volume should be set offline before restore. This value should be set to true if the volume is online. | [optional] 

## Example

```python
from dscc.models.nimble_restore_volume_input import NimbleRestoreVolumeInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleRestoreVolumeInput from a JSON string
nimble_restore_volume_input_instance = NimbleRestoreVolumeInput.from_json(json)
# print the JSON string representation of the object
print(NimbleRestoreVolumeInput.to_json())

# convert the object into a dict
nimble_restore_volume_input_dict = nimble_restore_volume_input_instance.to_dict()
# create an instance of NimbleRestoreVolumeInput from a dict
nimble_restore_volume_input_from_dict = NimbleRestoreVolumeInput.from_dict(nimble_restore_volume_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


