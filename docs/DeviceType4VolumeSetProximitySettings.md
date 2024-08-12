# DeviceType4VolumeSetProximitySettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4VolumeSetHostGroupList]**](DeviceType4VolumeSetHostGroupList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**resource_uri** | **str** | Resource URI for volume set proximity details | [optional] 
**total** | **int** | Total number of host groups | [optional] 

## Example

```python
from dscc.models.device_type4_volume_set_proximity_settings import DeviceType4VolumeSetProximitySettings

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VolumeSetProximitySettings from a JSON string
device_type4_volume_set_proximity_settings_instance = DeviceType4VolumeSetProximitySettings.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VolumeSetProximitySettings.to_json())

# convert the object into a dict
device_type4_volume_set_proximity_settings_dict = device_type4_volume_set_proximity_settings_instance.to_dict()
# create an instance of DeviceType4VolumeSetProximitySettings from a dict
device_type4_volume_set_proximity_settings_from_dict = DeviceType4VolumeSetProximitySettings.from_dict(device_type4_volume_set_proximity_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


