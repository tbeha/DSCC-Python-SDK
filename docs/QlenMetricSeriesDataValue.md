# QlenMetricSeriesDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestampms** | **int** | epoch timestamp | [optional] 
**value** | **float** | value at particular timestamp | [optional] 

## Example

```python
from dscc.models.qlen_metric_series_data_value import QlenMetricSeriesDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of QlenMetricSeriesDataValue from a JSON string
qlen_metric_series_data_value_instance = QlenMetricSeriesDataValue.from_json(json)
# print the JSON string representation of the object
print(QlenMetricSeriesDataValue.to_json())

# convert the object into a dict
qlen_metric_series_data_value_dict = qlen_metric_series_data_value_instance.to_dict()
# create an instance of QlenMetricSeriesDataValue from a dict
qlen_metric_series_data_value_from_dict = QlenMetricSeriesDataValue.from_dict(qlen_metric_series_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


