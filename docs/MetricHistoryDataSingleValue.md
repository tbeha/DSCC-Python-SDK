# MetricHistoryDataSingleValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart_legend_id** | **str** | Id to display chart legend, gives information about groupby and filtered objects | [optional] 
**time_series_data** | [**MetricDataValue**](MetricDataValue.md) |  | [optional] 

## Example

```python
from dscc.models.metric_history_data_single_value import MetricHistoryDataSingleValue

# TODO update the JSON string below
json = "{}"
# create an instance of MetricHistoryDataSingleValue from a JSON string
metric_history_data_single_value_instance = MetricHistoryDataSingleValue.from_json(json)
# print the JSON string representation of the object
print(MetricHistoryDataSingleValue.to_json())

# convert the object into a dict
metric_history_data_single_value_dict = metric_history_data_single_value_instance.to_dict()
# create an instance of MetricHistoryDataSingleValue from a dict
metric_history_data_single_value_from_dict = MetricHistoryDataSingleValue.from_dict(metric_history_data_single_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


