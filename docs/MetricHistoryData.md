# MetricHistoryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart_legend_id** | **str** | Id to display chart legend, gives information about groupby and filtered objects | [optional] 
**time_series_data** | [**MetricReadWriteData**](MetricReadWriteData.md) |  | [optional] 

## Example

```python
from dscc.models.metric_history_data import MetricHistoryData

# TODO update the JSON string below
json = "{}"
# create an instance of MetricHistoryData from a JSON string
metric_history_data_instance = MetricHistoryData.from_json(json)
# print the JSON string representation of the object
print(MetricHistoryData.to_json())

# convert the object into a dict
metric_history_data_dict = metric_history_data_instance.to_dict()
# create an instance of MetricHistoryData from a dict
metric_history_data_from_dict = MetricHistoryData.from_dict(metric_history_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


