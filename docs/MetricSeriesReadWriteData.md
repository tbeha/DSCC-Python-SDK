# MetricSeriesReadWriteData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the object at particular timestamp | [optional] 
**read_value** | **float** | average read metric value at particular timestamp | [optional] 
**timestampms** | **int** | epoch timestamp | [optional] 
**write_value** | **float** | average write metric value at particular timestamp | [optional] 

## Example

```python
from dscc.models.metric_series_read_write_data import MetricSeriesReadWriteData

# TODO update the JSON string below
json = "{}"
# create an instance of MetricSeriesReadWriteData from a JSON string
metric_series_read_write_data_instance = MetricSeriesReadWriteData.from_json(json)
# print the JSON string representation of the object
print(MetricSeriesReadWriteData.to_json())

# convert the object into a dict
metric_series_read_write_data_dict = metric_series_read_write_data_instance.to_dict()
# create an instance of MetricSeriesReadWriteData from a dict
metric_series_read_write_data_from_dict = MetricSeriesReadWriteData.from_dict(metric_series_read_write_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


