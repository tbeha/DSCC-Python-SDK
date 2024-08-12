# DeviceType4calendarTime

Time zone and epoch time

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | Epoch time in milliseconds | [optional] 
**tz** | **str** | Time zone name | [optional] 

## Example

```python
from dscc.models.device_type4calendar_time import DeviceType4calendarTime

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4calendarTime from a JSON string
device_type4calendar_time_instance = DeviceType4calendarTime.from_json(json)
# print the JSON string representation of the object
print(DeviceType4calendarTime.to_json())

# convert the object into a dict
device_type4calendar_time_dict = device_type4calendar_time_instance.to_dict()
# create an instance of DeviceType4calendarTime from a dict
device_type4calendar_time_from_dict = DeviceType4calendarTime.from_dict(device_type4calendar_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


