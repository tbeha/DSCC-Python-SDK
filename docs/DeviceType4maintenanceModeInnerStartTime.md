# DeviceType4maintenanceModeInnerStartTime

start time

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | epoc time | [optional] 
**tz** | **str** | time zone | [optional] 

## Example

```python
from dscc.models.device_type4maintenance_mode_inner_start_time import DeviceType4maintenanceModeInnerStartTime

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4maintenanceModeInnerStartTime from a JSON string
device_type4maintenance_mode_inner_start_time_instance = DeviceType4maintenanceModeInnerStartTime.from_json(json)
# print the JSON string representation of the object
print(DeviceType4maintenanceModeInnerStartTime.to_json())

# convert the object into a dict
device_type4maintenance_mode_inner_start_time_dict = device_type4maintenance_mode_inner_start_time_instance.to_dict()
# create an instance of DeviceType4maintenanceModeInnerStartTime from a dict
device_type4maintenance_mode_inner_start_time_from_dict = DeviceType4maintenanceModeInnerStartTime.from_dict(device_type4maintenance_mode_inner_start_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


