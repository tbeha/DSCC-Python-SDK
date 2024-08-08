# SystemPerformanceHistory

system performance trends for given granularity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**end_time** | **int** | End time of the history data | [optional] 
**history_data** | [**HistoryData**](HistoryData.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**start_time** | **int** | Start time of the history data | [optional] 

## Example

```python
from dscc.models.system_performance_history import SystemPerformanceHistory

# TODO update the JSON string below
json = "{}"
# create an instance of SystemPerformanceHistory from a JSON string
system_performance_history_instance = SystemPerformanceHistory.from_json(json)
# print the JSON string representation of the object
print(SystemPerformanceHistory.to_json())

# convert the object into a dict
system_performance_history_dict = system_performance_history_instance.to_dict()
# create an instance of SystemPerformanceHistory from a dict
system_performance_history_from_dict = SystemPerformanceHistory.from_dict(system_performance_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


