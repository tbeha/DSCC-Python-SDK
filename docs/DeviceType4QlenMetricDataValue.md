# DeviceType4QlenMetricDataValue

Timeseries data for particular metric type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4QlenMetricSeriesDataValue]**](DeviceType4QlenMetricSeriesDataValue.md) |  | [optional] 
**total** | **int** | total number of series data | [optional] 

## Example

```python
from dscc.models.device_type4_qlen_metric_data_value import DeviceType4QlenMetricDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4QlenMetricDataValue from a JSON string
device_type4_qlen_metric_data_value_instance = DeviceType4QlenMetricDataValue.from_json(json)
# print the JSON string representation of the object
print(DeviceType4QlenMetricDataValue.to_json())

# convert the object into a dict
device_type4_qlen_metric_data_value_dict = device_type4_qlen_metric_data_value_instance.to_dict()
# create an instance of DeviceType4QlenMetricDataValue from a dict
device_type4_qlen_metric_data_value_from_dict = DeviceType4QlenMetricDataValue.from_dict(device_type4_qlen_metric_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


