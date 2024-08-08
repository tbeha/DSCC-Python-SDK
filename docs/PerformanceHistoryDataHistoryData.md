# PerformanceHistoryDataHistoryData

performance history data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avgbusy_metrics_data_perct** | [**List[MetricHistoryDataSingleValue]**](MetricHistoryDataSingleValue.md) |  | [optional] 
**iops_metrics_data** | [**List[MetricHistoryData]**](MetricHistoryData.md) |  | [optional] 
**iosz_metrics_data_kbs** | [**List[MetricHistoryData]**](MetricHistoryData.md) |  | [optional] 
**latency_metrics_data_ms** | [**List[MetricHistoryData]**](MetricHistoryData.md) |  | [optional] 
**qlen_metrics_data** | [**List[MetricHistoryDataSingleValue]**](MetricHistoryDataSingleValue.md) |  | [optional] 
**throughput_metrics_data_kbps** | [**List[MetricHistoryData]**](MetricHistoryData.md) |  | [optional] 

## Example

```python
from dscc.models.performance_history_data_history_data import PerformanceHistoryDataHistoryData

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceHistoryDataHistoryData from a JSON string
performance_history_data_history_data_instance = PerformanceHistoryDataHistoryData.from_json(json)
# print the JSON string representation of the object
print(PerformanceHistoryDataHistoryData.to_json())

# convert the object into a dict
performance_history_data_history_data_dict = performance_history_data_history_data_instance.to_dict()
# create an instance of PerformanceHistoryDataHistoryData from a dict
performance_history_data_history_data_from_dict = PerformanceHistoryDataHistoryData.from_dict(performance_history_data_history_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


