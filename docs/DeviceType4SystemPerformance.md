# DeviceType4SystemPerformance

system performance statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | customerId | [optional] 
**iops** | [**DeviceType4pmPerfData**](DeviceType4pmPerfData.md) |  | [optional] 
**latency** | [**DeviceType4pmPerfData**](DeviceType4pmPerfData.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**resource_uri** | **str** | resourceUri for detailed storage object | [optional] 
**throughput** | [**DeviceType4pmPerfData**](DeviceType4pmPerfData.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_system_performance import DeviceType4SystemPerformance

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SystemPerformance from a JSON string
device_type4_system_performance_instance = DeviceType4SystemPerformance.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SystemPerformance.to_json())

# convert the object into a dict
device_type4_system_performance_dict = device_type4_system_performance_instance.to_dict()
# create an instance of DeviceType4SystemPerformance from a dict
device_type4_system_performance_from_dict = DeviceType4SystemPerformance.from_dict(device_type4_system_performance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


