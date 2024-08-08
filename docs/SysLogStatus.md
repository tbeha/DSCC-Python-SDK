# SysLogStatus

Remote syslog details of the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general** | **str** | General | [optional] 
**security** | **str** | Security | [optional] 

## Example

```python
from dscc.models.sys_log_status import SysLogStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SysLogStatus from a JSON string
sys_log_status_instance = SysLogStatus.from_json(json)
# print the JSON string representation of the object
print(SysLogStatus.to_json())

# convert the object into a dict
sys_log_status_dict = sys_log_status_instance.to_dict()
# create an instance of SysLogStatus from a dict
sys_log_status_from_dict = SysLogStatus.from_dict(sys_log_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


