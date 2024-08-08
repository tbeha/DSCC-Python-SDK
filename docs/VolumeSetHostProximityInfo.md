# VolumeSetHostProximityInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dscc_host_name** | **str** | Name of host in DSCC | [optional] 
**host_id** | **str** | Unique ID of host | [optional] 
**name** | **str** | Host name | [optional] 
**os** | **str** | OS of host | [optional] 
**proximity** | [**HostProximityDetail**](HostProximityDetail.md) |  | [optional] 

## Example

```python
from dscc.models.volume_set_host_proximity_info import VolumeSetHostProximityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeSetHostProximityInfo from a JSON string
volume_set_host_proximity_info_instance = VolumeSetHostProximityInfo.from_json(json)
# print the JSON string representation of the object
print(VolumeSetHostProximityInfo.to_json())

# convert the object into a dict
volume_set_host_proximity_info_dict = volume_set_host_proximity_info_instance.to_dict()
# create an instance of VolumeSetHostProximityInfo from a dict
volume_set_host_proximity_info_from_dict = VolumeSetHostProximityInfo.from_dict(volume_set_host_proximity_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


