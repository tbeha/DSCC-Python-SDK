# DeviceType4offlineClone

Offline clone of a volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_volume** | [**DeviceType4createVolume**](DeviceType4createVolume.md) |  | [optional] 
**enable_resync** | **bool** | Specify to save a snapshot for fast resynchronization. | [optional] 
**use_existing_volume** | **bool** | Specify to use existing volume or create a new volume for clone. | [optional] 

## Example

```python
from dscc.models.device_type4offline_clone import DeviceType4offlineClone

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4offlineClone from a JSON string
device_type4offline_clone_instance = DeviceType4offlineClone.from_json(json)
# print the JSON string representation of the object
print(DeviceType4offlineClone.to_json())

# convert the object into a dict
device_type4offline_clone_dict = device_type4offline_clone_instance.to_dict()
# create an instance of DeviceType4offlineClone from a dict
device_type4offline_clone_from_dict = DeviceType4offlineClone.from_dict(device_type4offline_clone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


