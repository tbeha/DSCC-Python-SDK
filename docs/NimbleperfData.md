# NimbleperfData

Performance metrics average values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_1day** | **float** | last one day avg data | [optional] 
**avg_1hour** | **float** | last one hour avg data | [optional] 
**avg_8hours** | **float** | last 8 hours avg data | [optional] 
**avg_latest** | **float** | latest perf data | [optional] 

## Example

```python
from dscc.models.nimbleperf_data import NimbleperfData

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleperfData from a JSON string
nimbleperf_data_instance = NimbleperfData.from_json(json)
# print the JSON string representation of the object
print(NimbleperfData.to_json())

# convert the object into a dict
nimbleperf_data_dict = nimbleperf_data_instance.to_dict()
# create an instance of NimbleperfData from a dict
nimbleperf_data_from_dict = NimbleperfData.from_dict(nimbleperf_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


