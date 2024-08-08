# NimblePerformanceHistoryDataHistoryData

performance history data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iops_metrics_data** | [**List[NimbleMetricHistoryData]**](NimbleMetricHistoryData.md) |  | [optional] 
**latency_metrics_data_ms** | [**List[NimbleMetricHistoryData]**](NimbleMetricHistoryData.md) |  | [optional] 
**throughput_metrics_data_kbps** | [**List[NimbleMetricHistoryData]**](NimbleMetricHistoryData.md) |  | [optional] 

## Example

```python
from dscc.models.nimble_performance_history_data_history_data import NimblePerformanceHistoryDataHistoryData

# TODO update the JSON string below
json = "{}"
# create an instance of NimblePerformanceHistoryDataHistoryData from a JSON string
nimble_performance_history_data_history_data_instance = NimblePerformanceHistoryDataHistoryData.from_json(json)
# print the JSON string representation of the object
print(NimblePerformanceHistoryDataHistoryData.to_json())

# convert the object into a dict
nimble_performance_history_data_history_data_dict = nimble_performance_history_data_history_data_instance.to_dict()
# create an instance of NimblePerformanceHistoryDataHistoryData from a dict
nimble_performance_history_data_history_data_from_dict = NimblePerformanceHistoryDataHistoryData.from_dict(nimble_performance_history_data_history_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


