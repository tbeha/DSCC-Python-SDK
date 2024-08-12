# VolumePerformanceHistoryHistoryData

performance history data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iops_metrics_data** | [**HistoricalMetricData**](HistoricalMetricData.md) |  | [optional] 
**iosz_metrics_data_kbs** | [**HistoricalMetricData**](HistoricalMetricData.md) |  | [optional] 
**latency_metrics_data_ms** | [**HistoricalMetricData**](HistoricalMetricData.md) |  | [optional] 
**qlen_metrics_data** | [**QlenMetricDataValue**](QlenMetricDataValue.md) |  | [optional] 
**throughput_metrics_data_kbps** | [**HistoricalMetricData**](HistoricalMetricData.md) |  | [optional] 

## Example

```python
from dscc.models.volume_performance_history_history_data import VolumePerformanceHistoryHistoryData

# TODO update the JSON string below
json = "{}"
# create an instance of VolumePerformanceHistoryHistoryData from a JSON string
volume_performance_history_history_data_instance = VolumePerformanceHistoryHistoryData.from_json(json)
# print the JSON string representation of the object
print(VolumePerformanceHistoryHistoryData.to_json())

# convert the object into a dict
volume_performance_history_history_data_dict = volume_performance_history_history_data_instance.to_dict()
# create an instance of VolumePerformanceHistoryHistoryData from a dict
volume_performance_history_history_data_from_dict = VolumePerformanceHistoryHistoryData.from_dict(volume_performance_history_history_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


