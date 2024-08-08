# DeviceType4capacitySeriesHistoricData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp_ms** | **int** | Epoch timestamp in milliseconds | [optional] 
**total_mi_b** | **float** | Total capacity in MiB | [optional] 
**used_mi_b** | **float** | Used capacity in MiB | [optional] 

## Example

```python
from dscc.models.device_type4capacity_series_historic_data import DeviceType4capacitySeriesHistoricData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4capacitySeriesHistoricData from a JSON string
device_type4capacity_series_historic_data_instance = DeviceType4capacitySeriesHistoricData.from_json(json)
# print the JSON string representation of the object
print(DeviceType4capacitySeriesHistoricData.to_json())

# convert the object into a dict
device_type4capacity_series_historic_data_dict = device_type4capacity_series_historic_data_instance.to_dict()
# create an instance of DeviceType4capacitySeriesHistoricData from a dict
device_type4capacity_series_historic_data_from_dict = DeviceType4capacitySeriesHistoricData.from_dict(device_type4capacity_series_historic_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


