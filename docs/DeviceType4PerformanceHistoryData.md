# DeviceType4PerformanceHistoryData

performance trends for given granularity and time range for a component

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**CommonResourceAttributesPerf**](CommonResourceAttributesPerf.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**end_time** | **int** | end time of history data | [optional] 
**history_data** | [**DeviceType4PerformanceHistoryDataHistoryData**](DeviceType4PerformanceHistoryDataHistoryData.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**start_time** | **int** | start time of history data | [optional] 

## Example

```python
from dscc.models.device_type4_performance_history_data import DeviceType4PerformanceHistoryData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4PerformanceHistoryData from a JSON string
device_type4_performance_history_data_instance = DeviceType4PerformanceHistoryData.from_json(json)
# print the JSON string representation of the object
print(DeviceType4PerformanceHistoryData.to_json())

# convert the object into a dict
device_type4_performance_history_data_dict = device_type4_performance_history_data_instance.to_dict()
# create an instance of DeviceType4PerformanceHistoryData from a dict
device_type4_performance_history_data_from_dict = DeviceType4PerformanceHistoryData.from_dict(device_type4_performance_history_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


