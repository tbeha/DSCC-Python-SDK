# DeviceType4systemSettingsDetailsRemoteSyslogSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_sys_log** | **int** | Remote Syslog Enabled/Disabled | [optional] 
**remote_sys_log_host** | **str** | Host details for Remote Syslog | [optional] 
**remote_sys_log_security_host** | **str** | Security Host details for Remote Syslog | [optional] 

## Example

```python
from dscc.models.device_type4system_settings_details_remote_syslog_settings import DeviceType4systemSettingsDetailsRemoteSyslogSettings

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4systemSettingsDetailsRemoteSyslogSettings from a JSON string
device_type4system_settings_details_remote_syslog_settings_instance = DeviceType4systemSettingsDetailsRemoteSyslogSettings.from_json(json)
# print the JSON string representation of the object
print(DeviceType4systemSettingsDetailsRemoteSyslogSettings.to_json())

# convert the object into a dict
device_type4system_settings_details_remote_syslog_settings_dict = device_type4system_settings_details_remote_syslog_settings_instance.to_dict()
# create an instance of DeviceType4systemSettingsDetailsRemoteSyslogSettings from a dict
device_type4system_settings_details_remote_syslog_settings_from_dict = DeviceType4systemSettingsDetailsRemoteSyslogSettings.from_dict(device_type4system_settings_details_remote_syslog_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


