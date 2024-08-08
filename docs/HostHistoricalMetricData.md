# HostHistoricalMetricData

Timeseries data for particular metric type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | count of series data | [optional] 
**series_data** | [**List[HostMetricSeriesData]**](HostMetricSeriesData.md) |  | [optional] 

## Example

```python
from dscc.models.host_historical_metric_data import HostHistoricalMetricData

# TODO update the JSON string below
json = "{}"
# create an instance of HostHistoricalMetricData from a JSON string
host_historical_metric_data_instance = HostHistoricalMetricData.from_json(json)
# print the JSON string representation of the object
print(HostHistoricalMetricData.to_json())

# convert the object into a dict
host_historical_metric_data_dict = host_historical_metric_data_instance.to_dict()
# create an instance of HostHistoricalMetricData from a dict
host_historical_metric_data_from_dict = HostHistoricalMetricData.from_dict(host_historical_metric_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


