# NimblehistoricalMetricData

Timeseries data for particular metric type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series_data** | [**List[NimbleMetricSeriesData]**](NimbleMetricSeriesData.md) |  | [optional] 
**total** | **int** | total number of series data | [optional] 

## Example

```python
from dscc.models.nimblehistorical_metric_data import NimblehistoricalMetricData

# TODO update the JSON string below
json = "{}"
# create an instance of NimblehistoricalMetricData from a JSON string
nimblehistorical_metric_data_instance = NimblehistoricalMetricData.from_json(json)
# print the JSON string representation of the object
print(NimblehistoricalMetricData.to_json())

# convert the object into a dict
nimblehistorical_metric_data_dict = nimblehistorical_metric_data_instance.to_dict()
# create an instance of NimblehistoricalMetricData from a dict
nimblehistorical_metric_data_from_dict = NimblehistoricalMetricData.from_dict(nimblehistorical_metric_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


