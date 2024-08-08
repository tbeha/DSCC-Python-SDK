# HostMetricSeriesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp_ms** | **int** | epoch timestamp | [optional] 
**value** | **float** | average metric value at particular timestamp | [optional] 

## Example

```python
from dscc.models.host_metric_series_data import HostMetricSeriesData

# TODO update the JSON string below
json = "{}"
# create an instance of HostMetricSeriesData from a JSON string
host_metric_series_data_instance = HostMetricSeriesData.from_json(json)
# print the JSON string representation of the object
print(HostMetricSeriesData.to_json())

# convert the object into a dict
host_metric_series_data_dict = host_metric_series_data_instance.to_dict()
# create an instance of HostMetricSeriesData from a dict
host_metric_series_data_from_dict = HostMetricSeriesData.from_dict(host_metric_series_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


