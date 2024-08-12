# DeviceType4ResyncCloneVolumeInput

Resynchronize clone input. Resynchronize a clone volume with given priority.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | [**DeviceType4ClonePriority**](DeviceType4ClonePriority.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_resync_clone_volume_input import DeviceType4ResyncCloneVolumeInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ResyncCloneVolumeInput from a JSON string
device_type4_resync_clone_volume_input_instance = DeviceType4ResyncCloneVolumeInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ResyncCloneVolumeInput.to_json())

# convert the object into a dict
device_type4_resync_clone_volume_input_dict = device_type4_resync_clone_volume_input_instance.to_dict()
# create an instance of DeviceType4ResyncCloneVolumeInput from a dict
device_type4_resync_clone_volume_input_from_dict = DeviceType4ResyncCloneVolumeInput.from_dict(device_type4_resync_clone_volume_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


