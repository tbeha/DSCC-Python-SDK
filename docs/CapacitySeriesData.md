# CapacitySeriesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp_ms** | **int** | epoch timestamp | [optional] 
**usage_mi_b** | **float** | capacity usage value at particular timestamp | [optional] 

## Example

```python
from dscc.models.capacity_series_data import CapacitySeriesData

# TODO update the JSON string below
json = "{}"
# create an instance of CapacitySeriesData from a JSON string
capacity_series_data_instance = CapacitySeriesData.from_json(json)
# print the JSON string representation of the object
print(CapacitySeriesData.to_json())

# convert the object into a dict
capacity_series_data_dict = capacity_series_data_instance.to_dict()
# create an instance of CapacitySeriesData from a dict
capacity_series_data_from_dict = CapacitySeriesData.from_dict(capacity_series_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


