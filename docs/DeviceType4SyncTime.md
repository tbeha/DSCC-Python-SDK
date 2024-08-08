# DeviceType4SyncTime

Last synchronization time in milliseconds since epoch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | Epoch time in milliseconds. | [optional] 
**tz** | **str** | Time zone name | [optional] 

## Example

```python
from dscc.models.device_type4_sync_time import DeviceType4SyncTime

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SyncTime from a JSON string
device_type4_sync_time_instance = DeviceType4SyncTime.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SyncTime.to_json())

# convert the object into a dict
device_type4_sync_time_dict = device_type4_sync_time_instance.to_dict()
# create an instance of DeviceType4SyncTime from a dict
device_type4_sync_time_from_dict = DeviceType4SyncTime.from_dict(device_type4_sync_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


