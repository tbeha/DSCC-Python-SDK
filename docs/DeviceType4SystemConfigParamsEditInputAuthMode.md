# DeviceType4SystemConfigParamsEditInputAuthMode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authmode** | **str** | Sets password authentication mode (totp or ciphertext) for a system | [optional] 

## Example

```python
from dscc.models.device_type4_system_config_params_edit_input_auth_mode import DeviceType4SystemConfigParamsEditInputAuthMode

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SystemConfigParamsEditInputAuthMode from a JSON string
device_type4_system_config_params_edit_input_auth_mode_instance = DeviceType4SystemConfigParamsEditInputAuthMode.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SystemConfigParamsEditInputAuthMode.to_json())

# convert the object into a dict
device_type4_system_config_params_edit_input_auth_mode_dict = device_type4_system_config_params_edit_input_auth_mode_instance.to_dict()
# create an instance of DeviceType4SystemConfigParamsEditInputAuthMode from a dict
device_type4_system_config_params_edit_input_auth_mode_from_dict = DeviceType4SystemConfigParamsEditInputAuthMode.from_dict(device_type4_system_config_params_edit_input_auth_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


