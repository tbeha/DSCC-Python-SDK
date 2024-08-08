# HostStoragePerformanceHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | customerId | [optional] 
**host_volume_perf_trend_data** | [**HostHistoryData**](HostHistoryData.md) |  | [optional] 
**request_uri** | **str** | requestUri for host storage performance history data | [optional] 

## Example

```python
from dscc.models.host_storage_performance_history import HostStoragePerformanceHistory

# TODO update the JSON string below
json = "{}"
# create an instance of HostStoragePerformanceHistory from a JSON string
host_storage_performance_history_instance = HostStoragePerformanceHistory.from_json(json)
# print the JSON string representation of the object
print(HostStoragePerformanceHistory.to_json())

# convert the object into a dict
host_storage_performance_history_dict = host_storage_performance_history_instance.to_dict()
# create an instance of HostStoragePerformanceHistory from a dict
host_storage_performance_history_from_dict = HostStoragePerformanceHistory.from_dict(host_storage_performance_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


