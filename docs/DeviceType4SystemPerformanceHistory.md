# DeviceType4SystemPerformanceHistory

system performance trends for given granularity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**end_time** | **int** | End time of the history data | [optional] 
**history_data** | [**DeviceType4historyData**](DeviceType4historyData.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**start_time** | **int** | Start time of the history data | [optional] 

## Example

```python
from dscc.models.device_type4_system_performance_history import DeviceType4SystemPerformanceHistory

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SystemPerformanceHistory from a JSON string
device_type4_system_performance_history_instance = DeviceType4SystemPerformanceHistory.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SystemPerformanceHistory.to_json())

# convert the object into a dict
device_type4_system_performance_history_dict = device_type4_system_performance_history_instance.to_dict()
# create an instance of DeviceType4SystemPerformanceHistory from a dict
device_type4_system_performance_history_from_dict = DeviceType4SystemPerformanceHistory.from_dict(device_type4_system_performance_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


