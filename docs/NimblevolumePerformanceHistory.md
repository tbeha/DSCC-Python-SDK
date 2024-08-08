# NimblevolumePerformanceHistory

volume performance trends for given granularity and time range

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**iops_metrics_data** | [**NimblehistoricalMetricData**](NimblehistoricalMetricData.md) |  | [optional] 
**latency_metrics_data** | [**NimblehistoricalMetricData**](NimblehistoricalMetricData.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**throughput_metrics_data** | [**NimblehistoricalMetricData**](NimblehistoricalMetricData.md) |  | [optional] 

## Example

```python
from dscc.models.nimblevolume_performance_history import NimblevolumePerformanceHistory

# TODO update the JSON string below
json = "{}"
# create an instance of NimblevolumePerformanceHistory from a JSON string
nimblevolume_performance_history_instance = NimblevolumePerformanceHistory.from_json(json)
# print the JSON string representation of the object
print(NimblevolumePerformanceHistory.to_json())

# convert the object into a dict
nimblevolume_performance_history_dict = nimblevolume_performance_history_instance.to_dict()
# create an instance of NimblevolumePerformanceHistory from a dict
nimblevolume_performance_history_from_dict = NimblevolumePerformanceHistory.from_dict(nimblevolume_performance_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


