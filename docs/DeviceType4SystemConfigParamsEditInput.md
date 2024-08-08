# DeviceType4SystemConfigParamsEditInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_mode** | [**DeviceType4SystemConfigParamsEditInputAuthMode**](DeviceType4SystemConfigParamsEditInputAuthMode.md) |  | [optional] 
**date_time** | **str** | system date time. timezone is mandatory to configure this parameter. | [optional] 
**installation_sites** | [**DeviceType4SystemConfigParamsEditInputInstallationSites**](DeviceType4SystemConfigParamsEditInputInstallationSites.md) |  | [optional] 
**name** | **str** | system name | [optional] 
**ntp_addresses** | **List[Optional[str]]** | system ntp addresses. timezone is mandatory to configure this parameter. | [optional] 
**remote_syslog_settings** | [**DeviceType4SystemConfigParamsEditInputRemoteSyslogSettings**](DeviceType4SystemConfigParamsEditInputRemoteSyslogSettings.md) |  | [optional] 
**srinfo** | [**DeviceType4SystemConfigParamsEditInputSrinfo**](DeviceType4SystemConfigParamsEditInputSrinfo.md) |  | [optional] 
**support_contact** | [**DeviceType4ContactsEditDetails**](DeviceType4ContactsEditDetails.md) |  | [optional] 
**system_parameters** | [**DeviceType4SystemConfigParamsEditInputSystemParameters**](DeviceType4SystemConfigParamsEditInputSystemParameters.md) |  | [optional] 
**timezone** | **str** | system time zone | [optional] 

## Example

```python
from dscc.models.device_type4_system_config_params_edit_input import DeviceType4SystemConfigParamsEditInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SystemConfigParamsEditInput from a JSON string
device_type4_system_config_params_edit_input_instance = DeviceType4SystemConfigParamsEditInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SystemConfigParamsEditInput.to_json())

# convert the object into a dict
device_type4_system_config_params_edit_input_dict = device_type4_system_config_params_edit_input_instance.to_dict()
# create an instance of DeviceType4SystemConfigParamsEditInput from a dict
device_type4_system_config_params_edit_input_from_dict = DeviceType4SystemConfigParamsEditInput.from_dict(device_type4_system_config_params_edit_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


