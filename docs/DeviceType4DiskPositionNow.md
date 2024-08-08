# DeviceType4DiskPositionNow

Disk Position Now

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cage** | **int** | cage ID | [optional] 
**disk** | **int** | disk ID. This field is deprecated. | [optional] 
**side** | **str** | disk side. This field is deprecated. | [optional] 
**sled** | **int** | sled ID | [optional] 

## Example

```python
from dscc.models.device_type4_disk_position_now import DeviceType4DiskPositionNow

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4DiskPositionNow from a JSON string
device_type4_disk_position_now_instance = DeviceType4DiskPositionNow.from_json(json)
# print the JSON string representation of the object
print(DeviceType4DiskPositionNow.to_json())

# convert the object into a dict
device_type4_disk_position_now_dict = device_type4_disk_position_now_instance.to_dict()
# create an instance of DeviceType4DiskPositionNow from a dict
device_type4_disk_position_now_from_dict = DeviceType4DiskPositionNow.from_dict(device_type4_disk_position_now_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


