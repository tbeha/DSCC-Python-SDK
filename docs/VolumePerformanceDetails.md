# VolumePerformanceDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iops** | [**KpiMetrics**](KpiMetrics.md) |  | [optional] 
**latency_ms** | [**KpiMetrics**](KpiMetrics.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed volume object | [optional] 
**resource_uri** | **str** | resourceUri for detailed volume object | [optional] 
**throughput_kbps** | [**KpiMetrics**](KpiMetrics.md) |  | [optional] 

## Example

```python
from dscc.models.volume_performance_details import VolumePerformanceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of VolumePerformanceDetails from a JSON string
volume_performance_details_instance = VolumePerformanceDetails.from_json(json)
# print the JSON string representation of the object
print(VolumePerformanceDetails.to_json())

# convert the object into a dict
volume_performance_details_dict = volume_performance_details_instance.to_dict()
# create an instance of VolumePerformanceDetails from a dict
volume_performance_details_from_dict = VolumePerformanceDetails.from_dict(volume_performance_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


