# DeviceType4SystemConfigParamsEditInputSystemParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overprov_ratio_limit** | **float** | Over provisioning ratio limit setting | [optional] 
**overprov_ratio_warning** | **float** | Over provisioning ratio warning setting | [optional] 

## Example

```python
from dscc.models.device_type4_system_config_params_edit_input_system_parameters import DeviceType4SystemConfigParamsEditInputSystemParameters

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SystemConfigParamsEditInputSystemParameters from a JSON string
device_type4_system_config_params_edit_input_system_parameters_instance = DeviceType4SystemConfigParamsEditInputSystemParameters.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SystemConfigParamsEditInputSystemParameters.to_json())

# convert the object into a dict
device_type4_system_config_params_edit_input_system_parameters_dict = device_type4_system_config_params_edit_input_system_parameters_instance.to_dict()
# create an instance of DeviceType4SystemConfigParamsEditInputSystemParameters from a dict
device_type4_system_config_params_edit_input_system_parameters_from_dict = DeviceType4SystemConfigParamsEditInputSystemParameters.from_dict(device_type4_system_config_params_edit_input_system_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


