# SystemPerformance

system performance statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**iops** | [**PmPerfData**](PmPerfData.md) |  | [optional] 
**latency** | [**PmPerfData**](PmPerfData.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**resource_uri** | **str** | resourceUri for detailed storage object | [optional] 
**throughput** | [**PmPerfData**](PmPerfData.md) |  | [optional] 

## Example

```python
from dscc.models.system_performance import SystemPerformance

# TODO update the JSON string below
json = "{}"
# create an instance of SystemPerformance from a JSON string
system_performance_instance = SystemPerformance.from_json(json)
# print the JSON string representation of the object
print(SystemPerformance.to_json())

# convert the object into a dict
system_performance_dict = system_performance_instance.to_dict()
# create an instance of SystemPerformance from a dict
system_performance_from_dict = SystemPerformance.from_dict(system_performance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


