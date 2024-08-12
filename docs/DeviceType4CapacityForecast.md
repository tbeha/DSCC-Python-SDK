# DeviceType4CapacityForecast

Capacity forecast data for HPE Alletra Storage MP system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence_level** | **float** | Confidence level represents the level of certainity or probability of a forecast made by a model | [optional] 
**customer_id** | **str** | CustomerId of the user | [optional] 
**forecasted** | [**List[DeviceType4capacitySeriesForecastData]**](DeviceType4capacitySeriesForecastData.md) |  | [optional] 
**historic** | [**List[DeviceType4capacitySeriesHistoricData]**](DeviceType4capacitySeriesHistoricData.md) |  | [optional] 
**message** | **str** | A message to describe why forecast data is not available | [optional] 
**request_uri** | **str** | RequestUri for detailed storage object | [optional] 

## Example

```python
from dscc.models.device_type4_capacity_forecast import DeviceType4CapacityForecast

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4CapacityForecast from a JSON string
device_type4_capacity_forecast_instance = DeviceType4CapacityForecast.from_json(json)
# print the JSON string representation of the object
print(DeviceType4CapacityForecast.to_json())

# convert the object into a dict
device_type4_capacity_forecast_dict = device_type4_capacity_forecast_instance.to_dict()
# create an instance of DeviceType4CapacityForecast from a dict
device_type4_capacity_forecast_from_dict = DeviceType4CapacityForecast.from_dict(device_type4_capacity_forecast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


