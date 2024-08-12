# NimblecapacitySeriesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**savings** | **float** | capacity savings value at particular timestamp  (in MiB) | [optional] 
**timestamp** | **int** | epoch timestamp | [optional] 
**usage** | **float** | capacity usage value at particular timestamp  (in MiB) | [optional] 

## Example

```python
from dscc.models.nimblecapacity_series_data import NimblecapacitySeriesData

# TODO update the JSON string below
json = "{}"
# create an instance of NimblecapacitySeriesData from a JSON string
nimblecapacity_series_data_instance = NimblecapacitySeriesData.from_json(json)
# print the JSON string representation of the object
print(NimblecapacitySeriesData.to_json())

# convert the object into a dict
nimblecapacity_series_data_dict = nimblecapacity_series_data_instance.to_dict()
# create an instance of NimblecapacitySeriesData from a dict
nimblecapacity_series_data_from_dict = NimblecapacitySeriesData.from_dict(nimblecapacity_series_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


