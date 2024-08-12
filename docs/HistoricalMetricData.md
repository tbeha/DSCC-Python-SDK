# HistoricalMetricData

Timeseries data for particular metric type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[MetricSeriesData]**](MetricSeriesData.md) |  | [optional] 
**total** | **int** | count of series data | [optional] 

## Example

```python
from dscc.models.historical_metric_data import HistoricalMetricData

# TODO update the JSON string below
json = "{}"
# create an instance of HistoricalMetricData from a JSON string
historical_metric_data_instance = HistoricalMetricData.from_json(json)
# print the JSON string representation of the object
print(HistoricalMetricData.to_json())

# convert the object into a dict
historical_metric_data_dict = historical_metric_data_instance.to_dict()
# create an instance of HistoricalMetricData from a dict
historical_metric_data_from_dict = HistoricalMetricData.from_dict(historical_metric_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


