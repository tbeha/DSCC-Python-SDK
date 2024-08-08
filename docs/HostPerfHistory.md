# HostPerfHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**historical_data** | [**HostHistoricalMetricData**](HostHistoricalMetricData.md) |  | [optional] 
**id** | **str** | The id of the volume | [optional] 
**system_id** | **str** | The id of the system | [optional] 
**volume_name** | **str** | The name of the volume | [optional] 

## Example

```python
from dscc.models.host_perf_history import HostPerfHistory

# TODO update the JSON string below
json = "{}"
# create an instance of HostPerfHistory from a JSON string
host_perf_history_instance = HostPerfHistory.from_json(json)
# print the JSON string representation of the object
print(HostPerfHistory.to_json())

# convert the object into a dict
host_perf_history_dict = host_perf_history_instance.to_dict()
# create an instance of HostPerfHistory from a dict
host_perf_history_from_dict = HostPerfHistory.from_dict(host_perf_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


