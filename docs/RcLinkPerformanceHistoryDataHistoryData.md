# RcLinkPerformanceHistoryDataHistoryData

performance history data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_round_trip_time_data** | [**List[MetricHistoryDataSingleValue]**](MetricHistoryDataSingleValue.md) |  | [optional] 
**link_throughput_data** | [**List[MetricHistoryDataSingleValue]**](MetricHistoryDataSingleValue.md) |  | [optional] 
**transmitted_data** | [**List[MetricHistoryDataSingleValue]**](MetricHistoryDataSingleValue.md) |  | [optional] 

## Example

```python
from dscc.models.rc_link_performance_history_data_history_data import RcLinkPerformanceHistoryDataHistoryData

# TODO update the JSON string below
json = "{}"
# create an instance of RcLinkPerformanceHistoryDataHistoryData from a JSON string
rc_link_performance_history_data_history_data_instance = RcLinkPerformanceHistoryDataHistoryData.from_json(json)
# print the JSON string representation of the object
print(RcLinkPerformanceHistoryDataHistoryData.to_json())

# convert the object into a dict
rc_link_performance_history_data_history_data_dict = rc_link_performance_history_data_history_data_instance.to_dict()
# create an instance of RcLinkPerformanceHistoryDataHistoryData from a dict
rc_link_performance_history_data_history_data_from_dict = RcLinkPerformanceHistoryDataHistoryData.from_dict(rc_link_performance_history_data_history_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


