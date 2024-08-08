# PerfData

Performance stats for the device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_of1day** | **float** | last one day avg data | [optional] 
**avg_of1hour** | **float** | last one hour avg data | [optional] 
**avg_of8hours** | **float** | last 8 hours avg data | [optional] 
**avg_oflatest** | **float** | latest perf data | [optional] 

## Example

```python
from dscc.models.perf_data import PerfData

# TODO update the JSON string below
json = "{}"
# create an instance of PerfData from a JSON string
perf_data_instance = PerfData.from_json(json)
# print the JSON string representation of the object
print(PerfData.to_json())

# convert the object into a dict
perf_data_dict = perf_data_instance.to_dict()
# create an instance of PerfData from a dict
perf_data_from_dict = PerfData.from_dict(perf_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


