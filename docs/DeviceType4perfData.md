# DeviceType4perfData

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
from dscc.models.device_type4perf_data import DeviceType4perfData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4perfData from a JSON string
device_type4perf_data_instance = DeviceType4perfData.from_json(json)
# print the JSON string representation of the object
print(DeviceType4perfData.to_json())

# convert the object into a dict
device_type4perf_data_dict = device_type4perf_data_instance.to_dict()
# create an instance of DeviceType4perfData from a dict
device_type4perf_data_from_dict = DeviceType4perfData.from_dict(device_type4perf_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


