# DeviceType4PerformanceHistoryDataHistoryData

performance history data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avgbusy_metrics_data_perct** | [**List[DeviceType4metricHistoryDataSingleValue]**](DeviceType4metricHistoryDataSingleValue.md) |  | [optional] 
**iops_metrics_data** | [**List[DeviceType4metricHistoryData]**](DeviceType4metricHistoryData.md) |  | [optional] 
**iosz_metrics_data_kbs** | [**List[DeviceType4metricHistoryData]**](DeviceType4metricHistoryData.md) |  | [optional] 
**latency_metrics_data_ms** | [**List[DeviceType4metricHistoryData]**](DeviceType4metricHistoryData.md) |  | [optional] 
**qlen_metrics_data** | [**List[DeviceType4metricHistoryDataSingleValue]**](DeviceType4metricHistoryDataSingleValue.md) |  | [optional] 
**throughput_metrics_data_kbps** | [**List[DeviceType4metricHistoryData]**](DeviceType4metricHistoryData.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_performance_history_data_history_data import DeviceType4PerformanceHistoryDataHistoryData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4PerformanceHistoryDataHistoryData from a JSON string
device_type4_performance_history_data_history_data_instance = DeviceType4PerformanceHistoryDataHistoryData.from_json(json)
# print the JSON string representation of the object
print(DeviceType4PerformanceHistoryDataHistoryData.to_json())

# convert the object into a dict
device_type4_performance_history_data_history_data_dict = device_type4_performance_history_data_history_data_instance.to_dict()
# create an instance of DeviceType4PerformanceHistoryDataHistoryData from a dict
device_type4_performance_history_data_history_data_from_dict = DeviceType4PerformanceHistoryDataHistoryData.from_dict(device_type4_performance_history_data_history_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


