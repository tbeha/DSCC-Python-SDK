# VolumePerformanceHistory

volume performance trends for given granularity and time range

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**end_time** | **int** | end time of history data | [optional] 
**history_data** | [**VolumePerformanceHistoryHistoryData**](VolumePerformanceHistoryHistoryData.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**start_time** | **int** | start time of history data | [optional] 

## Example

```python
from dscc.models.volume_performance_history import VolumePerformanceHistory

# TODO update the JSON string below
json = "{}"
# create an instance of VolumePerformanceHistory from a JSON string
volume_performance_history_instance = VolumePerformanceHistory.from_json(json)
# print the JSON string representation of the object
print(VolumePerformanceHistory.to_json())

# convert the object into a dict
volume_performance_history_dict = volume_performance_history_instance.to_dict()
# create an instance of VolumePerformanceHistory from a dict
volume_performance_history_from_dict = VolumePerformanceHistory.from_dict(volume_performance_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


