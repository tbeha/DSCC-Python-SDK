# DeviceType4uptime

The time that the system has been up since

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | Epoch time in milliseconds | [optional] 
**tz** | **str** | Time zone name | [optional] 

## Example

```python
from dscc.models.device_type4uptime import DeviceType4uptime

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4uptime from a JSON string
device_type4uptime_instance = DeviceType4uptime.from_json(json)
# print the JSON string representation of the object
print(DeviceType4uptime.to_json())

# convert the object into a dict
device_type4uptime_dict = device_type4uptime_instance.to_dict()
# create an instance of DeviceType4uptime from a dict
device_type4uptime_from_dict = DeviceType4uptime.from_dict(device_type4uptime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


