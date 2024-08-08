# StoragePoolPerformanceHistory

storage pool performance trends for given granularity and time range

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
from dscc.models.storage_pool_performance_history import StoragePoolPerformanceHistory

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePoolPerformanceHistory from a JSON string
storage_pool_performance_history_instance = StoragePoolPerformanceHistory.from_json(json)
# print the JSON string representation of the object
print(StoragePoolPerformanceHistory.to_json())

# convert the object into a dict
storage_pool_performance_history_dict = storage_pool_performance_history_instance.to_dict()
# create an instance of StoragePoolPerformanceHistory from a dict
storage_pool_performance_history_from_dict = StoragePoolPerformanceHistory.from_dict(storage_pool_performance_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


