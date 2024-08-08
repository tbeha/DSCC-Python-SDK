# MetricReadWriteData

Timeseries data for particular metric type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[MetricSeriesReadWriteData]**](MetricSeriesReadWriteData.md) |  | [optional] 
**total** | **int** | total number of series data | [optional] 

## Example

```python
from dscc.models.metric_read_write_data import MetricReadWriteData

# TODO update the JSON string below
json = "{}"
# create an instance of MetricReadWriteData from a JSON string
metric_read_write_data_instance = MetricReadWriteData.from_json(json)
# print the JSON string representation of the object
print(MetricReadWriteData.to_json())

# convert the object into a dict
metric_read_write_data_dict = metric_read_write_data_instance.to_dict()
# create an instance of MetricReadWriteData from a dict
metric_read_write_data_from_dict = MetricReadWriteData.from_dict(metric_read_write_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


