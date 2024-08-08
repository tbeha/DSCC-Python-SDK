# VolumeSetProximitySettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[VolumeSetHostGroupList]**](VolumeSetHostGroupList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**resource_uri** | **str** | Resource URI for volume set proximity details | [optional] 
**total** | **int** | Total number of host groups | [optional] 

## Example

```python
from dscc.models.volume_set_proximity_settings import VolumeSetProximitySettings

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeSetProximitySettings from a JSON string
volume_set_proximity_settings_instance = VolumeSetProximitySettings.from_json(json)
# print the JSON string representation of the object
print(VolumeSetProximitySettings.to_json())

# convert the object into a dict
volume_set_proximity_settings_dict = volume_set_proximity_settings_instance.to_dict()
# create an instance of VolumeSetProximitySettings from a dict
volume_set_proximity_settings_from_dict = VolumeSetProximitySettings.from_dict(volume_set_proximity_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


