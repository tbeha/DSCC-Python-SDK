# TimeSeriesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headroom** | **float** | headroom utilized on resource | [optional] 
**headroom_pct** | **float** | headroom percentage contribution from resource on system | [optional] 
**headroom_utilized** | **str** | headroom utilized in terms of Low/Medium/High | [optional] 
**timestamp_ms** | **float** | timestamp for which the metrics are present | [optional] 

## Example

```python
from dscc.models.time_series_data import TimeSeriesData

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSeriesData from a JSON string
time_series_data_instance = TimeSeriesData.from_json(json)
# print the JSON string representation of the object
print(TimeSeriesData.to_json())

# convert the object into a dict
time_series_data_dict = time_series_data_instance.to_dict()
# create an instance of TimeSeriesData from a dict
time_series_data_from_dict = TimeSeriesData.from_dict(time_series_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


