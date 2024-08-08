# NimblePerformanceHistoryData

performance trends for given granularity and time range for a component

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**end_time** | **int** | end time of history data | [optional] 
**history_data** | [**NimblePerformanceHistoryDataHistoryData**](NimblePerformanceHistoryDataHistoryData.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**start_time** | **int** | start time of history data | [optional] 

## Example

```python
from dscc.models.nimble_performance_history_data import NimblePerformanceHistoryData

# TODO update the JSON string below
json = "{}"
# create an instance of NimblePerformanceHistoryData from a JSON string
nimble_performance_history_data_instance = NimblePerformanceHistoryData.from_json(json)
# print the JSON string representation of the object
print(NimblePerformanceHistoryData.to_json())

# convert the object into a dict
nimble_performance_history_data_dict = nimble_performance_history_data_instance.to_dict()
# create an instance of NimblePerformanceHistoryData from a dict
nimble_performance_history_data_from_dict = NimblePerformanceHistoryData.from_dict(nimble_performance_history_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


