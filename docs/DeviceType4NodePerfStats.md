# DeviceType4NodePerfStats

nodes component performance statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_percentage** | [**DeviceType4perfData**](DeviceType4perfData.md) |  | [optional] 
**cpu_percentage** | [**DeviceType4perfData**](DeviceType4perfData.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**request_uri** | **str** | requestUri for detailed performance stats object | [optional] 

## Example

```python
from dscc.models.device_type4_node_perf_stats import DeviceType4NodePerfStats

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4NodePerfStats from a JSON string
device_type4_node_perf_stats_instance = DeviceType4NodePerfStats.from_json(json)
# print the JSON string representation of the object
print(DeviceType4NodePerfStats.to_json())

# convert the object into a dict
device_type4_node_perf_stats_dict = device_type4_node_perf_stats_instance.to_dict()
# create an instance of DeviceType4NodePerfStats from a dict
device_type4_node_perf_stats_from_dict = DeviceType4NodePerfStats.from_dict(device_type4_node_perf_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


