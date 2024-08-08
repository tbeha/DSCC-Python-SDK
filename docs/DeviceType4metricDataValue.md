# DeviceType4metricDataValue

Timeseries data for particular metric type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4metricSeriesDataValue]**](DeviceType4metricSeriesDataValue.md) |  | [optional] 
**total** | **int** | total number of series data | [optional] 

## Example

```python
from dscc.models.device_type4metric_data_value import DeviceType4metricDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4metricDataValue from a JSON string
device_type4metric_data_value_instance = DeviceType4metricDataValue.from_json(json)
# print the JSON string representation of the object
print(DeviceType4metricDataValue.to_json())

# convert the object into a dict
device_type4metric_data_value_dict = device_type4metric_data_value_instance.to_dict()
# create an instance of DeviceType4metricDataValue from a dict
device_type4metric_data_value_from_dict = DeviceType4metricDataValue.from_dict(device_type4metric_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


