# DeviceType4VolumePerformance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**iops** | [**DeviceType4KpiMetrics**](DeviceType4KpiMetrics.md) |  | [optional] 
**latency_ms** | [**DeviceType4KpiMetrics**](DeviceType4KpiMetrics.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed volume object | [optional] 
**resource_uri** | **str** | resourceUri for detailed volume object | [optional] 
**throughput_kbps** | [**DeviceType4KpiMetrics**](DeviceType4KpiMetrics.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_volume_performance import DeviceType4VolumePerformance

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VolumePerformance from a JSON string
device_type4_volume_performance_instance = DeviceType4VolumePerformance.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VolumePerformance.to_json())

# convert the object into a dict
device_type4_volume_performance_dict = device_type4_volume_performance_instance.to_dict()
# create an instance of DeviceType4VolumePerformance from a dict
device_type4_volume_performance_from_dict = DeviceType4VolumePerformance.from_dict(device_type4_volume_performance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


