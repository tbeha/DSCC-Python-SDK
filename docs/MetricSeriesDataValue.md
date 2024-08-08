# MetricSeriesDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the object at particular timestamp | [optional] 
**timestampms** | **int** | epoch timestamp | [optional] 
**value** | **float** | value at particular timestamp | [optional] 

## Example

```python
from dscc.models.metric_series_data_value import MetricSeriesDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of MetricSeriesDataValue from a JSON string
metric_series_data_value_instance = MetricSeriesDataValue.from_json(json)
# print the JSON string representation of the object
print(MetricSeriesDataValue.to_json())

# convert the object into a dict
metric_series_data_value_dict = metric_series_data_value_instance.to_dict()
# create an instance of MetricSeriesDataValue from a dict
metric_series_data_value_from_dict = MetricSeriesDataValue.from_dict(metric_series_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


