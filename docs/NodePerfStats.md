# NodePerfStats

nodes component performance statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_percentage** | [**PerfData**](PerfData.md) |  | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**cpu_percentage** | [**PerfData**](PerfData.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**request_uri** | **str** | requestUri for detailed performance stats object | [optional] 

## Example

```python
from dscc.models.node_perf_stats import NodePerfStats

# TODO update the JSON string below
json = "{}"
# create an instance of NodePerfStats from a JSON string
node_perf_stats_instance = NodePerfStats.from_json(json)
# print the JSON string representation of the object
print(NodePerfStats.to_json())

# convert the object into a dict
node_perf_stats_dict = node_perf_stats_instance.to_dict()
# create an instance of NodePerfStats from a dict
node_perf_stats_from_dict = NodePerfStats.from_dict(node_perf_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


