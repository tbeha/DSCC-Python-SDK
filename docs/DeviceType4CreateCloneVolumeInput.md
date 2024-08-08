# DeviceType4CreateCloneVolumeInput

Request body for creating physical copy of a volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_volume** | **str** | Name of the destination volume. | 
**offline_clone** | [**DeviceType4offlineClone**](DeviceType4offlineClone.md) |  | [optional] 
**online** | **bool** | Create an online or offline clone of a volume. | [optional] 
**online_clone** | [**DeviceType4onlineClone**](DeviceType4onlineClone.md) |  | [optional] 
**priority** | **str** | Priority of the task for clone volume. Defualts to MEDIUM. | [optional] 

## Example

```python
from dscc.models.device_type4_create_clone_volume_input import DeviceType4CreateCloneVolumeInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4CreateCloneVolumeInput from a JSON string
device_type4_create_clone_volume_input_instance = DeviceType4CreateCloneVolumeInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4CreateCloneVolumeInput.to_json())

# convert the object into a dict
device_type4_create_clone_volume_input_dict = device_type4_create_clone_volume_input_instance.to_dict()
# create an instance of DeviceType4CreateCloneVolumeInput from a dict
device_type4_create_clone_volume_input_from_dict = DeviceType4CreateCloneVolumeInput.from_dict(device_type4_create_clone_volume_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


