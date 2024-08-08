# DeviceType4VolumePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment if any | [optional] 
**custom_name** | **str** | Name for snapshot | [optional] 
**expire_secs** | **int** | Expiration time in seconds | [optional] 
**name_pattern** | [**DeviceType4NamePattern**](DeviceType4NamePattern.md) |  | 
**read_only** | **bool** | Read only or Read/Write | [optional] 
**retain_secs** | **int** | Reatain time in seconds | [optional] 

## Example

```python
from dscc.models.device_type4_volume_post import DeviceType4VolumePost

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VolumePost from a JSON string
device_type4_volume_post_instance = DeviceType4VolumePost.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VolumePost.to_json())

# convert the object into a dict
device_type4_volume_post_dict = device_type4_volume_post_instance.to_dict()
# create an instance of DeviceType4VolumePost from a dict
device_type4_volume_post_from_dict = DeviceType4VolumePost.from_dict(device_type4_volume_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


