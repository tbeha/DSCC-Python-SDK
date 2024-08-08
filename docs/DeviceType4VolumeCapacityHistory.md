# DeviceType4VolumeCapacityHistory

volume capacity trends for given granularity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_data** | [**DeviceType4VolumeCapacityHistoryCapacityData**](DeviceType4VolumeCapacityHistoryCapacityData.md) |  | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**end_time** | **int** | end time of the capacity history | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**start_time** | **int** | start time of the capacity history | [optional] 

## Example

```python
from dscc.models.device_type4_volume_capacity_history import DeviceType4VolumeCapacityHistory

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VolumeCapacityHistory from a JSON string
device_type4_volume_capacity_history_instance = DeviceType4VolumeCapacityHistory.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VolumeCapacityHistory.to_json())

# convert the object into a dict
device_type4_volume_capacity_history_dict = device_type4_volume_capacity_history_instance.to_dict()
# create an instance of DeviceType4VolumeCapacityHistory from a dict
device_type4_volume_capacity_history_from_dict = DeviceType4VolumeCapacityHistory.from_dict(device_type4_volume_capacity_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


