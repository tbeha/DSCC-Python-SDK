# DeviceType4VolumeCapacityHistoryCapacityData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | customerId | [optional] 
**items** | [**List[DeviceType4volumeCapacitySeriesData]**](DeviceType4volumeCapacitySeriesData.md) |  | [optional] 
**total** | **int** | count of series data | [optional] 

## Example

```python
from dscc.models.device_type4_volume_capacity_history_capacity_data import DeviceType4VolumeCapacityHistoryCapacityData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VolumeCapacityHistoryCapacityData from a JSON string
device_type4_volume_capacity_history_capacity_data_instance = DeviceType4VolumeCapacityHistoryCapacityData.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VolumeCapacityHistoryCapacityData.to_json())

# convert the object into a dict
device_type4_volume_capacity_history_capacity_data_dict = device_type4_volume_capacity_history_capacity_data_instance.to_dict()
# create an instance of DeviceType4VolumeCapacityHistoryCapacityData from a dict
device_type4_volume_capacity_history_capacity_data_from_dict = DeviceType4VolumeCapacityHistoryCapacityData.from_dict(device_type4_volume_capacity_history_capacity_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


