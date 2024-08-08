# SystemConfigParamsEditInputSystemParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_wrtback_single_node** | **float** | Allow writeback single node setting in days | [optional] 
**enable_aiqo_s** | **str** | Enable or disable AI QoS feature, allowed values are:yes or no | [optional] 
**host_dif** | **str** | Host Data Integrity Field, allowed values are:yes or no | [optional] 
**host_dif_template** | **str** | HostDIF Template | [optional] 
**overprov_ratio_limit** | **float** | Over provisioning ratio limit setting | [optional] 
**overprov_ratio_warning** | **float** | Over provisioning ratio warning setting | [optional] 

## Example

```python
from dscc.models.system_config_params_edit_input_system_parameters import SystemConfigParamsEditInputSystemParameters

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigParamsEditInputSystemParameters from a JSON string
system_config_params_edit_input_system_parameters_instance = SystemConfigParamsEditInputSystemParameters.from_json(json)
# print the JSON string representation of the object
print(SystemConfigParamsEditInputSystemParameters.to_json())

# convert the object into a dict
system_config_params_edit_input_system_parameters_dict = system_config_params_edit_input_system_parameters_instance.to_dict()
# create an instance of SystemConfigParamsEditInputSystemParameters from a dict
system_config_params_edit_input_system_parameters_from_dict = SystemConfigParamsEditInputSystemParameters.from_dict(system_config_params_edit_input_system_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


