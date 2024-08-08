# SystemLatencyFactors

system latency factors response structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer identifier | [optional] 
**end_time** | **int** | End time of the interval for which latency factors are determined | [optional] 
**latency_bands** | [**DeviceType4SystemLatencyFactorsLatencyBands**](DeviceType4SystemLatencyFactorsLatencyBands.md) |  | [optional] 
**start_time** | **int** | Start time of the interval for which latency factors are determined | [optional] 
**system_factors_metrics** | [**List[FactorData]**](FactorData.md) |  | [optional] 
**system_id** | **str** | System identifier | [optional] 

## Example

```python
from dscc.models.system_latency_factors import SystemLatencyFactors

# TODO update the JSON string below
json = "{}"
# create an instance of SystemLatencyFactors from a JSON string
system_latency_factors_instance = SystemLatencyFactors.from_json(json)
# print the JSON string representation of the object
print(SystemLatencyFactors.to_json())

# convert the object into a dict
system_latency_factors_dict = system_latency_factors_instance.to_dict()
# create an instance of SystemLatencyFactors from a dict
system_latency_factors_from_dict = SystemLatencyFactors.from_dict(system_latency_factors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


