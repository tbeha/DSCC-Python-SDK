# VolumePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment if any | [optional] 
**custom_name** | **str** | Name for snapshot | [optional] 
**expire_secs** | **int** | Expiration time in seconds | [optional] 
**name_pattern** | [**NamePattern**](NamePattern.md) |  | 
**read_only** | **bool** | Read only or Read/Write | [optional] 
**retain_secs** | **int** | Reatain time in seconds | [optional] 

## Example

```python
from dscc.models.volume_post import VolumePost

# TODO update the JSON string below
json = "{}"
# create an instance of VolumePost from a JSON string
volume_post_instance = VolumePost.from_json(json)
# print the JSON string representation of the object
print(VolumePost.to_json())

# convert the object into a dict
volume_post_dict = volume_post_instance.to_dict()
# create an instance of VolumePost from a dict
volume_post_from_dict = VolumePost.from_dict(volume_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


