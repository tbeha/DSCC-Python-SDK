# DeviceType4capacitySeriesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp_ms** | **int** | epoch timestamp | [optional] 
**usage_mi_b** | **float** | capacity usage value at particular timestamp | [optional] 

## Example

```python
from dscc.models.device_type4capacity_series_data import DeviceType4capacitySeriesData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4capacitySeriesData from a JSON string
device_type4capacity_series_data_instance = DeviceType4capacitySeriesData.from_json(json)
# print the JSON string representation of the object
print(DeviceType4capacitySeriesData.to_json())

# convert the object into a dict
device_type4capacity_series_data_dict = device_type4capacity_series_data_instance.to_dict()
# create an instance of DeviceType4capacitySeriesData from a dict
device_type4capacity_series_data_from_dict = DeviceType4capacitySeriesData.from_dict(device_type4capacity_series_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


