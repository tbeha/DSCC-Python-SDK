# VolumeCapacitySeriesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_usage_mi_b** | **float** | Actual usage value in MiB | [optional] 
**host_written_capacity_mi_b** | **float** | Host written capacity in MiB | [optional] 
**timestamp_ms** | **int** | epoch timestamp | [optional] 

## Example

```python
from dscc.models.volume_capacity_series_data import VolumeCapacitySeriesData

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeCapacitySeriesData from a JSON string
volume_capacity_series_data_instance = VolumeCapacitySeriesData.from_json(json)
# print the JSON string representation of the object
print(VolumeCapacitySeriesData.to_json())

# convert the object into a dict
volume_capacity_series_data_dict = volume_capacity_series_data_instance.to_dict()
# create an instance of VolumeCapacitySeriesData from a dict
volume_capacity_series_data_from_dict = VolumeCapacitySeriesData.from_dict(volume_capacity_series_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


