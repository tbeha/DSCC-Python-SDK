# PerfStats

Collection of average cpu percentage and average cache percentage for various durations.

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
from dscc.models.perf_stats import PerfStats

# TODO update the JSON string below
json = "{}"
# create an instance of PerfStats from a JSON string
perf_stats_instance = PerfStats.from_json(json)
# print the JSON string representation of the object
print(PerfStats.to_json())

# convert the object into a dict
perf_stats_dict = perf_stats_instance.to_dict()
# create an instance of PerfStats from a dict
perf_stats_from_dict = PerfStats.from_dict(perf_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


