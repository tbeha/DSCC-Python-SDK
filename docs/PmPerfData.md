# PmPerfData

Performance metrics average values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_of1day** | **float** | last one day avg data | [optional] 
**avg_of1hour** | **float** | last one hour avg data | [optional] 
**avg_of8hours** | **float** | last 8 hours avg data | [optional] 
**avg_of_latest** | **float** | latest perf data | [optional] 

## Example

```python
from dscc.models.pm_perf_data import PmPerfData

# TODO update the JSON string below
json = "{}"
# create an instance of PmPerfData from a JSON string
pm_perf_data_instance = PmPerfData.from_json(json)
# print the JSON string representation of the object
print(PmPerfData.to_json())

# convert the object into a dict
pm_perf_data_dict = pm_perf_data_instance.to_dict()
# create an instance of PmPerfData from a dict
pm_perf_data_from_dict = PmPerfData.from_dict(pm_perf_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


