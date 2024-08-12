# DeviceType4SystemConfigParamsEditInputRemoteSyslogSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_sys_log** | **int** | Remote Syslog Enabled/Disabled | [optional] 
**remote_sys_log_host** | **List[str]** | Host details for Remote Syslog | [optional] 
**remote_sys_log_security_host** | **List[str]** | Security Host details for Remote Syslog | [optional] 

## Example

```python
from dscc.models.device_type4_system_config_params_edit_input_remote_syslog_settings import DeviceType4SystemConfigParamsEditInputRemoteSyslogSettings

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SystemConfigParamsEditInputRemoteSyslogSettings from a JSON string
device_type4_system_config_params_edit_input_remote_syslog_settings_instance = DeviceType4SystemConfigParamsEditInputRemoteSyslogSettings.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SystemConfigParamsEditInputRemoteSyslogSettings.to_json())

# convert the object into a dict
device_type4_system_config_params_edit_input_remote_syslog_settings_dict = device_type4_system_config_params_edit_input_remote_syslog_settings_instance.to_dict()
# create an instance of DeviceType4SystemConfigParamsEditInputRemoteSyslogSettings from a dict
device_type4_system_config_params_edit_input_remote_syslog_settings_from_dict = DeviceType4SystemConfigParamsEditInputRemoteSyslogSettings.from_dict(device_type4_system_config_params_edit_input_remote_syslog_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


