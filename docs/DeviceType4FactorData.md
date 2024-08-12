# DeviceType4FactorData

Timestamp based latency values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_busy** | **float** | CPU busy percentage | [optional] 
**dack_ssd** | **float** | Delayed ack percentage | [optional] 
**pd_ssd_avg_busy** | **float** | PD average busy percentage | [optional] 
**read_cache_miss** | **float** | Read cache miss percentage | [optional] 
**timestamp** | **int** | Timestamp | [optional] 
**write_cache_miss** | **float** | Write cache miss percentage | [optional] 

## Example

```python
from dscc.models.device_type4_factor_data import DeviceType4FactorData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4FactorData from a JSON string
device_type4_factor_data_instance = DeviceType4FactorData.from_json(json)
# print the JSON string representation of the object
print(DeviceType4FactorData.to_json())

# convert the object into a dict
device_type4_factor_data_dict = device_type4_factor_data_instance.to_dict()
# create an instance of DeviceType4FactorData from a dict
device_type4_factor_data_from_dict = DeviceType4FactorData.from_dict(device_type4_factor_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


