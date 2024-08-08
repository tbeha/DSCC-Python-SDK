# DeviceType4RcLinkPerformanceHistoryDataHistoryData

performance history data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_round_trip_time_data** | [**List[DeviceType4metricHistoryDataSingleValue]**](DeviceType4metricHistoryDataSingleValue.md) |  | [optional] 
**link_throughput_data** | [**List[DeviceType4metricHistoryDataSingleValue]**](DeviceType4metricHistoryDataSingleValue.md) |  | [optional] 
**transmitted_data** | [**List[DeviceType4metricHistoryDataSingleValue]**](DeviceType4metricHistoryDataSingleValue.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_rc_link_performance_history_data_history_data import DeviceType4RcLinkPerformanceHistoryDataHistoryData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4RcLinkPerformanceHistoryDataHistoryData from a JSON string
device_type4_rc_link_performance_history_data_history_data_instance = DeviceType4RcLinkPerformanceHistoryDataHistoryData.from_json(json)
# print the JSON string representation of the object
print(DeviceType4RcLinkPerformanceHistoryDataHistoryData.to_json())

# convert the object into a dict
device_type4_rc_link_performance_history_data_history_data_dict = device_type4_rc_link_performance_history_data_history_data_instance.to_dict()
# create an instance of DeviceType4RcLinkPerformanceHistoryDataHistoryData from a dict
device_type4_rc_link_performance_history_data_history_data_from_dict = DeviceType4RcLinkPerformanceHistoryDataHistoryData.from_dict(device_type4_rc_link_performance_history_data_history_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


