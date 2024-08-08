# NimblevolumeCapacitySeriesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_usage** | **float** | capacity usage value at particular timestamp  (in MiB) | [optional] 
**timestamp** | **int** | epoch timestamp | [optional] 
**volume_usage** | **float** | capacity usage value at particular timestamp  (in MiB) | [optional] 

## Example

```python
from dscc.models.nimblevolume_capacity_series_data import NimblevolumeCapacitySeriesData

# TODO update the JSON string below
json = "{}"
# create an instance of NimblevolumeCapacitySeriesData from a JSON string
nimblevolume_capacity_series_data_instance = NimblevolumeCapacitySeriesData.from_json(json)
# print the JSON string representation of the object
print(NimblevolumeCapacitySeriesData.to_json())

# convert the object into a dict
nimblevolume_capacity_series_data_dict = nimblevolume_capacity_series_data_instance.to_dict()
# create an instance of NimblevolumeCapacitySeriesData from a dict
nimblevolume_capacity_series_data_from_dict = NimblevolumeCapacitySeriesData.from_dict(nimblevolume_capacity_series_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


