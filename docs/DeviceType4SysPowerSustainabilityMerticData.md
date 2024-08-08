# DeviceType4SysPowerSustainabilityMerticData

sustainability metrics trends for given granularity and time range for system and enclosure power supplies in Watts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | The customer application identifier | [optional] 
**end_time** | **int** | end time of history data | [optional] 
**history_data** | [**DeviceType4SysPowerSustainabilityMerticDataHistoryData**](DeviceType4SysPowerSustainabilityMerticDataHistoryData.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**start_time** | **int** | start time of history data | [optional] 

## Example

```python
from dscc.models.device_type4_sys_power_sustainability_mertic_data import DeviceType4SysPowerSustainabilityMerticData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SysPowerSustainabilityMerticData from a JSON string
device_type4_sys_power_sustainability_mertic_data_instance = DeviceType4SysPowerSustainabilityMerticData.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SysPowerSustainabilityMerticData.to_json())

# convert the object into a dict
device_type4_sys_power_sustainability_mertic_data_dict = device_type4_sys_power_sustainability_mertic_data_instance.to_dict()
# create an instance of DeviceType4SysPowerSustainabilityMerticData from a dict
device_type4_sys_power_sustainability_mertic_data_from_dict = DeviceType4SysPowerSustainabilityMerticData.from_dict(device_type4_sys_power_sustainability_mertic_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


