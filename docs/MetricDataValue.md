# MetricDataValue

Timeseries data for particular metric type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[MetricSeriesDataValue]**](MetricSeriesDataValue.md) |  | [optional] 
**total** | **int** | total number of series data | [optional] 

## Example

```python
from dscc.models.metric_data_value import MetricDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of MetricDataValue from a JSON string
metric_data_value_instance = MetricDataValue.from_json(json)
# print the JSON string representation of the object
print(MetricDataValue.to_json())

# convert the object into a dict
metric_data_value_dict = metric_data_value_instance.to_dict()
# create an instance of MetricDataValue from a dict
metric_data_value_from_dict = MetricDataValue.from_dict(metric_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


