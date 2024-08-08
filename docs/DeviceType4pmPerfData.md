# DeviceType4pmPerfData

Performance metrics average values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_of1day** | **float** | last one day avg data | [optional] 
**avg_of1hour** | **float** | last one hour avg data | [optional] 
**avg_of8hours** | **float** | last 8 hours avg data | [optional] 
**avg_of_latest** | **float** | latest perf data | [optional] 

## Example

```python
from dscc.models.device_type4pm_perf_data import DeviceType4pmPerfData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4pmPerfData from a JSON string
device_type4pm_perf_data_instance = DeviceType4pmPerfData.from_json(json)
# print the JSON string representation of the object
print(DeviceType4pmPerfData.to_json())

# convert the object into a dict
device_type4pm_perf_data_dict = device_type4pm_perf_data_instance.to_dict()
# create an instance of DeviceType4pmPerfData from a dict
device_type4pm_perf_data_from_dict = DeviceType4pmPerfData.from_dict(device_type4pm_perf_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


