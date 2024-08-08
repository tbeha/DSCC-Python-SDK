# RcLinkPerformanceHistoryData

performance trends for given granularity and time range for remote copy links component

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | customerId | [optional] 
**end_time** | **int** | end time of history data | [optional] 
**history_data** | [**RcLinkPerformanceHistoryDataHistoryData**](RcLinkPerformanceHistoryDataHistoryData.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**start_time** | **int** | start time of history data | [optional] 

## Example

```python
from dscc.models.rc_link_performance_history_data import RcLinkPerformanceHistoryData

# TODO update the JSON string below
json = "{}"
# create an instance of RcLinkPerformanceHistoryData from a JSON string
rc_link_performance_history_data_instance = RcLinkPerformanceHistoryData.from_json(json)
# print the JSON string representation of the object
print(RcLinkPerformanceHistoryData.to_json())

# convert the object into a dict
rc_link_performance_history_data_dict = rc_link_performance_history_data_instance.to_dict()
# create an instance of RcLinkPerformanceHistoryData from a dict
rc_link_performance_history_data_from_dict = RcLinkPerformanceHistoryData.from_dict(rc_link_performance_history_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


