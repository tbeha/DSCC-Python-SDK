# HistoryData

Performance history data for given time range and granularily for a device

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
from dscc.models.history_data import HistoryData

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryData from a JSON string
history_data_instance = HistoryData.from_json(json)
# print the JSON string representation of the object
print(HistoryData.to_json())

# convert the object into a dict
history_data_dict = history_data_instance.to_dict()
# create an instance of HistoryData from a dict
history_data_from_dict = HistoryData.from_dict(history_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


