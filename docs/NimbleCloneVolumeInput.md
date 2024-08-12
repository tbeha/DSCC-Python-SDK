# NimbleCloneVolumeInput

Create Nimble clone volume input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clone_volume_name** | **str** | Name of the clone volume. | 
**host_group_id** | **str** | Identifier for the host group. | [optional] 
**lun** | **int** | Custom LUN ID for the host group. Specify integer in the range 0 to 2047. | [optional] 

## Example

```python
from dscc.models.nimble_clone_volume_input import NimbleCloneVolumeInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleCloneVolumeInput from a JSON string
nimble_clone_volume_input_instance = NimbleCloneVolumeInput.from_json(json)
# print the JSON string representation of the object
print(NimbleCloneVolumeInput.to_json())

# convert the object into a dict
nimble_clone_volume_input_dict = nimble_clone_volume_input_instance.to_dict()
# create an instance of NimbleCloneVolumeInput from a dict
nimble_clone_volume_input_from_dict = NimbleCloneVolumeInput.from_dict(nimble_clone_volume_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


