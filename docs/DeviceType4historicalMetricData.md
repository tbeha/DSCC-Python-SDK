# DeviceType4historicalMetricData

Timeseries data for particular metric type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4metricSeriesData]**](DeviceType4metricSeriesData.md) |  | [optional] 
**total** | **int** | count of series data | [optional] 

## Example

```python
from dscc.models.device_type4historical_metric_data import DeviceType4historicalMetricData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4historicalMetricData from a JSON string
device_type4historical_metric_data_instance = DeviceType4historicalMetricData.from_json(json)
# print the JSON string representation of the object
print(DeviceType4historicalMetricData.to_json())

# convert the object into a dict
device_type4historical_metric_data_dict = device_type4historical_metric_data_instance.to_dict()
# create an instance of DeviceType4historicalMetricData from a dict
device_type4historical_metric_data_from_dict = DeviceType4historicalMetricData.from_dict(device_type4historical_metric_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


