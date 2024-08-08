# DeviceType4metricSeriesDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the object at particular timestamp | [optional] 
**timestampms** | **int** | epoch timestamp | [optional] 
**value** | **float** | value at particular timestamp | [optional] 

## Example

```python
from dscc.models.device_type4metric_series_data_value import DeviceType4metricSeriesDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4metricSeriesDataValue from a JSON string
device_type4metric_series_data_value_instance = DeviceType4metricSeriesDataValue.from_json(json)
# print the JSON string representation of the object
print(DeviceType4metricSeriesDataValue.to_json())

# convert the object into a dict
device_type4metric_series_data_value_dict = device_type4metric_series_data_value_instance.to_dict()
# create an instance of DeviceType4metricSeriesDataValue from a dict
device_type4metric_series_data_value_from_dict = DeviceType4metricSeriesDataValue.from_dict(device_type4metric_series_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


