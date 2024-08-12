# VolumePerformance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**iops** | [**KpiMetrics**](KpiMetrics.md) |  | [optional] 
**latency_ms** | [**KpiMetrics**](KpiMetrics.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed volume object | [optional] 
**resource_uri** | **str** | resourceUri for detailed volume object | [optional] 
**throughput_kbps** | [**KpiMetrics**](KpiMetrics.md) |  | [optional] 

## Example

```python
from dscc.models.volume_performance import VolumePerformance

# TODO update the JSON string below
json = "{}"
# create an instance of VolumePerformance from a JSON string
volume_performance_instance = VolumePerformance.from_json(json)
# print the JSON string representation of the object
print(VolumePerformance.to_json())

# convert the object into a dict
volume_performance_dict = volume_performance_instance.to_dict()
# create an instance of VolumePerformance from a dict
volume_performance_from_dict = VolumePerformance.from_dict(volume_performance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


