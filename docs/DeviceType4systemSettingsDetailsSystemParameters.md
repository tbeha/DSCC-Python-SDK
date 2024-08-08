# DeviceType4systemSettingsDetailsSystemParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fc_raw_space_alert** | **int** | FC raw space alert setting in MiB | [optional] 
**max_volume_retention** | **int** | Maximum global volume retention policy in seconds | [optional] 
**overprov_ratio_limit** | **float** | Over provisioning ratio limit setting | [optional] 
**overprov_ratio_warning** | **float** | Over provisioning ratio warning setting | [optional] 

## Example

```python
from dscc.models.device_type4system_settings_details_system_parameters import DeviceType4systemSettingsDetailsSystemParameters

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4systemSettingsDetailsSystemParameters from a JSON string
device_type4system_settings_details_system_parameters_instance = DeviceType4systemSettingsDetailsSystemParameters.from_json(json)
# print the JSON string representation of the object
print(DeviceType4systemSettingsDetailsSystemParameters.to_json())

# convert the object into a dict
device_type4system_settings_details_system_parameters_dict = device_type4system_settings_details_system_parameters_instance.to_dict()
# create an instance of DeviceType4systemSettingsDetailsSystemParameters from a dict
device_type4system_settings_details_system_parameters_from_dict = DeviceType4systemSettingsDetailsSystemParameters.from_dict(device_type4system_settings_details_system_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


