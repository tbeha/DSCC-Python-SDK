# NimbleMetricPerfSeriesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the object at particular timestamp | [optional] 
**read_value** | **float** | average read metric value at particular timestamp | [optional] 
**timestampms** | **int** | epoch timestamp | [optional] 
**write_value** | **float** | average write metric value at particular timestamp | [optional] 

## Example

```python
from dscc.models.nimble_metric_perf_series_data import NimbleMetricPerfSeriesData

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleMetricPerfSeriesData from a JSON string
nimble_metric_perf_series_data_instance = NimbleMetricPerfSeriesData.from_json(json)
# print the JSON string representation of the object
print(NimbleMetricPerfSeriesData.to_json())

# convert the object into a dict
nimble_metric_perf_series_data_dict = nimble_metric_perf_series_data_instance.to_dict()
# create an instance of NimbleMetricPerfSeriesData from a dict
nimble_metric_perf_series_data_from_dict = NimbleMetricPerfSeriesData.from_dict(nimble_metric_perf_series_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


