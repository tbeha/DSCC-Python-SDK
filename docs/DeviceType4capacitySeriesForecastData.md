# DeviceType4capacitySeriesForecastData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_used_mi_b** | **float** | Forecasted maximum used capacity in MiB | [optional] 
**min_used_mi_b** | **float** | Forecasted minimum used capacity in MiB | [optional] 
**timestamp_ms** | **int** | Epoch timestamp in milliseconds | [optional] 
**total_mi_b** | **float** | Forecasted total capacity in MiB. | [optional] 
**used_mi_b** | **float** | Forecasted used capacity in MiB | [optional] 

## Example

```python
from dscc.models.device_type4capacity_series_forecast_data import DeviceType4capacitySeriesForecastData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4capacitySeriesForecastData from a JSON string
device_type4capacity_series_forecast_data_instance = DeviceType4capacitySeriesForecastData.from_json(json)
# print the JSON string representation of the object
print(DeviceType4capacitySeriesForecastData.to_json())

# convert the object into a dict
device_type4capacity_series_forecast_data_dict = device_type4capacity_series_forecast_data_instance.to_dict()
# create an instance of DeviceType4capacitySeriesForecastData from a dict
device_type4capacity_series_forecast_data_from_dict = DeviceType4capacitySeriesForecastData.from_dict(device_type4capacity_series_forecast_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


