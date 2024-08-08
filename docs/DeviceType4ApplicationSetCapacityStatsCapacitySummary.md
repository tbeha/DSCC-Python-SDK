# DeviceType4ApplicationSetCapacityStatsCapacitySummary

Capacity of the applicationSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**free_size_mi_b** | **float** | Free Size in MiB | [optional] 
**size_mi_b** | **float** | Total size in MiB | [optional] 
**used_size_mi_b** | **float** | Used Size in MiB. | [optional] 

## Example

```python
from dscc.models.device_type4_application_set_capacity_stats_capacity_summary import DeviceType4ApplicationSetCapacityStatsCapacitySummary

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ApplicationSetCapacityStatsCapacitySummary from a JSON string
device_type4_application_set_capacity_stats_capacity_summary_instance = DeviceType4ApplicationSetCapacityStatsCapacitySummary.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ApplicationSetCapacityStatsCapacitySummary.to_json())

# convert the object into a dict
device_type4_application_set_capacity_stats_capacity_summary_dict = device_type4_application_set_capacity_stats_capacity_summary_instance.to_dict()
# create an instance of DeviceType4ApplicationSetCapacityStatsCapacitySummary from a dict
device_type4_application_set_capacity_stats_capacity_summary_from_dict = DeviceType4ApplicationSetCapacityStatsCapacitySummary.from_dict(device_type4_application_set_capacity_stats_capacity_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


