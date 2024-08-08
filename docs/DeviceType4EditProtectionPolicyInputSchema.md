# DeviceType4EditProtectionPolicyInputSchema

Request body for edit protection policy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_schedules** | [**List[DeviceType4ProtectionScheduleInputSchema]**](DeviceType4ProtectionScheduleInputSchema.md) |  | [optional] 
**modify_schedules** | [**List[DeviceType4ModifyProtectionScheduleInputSchema]**](DeviceType4ModifyProtectionScheduleInputSchema.md) |  | [optional] 
**policy** | [**DeviceType4ProtectionPolicyInputSchema**](DeviceType4ProtectionPolicyInputSchema.md) |  | [optional] 
**protection_policy_type** | **str** | Specifies Protection policy type. Synchronous replication/protection policy provides protection from array or site failures with zero RPO. Using this policy, you can also configure zero RTO policy like Active Peer Persistence. Asynchronous replication/protection policy provides protection from array or site failure with the user defined RPO.  Schedule snapshot policy takes snapshots of the member volumes of the protected volume set at periodic intervals defined by the user. You can setup the local snapshot schedule and also setup the co-ordinated synchronized snapshot schedule on the protected volume set configured with synchronous or asynchronous replication policy. You can do this by attaching a scheduled snapshot policy on the volume set having already a synchronous or asynchronous protecting policy. | 
**remove_schedules** | [**List[DeviceType4RemoveProtectionScheduleInputSchema]**](DeviceType4RemoveProtectionScheduleInputSchema.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_edit_protection_policy_input_schema import DeviceType4EditProtectionPolicyInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EditProtectionPolicyInputSchema from a JSON string
device_type4_edit_protection_policy_input_schema_instance = DeviceType4EditProtectionPolicyInputSchema.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EditProtectionPolicyInputSchema.to_json())

# convert the object into a dict
device_type4_edit_protection_policy_input_schema_dict = device_type4_edit_protection_policy_input_schema_instance.to_dict()
# create an instance of DeviceType4EditProtectionPolicyInputSchema from a dict
device_type4_edit_protection_policy_input_schema_from_dict = DeviceType4EditProtectionPolicyInputSchema.from_dict(device_type4_edit_protection_policy_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


