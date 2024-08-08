# SysPerformanceHistory

system performance trends for given granularity

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
from dscc.models.sys_performance_history import SysPerformanceHistory

# TODO update the JSON string below
json = "{}"
# create an instance of SysPerformanceHistory from a JSON string
sys_performance_history_instance = SysPerformanceHistory.from_json(json)
# print the JSON string representation of the object
print(SysPerformanceHistory.to_json())

# convert the object into a dict
sys_performance_history_dict = sys_performance_history_instance.to_dict()
# create an instance of SysPerformanceHistory from a dict
sys_performance_history_from_dict = SysPerformanceHistory.from_dict(sys_performance_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


