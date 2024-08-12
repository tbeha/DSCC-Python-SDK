# ResyncCloneVolumeInput

Resynchronize clone input. Resynchronize a clone volume with given priority.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | [**ClonePriority**](ClonePriority.md) |  | [optional] 

## Example

```python
from dscc.models.resync_clone_volume_input import ResyncCloneVolumeInput

# TODO update the JSON string below
json = "{}"
# create an instance of ResyncCloneVolumeInput from a JSON string
resync_clone_volume_input_instance = ResyncCloneVolumeInput.from_json(json)
# print the JSON string representation of the object
print(ResyncCloneVolumeInput.to_json())

# convert the object into a dict
resync_clone_volume_input_dict = resync_clone_volume_input_instance.to_dict()
# create an instance of ResyncCloneVolumeInput from a dict
resync_clone_volume_input_from_dict = ResyncCloneVolumeInput.from_dict(resync_clone_volume_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


