# DeviceType4metricData

Timeseries data for particular metric type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4metricSeriesRdWrData]**](DeviceType4metricSeriesRdWrData.md) |  | [optional] 
**total** | **int** | total number of series data | [optional] 

## Example

```python
from dscc.models.device_type4metric_data import DeviceType4metricData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4metricData from a JSON string
device_type4metric_data_instance = DeviceType4metricData.from_json(json)
# print the JSON string representation of the object
print(DeviceType4metricData.to_json())

# convert the object into a dict
device_type4metric_data_dict = device_type4metric_data_instance.to_dict()
# create an instance of DeviceType4metricData from a dict
device_type4metric_data_from_dict = DeviceType4metricData.from_dict(device_type4metric_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


