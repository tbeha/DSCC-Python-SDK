# NimbleMetricHistoryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart_legend_id** | **str** | Id to display chart legend, gives information about filtered object | [optional] 
**resource_id** | **str** | Unique Id to represent resource id of filtered object | [optional] 
**time_series_data** | [**NimbleMetricData**](NimbleMetricData.md) |  | [optional] 

## Example

```python
from dscc.models.nimble_metric_history_data import NimbleMetricHistoryData

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleMetricHistoryData from a JSON string
nimble_metric_history_data_instance = NimbleMetricHistoryData.from_json(json)
# print the JSON string representation of the object
print(NimbleMetricHistoryData.to_json())

# convert the object into a dict
nimble_metric_history_data_dict = nimble_metric_history_data_instance.to_dict()
# create an instance of NimbleMetricHistoryData from a dict
nimble_metric_history_data_from_dict = NimbleMetricHistoryData.from_dict(nimble_metric_history_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


