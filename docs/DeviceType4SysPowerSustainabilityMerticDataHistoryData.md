# DeviceType4SysPowerSustainabilityMerticDataHistoryData

sustainability history data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**power_consumption** | [**List[DeviceType4metricHistoryDataSingleValue]**](DeviceType4metricHistoryDataSingleValue.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_sys_power_sustainability_mertic_data_history_data import DeviceType4SysPowerSustainabilityMerticDataHistoryData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SysPowerSustainabilityMerticDataHistoryData from a JSON string
device_type4_sys_power_sustainability_mertic_data_history_data_instance = DeviceType4SysPowerSustainabilityMerticDataHistoryData.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SysPowerSustainabilityMerticDataHistoryData.to_json())

# convert the object into a dict
device_type4_sys_power_sustainability_mertic_data_history_data_dict = device_type4_sys_power_sustainability_mertic_data_history_data_instance.to_dict()
# create an instance of DeviceType4SysPowerSustainabilityMerticDataHistoryData from a dict
device_type4_sys_power_sustainability_mertic_data_history_data_from_dict = DeviceType4SysPowerSustainabilityMerticDataHistoryData.from_dict(device_type4_sys_power_sustainability_mertic_data_history_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


