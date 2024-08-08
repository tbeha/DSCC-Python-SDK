# NimbleMetricSeriesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_value** | **float** | average read metric value at particular timestamp | [optional] 
**timestampms** | **int** | epoch timestamp | [optional] 
**total_value** | **float** | total metric value at particular timestamp | [optional] 
**write_value** | **float** | average write metric value at particular timestamp | [optional] 

## Example

```python
from dscc.models.nimble_metric_series_data import NimbleMetricSeriesData

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleMetricSeriesData from a JSON string
nimble_metric_series_data_instance = NimbleMetricSeriesData.from_json(json)
# print the JSON string representation of the object
print(NimbleMetricSeriesData.to_json())

# convert the object into a dict
nimble_metric_series_data_dict = nimble_metric_series_data_instance.to_dict()
# create an instance of NimbleMetricSeriesData from a dict
nimble_metric_series_data_from_dict = NimbleMetricSeriesData.from_dict(nimble_metric_series_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


