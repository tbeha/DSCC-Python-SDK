# DeviceType4metricSeriesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_value** | **float** | average read metric value at particular timestamp | [optional] 
**timestampms** | **int** | epoch timestamp | [optional] 
**total_value** | **float** | total metric value at particular timestamp | [optional] 
**write_value** | **float** | average write metric value at particular timestamp | [optional] 

## Example

```python
from dscc.models.device_type4metric_series_data import DeviceType4metricSeriesData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4metricSeriesData from a JSON string
device_type4metric_series_data_instance = DeviceType4metricSeriesData.from_json(json)
# print the JSON string representation of the object
print(DeviceType4metricSeriesData.to_json())

# convert the object into a dict
device_type4metric_series_data_dict = device_type4metric_series_data_instance.to_dict()
# create an instance of DeviceType4metricSeriesData from a dict
device_type4metric_series_data_from_dict = DeviceType4metricSeriesData.from_dict(device_type4metric_series_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


