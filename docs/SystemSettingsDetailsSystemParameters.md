# SystemSettingsDetailsSystemParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_wrtback_single_node** | **float** | Allow writeback single node setting in days | [optional] 
**allow_wrtback_upgrade** | **float** | Allow the system to continue caching when in a single node state during an upgrade for up to the specified number of days | [optional] 
**enable_aiqo_s** | **str** | Enable or disable AI QoS feature, allowed values are:yes or no | [optional] 
**fc_raw_space_alert** | **int** | FC raw space alert setting in MiB | [optional] 
**host_dif** | **str** | Host Data Integrity Field, allowed values are:yes or no | [optional] 
**host_dif_template** | **str** | HostDIF Template | [optional] 
**max_volume_retention** | **int** | Maximum global volume retention policy in seconds | [optional] 
**overprov_ratio_limit** | **float** | Over provisioning ratio limit setting | [optional] 
**overprov_ratio_warning** | **float** | Over provisioning ratio warning setting | [optional] 

## Example

```python
from dscc.models.system_settings_details_system_parameters import SystemSettingsDetailsSystemParameters

# TODO update the JSON string below
json = "{}"
# create an instance of SystemSettingsDetailsSystemParameters from a JSON string
system_settings_details_system_parameters_instance = SystemSettingsDetailsSystemParameters.from_json(json)
# print the JSON string representation of the object
print(SystemSettingsDetailsSystemParameters.to_json())

# convert the object into a dict
system_settings_details_system_parameters_dict = system_settings_details_system_parameters_instance.to_dict()
# create an instance of SystemSettingsDetailsSystemParameters from a dict
system_settings_details_system_parameters_from_dict = SystemSettingsDetailsSystemParameters.from_dict(system_settings_details_system_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


