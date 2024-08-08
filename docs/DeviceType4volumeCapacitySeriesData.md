# DeviceType4volumeCapacitySeriesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_usage_mi_b** | **float** | Actual usage value in MiB | [optional] 
**host_written_capacity_mi_b** | **float** | Host written capacity in MiB | [optional] 
**timestamp_ms** | **int** | epoch timestamp | [optional] 

## Example

```python
from dscc.models.device_type4volume_capacity_series_data import DeviceType4volumeCapacitySeriesData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4volumeCapacitySeriesData from a JSON string
device_type4volume_capacity_series_data_instance = DeviceType4volumeCapacitySeriesData.from_json(json)
# print the JSON string representation of the object
print(DeviceType4volumeCapacitySeriesData.to_json())

# convert the object into a dict
device_type4volume_capacity_series_data_dict = device_type4volume_capacity_series_data_instance.to_dict()
# create an instance of DeviceType4volumeCapacitySeriesData from a dict
device_type4volume_capacity_series_data_from_dict = DeviceType4volumeCapacitySeriesData.from_dict(device_type4volume_capacity_series_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


