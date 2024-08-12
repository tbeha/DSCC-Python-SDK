# DeviceType4systemSettingsDetailsSrinfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percent_used** | **float** | Used Percentage | [optional] 
**total_capacity_mi_b** | **float** | Total Capacity in MiB | [optional] 
**used_capacity_mi_b** | **float** | Used Capacity in MiB | [optional] 

## Example

```python
from dscc.models.device_type4system_settings_details_srinfo import DeviceType4systemSettingsDetailsSrinfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4systemSettingsDetailsSrinfo from a JSON string
device_type4system_settings_details_srinfo_instance = DeviceType4systemSettingsDetailsSrinfo.from_json(json)
# print the JSON string representation of the object
print(DeviceType4systemSettingsDetailsSrinfo.to_json())

# convert the object into a dict
device_type4system_settings_details_srinfo_dict = device_type4system_settings_details_srinfo_instance.to_dict()
# create an instance of DeviceType4systemSettingsDetailsSrinfo from a dict
device_type4system_settings_details_srinfo_from_dict = DeviceType4systemSettingsDetailsSrinfo.from_dict(device_type4system_settings_details_srinfo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


