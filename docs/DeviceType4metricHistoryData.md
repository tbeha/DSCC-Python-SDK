# DeviceType4metricHistoryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart_legend_id** | **str** | Id to display chart legend, gives information about groupby and filtered objects | [optional] 
**time_series_data** | [**DeviceType4metricData**](DeviceType4metricData.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4metric_history_data import DeviceType4metricHistoryData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4metricHistoryData from a JSON string
device_type4metric_history_data_instance = DeviceType4metricHistoryData.from_json(json)
# print the JSON string representation of the object
print(DeviceType4metricHistoryData.to_json())

# convert the object into a dict
device_type4metric_history_data_dict = device_type4metric_history_data_instance.to_dict()
# create an instance of DeviceType4metricHistoryData from a dict
device_type4metric_history_data_from_dict = DeviceType4metricHistoryData.from_dict(device_type4metric_history_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


