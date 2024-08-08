# DeviceType4ProtectionPolicySchedules

Schedules on application set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4Schedule]**](DeviceType4Schedule.md) |  | [optional] 
**total** | **int** | Number of schedules on application set | [optional] 

## Example

```python
from dscc.models.device_type4_protection_policy_schedules import DeviceType4ProtectionPolicySchedules

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ProtectionPolicySchedules from a JSON string
device_type4_protection_policy_schedules_instance = DeviceType4ProtectionPolicySchedules.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ProtectionPolicySchedules.to_json())

# convert the object into a dict
device_type4_protection_policy_schedules_dict = device_type4_protection_policy_schedules_instance.to_dict()
# create an instance of DeviceType4ProtectionPolicySchedules from a dict
device_type4_protection_policy_schedules_from_dict = DeviceType4ProtectionPolicySchedules.from_dict(device_type4_protection_policy_schedules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


