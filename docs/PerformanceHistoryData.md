# PerformanceHistoryData

performance trends for given granularity and time range for a component

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**CommonResourceAttributesPerfPrimera**](CommonResourceAttributesPerfPrimera.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**end_time** | **int** | end time of history data | [optional] 
**history_data** | [**PerformanceHistoryDataHistoryData**](PerformanceHistoryDataHistoryData.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**start_time** | **int** | start time of history data | [optional] 

## Example

```python
from dscc.models.performance_history_data import PerformanceHistoryData

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceHistoryData from a JSON string
performance_history_data_instance = PerformanceHistoryData.from_json(json)
# print the JSON string representation of the object
print(PerformanceHistoryData.to_json())

# convert the object into a dict
performance_history_data_dict = performance_history_data_instance.to_dict()
# create an instance of PerformanceHistoryData from a dict
performance_history_data_from_dict = PerformanceHistoryData.from_dict(performance_history_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


