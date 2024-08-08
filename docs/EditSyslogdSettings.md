# EditSyslogdSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**syslogd_enabled** | **bool** | Enable or disable syslogd in system | [optional] 
**syslogd_port** | **int** | Port number for syslogd server. Positive integer value up to 65535 representing TCP/IP port. | [optional] 
**syslogd_server** | **str** | Hostname of the syslogd server. String of alphanumeric characters, valid range is from 2 to 255; Each label must be between 1 and 63 characters long; - and . are allowed after the first and before the last character. | [optional] 
**syslogd_servers** | [**List[NimbleSyslogdServerInfo]**](NimbleSyslogdServerInfo.md) | syslogd server info. | [optional] 

## Example

```python
from dscc.models.edit_syslogd_settings import EditSyslogdSettings

# TODO update the JSON string below
json = "{}"
# create an instance of EditSyslogdSettings from a JSON string
edit_syslogd_settings_instance = EditSyslogdSettings.from_json(json)
# print the JSON string representation of the object
print(EditSyslogdSettings.to_json())

# convert the object into a dict
edit_syslogd_settings_dict = edit_syslogd_settings_instance.to_dict()
# create an instance of EditSyslogdSettings from a dict
edit_syslogd_settings_from_dict = EditSyslogdSettings.from_dict(edit_syslogd_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


