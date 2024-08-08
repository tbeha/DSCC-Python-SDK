# DeviceType4RemoveProtectionPolicyInputSchema

Protection policy to be removed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote** | [**DeviceType4RemoveRemoteProtectionInputSchema**](DeviceType4RemoveRemoteProtectionInputSchema.md) | Remote protection to be removed | [optional] 
**remove_only_schedules** | **bool** | Remove only schedules and retain remote protection | [optional] 
**remove_schedules** | [**List[DeviceType4RemoveProtectionScheduleInputSchema]**](DeviceType4RemoveProtectionScheduleInputSchema.md) | List of protection schedules to be removed | [optional] 
**secondary_remote** | [**DeviceType4RemoveRemoteProtectionInputSchema**](DeviceType4RemoveRemoteProtectionInputSchema.md) | Secondary remote protection to be removed | [optional] 

## Example

```python
from dscc.models.device_type4_remove_protection_policy_input_schema import DeviceType4RemoveProtectionPolicyInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4RemoveProtectionPolicyInputSchema from a JSON string
device_type4_remove_protection_policy_input_schema_instance = DeviceType4RemoveProtectionPolicyInputSchema.from_json(json)
# print the JSON string representation of the object
print(DeviceType4RemoveProtectionPolicyInputSchema.to_json())

# convert the object into a dict
device_type4_remove_protection_policy_input_schema_dict = device_type4_remove_protection_policy_input_schema_instance.to_dict()
# create an instance of DeviceType4RemoveProtectionPolicyInputSchema from a dict
device_type4_remove_protection_policy_input_schema_from_dict = DeviceType4RemoveProtectionPolicyInputSchema.from_dict(device_type4_remove_protection_policy_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


