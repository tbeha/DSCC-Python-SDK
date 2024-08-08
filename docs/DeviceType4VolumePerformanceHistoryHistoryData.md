# DeviceType4VolumePerformanceHistoryHistoryData

performance history data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iops_metrics_data** | [**DeviceType4historicalMetricData**](DeviceType4historicalMetricData.md) |  | [optional] 
**iosz_metrics_data_kbs** | [**DeviceType4historicalMetricData**](DeviceType4historicalMetricData.md) |  | [optional] 
**latency_metrics_data_ms** | [**DeviceType4historicalMetricData**](DeviceType4historicalMetricData.md) |  | [optional] 
**qlen_metrics_data** | [**DeviceType4QlenMetricDataValue**](DeviceType4QlenMetricDataValue.md) |  | [optional] 
**throughput_metrics_data_kbps** | [**DeviceType4historicalMetricData**](DeviceType4historicalMetricData.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_volume_performance_history_history_data import DeviceType4VolumePerformanceHistoryHistoryData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VolumePerformanceHistoryHistoryData from a JSON string
device_type4_volume_performance_history_history_data_instance = DeviceType4VolumePerformanceHistoryHistoryData.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VolumePerformanceHistoryHistoryData.to_json())

# convert the object into a dict
device_type4_volume_performance_history_history_data_dict = device_type4_volume_performance_history_history_data_instance.to_dict()
# create an instance of DeviceType4VolumePerformanceHistoryHistoryData from a dict
device_type4_volume_performance_history_history_data_from_dict = DeviceType4VolumePerformanceHistoryHistoryData.from_dict(device_type4_volume_performance_history_history_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


