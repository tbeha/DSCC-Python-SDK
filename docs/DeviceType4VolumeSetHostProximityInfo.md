# DeviceType4VolumeSetHostProximityInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dscc_host_name** | **str** | Name of host in DSCC | [optional] 
**host_id** | **str** | Unique ID of host | [optional] 
**name** | **str** | Host name | [optional] 
**os** | **str** | OS of host | [optional] 
**proximity** | [**DeviceType4hostProximityDetail**](DeviceType4hostProximityDetail.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_volume_set_host_proximity_info import DeviceType4VolumeSetHostProximityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VolumeSetHostProximityInfo from a JSON string
device_type4_volume_set_host_proximity_info_instance = DeviceType4VolumeSetHostProximityInfo.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VolumeSetHostProximityInfo.to_json())

# convert the object into a dict
device_type4_volume_set_host_proximity_info_dict = device_type4_volume_set_host_proximity_info_instance.to_dict()
# create an instance of DeviceType4VolumeSetHostProximityInfo from a dict
device_type4_volume_set_host_proximity_info_from_dict = DeviceType4VolumeSetHostProximityInfo.from_dict(device_type4_volume_set_host_proximity_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


