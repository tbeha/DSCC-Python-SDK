# HostHistoryData

Performance history data for given time range and granularily for a volume

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iops_metrics_data** | [**List[HostPerfHistory]**](HostPerfHistory.md) |  | [optional] 
**latency_metrics_data_ms** | [**List[HostPerfHistory]**](HostPerfHistory.md) |  | [optional] 
**throughput_metrics_data_kbps** | [**List[HostPerfHistory]**](HostPerfHistory.md) |  | [optional] 

## Example

```python
from dscc.models.host_history_data import HostHistoryData

# TODO update the JSON string below
json = "{}"
# create an instance of HostHistoryData from a JSON string
host_history_data_instance = HostHistoryData.from_json(json)
# print the JSON string representation of the object
print(HostHistoryData.to_json())

# convert the object into a dict
host_history_data_dict = host_history_data_instance.to_dict()
# create an instance of HostHistoryData from a dict
host_history_data_from_dict = HostHistoryData.from_dict(host_history_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


