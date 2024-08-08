# DeviceType4utilizationSummaryCapacityUsageData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**free_size_mi_b** | **float** | Free size in MiB | [optional] 
**used_size_mi_b** | **float** | Used size in MiB | [optional] 

## Example

```python
from dscc.models.device_type4utilization_summary_capacity_usage_data import DeviceType4utilizationSummaryCapacityUsageData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4utilizationSummaryCapacityUsageData from a JSON string
device_type4utilization_summary_capacity_usage_data_instance = DeviceType4utilizationSummaryCapacityUsageData.from_json(json)
# print the JSON string representation of the object
print(DeviceType4utilizationSummaryCapacityUsageData.to_json())

# convert the object into a dict
device_type4utilization_summary_capacity_usage_data_dict = device_type4utilization_summary_capacity_usage_data_instance.to_dict()
# create an instance of DeviceType4utilizationSummaryCapacityUsageData from a dict
device_type4utilization_summary_capacity_usage_data_from_dict = DeviceType4utilizationSummaryCapacityUsageData.from_dict(device_type4utilization_summary_capacity_usage_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


