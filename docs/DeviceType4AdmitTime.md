# DeviceType4AdmitTime

admission time of disk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | time in millisecond | [optional] 
**tz** | **str** | timezone | [optional] 

## Example

```python
from dscc.models.device_type4_admit_time import DeviceType4AdmitTime

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4AdmitTime from a JSON string
device_type4_admit_time_instance = DeviceType4AdmitTime.from_json(json)
# print the JSON string representation of the object
print(DeviceType4AdmitTime.to_json())

# convert the object into a dict
device_type4_admit_time_dict = device_type4_admit_time_instance.to_dict()
# create an instance of DeviceType4AdmitTime from a dict
device_type4_admit_time_from_dict = DeviceType4AdmitTime.from_dict(device_type4_admit_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


