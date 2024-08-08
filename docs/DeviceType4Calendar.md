# DeviceType4calendar



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** |  | [optional] 
**tz** | **str** |  | [optional] 

## Example

```python
from dscc.models.device_type4calendar import DeviceType4calendar

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4calendar from a JSON string
device_type4calendar_instance = DeviceType4calendar.from_json(json)
# print the JSON string representation of the object
print(DeviceType4calendar.to_json())

# convert the object into a dict
device_type4calendar_dict = device_type4calendar_instance.to_dict()
# create an instance of DeviceType4calendar from a dict
device_type4calendar_from_dict = DeviceType4calendar.from_dict(device_type4calendar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


