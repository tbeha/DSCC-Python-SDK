# QlenMetricDataValue

Timeseries data for particular metric type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[QlenMetricSeriesDataValue]**](QlenMetricSeriesDataValue.md) |  | [optional] 
**total** | **int** | total number of series data | [optional] 

## Example

```python
from dscc.models.qlen_metric_data_value import QlenMetricDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of QlenMetricDataValue from a JSON string
qlen_metric_data_value_instance = QlenMetricDataValue.from_json(json)
# print the JSON string representation of the object
print(QlenMetricDataValue.to_json())

# convert the object into a dict
qlen_metric_data_value_dict = qlen_metric_data_value_instance.to_dict()
# create an instance of QlenMetricDataValue from a dict
qlen_metric_data_value_from_dict = QlenMetricDataValue.from_dict(qlen_metric_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


