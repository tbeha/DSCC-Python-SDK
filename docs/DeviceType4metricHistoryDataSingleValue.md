# DeviceType4metricHistoryDataSingleValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart_legend_id** | **str** | Id to display chart legend, gives information about groupby and filtered objects | [optional] 
**time_series_data** | [**DeviceType4metricDataValue**](DeviceType4metricDataValue.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4metric_history_data_single_value import DeviceType4metricHistoryDataSingleValue

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4metricHistoryDataSingleValue from a JSON string
device_type4metric_history_data_single_value_instance = DeviceType4metricHistoryDataSingleValue.from_json(json)
# print the JSON string representation of the object
print(DeviceType4metricHistoryDataSingleValue.to_json())

# convert the object into a dict
device_type4metric_history_data_single_value_dict = device_type4metric_history_data_single_value_instance.to_dict()
# create an instance of DeviceType4metricHistoryDataSingleValue from a dict
device_type4metric_history_data_single_value_from_dict = DeviceType4metricHistoryDataSingleValue.from_dict(device_type4metric_history_data_single_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


