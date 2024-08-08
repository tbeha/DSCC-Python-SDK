# DeviceType4volumePerformanceDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iops** | [**DeviceType4KpiMetrics**](DeviceType4KpiMetrics.md) |  | [optional] 
**latency_ms** | [**DeviceType4KpiMetrics**](DeviceType4KpiMetrics.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed volume object | [optional] 
**resource_uri** | **str** | resourceUri for detailed volume object | [optional] 
**throughput_kbps** | [**DeviceType4KpiMetrics**](DeviceType4KpiMetrics.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4volume_performance_details import DeviceType4volumePerformanceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4volumePerformanceDetails from a JSON string
device_type4volume_performance_details_instance = DeviceType4volumePerformanceDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4volumePerformanceDetails.to_json())

# convert the object into a dict
device_type4volume_performance_details_dict = device_type4volume_performance_details_instance.to_dict()
# create an instance of DeviceType4volumePerformanceDetails from a dict
device_type4volume_performance_details_from_dict = DeviceType4volumePerformanceDetails.from_dict(device_type4volume_performance_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


