# DeviceType4AppsetPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment if any | [optional] 
**expire_secs** | **int** | Expiration time in seconds | [optional] 
**read_only** | **bool** | Read only or Read/Write | [optional] 
**retain_secs** | **int** | Reatain time in seconds | [optional] 
**snapshot_name** | **str** | Name for snapshot | 
**vv_name_pattern** | [**DeviceType4vvNamePattern**](DeviceType4vvNamePattern.md) |  | 

## Example

```python
from dscc.models.device_type4_appset_post import DeviceType4AppsetPost

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4AppsetPost from a JSON string
device_type4_appset_post_instance = DeviceType4AppsetPost.from_json(json)
# print the JSON string representation of the object
print(DeviceType4AppsetPost.to_json())

# convert the object into a dict
device_type4_appset_post_dict = device_type4_appset_post_instance.to_dict()
# create an instance of DeviceType4AppsetPost from a dict
device_type4_appset_post_from_dict = DeviceType4AppsetPost.from_dict(device_type4_appset_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


