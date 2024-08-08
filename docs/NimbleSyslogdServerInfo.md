# NimbleSyslogdServerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**syslog_port** | **int** | Port number for syslogd server. Positive integer value up to 65535 representing TCP/IP port. | [optional] 
**syslog_server** | **str** | Hostname of the syslogd server. String of alphanumeric characters, valid range is from 2 to 255; Each label must be between 1 and 63 characters long; - and . are allowed after the first and before the last character. | [optional] 

## Example

```python
from dscc.models.nimble_syslogd_server_info import NimbleSyslogdServerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleSyslogdServerInfo from a JSON string
nimble_syslogd_server_info_instance = NimbleSyslogdServerInfo.from_json(json)
# print the JSON string representation of the object
print(NimbleSyslogdServerInfo.to_json())

# convert the object into a dict
nimble_syslogd_server_info_dict = nimble_syslogd_server_info_instance.to_dict()
# create an instance of NimbleSyslogdServerInfo from a dict
nimble_syslogd_server_info_from_dict = NimbleSyslogdServerInfo.from_dict(nimble_syslogd_server_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


