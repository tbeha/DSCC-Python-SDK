# NimbleMetricData

Timeseries data for particular metric type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleMetricPerfSeriesData]**](NimbleMetricPerfSeriesData.md) |  | [optional] 
**total** | **int** | total number of series data | [optional] 

## Example

```python
from dscc.models.nimble_metric_data import NimbleMetricData

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleMetricData from a JSON string
nimble_metric_data_instance = NimbleMetricData.from_json(json)
# print the JSON string representation of the object
print(NimbleMetricData.to_json())

# convert the object into a dict
nimble_metric_data_dict = nimble_metric_data_instance.to_dict()
# create an instance of NimbleMetricData from a dict
nimble_metric_data_from_dict = NimbleMetricData.from_dict(nimble_metric_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


