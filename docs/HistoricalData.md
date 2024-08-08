# HistoricalData

List of DISK/CPU metric per timestamp

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp_ms** | **float** | Timestamp in epoch milliseconds for which the metrics are listed | [optional] 
**value** | **float** | metric value for disk/cpu | [optional] 

## Example

```python
from dscc.models.historical_data import HistoricalData

# TODO update the JSON string below
json = "{}"
# create an instance of HistoricalData from a JSON string
historical_data_instance = HistoricalData.from_json(json)
# print the JSON string representation of the object
print(HistoricalData.to_json())

# convert the object into a dict
historical_data_dict = historical_data_instance.to_dict()
# create an instance of HistoricalData from a dict
historical_data_from_dict = HistoricalData.from_dict(historical_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


