# DeviceType4VolumePerformanceHistory

volume performance trends for given granularity and time range

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**end_time** | **int** | end time of history data | [optional] 
**history_data** | [**DeviceType4VolumePerformanceHistoryHistoryData**](DeviceType4VolumePerformanceHistoryHistoryData.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**start_time** | **int** | start time of history data | [optional] 

## Example

```python
from dscc.models.device_type4_volume_performance_history import DeviceType4VolumePerformanceHistory

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VolumePerformanceHistory from a JSON string
device_type4_volume_performance_history_instance = DeviceType4VolumePerformanceHistory.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VolumePerformanceHistory.to_json())

# convert the object into a dict
device_type4_volume_performance_history_dict = device_type4_volume_performance_history_instance.to_dict()
# create an instance of DeviceType4VolumePerformanceHistory from a dict
device_type4_volume_performance_history_from_dict = DeviceType4VolumePerformanceHistory.from_dict(device_type4_volume_performance_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


