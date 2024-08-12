# DeviceType4sysLogStatus

Remote syslog details of the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general** | **str** | General | [optional] 
**security** | **str** | Security | [optional] 

## Example

```python
from dscc.models.device_type4sys_log_status import DeviceType4sysLogStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4sysLogStatus from a JSON string
device_type4sys_log_status_instance = DeviceType4sysLogStatus.from_json(json)
# print the JSON string representation of the object
print(DeviceType4sysLogStatus.to_json())

# convert the object into a dict
device_type4sys_log_status_dict = device_type4sys_log_status_instance.to_dict()
# create an instance of DeviceType4sysLogStatus from a dict
device_type4sys_log_status_from_dict = DeviceType4sysLogStatus.from_dict(device_type4sys_log_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


