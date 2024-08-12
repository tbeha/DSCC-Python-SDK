# DeviceType4SystemLatencyFactorsLatencyBands


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read** | [**List[DeviceType4SystemLatencyFactorsLatencyBandsReadInner]**](DeviceType4SystemLatencyFactorsLatencyBandsReadInner.md) |  | [optional] 
**write** | [**List[DeviceType4SystemLatencyFactorsLatencyBandsWriteInner]**](DeviceType4SystemLatencyFactorsLatencyBandsWriteInner.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_system_latency_factors_latency_bands import DeviceType4SystemLatencyFactorsLatencyBands

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SystemLatencyFactorsLatencyBands from a JSON string
device_type4_system_latency_factors_latency_bands_instance = DeviceType4SystemLatencyFactorsLatencyBands.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SystemLatencyFactorsLatencyBands.to_json())

# convert the object into a dict
device_type4_system_latency_factors_latency_bands_dict = device_type4_system_latency_factors_latency_bands_instance.to_dict()
# create an instance of DeviceType4SystemLatencyFactorsLatencyBands from a dict
device_type4_system_latency_factors_latency_bands_from_dict = DeviceType4SystemLatencyFactorsLatencyBands.from_dict(device_type4_system_latency_factors_latency_bands_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


