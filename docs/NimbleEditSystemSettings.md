# NimbleEditSystemSettings

Edit Nimble system-settings input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_settings** | [**EditAlertSettings**](EditAlertSettings.md) |  | [optional] 
**date_timezone_settings** | [**EditDateTimezoneSettings**](EditDateTimezoneSettings.md) |  | [optional] 
**dns_settings** | [**EditDnsSettings**](EditDnsSettings.md) |  | [optional] 
**encryption_config** | [**EncryptionSettings**](EncryptionSettings.md) |  | [optional] 
**isns_settings** | [**EditIsnsSettings**](EditIsnsSettings.md) |  | [optional] 
**name** | **str** | Name of the group. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**proxy_settings** | [**EditProxySettings**](EditProxySettings.md) |  | [optional] 
**security_settings** | [**EditSecuritySettings**](EditSecuritySettings.md) |  | [optional] 
**smtp_settings** | [**EditSmtpMailSettings**](EditSmtpMailSettings.md) |  | [optional] 
**snmp_settings** | [**EditSnmpSettings**](EditSnmpSettings.md) |  | [optional] 
**support_settings** | [**EditSupportSettings**](EditSupportSettings.md) |  | [optional] 
**syslogd_settings** | [**EditSyslogdSettings**](EditSyslogdSettings.md) |  | [optional] 
**system_parameters** | [**EditSystemParameters**](EditSystemParameters.md) |  | [optional] 

## Example

```python
from dscc.models.nimble_edit_system_settings import NimbleEditSystemSettings

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleEditSystemSettings from a JSON string
nimble_edit_system_settings_instance = NimbleEditSystemSettings.from_json(json)
# print the JSON string representation of the object
print(NimbleEditSystemSettings.to_json())

# convert the object into a dict
nimble_edit_system_settings_dict = nimble_edit_system_settings_instance.to_dict()
# create an instance of NimbleEditSystemSettings from a dict
nimble_edit_system_settings_from_dict = NimbleEditSystemSettings.from_dict(nimble_edit_system_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


