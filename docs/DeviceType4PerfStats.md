# DeviceType4PerfStats

Collection of average cpu percentage and average cache percentage for various durations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_percentage** | [**DeviceType4perfData**](DeviceType4perfData.md) |  | [optional] 
**cpu_percentage** | [**DeviceType4perfData**](DeviceType4perfData.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**request_uri** | **str** | requestUri for detailed performance stats object | [optional] 

## Example

```python
from dscc.models.device_type4_perf_stats import DeviceType4PerfStats

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4PerfStats from a JSON string
device_type4_perf_stats_instance = DeviceType4PerfStats.from_json(json)
# print the JSON string representation of the object
print(DeviceType4PerfStats.to_json())

# convert the object into a dict
device_type4_perf_stats_dict = device_type4_perf_stats_instance.to_dict()
# create an instance of DeviceType4PerfStats from a dict
device_type4_perf_stats_from_dict = DeviceType4PerfStats.from_dict(device_type4_perf_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


