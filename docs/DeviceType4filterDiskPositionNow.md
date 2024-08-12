# DeviceType4filterDiskPositionNow

Disk Position Now

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cage** | **int** | cage ID. &#x60;Filter, Sort&#x60; | [optional] 
**sled** | **int** | sled ID. | [optional] 

## Example

```python
from dscc.models.device_type4filter_disk_position_now import DeviceType4filterDiskPositionNow

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4filterDiskPositionNow from a JSON string
device_type4filter_disk_position_now_instance = DeviceType4filterDiskPositionNow.from_json(json)
# print the JSON string representation of the object
print(DeviceType4filterDiskPositionNow.to_json())

# convert the object into a dict
device_type4filter_disk_position_now_dict = device_type4filter_disk_position_now_instance.to_dict()
# create an instance of DeviceType4filterDiskPositionNow from a dict
device_type4filter_disk_position_now_from_dict = DeviceType4filterDiskPositionNow.from_dict(device_type4filter_disk_position_now_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


