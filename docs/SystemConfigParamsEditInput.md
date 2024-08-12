# SystemConfigParamsEditInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_mode** | [**DeviceType4SystemConfigParamsEditInputAuthMode**](DeviceType4SystemConfigParamsEditInputAuthMode.md) |  | [optional] 
**date_time** | **str** | system date time | [optional] 
**installation_sites** | [**DeviceType4SystemConfigParamsEditInputInstallationSites**](DeviceType4SystemConfigParamsEditInputInstallationSites.md) |  | [optional] 
**name** | **str** | system name | [optional] 
**ntp_addresses** | **List[Optional[str]]** | system ntp addresses | [optional] 
**remote_syslog_settings** | [**DeviceType4SystemConfigParamsEditInputRemoteSyslogSettings**](DeviceType4SystemConfigParamsEditInputRemoteSyslogSettings.md) |  | [optional] 
**srinfo** | [**DeviceType4SystemConfigParamsEditInputSrinfo**](DeviceType4SystemConfigParamsEditInputSrinfo.md) |  | [optional] 
**support_contact** | [**ContactsEditDetails**](ContactsEditDetails.md) |  | [optional] 
**system_parameters** | [**SystemConfigParamsEditInputSystemParameters**](SystemConfigParamsEditInputSystemParameters.md) |  | [optional] 
**timezone** | **str** | system time zone | [optional] 

## Example

```python
from dscc.models.system_config_params_edit_input import SystemConfigParamsEditInput

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigParamsEditInput from a JSON string
system_config_params_edit_input_instance = SystemConfigParamsEditInput.from_json(json)
# print the JSON string representation of the object
print(SystemConfigParamsEditInput.to_json())

# convert the object into a dict
system_config_params_edit_input_dict = system_config_params_edit_input_instance.to_dict()
# create an instance of SystemConfigParamsEditInput from a dict
system_config_params_edit_input_from_dict = SystemConfigParamsEditInput.from_dict(system_config_params_edit_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


